from data import *
from vector_math import *
from math import *
from utility import *


def sphere_intersection_point(ray, sphere):
   A = dot_vector(ray.dir,ray.dir)
   B_a = difference_point(ray.pt,sphere.center)
   B_b = scale_vector(B_a,2)
   B = dot_vector(B_b, ray.dir)
   C_a = difference_point(ray.pt,sphere.center)
   C_b = dot_vector(C_a,C_a)
   C = C_b - (sphere.radius **2)
   if B**2 - (4*A*C) < 0:
      return None
   t = (-B + sqrt((B**2)-(4*A*C)))/(2*A)
   t1 = (-B - sqrt((B**2)-(4*A*C)))/(2*A)
   if t < 0 and t1 < 0:
      return None
   elif t > 0 and t1 < 0:
      return translate_point(scale_vector(ray.dir, t),ray.pt)
   elif t < 0 and t1 > 0:
      return translate_point(scale_vector(ray.dir, t1),ray.pt)
   else:
      return translate_point(scale_vector(ray.dir, min(t,t1)),ray.pt)



def find_intersection_points(sphere_list, ray):
   list = []
   for i in range(0, len(sphere_list)):
      a = sphere_intersection_point(ray, sphere_list[i])
      # get hold on object
      #sphere_interesection on object
      # if its none dont append 
      # if I get something back append into a tuple
      if a != None:
         list.append((sphere_list[i], a)) 
   return list
   
  
def sphere_normal_at_point(sphere,point):
   return normalize_vector(vector_from_to(sphere.center,point))
