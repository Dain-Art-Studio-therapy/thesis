
import sys
from puzzle_utility import *

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

def pixelizer(file_to_read):
	every_thing_in_file = listify(file_to_read)
	pixels_components = every_thing_in_file [3:]
	print pixels_components
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

def main(file_to_read):
	try:
		#open file - main
		#set dimensions- counters
		#chunk pixels - pixelixer
		#edit colors
		#print 
		f = open(file_to_read,'rb')
		every_thing_in_file = listify(f)
		dimensions  = every_thing_in_file[1]
		columns = dimensions [0]
		columns = int(columns)
		dimensions  = every_thing_in_file[1]
		rows = dimensions [1]
		rows = int(rows)
		write_my_file = open('hidden.ppm', 'wb')
		write_my_file.write("P3"+"\n")
		write_my_file.write(str(columns) + ' ' + str (rows) + '\n')
		write_my_file.write("255" + "\n")
		pixels_components = every_thing_in_file [3:]
		pixelizer = groups_of_3(pixels_components)
		pixel_colors = []
		for pixel in pixelizer:
			color_red = ''.join(pixel[0])
			red = int (color_red) * 10
			color = Color (red, red, red)
			write_my_file.write(str(color)+ "\n")
		write_my_file. close()	
		return f.close()
	except:
		print 'error in name of file'

if __name__=='__main__':
    main(sys.argv[1])
