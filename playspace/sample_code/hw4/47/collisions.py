from data import *
from vector_math import *
from math import sqrt

def quadratic(A, B, C):
    
    determinant = B**2.0 - 4.0*A*C
    if determinant < 0:
        return None

    d = sqrt(determinant)
        
    x1 = (-B + d) / (A*2.0)
    x2 = (-B - d) / (A*2.0)

    if x1 < 0 and x2 < 0:
        return None
    elif x1 < 0 or x2 < 0:
        return max(x1, x2)
    else:
        return min(x1, x2)


def sphere_intersection_point(ray, sphere):

    A = dot_vector(ray.dir, ray.dir)
    z = difference_point(ray.pt, sphere.center)
    B = dot_vector(z, ray.dir)*2.0
    C = dot_vector(z, z) - sphere.radius**2.0

    if A == 0 and C == 0:      # in case ray.pt lies on sphere
        return ray.pt          # but has zero vector component
    elif A == 0 and C != 0:    # also to prevent divide by 0
        return None            # in quadratic function

    t = quadratic(A, B, C)

    if t == None:
        return None
    else:
        return translate_point(ray.pt, scale_vector(ray.dir, t))


def find_intersection_points(sphere_list, ray):
    
    return [
        (sphere, sphere_intersection_point(ray, sphere)) 
        for sphere in sphere_list 
        if sphere_intersection_point(ray, sphere) != None
        ]


def sphere_normal_at_point(sphere, point):

    return normalize_vector(vector_from_to(sphere.center, point))
