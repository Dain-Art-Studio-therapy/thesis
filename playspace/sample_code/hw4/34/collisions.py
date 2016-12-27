import math
from data import *
import utility
from vector_math import *

def sphere_intersection_point(ray, sphere):
   a = dot_vector(ray.dir, ray.dir)
   b = 2 * (dot_vector(difference_point(ray.pt, sphere.center), ray.dir))
   c = dot_vector(difference_point(ray.pt, sphere.center), difference_point(ray.pt, sphere.center)) - sphere.radius**2

   if b**2 - 4*a*c <0:
      return None
   
   t1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a) 
   t2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
   point1 = translate_point(ray.pt, scale_vector(ray.dir, t1))
   point2 = translate_point(ray.pt, scale_vector(ray.dir, t2))

   if t1 == t2:
      if t1>0:
         return point1
      elif t1==0:
         return point1
      elif t1<0:
         return None

   elif t1>0 and t2>0:
      if t1>t2:
         return point2
      elif t2>t1:
         return point1

   elif t1>0 and t2<0:
      return point1

   elif t1<0 and t2>0:
      return point2


def find_intersection_points(sphere_list, ray):
   newList = []
   for sphere in sphere_list:
      if sphere_intersection_point(ray,sphere) != None:
         newList.append((sphere,sphere_intersection_point(ray,sphere)))
   return newList


def sphere_normal_at_point(sphere, point):
   vector_from_center_out = vector_from_to(sphere.center, point)
   length = length_vector(vector_from_center_out)
   return normalize_vector(vector_from_center_out, length)


















