from vector_math import *
from math import *
from utility import *

def quad_form(a, b, c, sqrt_desc, plus):
   #If we want the plus version
   if plus:
      return ((-1 * b) + sqrt_desc) / (2*a)
   else: # Subtract version
      return ((-1 * b) - sqrt_desc) / (2*a)



def sphere_intersection_point(ray, sphere):
   # First calculate our A, B, and C values
   # a
   a = dot_vector(ray.dir, ray.dir)

   # b
   b_scale = scale_vector(difference_point(ray.pt, sphere.center), 2)
   b = dot_vector(b_scale, ray.dir)

   # c
   c_dif = difference_point(ray.pt, sphere.center)
   c = (dot_vector(c_dif, c_dif)) - (sphere.radius**2)

   #Get two t values if possible
   # Calc descriminant
   desc = (b**2) - 4 * a * c
   
   # If desc < 0, no vals... if = 0, 1 val... if > 0, 2 vals
   t = 0
   t1 = 0
   if desc < 0:
      return None
   else:
      sqrt_desc = sqrt(desc)
      t = quad_form(a, b, c, sqrt_desc, True)
      t1 = quad_form(a, b, c, sqrt_desc, False)

   
   # Now that we have two t-values, figure out which one to return
   the_t = 0
   if t < 0 and t1 < 0:
      return None
   elif t >= 0 and t1 < 0:
      the_t = t
   elif t < 0 and t1 >= 0:
      the_t = t1
   else: # Accounts for t vals being the same
      the_t = min(t, t1)

   return translate_point(ray.pt, scale_vector(ray.dir, the_t))

def find_intersection_points(sphere_list, ray):
   r_list = []
   for s in sphere_list:
      intersect = sphere_intersection_point(ray, s)
      if intersect:
         q = (s, intersect)
         r_list.append(q)

   return r_list

def sphere_normal_at_point(sphere, point):
   v = vector_from_to(sphere.center, point)
   return normalize_vector(v)
