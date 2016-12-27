import data
import vector_math
import math
import unittest

def sphere_intersection_point(ray, sphere):
   A = vector_math.dot_vector(ray.dir, ray.dir)
   difptcenter = vector_math.difference_point(ray.pt, sphere.center)
   B = 2 * (vector_math.dot_vector(difptcenter, ray.dir))
   C = vector_math.dot_vector(difptcenter, difptcenter) - (sphere.radius ** 2)

   if (((B) ** 2) - (4 * A * C) >= 0):
      t1 = (-B + math.sqrt((B ** 2) - (4 * A * C))) / (2 * A)
      t2 = (-B - math.sqrt((B ** 2) - (4 * A * C))) / (2 * A)
      

      
      
      if t1 >=0 and t2 >=0:
         
         if t1 <= t2:
            pointT1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
            
            return pointT1
      
      

         else:      
            pointT2 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t2))
            
            
            return pointT2

      elif t1 >= 0 and t2 <0:
         
         pointT1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
         
         return pointT1
   
      elif t2 >= 0 and t1 <0:
         pointT2 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t2))
           
         return pointT2
      
      else:
         return None  
         
   else: 
      return None   



def find_intersection_points(sphere_list, ray):
   
   finallist = []
      

   for i in sphere_list:
      n = sphere_intersection_point(ray, i)
      if n != None:
         finallist.append((i, n))
        

   return finallist

def sphere_normal_at_point(sphere, point):

   newvec = vector_math.vector_from_to(sphere.center, point)
   normvec = vector_math.normalize_vector(newvec)
   return normvec        

         
   
