import data
import math

def scale_vector(vector, scalar):
   vec = data.Vector((vector.x * scalar), (vector.y * scalar), (vector.z * scalar))
   return vec

def dot_vector(vector1, vector2):
   return ((vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z))

def length_vector(vector):
   return math.sqrt(vector.x ** 2 + vector.y ** 2 + vector.z ** 2)

def normalize_vector(vector):
   vec = data.Vector((vector.x / length_vector(vector)), (vector.y / length_vector(vector)), (vector.z / length_vector(vector)))
   return vec

def difference_point(point1, point2):
   vec = data.Vector((point1.x - point2.x), (point1.y - point2.y), (point1.z - point2.z))
   return vec

def difference_vector(vector1, vector2):
   vec = data.Vector((vector1.x - vector2.x), (vector1.y - vector2.y), (vector1.z - vector2.z))
   return vec

def translate_point(point, vector):
   pt = data.Point((point.x + vector.x), (point.y + vector.y), (point.z + vector.z))
   return pt

def vector_from_to(from_point, to_point):
   vec = data.Vector((to_point.x - from_point.x), (to_point.y - from_point.y), (to_point.z - from_point.z))
   return vec
