import sys
from cast import *
from data import *
from commandline import *

def open_file(name, mode):
	try:
		return open(name, mode)
	except IOError as e: # return error if the file does not exist
		print >> sys.stderr, '{0}:{1}'.format(name, e.strerror)
		sys.exit(1) # exit open file

def main(argv):
	if len(sys.argv) < 2: # check if there are enough arguments
		print '''usage: python ray_caster.py <filename> [-eye x y z] 
		[-view min_x max_x min_y max_y width height] 
                [-light x y z r g b] [-ambient r g b]''' # instruction
	else:
		with open_file(argv[1], 'rb') as f: # open the input file
			sphere_list = process_file(f)
		with open_file('image.ppm', 'wb') as g: # open the output file
			flag_list = check_flag(sys.argv)

			# eye flag
			eye_values = find_flag(flag_list, 'eye')
			# view flag
			view_values = find_flag(flag_list, 'view')
			# light flag
			light_values = find_flag(flag_list, 'light')
			# ambient flag
			ambient_values = find_flag(flag_list, 'ambient')

			cast_all_rays(view_values[0], view_values[1], 
				      view_values[2], view_values[3], 
				      view_values[4], view_values[5],
				      eye_values, sphere_list, ambient_values, 
				      light_values, g)
			# create the image in the 'image.ppm' output file



if __name__ == '__main__':
	main(sys.argv)
