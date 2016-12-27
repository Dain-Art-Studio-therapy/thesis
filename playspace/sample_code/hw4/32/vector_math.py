import utility
from data import *
import math

def scale_vector(vector, scalar):
   v = Vector(0, 0, 0)
   v.x += vector.x * scalar
   v.y += vector.y * scalar
   v.z += vector.z * scalar
   return v

def dot_vector(vector1, vector2):
   return ((vector1.x * vector2.x) +
   (vector1.y * vector2.y) + 
   (vector1.z * vector2.z))

def length_vector(vector):
   return math.sqrt(vector.x**2 + vector.y**2 + vector.z**2)

def normalize_vector(vector):
   return scale_vector(vector, 1/length_vector(vector))

def difference_point(point1, point2):
   return Vector(point1.x - point2.x, point1.y - point2.y, point1.z - point2.z)

def difference_vector(vector1, vector2):
   return Vector(vector1.x - vector2.x,
   vector1.y - vector2.y,
   vector1.z - vector2.z)

def translate_point(point, vector):
   return Point(point.x + vector.x,
   point.y + vector.y,
   point.z + vector.z)

def vector_from_to(from_point, to_point):
   return difference_point(to_point, from_point)

def vector_mult(v1, v2):
   return Vector(v1.x*v2.x, v1.y*v2.y, v1.z*v2.z)
