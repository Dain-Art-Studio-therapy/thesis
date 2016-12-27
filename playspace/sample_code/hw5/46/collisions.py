from data import *
from math import sqrt
from vector_math import *


def sphere_intersection_point(ray, sphere):
    A = dot_vector(ray.dir, ray.dir)
    B = (2 * dot_vector(difference_point(ray.pt, sphere.center), ray.dir))
    C = (dot_vector(difference_point(ray.pt, sphere.center), 
                    difference_point(ray.pt, sphere.center)) - 
                    (sphere.radius ** 2))
    dsc = (B ** 2) - (4.0 * A * C)
    if dsc < 0:
        return None
    t = ((-B + sqrt(dsc)) / (2.0 * A))
    t2 = ((-B - sqrt(dsc)) / (2.0 * A))
    if(0 <= t2 <= t):
        return translate_point(ray.pt, scale_vector(ray.dir, t2))
    elif(t >= 0):
        return translate_point(ray.pt, scale_vector(ray.dir, t))


def find_intersection_points(sphere_list, ray):
    intersect_list = []
    for sphere in sphere_list:
        if (sphere_intersection_point(ray, sphere) != None):
            intersect_list.append((sphere, sphere_intersection_point(ray, 
                                                                     sphere)))
    return intersect_list


def sphere_normal_at_point(sphere, point): #point assumed to be on sphere
    vec = vector_from_to(sphere.center, point)
    vec = normalize_vector(vec)
    return vec

