from data import *
from vector_math import *
import math

def sphere_intersection_point(ray, sphere):
   a = dot_vector(ray.dir, ray.dir)
   x = difference_point(ray.pt, sphere.center)
   b = dot_vector(scale_vector(x, 2), ray.dir)
   c = dot_vector(x, x) - (sphere.radius ** 2)
   if (b ** 2 - 4 * a *c) >= 0:
      d = math.sqrt(b ** 2 - 4 * a * c)
      t1 = (-b - d)/(2 * a)
      t2 = (-b + d)/(2 * a)
   else:
      return None
   if (t1 >= 0) and (t2 >= 0):
      scaledRayDir = scale_vector(ray.dir, t1)
      return translate_point(ray.pt, scaledRayDir)
   elif (t1 < 0) and (t2 >= 0):
      scaledRayDir = scale_vector(ray.dir, t2)
      return translate_point(ray.pt, scaledRayDir)
   elif (t1 >= 0) and (t2 < 0):
      scaledRayDir = scale_vector(ray.dir, t1)
      return translate_point(ray.pt, scaledRayDir)
   else:
      return None

def find_intersection_points(sphere_list, ray):
   newlist = []
   for n in sphere_list:
      spheretest = sphere_intersection_point(ray, n)
      if spheretest != None:
         newlist.append((n, spheretest))
   return newlist

def sphere_normal_at_point(sphere, point):
   return normalize_vector(vector_from_to(sphere.center, point))
