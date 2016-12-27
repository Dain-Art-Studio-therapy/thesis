from data import *
import math
from vector_math import *

def sphere_intersection_point(ray, sphere):
   a = dot_vector(ray.dir, ray.dir)
   b = dot_vector(scale_vector(difference_point(ray.pt, sphere.center), 2), ray.dir)
   c = dot_vector(difference_point(ray.pt, sphere.center), 
   difference_point(ray.pt, sphere.center)) - (sphere.radius ** 2)

   t = quadratic(a, b, c)

   if t == None:
      return None

   else:
      return translate_point(ray.pt, scale_vector(ray.dir, t))

def find_intersection_points(sphere_list, ray):
   return [(s, sphere_intersection_point(ray, s))
   for s in sphere_list if sphere_intersection_point(ray, s)]

def sphere_normal_at_point(sphere, point):
   return normalize_vector(vector_from_to(sphere.center,
   point))

def quadratic(a, b, c):
   discrim = b**2 - 4*a*c
   if discrim < 0:
      return None
   else:
      t1 = (-b + math.sqrt(discrim))/(2*a)
      t2 = (-b - math.sqrt(discrim))/(2*a)
   
      if t1 > 0 and t2 >0:
         return min(t1, t2)

      elif t1 < 0 and t2 < 0:
         return None

      elif t1 < 0 and t2 > 0:
         return t2
     
      elif t1 > 0 and t2 < 0:
         return t1
     
      elif t1 == t2:
         return t1

def show_me(spheres, ray):
   print find_intersection_points(spheres, ray)
