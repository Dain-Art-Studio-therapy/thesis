from sys import *

def main(argv):
	puzzle_file = []
	with open_file(argv[1],'r') as f:
		faded = open_file("faded.ppm", 'w')
		file_list = process_file(f)
		pixel_list = groups_of_3(file_list,argv)
		scaled_list = writeNewPixel(pixel_list,argv)
		writeToFile(scaled_list,faded)

		faded.close()

def open_file(name,mode):
		try:
			return open(name,mode)
		except IOError as e:
			print >> stderr, '{0} : {1}'.format(name,e.strerror)
			exit(1)

def writeToFile(input_list,outfile):
	next_line = "\n"
	outfile.write(str(input_list[0]))
	outfile.write(next_line)
	outfile.write(str(input_list[1]) + " " + str(input_list[2]))
	outfile.write(next_line)
	outfile.write(str(input_list[3]))
	outfile.write(next_line)
	for i in range(4, len(input_list)):
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

def groups_of_3(input_list,argv):
	error = "Error with file, not convertable to integer...exiting"
	number_of_cuts = len(input_list)/3
	l_one = 3
	l_two = l_one + 1
	l_three = l_one + 2
	header = input_list[0][0]
	try:
		w = int(input_list[1][0])
		h = int(input_list[1][1])
		c = int(input_list[2][0])
	except:
		print error
		exit(1)
	new_list = [header,w,h,c]
	for i in range(0,number_of_cuts-1):
		l_two = l_one + 1
		l_three = l_one + 2
		try:
			r = int(input_list[l_one][0])
			g = int(input_list[l_two][0])
			b = int(input_list[l_three][0])
		except:
			print error
			exit(1)
		pixel = [r,g,b]
		new_list.append(pixel)
		l_one = l_one + 3
	return new_list

def writeNewPixel(input_list,argv):
	new_list = [input_list[0],input_list[1],input_list[2],input_list[3]]
	w = int(input_list[1])
	h = int(input_list[2])
	counter = 4
	for y in range(0,h):
		for x in range(0,w):
			r = float(input_list[counter][0])
			g = float(input_list[counter][1])
			b = float(input_list[counter][2])
			pixel = [r,g,b]
			pix = scalePixel(pixel,argv,x,y)
			new_list.append(pix)
			counter = counter + 1
	return new_list

def findDistance(pix_x,pix_y,argv):
	pt_x = int(argv[2])
	pt_y = int(argv[3])
	x = pt_x - pix_x
	y = pt_y - pix_y
	dist = ((x**2) + (y**2))**0.5
	return dist

def scalePixel(pixel,argv,x,y):
	radius = float(argv[4])
	distance = float(findDistance(x,y,argv))
	scalar = float((radius - distance)/radius)
	checked_scale = checkScale(scalar)
	r = float(pixel[0])*checked_scale
	g = float(pixel[1])*checked_scale
	b = float(pixel[2])*checked_scale
	return [r,g,b]

def checkScale(num):
	if num < 0.2:
		return 0.2
	else:
		return num

if __name__ == '__main__':
	if len(argv) > 4:
		main(argv)
	else:
		print "Must specify a file to run, y position, x position, and radius"
		exit(1)