from vector_math import *
import math

def sphere_intersection_point(ray, sphere):
    A = dot_vector(ray.dir,ray.dir)
    B = 2 * (dot_vector(difference_point(ray.pt, sphere.center), ray.dir))
    C = dot_vector(difference_point(ray.pt, sphere.center), \
    difference_point(ray.pt, sphere.center)) - sphere.radius ** 2
    discriminant = B**2 - 4 * A * C
    if discriminant > 0:
        t1 = (-B + math.sqrt(discriminant))/(2*A)
        t2 = (-B - math.sqrt(discriminant))/(2*A)
        if t1 < 0:
            return None
        elif t1 < t2:
            usedt = t1
        else:
            usedt = t2
        intersection_point = translate_point(ray.pt, 
        scale_vector(ray.dir, usedt))
        return intersection_point
    elif discriminant == 0:
        t = (-B)/(2 * A)
        return translate_point(ray.pt, scale_vector(ray.dir, t))
    else:
        return None

def find_intersection_points(sphere_list, ray):
    spheres = []
    for sphere in sphere_list:
        intersection = sphere_intersection_point(ray, sphere)
        if intersection is not None:
            spheres.append((sphere, intersection))
    return spheres

def sphere_normal_at_point(sphere, point):
    vector = vector_from_to(sphere.center, point)
    return normalize_vector(vector)