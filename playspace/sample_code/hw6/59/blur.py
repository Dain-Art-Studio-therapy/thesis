import sys
from blur_utility import *
from math import sqrt

class Point:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def __eq__(self, other):
		return (utility.epsilon_equal(self.x,other.x) 
			and utility.epsilon_equal(self.y,other.y) 
			and utility.epsilon_equal(self.z,other.z))

class Color:
	def __init__(self,r,g,b):
		self.r = r # internal colors
		self.g = g 
		self.b = b 
	def __str__(self): # external colors
		r = int(self.r)
		g = int(self.g)
		b = int(self.b)
		return str(r) + ' '+ str(g) + ' ' + str (b) #string-ify
	def __eq__(self, other):
		return (utility.epsilon_equal(self.r,other.r) 
			and utility.epsilon_equal(self.g,other.g) 
			and utility.epsilon_equal(self.b,other.b))

def groups_of_3(raw):
    end_list=[]
    for i in range(len(raw)):
        if len(raw)%3==0:
            if i%3==0:
                sublist=[raw[i],raw[(i+1)],raw[(i+2)]]
                end_list.append(sublist)
        elif len(raw)%3==1:
            if i%3==0:
                sublist=[raw[i],raw[(i+1)],raw[(i+2)]]
                end_list.append(sublist)
            elif i==len(raw):
                left_over=[raw[i]]
                end_list.append(left_over)
            else:
                pass
        else:
            if i%3==0:
                sublist=[raw[i],raw[(i+1)],raw[(i+2)]]
                end_list.append(sublist)
            elif i==(len(raw)-1):                
                left_over=[raw[i],raw[(i+1)]]
                end_list.append(left_over)
            else:
                pass
                
    return end_list

def pixelizer(every_thing_in_file):
	pixels_components = every_thing_in_file [3:]
	pixelizer = groups_of_3(pixels_components)
	return pixelizer

def listify(f):
	every_thing_in_file = []
	for line in f:
		l = line.split()
		every_thing_in_file.append(l)
	return every_thing_in_file

def x_range(i, blur, every_thing_in_file, pixelized):
	row_counter = row_count(every_thing_in_file)
	b = int (blur)
	if i-b>=0:
		min_x = i-b
		if i+b<= len(row_counter)-1:
			max_x= i+b
			return range (min_x, max_x)
		else:
			max_x = len(row_counter)-1
			return range (min_x, max_x)
	else:
		min_x = 0
		if i+b<= len(row_counter)-1:
			max_x= i+b
			return range (min_x, max_x)
		else:
			max_x = len(row_counter)-1
			return range (min_x, max_x)
def y_range(i, blur, every_thing_in_file, pixelized):
	row_counter = row_count(every_thing_in_file)
	b = int (blur)
	if i-b>=0:
		min_y = i-b
		if i+b<= len(row_counter)-1:
			max_y= i+b
			return range (min_y, max_y)
		else:
			max_y = len(row_counter)-1
			return range (min_y, max_y)
	else:
		min_y = 0
		if i+4<= len(row_counter)-1:
			max_y= i+4
			return range (min_y, max_y)
		else:
			max_y = len(row_counter)-1
			return range (min_y, max_y)


def pt_finder(every_thing_in_file, pixelized):
	row_counter = row_count(every_thing_in_file)
	all_pts = []
	x_spots = range (len(row_counter))
	y_spots = range (len(row_counter))
	for i in range(len(pixelized)):
		blured_x_domain = x_range(i, every_thing_in_file, pixelized)
		blured_y_range = y_range(i, every_thing_in_file, pixelized)
		for x in blured_x_domain:
			pts_list = []
			for y in blured_y_domain:
				pt = Point (x , y, 0)
				pts_list.append(pt)
		all_pts.append[pts_list]
	return all_pts
def color_at_pt (every_thing_in_file, pixelized):
	for i in range(len(pixelized)):
		x_now = i % row_counter
		y_now = i/ row_counter
		point = Point (x_now, y_now, 0)
		color = pixelized[0]
		color = pixelized[0]

def color_storer (every_thing_in_file, pixelized):
	pts = pt_finder(every_thing_in_file, pixelized)


def coloring(every_thing_in_file, pixelized, row, col, radius):
	 pixels = pixelizer(every_thing_in_file)
	 stored_color_list = fade_factor(every_thing_in_file, pixelized, row, col, radius)
	 color_list = []
	 for i1 in range(len(pixels)):
	 	for i2 in range(len(fade_list)):
	 		if i1 == i2:
	 			fade =  fade_list[i2]
	 			color_base = pixels[i1]
	 			red = ''.join(color_base[0]) 
	 			red = int (red) * fade
	 			green = ''.join(color_base[1])
	 			green = int (green) * fade
	 			blue = ''.join(color_base[2])
	 			green = int (green) * fade
	 			color = Color (red, green, blue)
	 			color_list.append(color)
	 return color_list


def blur_factor(entry, every_thing_in_file):
	pixels = pixelizer(every_thing_in_file)
	denominator = len(entry)
	red_sum = 0
	green_sum = 0
	blue_sum = 0
	for i1 in range(len(pixels)):
	 	for i2 in range(len(entry)):
 			color_base = pixels[i1]
 			red = ''.join(color_base[0]) 
 			red = int (red) / float(denominator)
 			green = ''.join(color_base[1])
 			green = int (green) * fade
 			blue = ''.join(color_base[2])
 			green = int (green) * fade
 			color = Color (red, green, blue)
 			color_list.append(color)
		return color_list
		average_color = sum(stored)/float(denominator)
		return average_color

def column_count(every_thing_in_file):
	file_list = every_thing_in_file 
	dimensions  = file_list[1]
	columns = dimensions [0]
	columns = int(columns)
	return columns

def row_count(every_thing_in_file):
	file_list = every_thing_in_file
	dimensions  = file_list[1]
	rows = dimensions [1]
	rows = int(rows)
	return rows 

def coloring(every_thing_in_file, pixelized,):
	 pixels = pixelizer(every_thing_in_file)
	 color_list = []
	 for i1 in range(len(pixels)):
	 	for i2 in range(len(fade_list)):
	 		if i1 == i2:
	 			blur =  fade_list[i2]
	 			color_base = pixels[i1]
	 			red = ''.join(color_base[0]) 
	 			red = int (red) * fade
	 			green = ''.join(color_base[1])
	 			green = int (green) * fade
	 			blue = ''.join(color_base[2])
	 			green = int (green) * fade
	 			color = Color (red, green, blue)
	 			color_list.append(color)
	 return color_list


def main(file_to_read, blur):
	try:
		try:
			len(argv)=2
		f = open(file_to_read,'rb')
		every_thing_in_file = listify(f)
		dimensions  = every_thing_in_file[1]
		columns = dimensions [0]
		columns = int(columns)
		dimensions  = every_thing_in_file[1]
		rows = dimensions [1]
		rows = int(rows)
		write_my_file = open('blurred.ppm', 'wb')
		write_my_file.write("P3"+"\n")
		write_my_file.write(str(columns) + ' ' + str (rows) + '\n')
		write_my_file.write("255" + "\n")
		pixels_components = every_thing_in_file [3:]
		pixelized = groups_of_3(pixels_components)
		pixel_colors = []
		color_list = coloring(every_thing_in_file, pixelized, row, col, radius)
		for color in color_list:
			write_my_file.write(str(color)+ "\n")
		write_my_file. close()	
		return f.close()
		except:
			blur = 4
	except:
		print 'error in name of file'

if __name__=='__main__':
    main(sys.argv[1], sys.argv[2])

