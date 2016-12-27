import math
import data

def add_vector(v1, v2):
   return data.Vector((v1.x + v2.x), (v1.y + v2.y), (v1.z + v2.z))

def scale_vector(vector, scalar):
   return data.Vector((vector.x * scalar) , (vector.y * scalar) , (vector.z * scalar))
   

def dot_vector(vector1, vector2):
   return (vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z)
   

def length_vector(vector):
   vectormag = math.sqrt((vector.x**2) + (vector.y**2) + (vector.z**2))
   return vectormag

def normalize_vector(vector):
   vectormag = math.sqrt((vector.x**2) + (vector.y**2) + (vector.z**2))
   return data.Vector(vector.x / vectormag , vector.y / vectormag, vector.z / vectormag)
   
def difference_point(pt1, pt2):
   ptdif = data.Vector((pt1.x - pt2.x) , (pt1.y - pt2.y) , (pt1.z - pt2.z))
   return ptdif

def difference_vector(vector1, vector2):
   vectdif = data.Vector((vector1.x - vector2.x) , (vector1.y - vector2.y) , (vector1.z - vector2.z))
   return vectdif
      
def translate_point(point, vector):
   newpt = data.Point((point.x + vector.x), (point.y + vector.y), (point.z + vector.z))
   return newpt

def vector_from_to(from_point, to_point):
   newvec = data.Vector((to_point.x - from_point.x), (to_point.y - from_point.y), (to_point.z - from_point.z))
   return newvec



