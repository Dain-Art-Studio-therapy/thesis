from sys import *
from cast import *
from data import *
from commandline import *

def main(argv):
	spheres_from_file = []
	with open_file(argv[1],'r') as f:
		spheres_from_file = process_file(f)

	createImage(argv,spheres_from_file)

def open_file(name,mode):
		try:
			return open(name,mode)
		except IOError as e:
			print >> stderr, '{0} : {1}'.format(name,e.strerror)
			exit(1)

def process_file(f):
	i = 1
	new_sphere_list = []

	for line in f:
		try:
			split_line = [float(num) for num in line.split()]
			if len(split_line) != 11:
				raise
			else:
				new_sphere = createSphere(split_line)
				new_sphere_list.append(new_sphere)
		except:
			print "malformed sphere on line " + str(i) + " ... skipping"
		i = i + 1
	return new_sphere_list

def createImage(f,sphere_list):
	new_sphere_list = sphere_list

	cast_arguments = checkInputs(argv)

	min_x = cast_arguments[0]
	max_x = cast_arguments[1]
	min_y = cast_arguments[2]
	max_y = cast_arguments[3]
	w = cast_arguments[4]
	h = cast_arguments[5]
	eye_pt = cast_arguments[6]
	amb = cast_arguments[7]
	lte = cast_arguments[8]

	cast_all_rays(min_x,max_x,min_y,max_y,w,h,eye_pt,new_sphere_list,amb,lte)

#SPHERE FUNCTIONS FOR SPHERE LIST
def createSphere(input_list):
	sphere_point = spherePoint(input_list)
	sphere_radius = (input_list[3])
	sphere_color = sphereColor(input_list)
	sphere_finish = sphereFinish(input_list)

	return Sphere(sphere_point,sphere_radius,sphere_color,sphere_finish)

def spherePoint(input_list):
	point_x = (input_list[0])
	point_y = (input_list[1])
	point_z = (input_list[2])

	return Point(point_x,point_y,point_z)

def sphereColor(input_list):
	color_r = (input_list[4])
	color_g = (input_list[5])
	color_b = (input_list[6])

	return Color(color_r,color_g,color_b)

def sphereFinish(input_list):
	ambient = (input_list[7])
	diffuse = (input_list[8])
	specular = (input_list[9])
	roughness = (input_list[10])

	return Finish(ambient,diffuse,specular,roughness)

if __name__ == '__main__':
	if len(argv) > 1:
		main(argv)
	else:
		str1 = "usage: python ray_caster.py "
		str2 = "<filename> [-eye x y z] "
		str3 = "[-view min_x max_x min_y max_y width height] "
		str4 = "[-light x y z r g b] [-ambient r g b]"
		print str1 + str2 + str3 + str4

