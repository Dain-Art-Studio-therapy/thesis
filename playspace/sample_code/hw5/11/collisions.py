from data import *
from vector_math import *
from math import *

def sphere_intersection_point(ray, sphere):
   a = dot_vector(ray.dir,ray.dir)
   b = dot_vector(difference_point(ray.pt,sphere.center),ray.dir)*2
   c = (dot_vector(difference_point(ray.pt, sphere.center),
 difference_point(ray.pt,sphere.center))-sphere.radius**2)
   d = b**2 - (4 * a * c)
   
   if d < 0:
      return None
   elif d == 0:
      root1 = -b / (2*a)
      if root1 < 0:
         return None
      else:
         ray1 = scale_vector(ray.dir, root1)
         return Point(ray.pt.x+ray1.x,ray.pt.y+ray1.y,ray.pt.z+ray1.z)
   else:
      d = sqrt(d)
      root2 = (-b + d)/(2*a)
      root3 = (-b - d)/(2*a)
      if root3 < 0 and root2 < 0:
         return None
      elif root2 < 0:
         ray1 = scale_vector(ray.dir, root3)
         return  Point(ray.pt.x+ray1.x,ray.pt.y+ray1.y,ray.pt.z+ray1.z)
      elif root3 < 0:
         ray1 = scale_vector(ray.dir, root2)
         return Point(ray.pt.x+ray1.x,ray.pt.y+ray1.y,ray.pt.z+ray1.z)
      else:
         ray1 = scale_vector(ray.dir, min(root2,root3))
         return Point(ray.pt.x+ray1.x,ray.pt.y+ray1.y,ray.pt.z+ray1.z)

def find_intersection_points(sphere_list, ray):
   nl = []
   for s in sphere_list:
       res = sphere_intersection_point(ray,s)
       if res != None:
          nl.append((s, res)) 
   return nl

def sphere_normal_at_point(sphere, point):
   return normalize_vector(vector_from_to(sphere.center, point))

