from sys import *

def main(argv):
	saved_list = []
	with open_file(argv[1],'r') as f:
		file_list = process_file(f)
		saved_list = groups_of_3(file_list,argv)
		
	blurred = open_file("blurred.ppm", 'w')
	saved_list = writeNewPixel(saved_list,argv)
	writeToFile(saved_list,blurred)
	blurred.close()

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
	blur_factor = checkBlurFactor(argv)
	counter = 4
	for y in range(0,h):
		for x in range(0,w):
			pix = blurPixel(input_list,counter,blur_factor,x,y,w,h)
			new_list.append(pix)
			counter = counter + 1
	return new_list

def checkBlurFactor(argv):
	if len(argv) > 2:
		blur_factor = int(argv[2])
	else:
		blur_factor = 4
		print "default blur"
	return blur_factor

def blurPixel(input_list,init,blur_factor,x,y,width,height):
	blur = blur_factor
	r_avg = 0
	g_avg = 0
	b_avg = 0
	min_y = checkGridHeight((y-blur),height)
	max_y = checkGridHeight((y+blur),height)
	min_x = checkGridWidth((x-blur),width)
	max_x = checkGridWidth((x+blur),width)
	#same row as initial pixel
	for row in range(-blur,blur+1):
		for pix in range(-blur,blur+1):
			try:
				pos = init + pix + (width*row)
				r_avg += input_list[pos][0]
				g_avg += input_list[pos][1]
				b_avg += input_list[pos][2]
			except:
				pass

	denom = int((max_x - min_x+1)*(max_y - min_y+1))
	r = int(r_avg/denom)
	g = int(g_avg/denom)
	b = int(b_avg/denom)
	return [r,g,b]

def checkGridWidth(num,width):
	if num < 0:
		return 0
	elif num > width:
		return width
	else:
		return num

def checkGridHeight(num,height):
	if num < 0:
		return 0
	elif num > height:
		return height
	else:
		return num

if __name__ == '__main__':
	if len(argv) > 1:
		main(argv)
	else:
		print "Must specify a file to run and optional blur value"
		exit(1)