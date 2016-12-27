import math
import data

def scale_vector(Vector,scalar):
    return data.Vector(Vector.x*scalar,Vector.y*scalar,Vector.z*scalar)
def dot_vector(vector1,vector2):
    return vector1.x*vector2.x+vector1.y*vector2.y+vector1.z*vector2.z
def length_vector(Vector):
    return math.sqrt((Vector.x)**2+(Vector.y)**2+(Vector.z)**2)
def normalize_vector(vector):
    invlen=1/length_vector(vector) #inverselength
    return scale_vector(vector,invlen)
def difference_point(point1,point2):
    return data.Vector(point1.x-point2.x,pont1.y-point2.y, point1.z-point2.z)
def difference_vector(vector1,vector2):
    return data.Vector(vector1.x-vector2.x,vector1.y-vector2.y,vector1.z-vector2.z)
def translate_point(point,vector):
    return data.Point(point.x+vector.x,point.y+vector.y,point.z+vector.z)
def vector_from_to(from_point,to_point):
    return data.Vector(to_point.x-from_point.x,to_point.y-from_point.y,to_point.z-from_point.z)

