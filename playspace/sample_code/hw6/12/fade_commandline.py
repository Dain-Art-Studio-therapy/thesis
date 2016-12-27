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

# find the scale of the color component
def fade_scale(x1, y1, x2, y2, r):
	try:
		col = int(x2)
		row = int(y2)
		radius = int(r)
		distance = math.sqrt((x1 - col)**2 + (y1 - row)**2)
		scale = max((radius - distance) / radius, 0.2)
	except: # if the col, row, radius are float or non-integer
		print 'argument need to be an integer'
		sys.exit(1)
	if row < 0 or col < 0 or radius < 0:
		print 'arguments cannot be negative'
		sys.exit(1)
	return scale

# get the faded color components and group them into rgb list with the header
def find_fade(values, argv):
	fade_values = []
	ppm_header = [values[0], values[1], values[2], values[3]]
	x = 0 # x pixel coordinate
	y = 0 # y pixel coordinate
	
	for i in range(4, len(values), 3):
		scale = fade_scale(x, y, argv[3], argv[2], argv[4])
		fade_values.extend([int(values[i] * scale), 
				    int(values[i+1] * scale), 
				    int(values[i+2] * scale)])
		# color component modified by the faded scale

		# checking each pixel location for faded value change
		if x < (values[1] - 1):
			x += 1
		else:
			x = 0
			y += 1

	fade_groups = group_of_3(fade_values) # group each rgb into a list
	fade_result = ppm_header + fade_groups # add the header in front
	return fade_result

# process the input file for the print out
def process_file(f, argv):
	string_list = []
	for line in f:
		string = line.split()
		string_list.extend(string)
	values = string_to_int(string_list)
	ppm_format = find_fade(values, argv)
	return ppm_format

# print out the picture in ppm format
def fade_print_out(ppm_format, output):
	print >> output, ppm_format[0] # P3
	print >> output, ppm_format[1], ppm_format[2] # width, height
	print >> output, ppm_format[3] # max value of color component
	for i in range(4, len(ppm_format)):
		print >> output, ppm_format[i][0], ppm_format[i][1], \
		    ppm_format[i][2]
    
