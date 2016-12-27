from data import *
from math import *
from vector_math import *

def sphere_intersection_point(ray, sphere):
   a = dot_vector(ray.dir, ray.dir)
   b = dot_vector(scale_vector(difference_point(ray.pt, sphere.center), 2), ray.dir)
   c = dot_vector(difference_point(ray.pt, sphere.center), difference_point(ray.pt, sphere.center)) - sphere.radius**2
   discriminant = b**2 - 4 * a * c
   if discriminant < 0:
      return None
   bigt = ((b * -1) + sqrt(discriminant))/ (2 * a)
   smallt = ((b * -1) - sqrt(discriminant))/ (2 * a)
   if bigt >= 0 and smallt >= 0:
      return translate_point(ray.pt, scale_vector(ray.dir, smallt))
   elif bigt < 0 and smallt < 0:
      return None
   elif bigt >= 0 and smallt < 0:
      return translate_point(ray.pt, scale_vector(ray.dir, bigt))
   
def find_intersection_points(sphere_list, ray):
   intersectionlist = []
   for sph in sphere_list:
      pt = sphere_intersection_point(ray, sph)
      if pt is None:
         pass
      else:
         intersectionlist.append((sph, pt))
   return intersectionlist

def sphere_normal_at_point(sphere, point):
   return normalize_vector(vector_from_to(sphere.center, point))  
