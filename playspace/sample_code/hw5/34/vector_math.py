import math
import data

def scale_vector(vector, scalar):
    scaledvector = data.Vector(vector.x, vector.y, vector.z)
    scaledvector.x = scaledvector.x * scalar
    scaledvector.y = scaledvector.y * scalar
    scaledvector.z = scaledvector.z * scalar
    return scaledvector

def dot_vector(vector1, vector2):
    return (vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z)

def length_vector(vector):
    return math.sqrt(vector.x**2 + vector.y**2 + vector.z**2)

def normalize_vector(vector):
    l=length_vector(vector)
    normalizedvector = data.Vector(vector.x, vector.y, vector.z)
    normalizedvector.x = normalizedvector.x/l
    normalizedvector.y = normalizedvector.y/l
    normalizedvector.z = normalizedvector.z/l
    return normalizedvector

def difference_point(point1, point2):
    dx = point1.x-point2.x
    dy = point1.y-point2.y
    dz = point1.z-point2.z
    differencevector = data.Vector(dx, dy, dz)
    return differencevector

def difference_vector(vector1, vector2):
    dx = vector1.x-vector2.x 
    dy = vector1.y-vector2.y
    dz = vector1.z-vector2.z
    differencevector = data.Vector(dx, dy, dz)   
    return differencevector

def translate_point(point, vector):
    dx = point.x + vector.x  
    dy = point.y + vector.y 
    dz = point.z + vector.z
    differencepoint = data.Point(dx, dy, dz)
    return differencepoint

def vector_from_to(from_point, to_point):
    return difference_point(to_point, from_point)


  
