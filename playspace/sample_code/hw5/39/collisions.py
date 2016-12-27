import data
import utility
import vector_math
import math

def sphere_intersection_point(ray, sphere):
   A = (vector_math.dot_vector(ray.direction, ray.direction))
   B = (vector_math.dot_vector((data.Point(2 *(ray.pt.x - sphere.center.x), 2 * (ray.pt.y - sphere.center.y), 2 * (ray.pt.z - sphere.center.z))), ray.direction)) 
   C = (vector_math.dot_vector(data.Point((ray.pt.x - sphere.center.x), (ray.pt.y - sphere.center.y), (ray.pt.z - sphere.center.z)), data.Point((ray.pt.x - sphere.center.x), (ray.pt.y - sphere.center.y), (ray.pt.z - sphere.center.z))) - (sphere.radius ** 2))
   if (((B ** 2) - (4 * A * C))  < 0):
      return None
   X1 = ((-B + math.sqrt((B ** 2) - (4 * A * C))) / (2 * A))
   X2 = ((-B - math.sqrt((B ** 2) - (4 * A * C))) / (2 * A))
   if (X1 >= 0 and X2 >= 0):
      if (X1 > X2):
         t = X2
      if (X2 > X1):
         t = X1
      else:
         t = X1
   if (X1 >= 0):
      t = X1
   if (X2 >= 0):
      t = X2
   if (X1 < 0 and X2 < 0):
      return None
   x0 = ray.pt.x + t * ray.direction.x
   y0 = ray.pt.y + t * ray.direction.y
   z0 = ray.pt.z + t * ray.direction.z
   final = data.Point(x0, y0, z0)
   return final


def find_intersection_points(sphere_list, ray):
   new = []
   for e in sphere_list:
      s = sphere_intersection_point(ray,e)
      if (s != None):
         tuple = (e, s)
         new.append(tuple)
      else:
         pass
   return new


def sphere_normal_at_point(sphere, point):
   vector = vector_math.difference_point(point, sphere.center)   
   norm =  vector_math.normalize_vector(vector)
   return norm
