from data import *
from vector_math import *
from math import sqrt

def sphere_intersection_point(ray, sphere):
   a = dot_vector(ray.dir, ray.dir)
   b = 2 * dot_vector(difference_point(ray.pt, sphere.center), ray.dir)
   c = dot_vector(difference_point(ray.pt, sphere.center), difference_point(ray.pt, sphere.center)) - sphere.radius**2

   if b**2 < 4*a*c:
      return None

   t1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
   t2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

   if t1 >= 0 and t2 >= 0:
      return translate_point(ray.pt, (scale_vector(ray.dir, min(t1, t2))))
   elif t1 >= 0:
      return translate_point(ray.pt, (scale_vector(ray.dir, t1)))
   elif t2 >= 0:
      return translate_point(ray.pt, (scale_vector(ray.dir, t2)))
   else:
      return None

   
def find_intersection_points(sphere_list, ray):
   l = []

   for sphere in sphere_list:
      pt = sphere_intersection_point(ray, sphere)
      if pt is not None:
         l.append((sphere, pt))

   return l

def sphere_normal_at_point(sphere, point):
   return normalize_vector(vector_from_to(sphere.center, point))
