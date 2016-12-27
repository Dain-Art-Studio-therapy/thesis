import vector_math
import data
import math

def sphere_intersection_point(ray,sphere):
   R = vector_math.normalize_vector(ray.dir)

   A = vector_math.dot_vector(R,R)

   B = (2*(vector_math.dot_vector(vector_math.difference_point(ray.pt,sphere.center),R)))

   C = (vector_math.dot_vector((vector_math.difference_point(ray.pt,sphere.center)),(vector_math.difference_point(ray.pt,sphere.center)))-(sphere.radius)**2) 

   Disc = (B**2)-(4*A*C)

   if Disc < 0:
      return None

   t = (-B + math.sqrt(Disc))/(2*A)
   t2 = (-B - math.sqrt(Disc))/(2*A)

   if t2 < t and t2 >= 0 or t <= 0 and t2 >= 0:
      t = t2
      return vector_math.translate_point(ray.pt,vector_math.scale_vector(R,t))
   elif t <= t2 and t >=0 or t2 <= 0 and t >= 0 :
      return vector_math.translate_point(ray.pt,vector_math.scale_vector(R,t))
   


   else: 
      return None
   
   
def find_intersection_points(sphere_list,ray):
   S = []
   for i in range(len(sphere_list)):
      if sphere_intersection_point(ray,sphere_list[i]) != None:
         s = (sphere_list[i],sphere_intersection_point(ray,sphere_list[i]))
         S.append(s)
   return S

def sphere_normal_at_point(sphere, point):
   return vector_math.normalize_vector(vector_math.difference_vector(point,sphere.center))


