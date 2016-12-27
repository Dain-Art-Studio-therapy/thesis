import math
from data import *
from vector_math import *


def small_positive_quadratic_root(a, b, c):
   disc = (b**2) - (4 * a * c)

   if (disc >= 0):
      r1 = (-b + math.sqrt(disc)) / (2 * a)
      r2 = (-b - math.sqrt(disc)) / (2 * a)
      if r1 > 0 and r2 > 0:
         if r1 < r2:
            return r1
         return r2
      elif r1 > 0:
         return r1
      elif r2 > 0:
         return r2
      else:
         return None
   else:
      return None


def sphere_intersection_point(ray, sphere):
   A = dot_vector(ray.dir, ray.dir)
   B = dot_vector((scale_vector(difference_point(ray.pt, sphere.center), 2)), 
      ray.dir)
   C = (dot_vector(difference_point(ray.pt, sphere.center), 
      difference_point(ray.pt, sphere.center)) - sphere.radius ** 2)
   t = small_positive_quadratic_root(A, B, C)

   if (t != None):
      return translate_point(ray.pt, scale_vector(ray.dir, t))
   else:
      return None


def find_intersection_points(sphere_list, ray):
   resultList = []
   for i in range(len(sphere_list)):
      if sphere_intersection_point(ray, sphere_list[i]) != None:
         new = sphere_intersection_point(ray, sphere_list[i])
         resultList.append((sphere_list[i], new))
   return resultList


def sphere_normal_at_point(sphere, point):
   vector = vector_from_to(sphere.center, point)
   return normalize_vector(vector)
