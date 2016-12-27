from math import *
from data import *
from vector_math import *
from utility import *

def sphere_intersection_point(ray,sphere):
   a = dot_vector(ray.dir,ray.dir)
   b = dot_vector(scale_vector(difference_point(ray.pt,sphere.center),2),ray.dir)
   c = dot_vector(difference_point(ray.pt,sphere.center),
           difference_point(ray.pt,sphere.center))-sphere.radius*sphere.radius
   d = b**2-4*a*c
   if(d<0):
      return None
   t = (-b+math.sqrt(d))/(2*a)
   t1 = (-b-math.sqrt(d))/(2*a)
   if(t < 0 and t1 < 0):
      return None
   elif(t > 0 and t1 < 0):
      tfirst = t
   elif(t < 0 and t1 > 0):
      tfirst = t1
   else:
      tfirst = min(t,t1)
   return translate_point(scale_vector(ray.dir,tfirst),ray.pt)

def find_intersection_points(sphere_list, ray):
   list = []
   for i in range(0, len(sphere_list)):
      a = sphere_intersection_point(ray, sphere_list[i])
      if(a != None):
         list.append((sphere_list[i], a)) 
   return list
  
def sphere_normal_at_point(sphere,point):
   return normalize_vector(vector_from_to(sphere.center,point))
