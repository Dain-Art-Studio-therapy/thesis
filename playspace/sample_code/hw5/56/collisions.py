from data import *
from vector_math import *
import math

def sphere_intersection_point(ray, sphere):
  b = dot_vector(scale_vector(difference_point(ray.pt, sphere.center), 2), ray.dir)
  a = dot_vector(ray.dir, ray.dir)
  c = dot_vector(difference_point(ray.pt, sphere.center),
                 difference_point(ray.pt, sphere.center)) - sphere.radius**2
  

  if b**2 - 4*a*c < 0:
    return None

  # t is a tuple
  t = solve_quadratic(a, b, c)

  disc = b**2 - (4*a*c)

  if disc == 0:
    if t[0] < 0:
      return None
    else:
      return translate_point(ray.pt, scale_vector(ray.dir, t[0]))

  if disc > 0:
    if t[0] >= 0 and t[1] >= 0:
      return translate_point(ray.pt, scale_vector(ray.dir, min(t)))
    elif t[0] < 0 and t[1] < 0:
      return None
    else:
      return translate_point(ray.pt, scale_vector(ray.dir, max(t)))

      

def solve_quadratic(a, b, c):
  discriminant = b**2 - (4.0*a*c)
  sqrt_disc = math.sqrt(discriminant)

  t = ((-b + sqrt_disc)/(2.0*a), (-b - sqrt_disc)/(2.0*a))
  return t


def find_intersection_points(sphere_list, ray):
  result = []
  #print 'sphere_list for find_intersection_points: ', sphere_list
  for sphere in sphere_list:
    f = sphere_intersection_point(ray, sphere)
    if f != None:
      result.append((sphere, f))

  #print 'result of find_intersection_points: ', result

  return result


def sphere_normal_at_point(sphere, point):
  return normalize_vector(difference_point(point, sphere.center))
  

if __name__ == '__main__':
  pass
