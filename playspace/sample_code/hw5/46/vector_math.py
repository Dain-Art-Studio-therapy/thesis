import data
import math

def scale_vector(vector, scale):
	return data.Vector(vector.x * scale,
			   vector.y * scale,
			   vector.z * scale)

def dot_vector(vec1, vec2):
	return ((vec1.x * vec2.x) +
               (vec1.y * vec2.y) +
	       (vec1.z * vec2.z))

def length_vector(vec):
	return math.sqrt((vec.x ** 2) + (vec.y ** 2) + (vec.z ** 2))

def normalize_vector(vec):
	return data.Vector(vec.x / length_vector(vec),
			   vec.y / length_vector(vec),
			   vec.z / length_vector(vec))

def difference_point(p1, p2):
	return data.Vector(p1.x - p2.x,
			   p1.y - p2.y,
			   p1.z - p2.z)

def difference_vector(vec1, vec2):
	return data.Vector(vec1.x - vec2.x,
			   vec1.y - vec2.y,
			   vec1.z - vec2.z)

def translate_point(pt, vec):
	return data.Point(pt.x + vec.x,
			  pt.y + vec.y,
			  pt.z + vec.z)

def vector_from_to(from_point, to_point):
	return data.Vector(to_point.x - from_point.x,
			   to_point.y - from_point.y,
			   to_point.z - from_point.z)

