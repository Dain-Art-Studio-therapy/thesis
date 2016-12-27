import data
import vector_math
from math import sqrt

def sphere_intersection_point(ray, sphere):
   
   p_diff = vector_math.difference_point(ray.pt, sphere.center)
   
   a = vector_math.dot_vector(ray.dir, ray.dir)
   b = (2.0 * vector_math.dot_vector(p_diff, ray.dir))
   c = vector_math.dot_vector(p_diff, p_diff) - sphere.radius**2.0
   
   if (b**2.0 - 4.0*a*c) < 0:
      return None
   
   #added discrim nest 2/13
   discrim = sqrt(b**2.0 - 4.0*a*c)
   t1 = (((-1.0 * b) + discrim) / (2.0 * a))
   t2 = (((-1.0 * b) - discrim) / (2.0 * a))
   
   pointt1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(
      ray.dir, t1))
   pointt2 = vector_math.translate_point(ray.pt, vector_math.scale_vector(
      ray.dir, t2))
   
   if (0 <= t1) and (0 <= t2):
      if t1 <= t2:
         return pointt1
      else:
         return pointt2
   elif (0 > t1) and (0 > t2):
      return None
   elif (0 <= t1) and (0 > t2):
      return pointt1
   elif (0 > t1) and (0 <= t2):
      return pointt2
   elif (t1 == t2) and (t1 >= 0):
      return pointt1

def find_intersection_points(sphere_list, ray):
   intersection_list = []
   for sphere_ob in sphere_list:
      intersection = sphere_intersection_point(ray, sphere_ob)
      if intersection is not None:
         intersection_list.append((sphere_ob, intersection))
   return intersection_list
   
def sphere_normal_at_point(sphere, point):
   if vector_math.length_vector(vector_math.vector_from_to(sphere.center, point)
      ) == 0:
      return None
   else:
      return vector_math.normalize_vector(
         vector_math.vector_from_to(sphere.center, point))