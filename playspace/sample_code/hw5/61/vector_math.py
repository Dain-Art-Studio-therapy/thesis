import math
import data
def scale_vector(vector, scalar):
   newVector= data.Vector((vector.x *scalar), (vector.y * scalar), (vector.z *scalar))
   return newVector

def dot_vector(vector1, vector2):
   Value=  vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z
   return Value

def length_vector(vector):
   Value=  math.sqrt(vector.x**2 + vector.y**2 + vector.z**2)
   return Value

def normalize_vector(vector):
   newVector= data.Vector((vector.x/length_vector(vector)), (vector.y/length_vector(vector)), (vector.z/length_vector(vector)))
   return newVector

def difference_point(point1, point2):
   newVector= data.Vector((point1.x-point2.x), (point1.y-point2.y), (point1.z-point2.z))
   return newVector

def difference_vector(vector1, vector2):
   newVector= data.Vector((vector1.x-vector2.x), (vector1.y-vector2.y), (vector1.z-vector2.z))
   return newVector

def translate_point(point, vector):
   newPoint= data.Point((point.x+vector.x), (point.y+vector.y), (point.z+vector.z))
   return newPoint

def vector_from_to(from_point, to_point):#to_point-from_point
   newVector= data.Vector((to_point.x-from_point.x), (to_point.y-from_point.y), (to_point.z-from_point.z))
   return newVector
