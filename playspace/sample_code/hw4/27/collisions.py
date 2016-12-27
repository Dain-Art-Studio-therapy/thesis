import math
import unittest
from vector_math import *
from data import *

def sphere_intersection_point(ray, sphere):
        a = dot_vector(ray.dir, ray.dir)
        b = dot_vector(scale_vector(difference_point(ray.pt, sphere.center), 2), ray.dir)
        c = dot_vector(difference_point(ray.pt,  sphere.center), difference_point(ray.pt, sphere.center)) - (sphere.radius ** 2)
        d = (b*b) - (4 * a * c)
        if d < 0:
                return None
        t1 = ((-b + math.sqrt(d)) / (2 * a))
        t2 = ((-b - math.sqrt(d)) / (2 * a))
        if t1 >= 0 and t2 >= 0:
                t = min(t1, t2)
        if t1 <= 0 and t2 <= 0:
                return None
        if t1 >= 0 and t2 <= 0:
                t = t1
        if t2 >= 0 and t1 <= 0:
                t =  t2
        if t1 == t2:
                t =  t1

        scale_vector1 = scale_vector(ray.dir, t)
        point = translate_point(ray.pt, scale_vector1)
        return point

def find_intersection_points(sphere_list, ray):
        new_sphere_list = []
        for sphere in sphere_list:
                if sphere_intersection_point(ray, sphere) is not None:
                        new_sphere_list.append((sphere, sphere_intersection_point(ray, sphere)))
	return new_sphere_list

def sphere_normal_at_point(sphere, point):
	return normalize_vector(vector_from_to(sphere.center, point))


