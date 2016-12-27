import data
import math

def scale_vector(vector,scalar):
    new_vec=data.Vector(vector.x*scalar,vector.y*scalar,vector.z*scalar)
    return new_vec

def dot_vector(vector1,vector2):
    return vector1.x*vector2.x+vector1.y*vector2.y+vector1.z*vector2.z

def length_vector(vector):
    return math.sqrt(vector.x**2+vector.y**2+vector.z**2)

def normalize_vector(vector):
    length= length_vector(vector)
    new_vec=data.Vector(vector.x/length,vector.y/length, vector.z/length)
    return new_vec

def difference_point(point1,point2):
    new_vec=data.Vector(point1.x-point2.x,point1.y-point2.y, point1.z-point2.z)
    return new_vec

def difference_vector(vector1,vector2):
    new_vec=data.Vector(vector1.x-vector2.x,vector1.y-vector2.y,vector1.z-
    vector2.z)
    return new_vec

def translate_point(point,vector):
    trans_pt=data.Point(point.x+vector.x,point.y+vector.y,point.z+vector.z)
    return trans_pt

def vector_from_to(from_point,to_point):
    return difference_point(to_point,from_point)    

def calc_dist(point1,point2):
   return math.sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2+ (point1.z-point2.z)**2 )