import math
import data

def scale_vector(v,s):
    return data.Vector(v.x*s,v.y*s,v.z*s)

def dot_vector(v1,v2):
    return ((v1.x*v2.x)+(v1.y*v2.y)+(v1.z*v2.z))

def length_vector(v):
    return (math.sqrt((v.x*v.x)+(v.y*v.y)+(v.z*v.z)))
            
def normalize_vector(v):
    return scale_vector(v,1/length_vector(v))

def difference_point(point1,point2):
    return data.Vector(point1.x-point2.x,point1.y-point2.y,point1.z-point2.z)

def difference_vector(v1,v2):
    return data.Vector(v1.x-v2.x,v1.y-v2.y,v1.z-v2.z)

def translate_point(p,v):
    return data.Point(p.x+v.x,p.y+v.y,p.z+v.z)

def vector_from_to(from_point,to_point):
    return difference_point(to_point,from_point)




