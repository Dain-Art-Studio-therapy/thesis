import data
import math

def scale_vector(vector, scalar):
   c1 = vector.x * scalar
   c2 = vector.y * scalar
   c3 = vector.z * scalar
   v = data.Vector(c1, c2, c3)
   return v

def dot_vector(vector1, vector2):
   return (vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z)

def length_vector(vector):
   return math.sqrt(vector.x**2 + vector.y**2 + vector.z **2)

def normalize_vector(vector):
   l = math.sqrt(vector.x**2 + vector.y**2 + vector.z**2)
   c1 = vector.x / l
   c2 = vector.y / l
   c3 = vector.z / l
   v = data.Vector(c1, c2, c3)
   return v

def difference_point(point1, point2):
   c1 = point1.x - point2.x
   c2 = point1.y - point2.y
   c3 = point1.z - point2.z
   v = data.Vector(c1, c2, c3)
   return v

def difference_vector(vector1, vector2):
   c1 = vector1.x - vector2.x
   c2 = vector1.y - vector2.y
   c3 = vector1.z - vector2.z
   v = data.Vector(c1, c2, c3)
   return v

def translate_point(point,vector):
   c1 = point.x + vector.x
   c2 = point.y + vector.y
   c3 = point.z + vector.z
   p = data.Point(c1, c2, c3)
   return p

def vector_from_to(from_point, to_point):
   v = difference_point(to_point, from_point)
   return v

