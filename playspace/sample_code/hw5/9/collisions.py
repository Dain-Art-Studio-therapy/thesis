import data
import math
import vector_math

def sphere_intersection_point(ray, sphere):
   a = (vector_math.dot_vector(ray.dir,ray.dir))
   b = (2 * vector_math.dot_vector((vector_math.difference_point(ray.pt,sphere.center)),ray.dir))
   c = (vector_math.dot_vector(vector_math.difference_point(ray.pt,sphere.center), vector_math.difference_point(ray.pt,sphere.center)) - sphere.radius**2)
   disc = b**2 - 4*(a*c)   

   if disc < 0:
      return None

   t1 = (-b + math.sqrt(disc))/(2.0*a)
   t2 = (-b - math.sqrt(disc))/(2.0*a) 

   if disc == 0: 
      return vector_math.translate_point(ray.pt,(vector_math.scale_vector(ray.dir,t1)))

   if t1 >= 0 and t2 >= 0 and disc != 0:
      if t1 < t2:
         return vector_math.translate_point(ray.pt,(vector_math.scale_vector(ray.dir,t1)))
      elif t2 < t1:
         return vector_math.translate_point(ray.pt,(vector_math.scale_vector(ray.dir,t2)))

   if t1 < 0 and t2 <0:
      return None
           
   if t1 >= 0 and t2 < 0:
      return vector_math.translate_point(ray.pt,(vector_math.scale_vector(ray.dir,t1)))

   if t2 >= 0 and t1 < 0:
      return vector_math.translate_point(ray.pt,(vector_math.scale_vector(ray.dir,t2)))

def find_intersection_points(sphere_list,ray):
   return [(s,sphere_intersection_point(ray,s)) for s in sphere_list if sphere_intersection_point(ray,s) is not None]    



def sphere_normal_at_point(sphere,point):
   return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center,point))
