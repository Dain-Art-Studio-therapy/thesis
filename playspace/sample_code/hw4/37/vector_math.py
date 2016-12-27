import data
import math

def scale_vector(vector, scalar):
    return data.Vector(vector.x*scalar, vector.y*scalar, vector.z*scalar)

def dot_vector(vector1, vector2):
    return vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z

def length_vector(vector):
    return math.sqrt(dot_vector(vector, vector))

def normalize_vector(vector):
    return scale_vector(vector, 1/length_vector(vector))

def difference_point(point1, point2):
    #from point2 to point1
    x = point1.x - point2.x
    y = point1.y - point2.y
    z = point1.z - point2.z
    return data.Vector(x, y, z)
    
def difference_vector(vector1, vector2):
    x = vector1.x - vector2.x
    y = vector1.y - vector2.y
    z = vector1.z - vector2.z
    return data.Vector(x, y, z)

def translate_point(point, vector):
    x = point.x + vector.x
    y = point.y + vector.y
    z = point.z + vector.z
    return data.Point(x, y, z)
    
def vector_from_to(from_point, to_point):
    return difference_point(to_point, from_point)