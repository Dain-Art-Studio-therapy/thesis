import utility
import data
from math import sqrt


def scale_vector(vec, scalar):
   return data.Vector((vec.x * scalar), (vec.y * scalar), (vec.z * scalar))

def dot_vector(vec1, vec2):
   return ((vec1.x * vec2.x) + (vec1.y * vec2.y) + (vec1.z * vec2.z))

def length_vector(vec):
   return sqrt(vec.x**2 + vec.y**2 + vec.z**2)
   
def normalize_vector(vec):
   return scale_vector(vec, 1.0 / length_vector(vec))

def difference_point(pt1, pt2):
   return data.Vector((pt1.x - pt2.x), (pt1.y-pt2.y), (pt1.z-pt2.z))

def difference_vector(vec1, vec2):
   return data.Vector((vec1.x - vec2.x), (vec1.y-vec2.y), (vec1.z-vec2.z))

def point_distance(pt1, pt2):
   return sqrt((pt1.x - pt2.x)**2 + (pt1.y-pt2.y)**2 + (pt1.z-pt2.z)**2)

def translate_point(pt, vec):
   return data.Point((pt.x + vec.x), (pt.y + vec.y), (pt.z + vec.z))
   
def vector_from_to(from_point, to_point):
   return data.Vector((to_point.x - from_point.x), (to_point.y - from_point.y), 
      (to_point.z - from_point.z))
