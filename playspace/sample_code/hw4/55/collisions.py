from data import *
import math
import utility
import vector_math



def sphere_intersection_point(ray, sphere):
   A = vector_math.dot_vector(ray.dir, ray.dir)
   B = vector_math.dot_vector(vector_math.scale_vector((vector_math.difference_point(ray.pt, sphere.center)), 2), ray.dir)
   C = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), vector_math.difference_point(ray.pt, sphere.center)) - (sphere.radius**2)
   radical = B**2 - 4*A*C
   if radical < 0:
      return None
   elif radical == 0:
      root = -B / (2*A)
      if root >= 0:
         return vector_math.translate_point(vector_math.scale_vector(ray.dir, root), ray.pt)
      else:
         return None
   else:
      quadratic_pos = (-B + math.sqrt(radical)) / (2*A)
      quadratic_neg = (-B - math.sqrt(radical)) / (2*A)
      t = [quadratic_pos, quadratic_neg] 
      if t[0] >= 0 and t[1] >= 0:
         if t[0] <= t[1]:
            return vector_math.translate_point(vector_math.scale_vector(ray.dir, t[0]), ray.pt)
         else:
            return vector_math.translate_point(vector_math.scale_vector(ray.dir, t[1]), ray.pt)
      elif t[0] < 0 and t[1] < 0:
         return None
      elif (t[0] < 0 and t[1] >= 0):
         return vector_math.translate_point(vector_math.scale_vector(ray.dir, t[1]), ray.pt)
      elif (t[0] >= 0 and t[1] < 0):
         return vector_math.translate_point(vector_math.scale_vector(ray.dir, t[0]), ray.pt)

def find_intersection_points(sphere_list, ray):
   intersection_points_list = []
   for sphere in sphere_list:
      if sphere_intersection_point(ray,sphere) != None:
         intersection_points_list.append((sphere, sphere_intersection_point(ray,sphere)))
   return intersection_points_list 

def sphere_normal_at_point(sphere,point):
   return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, point))
      
