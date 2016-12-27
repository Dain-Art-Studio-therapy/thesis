import data
import math
import vector_math

def sphere_intersection_point(ray, sphere):
   
   A = vector_math.dot_vector(ray.dir, ray.dir)
   B = vector_math.dot_vector(vector_math.scale_vector(vector_math.difference_point(ray.pt, sphere.center), 2), ray.dir)
   C = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), vector_math.difference_point(ray.pt, sphere.center)) - sphere.radius**2

   discrim = B**2 - (4*A*C)
  
   if discrim < 0:
     return None    
       
   t1 = (-B+(math.sqrt(discrim)))/(2*A) 
   t2 = (-B-(math.sqrt(discrim)))/(2*A)
   

   if t1 < 0 and t2 < 0:
     return None
 
   elif t1 >= 0 and t2< 0:
     point1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
     return point1
     
   elif t2 >= 0 and t1 < 0:
     point2 = vector_math.translate_point(ray.pt ,vector_math.scale_vector(ray.dir, t2))
     return point2

   elif t1 >= 0 and t2 >= 0: 
     point1 = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
     point2 = vector_math.translate_point(ray.pt ,vector_math.scale_vector(ray.dir, t2))
     if abs(t1) > abs(t2):
        return point2
     else:
        return point1


def find_intersection_points(sphere_list, ray):
   newlist = [sphere_intersection_point(ray, sphere) for sphere in sphere_list] 
   differentlist = []
   
   for i in range(len(newlist)): 
     if newlist[i] != None: 
         differentlist.append((sphere_list[i], newlist[i]))
   return differentlist
   #this returns a tuple within a list (sphere and the point where the ray intersected the sphere)
       
  

def sphere_normal_at_point(sphere, point):
   return vector_math.normalize_vector(vector_math.difference_point(point, sphere.center))
   

# 916-479-5025 Jessie Pease (SS leader)
