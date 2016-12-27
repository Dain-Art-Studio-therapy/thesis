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

# get the hidden color components and group them into rgb list with the header
def find_hidden(values):
	hidden_values = []
	ppm_header = [values[0], values[1], values[2], values[3]]
	for i in range(4, len(values), 3):
		# the 3 color components become the modified red value
		red = min(values[i] * 10, 255)
		green = red
		blue = red
		hidden_values.extend([red, green, blue])
	hidden_groups = group_of_3(hidden_values) # group each rgb into a list
	hidden_result = ppm_header + hidden_groups # add the header in front
	return hidden_result

# process the input file for print out
def process_file(infile):
	string_list = []
	for line in infile:
		string = line.split()
		string_list.extend(string)
	values = string_to_int(string_list)
	ppm_format = find_hidden(values)
	return ppm_format

# print out the picture in ppm format
def puzzle_print_out(ppm_format, output):
	print >> output, ppm_format[0]
	print >> output, ppm_format[1], ppm_format[2]
	print >> output, ppm_format[3]
	for i in range(4, len(ppm_format)):
		print >> output, ppm_format[i][0], ppm_format[i][1], \
		    ppm_format[i][2]

