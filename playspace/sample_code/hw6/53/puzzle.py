from sys import *

def main(argv):
	puzzle_file = []
	with open_file(argv[1],'r') as f:
		hidden = open_file("hidden.ppm", 'w')
		file_list = process_file(f)
		pixel_list = groups_of_3(file_list)
		writeToFile(pixel_list,hidden)

		hidden.close()

def open_file(name,mode):
		try:
			return open(name,mode)
		except IOError as e:
			print >> stderr, '{0} : {1}'.format(name,e.strerror)
			exit(1)

def writeToFile(input_list,outfile):
	next_line = "\n"
	outfile.write(str(input_list[0][0]))
	outfile.write(next_line)
	outfile.write(str(input_list[1][0]) + " " + str(input_list[1][1]))
	outfile.write(next_line)
	outfile.write(str(input_list[2][0]))
	outfile.write(next_line)
	for i in range(3, len(input_list)):
		r = input_list[i][0]
		g = input_list[i][1]
		b = input_list[i][2]
		pixel_string = str(r) + " " + str(g) + " " + str(b)
		outfile.write(pixel_string)
		outfile.write(next_line)

def process_file(f):
	new_list = []
	for line in f:
		split_line = [num for num in line.split()]
		new_list.append(split_line)
	return new_list

def groups_of_3(input_list):
	number_of_cuts = len(input_list)/3
	start = 3
	new_list = [input_list[0],input_list[1],input_list[2]]
	for i in range(0,number_of_cuts - 1):
		pixel = input_list[start:start+3]
		pixel_list = writeNewPixel(pixel)
		new_list.append(pixel_list)
		start = start + 3
	return new_list

def writeNewPixel(input_list):
	error = "Error with file, not convertable to integer...exiting"
	try:
		num = int(input_list[0][0])
	except:
		print error
		exit(1)
	r_mult = (num*10)
	r = checkMin(r_mult)
	g = input_list[1][0]
	b = input_list[2][0]

	return solvePuzzle([r,g,b])

def solvePuzzle(input_list):
	red = input_list[0]
	green = red
	blue = red
	return [red,green,blue]

def checkMin(color_value):
    if color_value > 255:
        color_value = 255
        return color_value
    else:
        return color_value

if __name__ == '__main__':
	if len(argv) > 1:
		main(argv)
	else:
		print "Must specify a file to run"
		exit(1)