import math
import data
import utility

def scale_vector(vector,scalar):
   new = data.Vector (vector.x * scalar, vector.y * scalar, vector.z * scalar)
   return new

def dot_vector(vector1, vector2):
   return ( (vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z) )

def length_vector(vector):
   scale = math.sqrt( (vector.x ** 2) + (vector.y ** 2) + (vector.z ** 2))
   return scale
   
def normalize_vector(vector):
   scale = math.sqrt( (vector.x ** 2) + (vector.y ** 2) + (vector.z ** 2))
   new = data.Vector (vector.x / scale, vector.y / scale, vector.z / scale)
   return new

def difference_point(point1,point2):
   new = data.Vector (point1.x - point2.x , point1.y - point2.y , point1.z - point2.z)
   return new

def difference_vector(vector1,vector2):
   new = data.Vector (vector1.x - vector2.x , vector1.y - vector2.y , vector1.z - vector2.z)
   return new

def translate_point(point, vector):
   new = data.Point (point.x + vector.x , point.y + vector.y , point.z + vector.z)
   return new

def vector_from_to(from_point,to_point):
   new = data.Vector (to_point.x - from_point.x, to_point.y - from_point.y , to_point.z - from_point.z)
   return new

def scale_ray(ray,scalar):
   vector = data.Vector (ray.dir.x * scalar, ray.dir.y * scalar, ray.dir.z * scalar)
   new = data.Ray (ray.pt, vector)
   return new

