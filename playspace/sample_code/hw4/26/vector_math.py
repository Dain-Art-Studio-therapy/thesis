import data
import math

def scale_vector(vector, scalar):
    scaled = data.Vector(vector.x*scalar, vector.y*scalar, vector.z*scalar)
    return scaled

def dot_vector(vector1, vector2):
    product = (vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z)
    return product

def length_vector(vector):
    thelength = math.sqrt((vector.x)**2 + (vector.y)**2 + (vector.z)**2)
    return thelength

def normalize_vector(vector):
    veclen = math.sqrt((vector.x)**2 + (vector.y)**2 + (vector.z)**2)
    normal = data.Vector(vector.x/veclen, vector.y/veclen, vector.z/veclen)
    return normal

def difference_point(point1, point2):
    diff = data.Vector(point1.x-point2.x, point1.y - point2.y, point1.z - point2.z)
    return diff

def difference_vector(vector1, vector2):
    diffvec = data.Vector(vector1.x-vector2.x,vector1.y-vector2.y,vector1.z-vector2.z)
    return diffvec

def translate_point(point, vector):
    translated = data.Point(point.x + vector.x, point.y + vector.y, point.z+ vector.z)
    return translated

def vector_from_to(from_point, to_point):
    vecfromto = data.Vector(to_point.x-from_point.x, to_point.y-from_point.y, to_point.z-from_point.z)
    return vecfromto


    
    
    
    


    

    

    
