from vector_math import *


def sphere_intersection_point(ray, sphere):
   # a = (theRay.dir dot theRay.dir)
   a = dot_vector(ray.dir, ray.dir)
   # B = (2 * (theRay.pt - theSphere.center) dot theRay.dir)
   diff = difference_point(ray.pt, sphere.center)
   b = 2 * dot_vector(diff, ray.dir)
   # c = (((theRay.pt - theSphere.center) dot (theRay.pt - theSphere.center)) - theSphere.radius^2)
   c = dot_vector(diff, diff) - sphere.radius ** 2

   discriminant = b ** 2 - 4 * a * c
   if discriminant < 0:  # nonreal, no intersect
      return None
   elif discriminant == 0:  # one root
      t = -b / (2 * a)
      if t < 0:
         return None
   else:
      droot = math.sqrt(discriminant)
      root1 = (-b + droot) / (2 * a)
      root2 = (-b - droot) / (2 * a)
      if root1 < 0 and root2 < 0:
         return None
      elif root1 < 0 or root2 < 0:
         t = root1 if root1 > root2 else root2
      else:
         t = root1 if root1 < root2 else root2

   # point = ray.pt + t * ray.dir
   return translate_point(ray.pt, scale_vector(ray.dir, t))


def find_intersection_points(sphere_list, ray):
   points = []
   for sphere in sphere_list:
      point = sphere_intersection_point(ray, sphere)
      if point:
         points.append((sphere, point))
   return points


def find_closest_sphere(sphere_list, ray):
   points = find_intersection_points(sphere_list, ray)
   if not points:
      return None
   closest_sphere = 0
   shortest_distance = distance(points[0][1], ray.pt)
   for i in range(1, len(points)):
      distance_to_point = distance(points[i][1], ray.pt)
      if distance_to_point <= shortest_distance:
         shortest_distance = distance_to_point
         closest_sphere = i
   return points[closest_sphere]


def sphere_normal_at_point(sphere, point):
   return normalize_vector(vector_from_to(sphere.center, point))