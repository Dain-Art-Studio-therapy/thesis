# Han Tran | CPE 101-01,02 | Professor: Aaron Keen
import math
import data

# Scale
def scale_vector(vector, scalar):
   return data.Vector(vector.x*scalar, vector.y*scalar, vector.z*scalar)


# Dot Product
def dot_vector(vector1, vector2):
   return (vector1.x * vector2.x + vector1.y * vector2.y + vector1.z*vector2.z)


# Length
def length_vector(vector):
   return math.sqrt(vector.x**2 + vector.y**2 + vector.z**2)

  
# Normalize Vector
def normalize_vector(vector):
   return data.Vector(vector.x/length_vector(vector), vector.y/length_vector(vector), vector.z/length_vector(vector))


# Point Difference
def difference_point(point1, point2):
   return data.Vector(point1.x - point2.x, point1.y - point2.y, point1.z - point2.z)


# Vector Difference
def difference_vector(vector1, vector2):
   return data.Vector(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)
   

# Translate Point
def translate_point(point, vector):
   return data.Point(point.x + vector.x, point.y + vector.y, point.z + vector.z)

   
# Vector From To
def vector_from_to(from_point, to_point):
   return data.Vector(to_point.x - from_point.x, to_point.y - from_point.y, to_point.z - from_point.z)

