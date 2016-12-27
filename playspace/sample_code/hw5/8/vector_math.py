import math
import data


def scale_vector(vector, scalar):
    x = vector.x * scalar
    y = vector.y * scalar
    z = vector.z * scalar

    return data.Vector(x,y,z)

def dot_vector(vector1, vector2):
    v1x = vector1.x
    v1y = vector1.y
    v1z = vector1.z
    v2x = vector2.x
    v2y = vector2.y
    v2z = vector2.z

    return (v1x * v2x) + (v1y * v2y) + (v1z * v2z)

def length_vector(vector):
    x = vector.x
    y = vector.y
    z = vector.z
    return math.sqrt(x**2+y**2+z**2)


def normalize_vector(vector):
    return scale_vector(vector,1/length_vector(vector))

def difference_point(point1, point2):
    x = point1.x - point2.x
    y = point1.y - point2.y
    z = point1.z - point2.z

    return data.Vector(x,y,z)

def difference_vector(vector1, vector2):
    x = vector1.x - vector2.x
    y = vector1.y - vector2.y
    z = vector1.z - vector2.z

    return data.Vector(x,y,z)

def translate_point(point, vector):
    x = point.x + vector.x
    y = point.y + vector.y
    z = point.z + vector.z

    return data.Point(x,y,z)

def vector_from_to(from_point, to_point):
    x = to_point.x - from_point.x
    y = to_point.y - from_point.y
    z = to_point.z - from_point.z

    return data.Vector(x,y,z)