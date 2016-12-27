import data
import vector_math
import math

def quad_eqn(a,b,c):
   d = b*b - 4*a*c
   if d == 0:
      return [float(-1*b) / (2*a), None]
   elif d > 0:
      return [(-1*b + math.sqrt(d)) / (2*a), (-1*b - math.sqrt(d)) / (2*a)]
   else:
      return [None, None]

def intersect_t(a,b,c):
   lop = quad_eqn(a,b,c) #list of potential t values
   #within the list of potentials, return the one closest to 0, but positive
   if lop[1] >= 0:
      return lop[1]
   elif lop[0] >= 0:
      return lop[0] 
   else:
      return None

def sphere_intersection_point(ray, sphere):
   A = vector_math.dot_vector(ray.dir,ray.dir)
   B = vector_math.dot_vector(vector_math.scale_vector(vector_math.difference_point(ray.pt,sphere.center),2),ray.dir)
   C = vector_math.dot_vector(vector_math.difference_point(ray.pt,sphere.center),vector_math.difference_point(ray.pt,sphere.center)) - sphere.radius*sphere.radius
   t = intersect_t(A,B,C)
   if t != None:
      return vector_math.translate_point(ray.pt,vector_math.scale_vector(ray.dir,t))

def find_intersection_points(sphere_list, ray):
   list_of_intersections = []
   for i in range(len(sphere_list)):
      pt = sphere_intersection_point(ray, sphere_list[i])
      if pt != None:
         list_of_intersections.append((sphere_list[i], pt))
   return list_of_intersections

def sphere_normal_at_point(sphere,point):
   return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center,point))

