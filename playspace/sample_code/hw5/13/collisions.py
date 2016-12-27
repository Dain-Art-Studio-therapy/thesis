import math
from vector_math import *
import data

def sphere_intersection_point(ray, sphere):
   A = dot_vector(ray.dir, ray.dir)
   B = dot_vector(scale_vector(difference_point(ray.pt,sphere.center),2), ray.dir)
   C = dot_vector(difference_point(ray.pt,sphere.center), difference_point(ray.pt,  sphere.center)) - sphere.radius ** 2
   if ((B ** 2) - 4 * A * C) >= 0:
      T1 = (-B - math.sqrt((B**2) - 4 * A * C))/(2 * A)
      T2 = (-B + math.sqrt((B**2) - 4 * A * C))/(2 * A)
      P1 = translate_point(ray.pt, scale_vector(ray.dir, T1))
      P2 = translate_point(ray.pt, scale_vector(ray.dir, T2))
      if T1 > T2 > 0:
         return P2
      elif T2 > T1 > 0:
         return P1
      elif T1 < 0 and T2 < 0:
         return None
      elif T1 > 0 and T2 < 0:
         return P1
      elif T1 < 0 and T2 > 0:
         return P2
      else:
         return P1

def find_intersection_points(sphere_list, ray):
   newlist = []   
   for s in sphere_list:
     if sphere_intersection_point(ray, s) is not None:
        newlist.append((s, sphere_intersection_point(ray, s)))
   return newlist

def sphere_normal_at_point(sphere, point):
   V1 = vector_from_to(sphere.center, point)   
   V2 = normalize_vector(V1)
   return V2
