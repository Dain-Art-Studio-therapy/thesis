from vector_math import *
import math



def sphere_intersection_point(ray, sphere):
      A = dot_vector(ray.dir, ray.dir)
      B = 2 * dot_vector(difference_point(ray.pt, sphere.center), ray.dir)
      C = dot_vector(difference_point(ray.pt, sphere.center), difference_point(ray.pt, sphere.center)) - sphere.radius **2

      discrim = B **2 - 4*A*C

      if discrim < 0:
          return None
      else:
          t1 = (-B + math.sqrt(discrim)) / (2*A)
          t2 = (-B - math.sqrt(discrim)) / (2*A)
          
          if t1<0 and t2<0:
              return None
          if t1>=0 and t2>=0:
              if t1<=t2:
                  return translate_point(ray.pt, scale_vector(ray.dir, t1))
              elif t2<t1:
                  return translate_point(ray.pt, scale_vector(ray.dir, t2))
          elif t2>=0 and t1<0:
               return translate_point(ray.pt, scale_vector(ray.dir, t2))          
          elif t1>=0 and t2<0:
               return translate_point(ray.pt, scale_vector(ray.dir, t1))     

def find_intersection_points(sphere_list, ray):
    list = []
    for sphere in sphere_list:
        point = sphere_intersection_point(ray, sphere)
        if(point is not None):
            pair = (sphere, point)
            list.append(pair)

    return list
    




def sphere_normal_at_point(sphere, point):
    vector = vector_from_to(sphere.center, point)
    return normalize_vector(vector)
