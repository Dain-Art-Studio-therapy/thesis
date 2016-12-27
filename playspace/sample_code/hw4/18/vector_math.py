from data import *
import math

def scale_vector(vector, scalar):
    return Vector(vector.x * scalar, vector.y * scalar, vector.z * scalar)

def dot_vector(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

def length_vector(vector):
    return math.sqrt((vector.x ** 2) + (vector.y ** 2) + (vector.z ** 2))

def normalize_vector(v):
    return scale_vector(v, 1 / length_vector(v))

def difference_point(pt1, pt2):
    return Vector(pt1.x - pt2.x , pt1.y - pt2.y , pt1.z - pt2.z)

def difference_vector(v1, v2):
    return Vector(v1.x - v2.x , v1.y - v2.y , v1.z - v2.z)

def translate_point(pt, v):
    return Point(pt.x + v.x, pt.y + v.y, pt.z + v.z)

def vector_from_to(from_pt, to_pt):
    return Vector(to_pt.x - from_pt.x, to_pt.y - from_pt.y, to_pt.z - from_pt.z)


    
