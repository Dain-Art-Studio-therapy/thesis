import data
from vector_math import *

def sphere_intersection_point(ray, sphere):
   A = dot_vector(ray.dir, ray.dir)
   B = 2 * dot_vector((difference_point(ray.pt, sphere.center)), ray.dir)
   C = dot_vector((difference_point(ray.pt, sphere.center)), 
(difference_point(ray.pt, sphere.center))) - sphere.radius ** 2
   v = discriminant(A, B, C)

   if v >= 0:
      t = (-B - math.sqrt(v)) / (2 * A)
      t2 = (-B + math.sqrt(v)) / (2 * A)
      if t >= 0:
         return translate_point(ray.pt, scale_vector(ray.dir, t))
      elif t2 >= 0:
         return translate_point(ray.pt, scale_vector(ray.dir, t2))

def discriminant(a, b, c):
   return (b ** 2) - (4 * a * c)

def find_intersection_points(sphere_list, ray):
   E = []
   N = [sphere_intersection_point(ray, x) for x in sphere_list]
   i = 0
   for n in N:
       if n != None:
          E.append((sphere_list[i], n))
          i += 1
       else:
          i += 1
   return E

def sphere_normal_at_point(sphere, point):
   vec = vector_from_to(sphere.center, point)
   return normalize_vector(vec)
