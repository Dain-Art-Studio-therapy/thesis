# Han Tran || CPE101-01,01 || Proffessor Aeron Keen || Asignment 3

import data
import vector_math
import math


def sphere_intersection_point(ray, sphere):
   A = vector_math.dot_vector(ray.dir, ray.dir)
   Bpart1 = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), ray.dir)
   B = 2*Bpart1
   Cpart1 = vector_math.difference_point(ray.pt, sphere.center)
   C = vector_math.dot_vector(Cpart1, Cpart1) - sphere.radius**2
   if (B**2 - 4*A*C >= 0): # Check if the roots have any complex numbers
      # Solve for At^2 + Bt + C == 0  >> get root t
      t = [(-B + math.sqrt(B**2 - 4*A*C))/(2*A) ,(-B - math.sqrt(B**2 - 4*A*C))/(2*A)]
      if t[0] >= 0 and t[1] >= 0:
         temp_t = min(t)
      elif t[0] >= 0:
         temp_t = t[0]
      elif t[1] >= 0:
         temp_t = t[1]
      else:
         return None
   else:
      return None
   
   return vector_math.translate_point( ray.pt, vector_math.scale_vector(ray.dir, temp_t))



# All Ray-Sphere intersection
def find_intersection_points(sphere_list, ray):
   new_tup = []
   for i in sphere_list:
      sp_pt = sphere_intersection_point(ray, i)
      if sp_pt != None:
         new_tup.append((i, sp_pt))
   
   return new_tup



# sphere_normal_at_point
def sphere_normal_at_point(sphere, point):
   len_vec = vector_math.vector_from_to(sphere.center, point)
   return vector_math.normalize_vector(len_vec)

