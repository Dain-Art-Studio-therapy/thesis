import data
import math
import utility

# multiply vector by a constant, only changes length
def scale_vector(vector, scalar):
   new_vector = data.Vector(vector.x * scalar, vector.y * scalar, vector.z * scalar)
   return new_vector

# dot product of 2 vectors
def dot_vector(vector1, vector2):
   return ((vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z))

# length of the vector
def length_vector(vector):
   return math.sqrt(vector.x ** 2 + vector.y ** 2 + vector.z ** 2)

# vector with same dir and length of 1
def normalize_vector(vector):
   vec_length = length_vector(vector)
   return scale_vector(vector, (1. / vec_length))

# returns a vector going from p2 to p1
def difference_point(point1, point2):
   newx = point1.x - point2.x
   newy = point1.y - point2.y
   newz = point1.z - point2.z
   return data.Vector(newx, newy, newz)

# vector1 - vector2
def difference_vector(vector1, vector2):
   newx = vector1.x - vector2.x
   newy = vector1.y - vector2.y
   newz = vector1.z - vector2.z
   return data.Vector(newx, newy, newz)

# translate a point along a vector
def translate_point(point, vector):
   x = point.x + vector.x
   y = point.y + vector.y
   z = point.z + vector.z
   return data.Point(x, y, z)

# vector going from a point to a point
def vector_from_to(from_point, to_point):
   x = to_point.x - from_point.x
   y = to_point.y - from_point.y
   z = to_point.z - from_point.z
   return data.Vector(x, y, z)

# distance between 2 points
def distance(point1, point2):
   dx = point2.x - point1.x
   dy = point2.y - point1.y
   dz = point2.z - point1.z
   return math.sqrt((dx ** 2) + (dy ** 2) + (dz ** 2))
