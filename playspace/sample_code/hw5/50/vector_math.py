import math
import data

def scale_vector(vector, scalar):
   vector2 = data.Vector(0.0, 0.0, 0.0)
   vector2.x = vector.x * scalar
   vector2.y = vector.y * scalar
   vector2.z = vector.z * scalar

   return vector2

def dot_vector(vector1, vector2):
   value = (vector1.x * vector2.x) + (vector1.y * vector2.y) + \
      (vector1.z * vector2.z)
   return value

def length_vector(vector):
   distance = math.sqrt(vector.x**2 + vector.y**2 + vector.z**2)
   return distance

def normalize_vector(vector):
   vector2 = data.Vector(0.0, 0.0, 0.0)
   vector2.x = vector.x * (1/length_vector(vector))
   vector2.y = vector.y * (1/length_vector(vector))
   vector2.z = vector.z * (1/length_vector(vector))
   return vector2

def difference_point(point1, point2):
   vector = data.Vector(0.0, 0.0, 0.0)
   vector.x = point1.x - point2.x
   vector.y = point1.y - point2.y
   vector.z = point1.z - point2.z

   return vector

def difference_vector(vector1, vector2):
   fin_vec = data.Vector(0.0, 0.0, 0.0)
   fin_vec.x = vector1.x - vector2.x
   fin_vec.y = vector1.y - vector2.y
   fin_vec.z = vector1.z - vector2.z
   
   return fin_vec

def translate_point(point, vector):
   point2 = data.Point(0, 0, 0)
   point2.x = point.x + vector.x
   point2.y = point.y + vector.y
   point2.z = point.z + vector.z

   return point2

def vector_from_to(from_point, to_point):
   vector = data.Vector(0.0, 0.0, 0.0)
   vector.x = to_point.x - from_point.x
   vector.y = to_point.y - from_point.y
   vector.z = to_point.z - from_point.z

   return vector
