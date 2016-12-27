import data
import math

def scale_vector(vector, s):
   return data.Vector(vector.x * s, vector.y * s, vector.z * s)

def dot_vector(v1, v2):
   return (v1.x * v2.x + v1.y * v2.y + v1.z * v2.z)

def length_vector(vector):
   return math.sqrt(vector.x ** 2 + vector.y ** 2 + vector.z ** 2)

def normalize_vector(vector):
   m = length_vector(vector)
   return data.Vector(vector.x/m, vector.y/m, vector.z/m)

def difference_point(p1, p2):
   return data.Vector(p1.x - p2.x, p1.y - p2.y, p1.z - p2.z)

def difference_vector(v1, v2):
   return data.Vector(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)

def translate_point(p, v):
   return data.Point(p.x + v.x, p.y + v.y, p.z + v.z)

def vector_from_to(p1, p2):
   return data.Vector(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)
