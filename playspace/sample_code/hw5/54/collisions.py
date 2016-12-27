from data import *
from vector_math import *
import math

def sphere_intersection_point(ray, sphere):
   diffPt = difference_point(ray.pt, sphere.center)
   A = dot_vector(ray.dir, ray.dir)
   B = 2 * dot_vector(diffPt, ray.dir)
   C = dot_vector(diffPt, diffPt) - sphere.radius ** 2
   discrim = B ** 2 - (4 * A * C) 

   if discrim < 0: # well this would be unreal *har de har har* 
      return None  # so it does not hit the sphere
   # vec2Ntrsct is the vector of the ray to the point of intersection
   # on the sphere

   elif discrim == 0:
      root_tuple = calculate_quadratic_root(A, B, C)
      if root_tuple[0] < 0: # both values in tuple are the same 
         return None        # so I just check against one of them. 

      else: 
         vec2Ntrsct = scale_vector(ray.dir, root_tuple[0])
         return Point(ray.pt.x + vec2Ntrsct.x, ray.pt.y + vec2Ntrsct.y, 
            ray.pt.z + vec2Ntrsct.z)

   else: 
      root_tuple = calculate_quadratic_root(A, B, C)
      if root_tuple[0] < 0 and root_tuple[1] < 0:
         return None # both are negative and so boom. We don't care

      elif root_tuple[1] < 0: # RT[1] < 0 but at least one of them is pos
         # therefore RT[0] is pos and is the one that we use
         vec2Ntrsct = scale_vector(ray.dir, root_tuple[0])
         return Point(ray.pt.x + vec2Ntrsct.x, ray.pt.y + vec2Ntrsct.y, 
            ray.pt.z + vec2Ntrsct.z)

      else: # well if both are positive, there exists no reason why
         # the part of the tuple that subtracts the root (RT[1]) wouldn't  
         # be the lesser value of t; therefore we will use RT[1]
         vec2Ntrsct = scale_vector(ray.dir, root_tuple[1])
         return Point(ray.pt.x + vec2Ntrsct.x, ray.pt.y + vec2Ntrsct.y, 
         ray.pt.z + vec2Ntrsct.z)


def calculate_quadratic_root(a, b, c):
   sqrt = math.sqrt(b**2 - 4 * a * c)
   return ((-b + sqrt)/ (2 * a), 
      (-b - sqrt)/(2 * a))


def find_intersection_points(sphere_list, ray):
   listOfSphereNtrs = [] 
   for s in sphere_list:
      ntrPt = sphere_intersection_point(ray, s)
      if ntrPt is not None:
         listOfSphereNtrs.append((s, ntrPt))
   return listOfSphereNtrs


def sphere_normal_at_point(sphere, point):
   v = normalize_vector(vector_from_to(sphere.center, point))
   return v

