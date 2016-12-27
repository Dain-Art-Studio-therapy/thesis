import vector_math
import data
import utility
import math

def sphere_intersection_point(ray, sphere):
   a = vector_math.dot_vector(ray.dir, ray.dir)
   b = 2 * vector_math.dot_vector(ray.dir, vector_math.difference_point(ray.pt, sphere.center))
   c = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center),
                              vector_math.difference_point(ray.pt, sphere.center)) - (sphere.radius ** 2)

   d = discriminant(a, b, c)
   if d < 0:
      return None
   elif d == 0:
      t = solve_quadratic(a, b, c)
      if t > 0:
        return point_along_ray(ray, t)
      else:
         return None
   elif d > 0:
      t1 = solve_quadratic(a, b, c)
      t2 = solve_quadratic_2(a, b, c)
      if t1 > 0 and t2 > 0:
         return point_along_ray(ray, min(t1, t2))
      elif xor(t1 > 0, t2 > 0):
          return point_along_ray(ray, max(t1, t2))
      elif t1 == 0 and t2 == 0:
         return ray.pt
      else:
         return None
   else:
      return "something went wrong"



def find_intersection_points(sphere_list, ray):
   newlist = []
   for sphere in sphere_list:
      int_pt = sphere_intersection_point(ray, sphere)
      if isinstance(int_pt, data.Point):
         newlist.append((sphere, int_pt))
   return newlist


def sphere_normal_at_point(sphere, point):
   nonscaled = vector_math.vector_from_to(sphere.center, point)
   return vector_math.normalize_vector(nonscaled)



# these are all helper functions to the above three functions
def point_on_sphere(point, sphere):
   v = vector_math.vector_from_to(sphere.center, point)
   return vector_math.dot_vector(v, v) == sphere.radius ** 2

def solve_quadratic(a, b, c):
   return (-b + math.sqrt(discriminant(a, b, c))) / (2 * a)

def solve_quadratic_2(a, b, c):
   d = discriminant(a, b, c)
   if d >= 0:
      return (-b - math.sqrt(d)) / (2 * a)

def discriminant(a, b, c):
   return b ** 2 - (4 * a * c)

   
# returns a point in the direction of the ray, at a parameter t away from
# the originating point of the ray
def point_along_ray(ray, t):
   x = ray.pt.x + (t * ray.dir.x)
   y = ray.pt.y + (t * ray.dir.y)
   z = ray.pt.z + (t * ray.dir.z)
   return data.Point(x, y, z)

def xor(a, b):
   return (a and not b) or (b and not a)
