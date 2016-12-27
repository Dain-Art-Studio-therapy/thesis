from data import *
import math

def scale_vector(vector, scalar):
        x = vector.x * scalar
        y = vector.y * scalar
        z = vector.z * scalar
        return Point(x, y, z)

def dot_vector(vector1, vector2):
        dot_vector = (vector1.x * vector2.x) + ( vector1.y * vector2.y) + (vector1.z * vector2.z)
        return dot_vector


def length_vector(vector):
        length_vector = math.sqrt((vector.x ** 2) + (vector.y ** 2) + (vector.z ** 2))
        return length_vector

def normalize_vector(vector):
        i = math.sqrt((vector.x ** 2) + (vector.y ** 2) + (vector.z ** 2))
        x = vector.x / i
        y = vector.y / i
        z = vector.z / i
        return Vector(x, y, z)

def difference_point(point1, point2):
        x = point1.x - point2.x
        y = point1.y - point2.y
        z = point1.z - point2.z
        return Point(x, y, z)

def difference_vector(vector1, vector2):
        x = vector1.x - vector2.x
        y = vector1.y - vector2.y
        z = vector1.z - vector2.z
        return Vector(x, y, z)

def translate_point(point, vector):
        x = point.x + vector.x
        y = point.y + vector.y
        z = point.z + vector.z
        return Point(x, y, z)

def vector_from_to(from_point, to_point):
        x = to_point.x - from_point.x
        y = to_point.y - from_point.y
        z = to_point.z - from_point.z
        return Vector(x, y, z)

def scale_color(color, scalar):
        r = color.r * scalar
	if r > scalar:
		r = scalar
        g = color.g * scalar
	if g > scalar:
		g = scalar
        b = color.b * scalar
	if b > scalar:
		b = scalar
        return Color(r, g, b)

