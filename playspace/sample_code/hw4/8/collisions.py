# Name: Allison Lee
# Instructor: Aaron Keen
# Section: 09

import utility
import data
import vector_math
import math

def sphere_intersection_point(ray,sphere):
    A = vector_math.dot_vector(ray.d,ray.d)
    B = 2*(vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center),ray.d))
    C = (vector_math.dot_vector(vector_math.difference_point(ray.pt,sphere.center),vector_math.difference_point(ray.pt,sphere.center)))-(sphere.radius**2)

    d = (B**2)-(4*A*C)

    if d<0:
        return None
    elif d == 0:
        pt1 = -B/(2*A)
        point1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.d, pt1))

        if pt1 >=0:
            return point1
    else: 
        pt1 = (-B+math.sqrt(d))/(2*A)
        pt2 = (-B-math.sqrt(d))/(2*A)
        point1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.d,pt1))
        point2 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.d,pt2))

        if pt1 >=0 and pt2 >=0:
            if pt1<pt2:
                return point1
            else:
                return point2
        elif pt1<0 and pt2<0:
            return None
        else:
            return point1

def find_intersection_points(sphere_list, ray):
    #checks for intersection between ray and each sphere on list. return list of tuples with found intersections. determines sphere_intersection_point and adds pair to list.

    solutions = []

    for sphere in sphere_list:
        sol = sphere_intersection_point(ray,sphere)

        if sol is None:
            pass
        else:
            solutions.append((sphere,sol))
            
    return solutions


def sphere_normal_at_point(sphere, point):
    v = vector_math.vector_from_to(sphere.center,point)
    normalized = vector_math.normalize_vector(v)
    return normalized

        
