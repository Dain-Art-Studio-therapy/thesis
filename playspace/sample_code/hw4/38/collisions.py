#collisions.py
import vector_math

def sphere_intersection_point(ray, sphere):
  a = vector_math.dot_vector(ray.dir, ray.dir)
  b = (2*vector_math.dot_vector(vector_math.difference_point(ray.pt,
                                   sphere.center), ray.dir))
  c = (vector_math.dot_vector(vector_math.difference_point(ray.pt,
           sphere.center), vector_math.difference_point(ray.pt,
           sphere.center))- (sphere.radius**2))
  if ((b**2)-4*a*c) < 0: return None
  else:
    t1 = (-b + (((b**2)-4*a*c)**.5)) / (2*a)
    t2 = (-b - (((b**2)-4*a*c)**.5)) / (2*a)
    if t1 >= 0 and t2 >= 0:
       if t1 <= t2:
          t = t1
       else:
          t = t2
    elif t1 < 0 and t2 >= 0:
       t = t2
    elif t1 < 0 and t2 < 0:
       return None
    elif t1 >= 0 and t2 < 0:
       t = t1
  poi = vector_math.translate_point(ray.pt,
         vector_math.scale_vector(ray.dir, t))
  return poi  

def find_intersection_points(sphere_list, ray):
  f = [(s, sphere_intersection_point(ray, s)) for s in sphere_list
         if sphere_intersection_point(ray, s) != None]
  return f


def sphere_normal_at_point(sphere, point):
  v = vector_math.vector_from_to(sphere.center, point)
  r = vector_math.normalize_vector(v)
  return r
