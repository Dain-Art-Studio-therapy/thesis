import sys
from fade_utility import *
import math

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

def colors(file_to_read):
	pixels = pixelixer(file_to_read)
	pixel_colors = []
	for pixel in pixels:
		color = Color (pixel[0], pixel[1], pixel[2])
		pixel_colors.append(color)
	return pixel_colors

def listify(f):
	every_thing_in_file = []
	for line in f:
		l = line.split()
		every_thing_in_file.append(l)
	return every_thing_in_file

def fade_factor(every_thing_in_file, pixelized, row, col, radius):
	row_counter = row_count(every_thing_in_file)
	fade_list = []
	for i in range(len(pixelized)):
		x_now = i % row_counter
		y_now = i/ row_counter
		distance = math.sqrt ((x_now-int (row))**2+(y_now-int (col))**2)
		scaler = (float(radius) - distance) / float (radius)
		fade_list.append(scaler)
	return fade_list

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

def coloring(every_thing_in_file, pixelized, row, col, radius):
	 pixels = pixelizer(every_thing_in_file)
	 fade_list = fade_factor(every_thing_in_file, pixelized, row, col, radius)
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

def main(file_to_read, row, col, radius):
	#try:
		f = open(file_to_read,'rb')
		every_thing_in_file = listify(f)
		dimensions  = every_thing_in_file[1]
		columns = dimensions [0]
		columns = int(columns)
		dimensions  = every_thing_in_file[1]
		rows = dimensions [1]
		rows = int(rows)
		write_my_file = open('faded.ppm', 'wb')
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
	#except:
	#	print 'error in name of file'

if __name__=='__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
