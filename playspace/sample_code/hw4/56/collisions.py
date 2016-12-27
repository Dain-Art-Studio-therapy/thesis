import data
import math
import vector_math

def sphere_intersection_point(ray, sphere):
   A = vector_math.length_vector(ray.dir) ** 2
   B = 2 * vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), ray.dir)
   C = vector_math.length_vector(vector_math.difference_point(ray.pt, sphere.center)) ** 2 - sphere.radius ** 2

   determinate = B ** 2 - (4 * A * C)
   if determinate < 0:
      return None
   t1 = (-1 * B - math.sqrt(determinate)) / (2 * A)
   t2 = (-1 * B + math.sqrt(determinate)) / (2 * A)
   t = 0

   if t1 >= 0 and t2 >= 0:
      if t1 < t2:
         t = t1
      else:
         t = t2
   elif t1 >= 0 and t2 < 0:
      t = t1
   elif t1 < 0 and t2 >= 0:
      t = t2
   elif t1 < 0 and t2 < 0:
      return None

   point =  vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t))
   return point 

def find_intersection_points(sphere_list, ray):
   if sphere_list == []:
      return None

   intersections = []
   for s in sphere_list:
      i = sphere_intersection_point(ray, s)
      if i != None:
         intersections.append((s, i))
   if intersections == []:
      return None
   return intersections

def sphere_normal_at_point(sphere, point):
   vector = vector_math.vector_from_to(sphere.center, point)
   return vector_math.normalize_vector(vector)
