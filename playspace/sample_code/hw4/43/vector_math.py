__author__ = 'Jarrett'

from data import *
import math

# scale_vector increases a vector
# by the scalar quantity
def scale_vector(vector, scalar):
    x = vector.x * scalar
    y = vector.y * scalar
    z = vector.z * scalar
    return Vector(x, y, z)

# dot_vector performs the dot
# product on two vectors
def dot_vector(vector1, vector2):
    productx = vector1.x * vector2.x
    producty = vector1.y * vector2.y
    productz = vector1.z * vector2.z
    return productx + producty + productz

# length_vector returns the length of a vector
def length_vector(vector):
    return math.sqrt((vector.x)**2 + (vector.y)**2 + (vector.z)**2)

# normalize_vector takes a vector
# and makes a new unit vector
def normalize_vector(vector):
    x = vector.x / length_vector(vector)
    y = vector.y / length_vector(vector)
    z = vector.z / length_vector(vector)
    return Vector(x, y, z)

# point_difference takes the difference
# between two points and makes a vector
def difference_point(point1, point2):
    return Vector(point1.x - point2.x, point1.y - point2.y, point1.z - point2.z)

# vector_difference takes the difference
# between two vectors and returns a new vector
def difference_vector(vector1, vector2):
    return Vector(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)

# translate_point takes a point and moves it
# by adding by the vector quantities
def translate_point(point, vector):
    return Point(point.x + vector.x, point.y + vector.y, point.z + vector.z)

# vector_from_to makes a new vector
# from two points
def vector_from_to(from_point, to_point):
    return Vector(to_point.x - from_point.x, to_point.y - from_point.y, to_point.z - from_point.z)