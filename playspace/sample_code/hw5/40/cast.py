from collisions import *
from vector_math import *
import data
import math

def cast_ray(ray, sphere_list, ambient, light, eye_point):
	intersections = find_intersection_points(sphere_list, ray)
	distances = [distance(ray.pt, tuple[1]) for tuple in intersections]
	
	if (distances == []): # no intersections found
		return data.Color(1.0, 1.0, 1.0)
	else:
		min = mIndex(distances)
		sphere = intersections[min][0]
		intersection = intersections[min][1]
		
		normal = sphere_normal_at_point(sphere, intersection)
		pe = translate_point(intersection, scale_vector(normal, 0.01))
		ldir = normalize_vector(vector_from_to(pe, light.pt))
		
		nDotldir = dot_vector(normal, ldir)
		lightRay = data.Ray(pe, ldir)
		
		reflection = difference_vector(ldir, scale_vector(normal, 2 * nDotldir))
		vdir = normalize_vector(vector_from_to(eye_point, pe))
		specIntensity = dot_vector(reflection, vdir)
		
		if specIntensity < 0:
			specIntensity = 0
		
		if nDotldir > 0 and not sphereBlocking(sphere_list, lightRay, light):
			return renderLight(sphere, ambient, light, nDotldir, specIntensity)
		else:
			return renderShadow(sphere, ambient)

def sphereBlocking(sphere_list, lightRay, light):
	int = find_intersection_points(sphere_list, lightRay)
	if len(int) == 0:
		return False
	distances = [distance(lightRay.pt, x[1]) for x in int]
	min = mIndex(distances)
	if distance(lightRay.pt, int[min][1]) <= distance(lightRay.pt, light.pt):
		return True
	else:
		return False
	
def cast_all_rays(min_x, max_x, min_y, max_y, width, height,\
				  eye_point, sphere_list, ambient, light):			  
	print "P3\n", width, height, "\n255"
	
	dx = (max_x - min_x) / float(width)
	dy = (max_y - min_y) / float(height)
	for j in range(height):
		for i in range(width):
			currentPoint = data.Point(min_x + i * dx, max_y - j * dy, 0)
			eyeToPoint = vector_from_to(eye_point, currentPoint)
			castRay = data.Ray(eye_point, eyeToPoint)
			
			pixel = cast_ray(castRay, sphere_list, ambient, light, eye_point)
			if pixel.r > 1.0:
				pixel.r = 1.0
			if pixel.g > 1.0:
				pixel.g = 1.0
			if pixel.b > 1.0:
				pixel.b = 1.0
			
			print int(pixel.r * 255),\
				  int(pixel.g * 255),\
				  int(pixel.b * 255)

def renderLight(sphere, ambient, light, nDotldir, specIntensity):
	# shorter variable names
	s_ambient = sphere.finish.ambient
	s_diffuse = sphere.finish.diffuse
	s_specular = sphere.finish.specular
	s_roughness = sphere.finish.roughness
	
	r = sphere.color.r * (s_ambient * ambient.r +\
						  light.color.r * s_diffuse * nDotldir)
	r += light.color.r * s_specular * specIntensity**(1 / s_roughness)
	
	g = sphere.color.g * (s_ambient * ambient.g +\
						  light.color.g * s_diffuse * nDotldir)
	g += light.color.g * s_specular * specIntensity**(1 / s_roughness)
	
	b = sphere.color.b * (s_ambient * ambient.b +\
						  light.color.b * s_diffuse * nDotldir)
	b += light.color.b * s_specular * specIntensity**(1 / s_roughness)
	return data.Color(r, g, b)

def renderShadow(sphere, ambient):
	s_ambient = sphere.finish.ambient
	
	r = sphere.color.r * s_ambient * ambient.r
	g = sphere.color.g * s_ambient * ambient.g
	b = sphere.color.b * s_ambient * ambient.b
	return data.Color(r, g, b)
				  
def distance(point1, point2):
	return math.sqrt((point1.x - point2.x)**2 +\
					 (point1.y - point2.y)**2 +\
					 (point1.z - point2.z)**2)
		
def mIndex(list):
	mIndex = 0
	for i in xrange(1, len(list)):
		if list[i] < list[mIndex]:
			mIndex = i
	return mIndex