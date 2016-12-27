import data
import utility
import math

def scale_vector(vector, scalar):
   vec1 = vector.x * scalar
   vec2 = vector.y * scalar
   vec3 = vector.z * scalar
   Scaled = data.Vector(vec1, vec2, vec3)
   return Scaled

def dot_vector(vector1, vector2):
   xproduct = vector1.x * vector2.x
   yproduct = vector1.y * vector2.y
   zproduct = vector1.z * vector2.z
   fproduct = xproduct + yproduct + zproduct
   return fproduct

def length_vector(vector):
   l = ((vector.x ** 2) + (vector.y ** 2) + (vector.z ** 2)) ** .5
   return l

def normalize_vector(vector):
   length = 1 / length_vector(vector)
   return scale_vector(vector, length)

def difference_point(point1, point2):
   xp = point1.x - point2.x
   yp = point1.y - point2.y
   zp = point1.z - point2.z
   fp = data.Vector(xp, yp, zp)
   return fp

def difference_vector(vector1, vector2):
   xp = vector1.x - vector2.x
   yp = vector1.y - vector2.y
   zp = vector1.z - vector2.z
   fp = data.Vector(xp, yp, zp)
   return fp

def translate_point(point, vector):
   xp = point.x + vector.x
   yp = point.y + vector.y
   zp = point.z + vector.z
   fp = data.Vector(xp, yp, zp)
   return fp

def vector_from_to(from_point, to_point):
   xp = to_point.x - from_point.x
   yp = to_point.y - from_point.y
   zp = to_point.z - from_point.z
   fp = data.Vector(xp, yp, zp)
   return fp
