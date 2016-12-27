from data import *
import math
def scale_vector(vector, scalar):
	scaled_vector = Vector(vector.x*scalar, vector.y*scalar, vector.z*scalar)
	return scaled_vector
def dot_vector(vector1, vector2):
	doted_vector = (vector1.x*vector2.x + vector1.y*vector2.y
	+ vector1.z*vector2.z)
	return doted_vector
def length_vector(vector):
	length = math.sqrt((vector.x)**2+(vector.y)**2+(vector.z)**2) #magnitude
	return length
def square_length_vector(vector):
	return (vector.x)**2+(vector.y)**2+(vector.z)**2
def normalize_vector(vector):
	length = math.sqrt((vector.x)**2+(vector.y)**2+(vector.z)**2)
	normal = Vector (float(vector.x/length), float(vector.y/length), 
	float(vector.z/length))
	return normal
def difference_point(point1, point2):
	diff_vector = Vector(point1.x-point2.x, point1.y-point2.y, 
		point1.z-point2.z)
	return diff_vector
def difference_vector(vector1, vector2):
	diff_vector = Vector(vector1.x-vector2.x, vector1.y-vector2.y,
	vector1.z-vector2.z)
	return diff_vector
def translate_point(point, vector):
	translated_pt = Point(point.x+vector.x, point.y+vector.y, point.z+vector.z)
	return translated_pt
def vector_from_to(from_point, to_point):
	vect_t_f = Vector(to_point.x - from_point.x, to_point.y - from_point.y, 
		to_point.z - from_point.z)
	return vect_t_f
def square_vector(vector):
	v_squared = dot_vector(vector, vector)
	return v_squared
def cross_vector(vector1,vector2):
	crossed_vector = Vector(vector1.y*vector2.z-vector2.y*vector1.z,
		-(vector1.x*vector2.z-vector2.x*vector1.z),
		vector1.x*vector2.y-vector2.x*vector1.y) 
	return crossed_vector
