import sys
from cast import *
from data import *
from ray_caster import * 

def sphere_list_maker(filename):
	try:
		fin = open(filename[1],'rb')
				for line in fin:
					sphere_list = []
					l = line.split()
					number_of_numbers_in_line = []
					for number in l:
						try:
							if number is int:
								m = float(number)
							elif number is float:
								m = number
							number_of_numbers_in_line.append(m)
						except:
							print'malformed sphere ... skipping'
							l.next()
					try:
						len(number_of_numbers_in_line)==11
						center = Point (number_of_numbers_in_line[1],
							number_of_numbers_in_line[2],
							number_of_numbers_in_line[3])
						radius = number_of_numbers_in_line[4]
						color = Color (number_of_numbers_in_line[5],
							number_of_numbers_in_line[6],
							number_of_numbers_in_line[7])
						finish = Finish (number_of_numbers_in_line[8],
							number_of_numbers_in_line[9],
							number_of_numbers_in_line[10],
							number_of_numbers_in_line[11])
						sphere = Sphere (center, radius, color, finish)
						sphere_list.append(sphere)
					except:
						print'malformed sphere ... skipping'
						l.next()
				return sphere_list
				f.close()
	except:
			print 'usage: python ray_caster.py <filename>\
	[-eye x y z]\
	[-view min_x max_x min_y max_y width height]\
	[-light x y z r g b]\
	[-ambient r g b]'

def eye_check(argv):
	if '-eye' is in argv:
		list(argv)
		eye_point = Point (argv[3], argv[4], argv [5])
	else:
		eye_point = Point (0.0, 0.0, -14.0)
def view_check(argv):
	if '-view' is in argv:
		list(argv)
		m = 0
		for argv[i] in range(len(argv)):
			if argv[i] = -view:
				m = i
		return min_x = argv[m+1]
		return max_x = argv[m+2]
		return min_y = argv[m+3]
		return max_y = argv[m+4]
		return width = argv[m+5]
		return height = argv[m+6]
	else:
		return min_x = -10
		return max_x = 10
		return min_y = -7.5
		return max_y = 7.5
		return width = 1024
		return height = 768

def light_check(argv):
	if '-light' is in argv:
		list(argv)
		m = 0
		for argv[i] in range(len(argv)):
			if argv[i] = -light:
				m = i
		light_pt = Point (argv[m+1], argv[m+2], argv [m+3])
		light_co = Color (argv[m+4], argv[m+5], argv [m+6])
		light = Light (light_pt,light_co)
	else:
		eye_point = Point (0.0, 0.0, -14.0)

def ambient_check(argv):
	if '-ambient' is in argv:
		list(argv)
		m = 0
		for argv[i] in range(len(argv)):
			if argv[i] = -ambient:
				m = i
		ambient = Color (argv[m+1], argv[m+2], argv [m+3])
	else:
		eye_point = Point (0.0, 0.0, -14.0)


fout.write(cast_all_rays(min_x, max_x, min_y, max_y, width, height,
	eye_point, sphere_list, ambient_light, light))

f.close()

if __name__=='__main__':
    command_line(sys.argv)
