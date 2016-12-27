import data
import math
import vector_math

def sphere_intersection_point(ray,sphere):
   a = vector_math.dot_vector(ray.dir, ray.dir)
   b = (2 * vector_math.dot_vector( (vector_math.difference_point(ray.pt,sphere.center)) , ray.dir))
   c =  vector_math.dot_vector(vector_math.difference_point(ray.pt,sphere.center), vector_math.difference_point(ray.pt,sphere.center)) - (sphere.radius ** 2) 

   if ((b ** 2 - 4*a*c) >  0):
      t1 = (-b + math.sqrt(b ** 2 - 4*a*c)) / (2 * a)
      t2 = (-b - math.sqrt(b ** 2 - 4*a*c)) / (2 * a)

   else:
      return None
    
   if (t1 > 0):
      new_ray = vector_math.scale_ray(ray,t1)
      answer = vector_math.translate_point(ray.pt, new_ray.dir)
      return answer
   else:
      if (t2 > 0):
         new_ray = vector_math.scale_ray(ray,t2)
         answer = vector_math.translate_point(ray.pt, new_ray.dir)
         return answer  
      else:
         return None

def find_intersection_points(sphere_list,ray):
   answer = []
   for i in sphere_list:
      point = sphere_intersection_point(ray,i)
      if point != None:
         answer.append((i, point))
   return answer

def sphere_normal_at_point(sphere, point):
   diff = vector_math.difference_point(point,sphere.center)
   normal = vector_math.normalize_vector(diff)
   return normal

