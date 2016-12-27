# contains the function implementations

import data
import math

def scale_vector(vector, scalar):
   v1 = data.Vector(vector.x * scalar, vector.y * scalar, vector.z * scalar)
   return v1   

def dot_vector(vector1, vector2):
   dot_product = (vector1.x * vector2.x + 
		 vector1.y * vector2.y +
		 vector1.z * vector2.z)
   return dot_product

def length_vector(vector):
   length = math.sqrt((vector.x ** 2) + (vector.y ** 2) + (vector.z ** 2))
   return length

def normalize_vector(vector):
   normal_vector = scale_vector(vector, 1/length_vector(vector))
   return normal_vector

def difference_point(point1, point2):
   diff_vector = data.Vector(point1.x - point2.x, point1.y - point2.y, point1.z - point2.z)
   return diff_vector

def difference_vector(vector1, vector2):
   diff_vector = data.Vector(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)
   return diff_vector

def translate_point(point, vector):
   trans_point = data.Point(point.x + vector.x, point.y + vector.y, point.z + vector.z)
   return trans_point

def vector_from_to(from_point, to_point):
   direction = data.Vector(to_point.x - from_point.x, to_point.y - from_point.y, to_point.z - from_point.z)
   return direction
