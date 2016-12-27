import math
import data
from vector_math import *

def sphere_intersection_point(ray,sphere):

    a = dot_vector(ray.dir,ray.dir)

    b = 2*(dot_vector((difference_point(ray.point,sphere.center)),ray.dir))

    c_diff_pt1 = difference_point(ray.point,sphere.center)
    c_diff_pt2 = difference_point(ray.point,sphere.center)
    c = (dot_vector(c_diff_pt1,c_diff_pt2))-sphere.radius**2

    if ((((b**2) - (4*a*c))) < 0):
       return None
    else:
       t1 = ((-b) + (((b**2) - (4*a*c)))**0.5)/(2*a)
       t2 = ((-b) - (((b**2) - (4*a*c)))**0.5)/(2*a)

    if (t1 >= 0 and t2 >= 0):

       if (t1 <= t2):
          pointT = translate_point(ray.point,scale_vector(ray.dir,t1))
          return pointT

       else:
          pointT = translate_point(ray.point,scale_vector(ray.dir,t2))
          return pointT

    elif (t1 >= 0 and t2 < 0):
       pointT = translate_point(ray.point,scale_vector(ray.dir,t1))
       return pointT

    elif (t1 < 0  and t2 >= 0):
       pointT = translate_point(ray.point,scale_vector(ray.dir,t2))
       return pointT

    else:
       return None

def find_intersection_points(sphere_list,ray):
    l = []
    for n in range(0,len(sphere_list)):

       if sphere_intersection_point(ray, sphere_list[n]) != None:
          sphere_intersec = sphere_intersection_point(ray,sphere_list[n])
          points = (sphere_list[n],sphere_intersec)
          l.append(points)

    return l


def sphere_normal_at_point(sphere,point):
    move_vector = vector_from_to(sphere.center,point)
    norm_vector = normalize_vector(move_vector)
    return norm_vector