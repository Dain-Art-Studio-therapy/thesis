import vector_math
import data
import math
def sphere_intersection_point(ray,sphere):
   A = vector_math.dot_vector(ray.dir,ray.dir)
   B = 2 * (vector_math.dot_vector(vector_math.difference_point(ray.pt,sphere.center), ray.dir))
   C = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), vector_math.difference_point(ray.pt, sphere.center)) - sphere.radius**2
   if B**2 - (4 * A * C) < 0:
      return None
   t1 = ((-B) + math.sqrt(B**2 - (4 * A * C))) / (2 * A)
   t2 = ((-B) - math.sqrt(B**2 - (4 * A * C))) / (2 * A)
   if t1 >= 0 and t2 >= 0: 
      if t1 > t2:
         return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t2))
      else:
         return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
   elif t1 < 0 and t2 < 0:
      return None
   elif t1 >= 0 and t2 < 0:
      return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
   elif t1 < 0 and t2 >= 0:
      return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t2))
      
def find_intersection_points(sphere_list,ray):
   newList = []
   for sphere in sphere_list:
      point = sphere_intersection_point(ray,sphere) 
      if point != None:
         newList.append((sphere,point))
   return newList

def sphere_normal_at_point(sphere,point):
   return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center,point))
