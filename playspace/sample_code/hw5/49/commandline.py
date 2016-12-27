from cast import *
from data import *

# turn string into float
def string_to_float(num_list):
	float_list = []
	for num in num_list:			
		float_list.append(float(num))
	return float_list

# read the input file and turns it into a list of spheres
def process_file(f):
	sphere_list = []
	current_line = 1
	for line in f:
		sphere_values = line.split()
		if len(sphere_values) == 11:
			# check for correctly formatted input file
			try:
				float_values = string_to_float(sphere_values)
			except:
				print ('malform sphere on line ' + 
				       str(current_line) + ' ... skipping')
			               # invalid input
			sphere_list.append(
				Sphere(Point(float_values[0], 
					     float_values[1], 
					     float_values[2]), 
				       float_values[3], 
				       Color(float_values[4], 
					     float_values[5], 
					     float_values[6]), 
				       Finish(float_values[7], 
					      float_values[8], 
					      float_values[9], 
					      float_values[10])))
		                       # creates the list of spheres
			current_line += 1 # keep track of current line
		else:
			print ('malform sphere on line ' + str(current_line) + 
					' ... skipping') # invalid input
			current_line += 1 # keep track of current line
	return sphere_list

# validate the eye arguments
def eye_flag(x, y, z, default_value):
	try:
		return Point(float(x), float(y), float(z))
	except:
		return default_value

# validate the view arguments
def view_flag(min_x, max_x, min_y, max_y, width, height, default_value):
	try:
		view_values = [float(min_x), float(max_x), float(min_y), 
			       		float(max_y), int(float(width)), 
			       		int(float(height))]
		return view_values
	except:
		return default_value

# validate the ambient arguments
def ambient_flag(r, g, b, default_value):
	try:
		return Color(float(r), float(g), float(b))
	except:
		return default_value

# validate the light arguments
def light_flag(x, y, z, r, g, b, default_value):
	try:
		return Light(Point(float(x), float(y), float(z)), 
					Color(float(r), float(g), float(b)))
	except:
		return default_value

# check for any flag that is present in the command line
def check_flag(argv):
	flag_list = []
	eye = Point(0.0, 0.0, -14.0) # default eye_point value
	view = [-10.0, 10.0, -7.5, 7.5, 1024, 768] # default view values
	light = Light(Point(-100.0, 100.0, -100.0), 
		      Color(1.5, 1.5, 1.5))# default light value
	ambient = Color(1.0, 1.0, 1.0) # default ambient value
	for i in range(len(argv)):
		# check for flag argument in the command line
		if argv[i] == '-eye':
			eye = eye_flag(argv[i+1], 
						   argv[i+2], 
						   argv[i+3], 
						   eye)
		if argv[i] == '-view':
			view = view_flag(argv[i+1], argv[i+2], 
						    argv[i+3], argv[i+4], 
						    argv[i+5], argv[i+6], 
						    view)
		if argv[i] == '-light':
			light = light_flag(argv[i+1], argv[i+2], 
						     argv[i+3], argv[i+4], 
						     argv[i+5], argv[i+6],
						     light)
		if argv[i] == '-ambient':
			ambient = ambient_flag(argv[i+1], argv[i+2], 
						       argv[i+3], 
						       ambient)
	flag_list.extend([('eye', eye), ('view', view), 
			  ('light', light), ('ambient', ambient)])
	return flag_list

# find a specific flag and its arguments from a list of flag
def find_flag(flag_list, flag_type):
	for i in range(len(flag_list)):
		if flag_list[i][0] == flag_type:
			return flag_list[i][1]



