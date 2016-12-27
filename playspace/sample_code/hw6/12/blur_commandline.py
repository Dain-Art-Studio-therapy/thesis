import math
import sys

# group the rgb values for the ppm file into a list inside a list
def group_of_3(num_list):
	result = [num_list[i:i+3] for i in range(0, len(num_list), 3)]
	return result

# convert the string into integer
def string_to_int(string_list):
	num_list = []
	header = [string_list[0]]
	for i in range(1, len(string_list)):			
		num_list.append(int(string_list[i]))
	values = header + num_list
	return values

# the average of a list of numbers
def average(total, amount):
	avg = total / amount
	return avg

# check if the reach argument exists and if the reach argument is valid
def reach_check(argv):
	default = 4
	try:
		return int(argv[2])
	except:
		if len(sys.argv) < 3: # no reach argument
			return default # default reach
		else: # non-integer reach argument
			print 'the neighbor reach is not an integer'
			sys.exit(1)

# calculate the average of the neighbor pixel
def neighbors_average(pixel_pos, x, y, reach, values, argv):
	total_red = 0 # total red component values
	total_green = 0 # total green component values
	total_blue = 0 # total blue component values
	area = 0 # total pixel accounted for in the average

	for dy in range(-reach, reach + 1): # neighbor reach for y
		for dx in range(-reach, reach + 1): # neightbor reach for x
			# pixel position shifted by the reach
			reach_x = x + dx
			reach_y = y + dy

			# check if the pixel position is within the pixel range
			if (0 <= reach_x < values[1] and 
			    0 <= reach_y < values[2]):
				shift = dx * 3 + dy * 3 * values[1]
				area += 1
				total_red += values[pixel_pos+shift]
				total_green += values[pixel_pos+1+shift]
				total_blue += values[pixel_pos+2+shift]

	# average values of color components
	average_red = average(total_red, area)
	average_green = average(total_green, area)
	average_blue = average(total_blue, area)

	average_rgb = [average_red, average_green, average_blue]
	return average_rgb

# get the blurred color components and group them into rgb list with the header
def find_blur(values, argv):
	blur_values = []
	ppm_values = [values[0], values[1], values[2], values[3]]
	x = 0 # x pixel coordinate
	y = 0 # y pixel coordinate
	reach = reach_check(argv) # neighbor reach
	if reach < 0:
		print 'reach value cannot be negative'
		sys.exit(1)

	for i in range(4, len(values), 3):
		average_rgb = neighbors_average(i, x, y, reach, values, argv)

		# color component modified by the blur
		blur_values.extend([average_rgb[0], 
				    average_rgb[1], 
				    average_rgb[2]])

		# checking each pixel location for blurred value change
		if x < (values[1] - 1):
			x += 1
		else:
			x = 0
			y += 1

	blur_groups = group_of_3(blur_values) # group each rgb into a list
	blur_result = ppm_values + blur_groups # add the header in front
	return blur_result

# process the input file for the print out
def process_file(f, argv):
	string_list = []
	for line in f:
		string = line.split()
		string_list.extend(string)
	values = string_to_int(string_list)
	ppm_groups = find_blur(values, argv)
	return ppm_groups

# print out the picture in ppm format
def blur_print_out(ppm_format, output):
	print >> output, ppm_format[0] # P3
	print >> output, ppm_format[1], ppm_format[2] # width, height
	print >> output, ppm_format[3] # max value of color component
	for i in range(4, len(ppm_format)):
		print >> output, ppm_format[i][0], ppm_format[i][1], \
		    ppm_format[i][2]
