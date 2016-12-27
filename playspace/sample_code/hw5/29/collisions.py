from vector_math import *
import math
from data import *

def sphere_intersection_point(ray,sphere):
    A = dot_vector(ray.dir,ray.dir)
    diff = difference_point(ray.pt,sphere.center)
    B = 2*dot_vector(diff,ray.dir)
    C = dot_vector(diff,diff) - (sphere.radius**2)
    if ((B**2) - (4 * A * C)) >= 0:
        t0 = (-B + math.sqrt((B**2) - (4 * A * C)))/(2 * A)
        t1 = (-B - math.sqrt((B**2) - (4 * A * C)))/(2 * A)
        if t0 >= 0 and t1 >= 0:
            if t0 <= t1:
                t = t0
            else:
                t = t1
        elif t0 >= 0:
            t = t0
        elif t1 >= 0:
            t = t1
        else:
            return None
        Pt = translate_point(ray.pt,scale_vector(ray.dir,t))
        return Pt
    else:
        return None

def find_intersection_points(sphere_list,ray):
    sphere_intersection_list = []
    for sphere in sphere_list:
        intersection = sphere_intersection_point(ray,sphere)
        if intersection != None:
            sphere_intersection_list.append((sphere,intersection))
    return sphere_intersection_list        

def sphere_normal_at_point(sphere,point):
    v = vector_from_to(sphere.center,point)
    if length_vector(v)==1:
        return v
    else:
        newVec = normalize_vector(v)
        return newVec
