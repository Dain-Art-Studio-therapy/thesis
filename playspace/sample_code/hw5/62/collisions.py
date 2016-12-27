import data
import math
import utility
import vector_math

def scale_vector(vector, scalar):
    scaled = data.Vector(vector.x*scalar, vector.y*scalar, vector.z*scalar)
    return scaled

def dot_vector(vector1, vector2):
    product = (vector1.x * vector2.x) + (vector1.y * vector2.y) + (vector1.z * vector2.z)
    return product

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

def length_vector(vector):
    thelength = math.sqrt((vector.x)**2 + (vector.y)**2 + (vector.z)**2)
    return thelength

def normalize_vector(vector):
    veclen = math.sqrt((vector.x)**2 + (vector.y)**2 + (vector.z)**2)
    normal = data.Vector(vector.x/veclen, vector.y/veclen, vector.z/veclen)
    return normal

def vector_from_to(from_point, to_point):
    vecfromto = data.Vector(to_point.x-from_point.x, to_point.y-from_point.y, to_point.z-from_point.z)
    return vecfromto






def sphere_intersection_point(Ray, Sphere):
    A = (dot_vector(Ray.dir, Ray.dir))
    B = dot_vector(scale_vector((difference_point(Ray.pt, Sphere.center)), 2),Ray.dir)
    C_half = dot_vector((difference_point(Ray.pt, Sphere.center)), (difference_point(Ray.pt,Sphere.center))) 
    C = C_half - (Sphere.radius)**2


    if (B**2 - 4*A*C > 0):
        t = [(-B + math.sqrt(B**2 - 4*A*C))/(2*A), (-B -math.sqrt(B**2 - 4*A*C))/(2*A)]
        if (t[0] >= 0 and t[1] >=0):
             if (t[1] < t[0]):
                 return translate_point(Ray.pt,scale_vector(Ray.dir, t[1]))
             else:
                 return translate_point(Ray.pt, scale_vector(Ray.dir, t[0]))
        elif (t[0] <0 and t[1] <0):
             return None
        elif (t[0] >=0 and t[1] <0):
             return translate_point(Ray.pt, scale_vector(Ray.dir, t[0]))
        elif (t[1] >=0 and t[0] <0):
             return translate_point(Ray.pt, scale_vector(Ray.dir, t[1]))
    elif (B**2 - 4*A*C == 0):
        t1 = -B/(2*A)
        if t1 >=0:
             return translate_point(Ray.pt, scale_vector(Ray.dir, t1))
        else:
             return None
    else:
        return None


def find_intersection_points(sphere_list, ray):
    intlist = []
    for sp in sphere_list:
        S = sphere_intersection_point(ray,sp)
        if S != None:
            intlist.append((sp,S))
    return intlist


def sphere_normal_at_point(sphere,point):
    return normalize_vector(vector_from_to(sphere.center,point))
    

 














    
