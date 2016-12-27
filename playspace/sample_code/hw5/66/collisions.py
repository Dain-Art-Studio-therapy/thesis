import data
import vector_math
import math


def sphere_intersection_point(ray, sphere):
   a = vector_math.dot_vector(ray.dir, ray.dir)
   
   v1 = vector_math.difference_vector(ray.pt, sphere.center)
   v2 = vector_math.scale_vector(v1, 2)
   b = vector_math.dot_vector(v2, ray.dir)

   c = vector_math.dot_vector(v1, v1) - (sphere.radius**2)

   if b**2 - 4*a*c < 0:
      return None

   t1 = (-b + math.sqrt(b**2-4*a*c)) / (2.0*a)
   t2 = (-b - math.sqrt(b**2-4*a*c)) / (2.0*a)

   pt1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
   pt2 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t2))

   if t1 >= 0 and t2 >= 0:   # both positive
      if t1 > t2:
         return pt2
      else:
         return pt1

   if t1 >= 0 and t2 < 0:    # t2 negative
      return pt1

   if t2 >= 0 and t1 < 0:    # t1 negative
      return pt2

   if t1 < 0 and t2 < 0:     # both negative
      return None 

   if t1 == t2:               # t1 and t2 are equal
      if t1 >= 0:
         return pt1
      else:
         return None

def find_intersection_points(sphere_list, ray):
   newlist = []
   for e in sphere_list:
      pt = sphere_intersection_point(ray, e)
      if pt != None:
         newlist.append((e, pt))
   return newlist

def sphere_normal_at_point(sphere, point):
   v = vector_math.vector_from_to(sphere.center, point)
   return vector_math.normalize_vector(v)
