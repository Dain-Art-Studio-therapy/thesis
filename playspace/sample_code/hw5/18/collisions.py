import unittest
import math
from data import *
from vector_math import *

def sphere_intersection_point(ray, sphere):
    A = dot_vector(ray.dir, ray.dir)
    b0 = difference_point(ray.pt, sphere.center)
    b1 = scale_vector(b0, 2)
    B = dot_vector(b1, ray.dir)
    C = dot_vector(b0,b0) - sphere.radius**2
    discr = B**2 - 4*A*C

    if discr < 0:
      return None
    elif discr == 0:
      t1 = -B/(2*A)
      if t1 >=0:
         return translate_point(ray.pt, scale_vector(ray.dir, t1))
      else:
         return None
    else:
      t_1 = (-B + math.sqrt(discr))/(2*A)
      t_2 = (-B - math.sqrt(discr))/(2*A)
      if t_1 >= 0 and t_2 >= 0:
        return translate_point(ray.pt, scale_vector(ray.dir, min(t_1, t_2)))
      elif t_1 < 0 and t_2 < 0:
        return None
      elif t_1 >= 0:
         return translate_point(ray.pt, scale_vector(ray.dir, t_1))
      else:
         return translate_point(ray.pt, scale_vector(ray.dir, t_2))
         

def find_intersection_points(sphere_list, ray):
    PointList = [sphere_intersection_point(ray, sphere_list[i]) for i in range(len(sphere_list))]
    final = [(sphere_list[i], PointList[i]) for i in range(len(PointList)) if PointList[i] != None]
    return final

def sphere_normal_at_point(sphere, point):
    v = vector_from_to(sphere.center, point)
    v2 = normalize_vector(v)
    return v2
