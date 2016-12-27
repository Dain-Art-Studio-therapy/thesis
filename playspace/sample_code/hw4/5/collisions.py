import math
import data
import vector_math
import utility

def sphere_intersection_point(ray, sphere):
   a = vector_math.dot_vector(ray.dir,ray.dir)
   b = (2 * vector_math.dot_vector(vector_math.difference_vector(ray.pt, sphere.center), ray.dir))
   c = ((vector_math.dot_vector(vector_math.difference_vector(ray.pt, sphere.center),vector_math.difference_vector(ray.pt,sphere.center)))-(sphere.radius**2))
   
   if ((b**2) - 4*a*c) > 0:
      t1 = (-b + math.sqrt((b**2) - (4*a*c)))/(2*a)
      t2 = (-b - math.sqrt((b**2) - (4*a*c)))/(2*a)
      if t1 >= 0 and t2 >= 0:
         if t1 <= t2:
            return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir, t1))
         else:
            return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir, t2))
      elif t1 >= 0 and t2 < 0:
         return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir, t1))
      elif t2 >= 0 and t1 < 0:
         return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir, t2))    
      else:
         return None
   elif ((b**2) - 4*a*c) < 0:
      return None
   else:
      t1 = -b/(2*a)
      return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir, t1))

def find_intersection_points(sphere_list, ray):
   if sphere_list == []:
      return []
   result = []
   for sphere in sphere_list:
      check = sphere_intersection_point(ray, sphere)
      if check != None:
         result.append((sphere, check))
   return result

def sphere_normal_at_point(sphere, point):
   return vector_math.normalize_vector(vector_math.difference_point(point, sphere.center))
