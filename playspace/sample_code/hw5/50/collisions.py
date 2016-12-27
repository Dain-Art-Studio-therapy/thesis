#Contains Function Implementations

import data, math, vector_math

def sphere_intersection_point(ray, sphere):
   point = data.Point(0, 0, 0)
   t = 0
   a = (vector_math.dot_vector(ray.dir, ray.dir))
   b = 2*(vector_math.dot_vector((vector_math.difference_point(ray.pt,
      sphere.center)), ray.dir))
   c = vector_math.dot_vector((vector_math.difference_point(ray.pt,
      sphere.center)), (vector_math.difference_point(ray.pt, sphere.center))) \
      - (sphere.radius)**2

   descriminant = ((b**2) - (4 * a * c))

   if descriminant < 0:
      return None
   else:
      poss = []
      poss.append((-b + math.sqrt(descriminant))/(2*a))
      poss.append((-b - math.sqrt(descriminant))/(2*a))
   
      if (poss[0] >= 0 and poss[1] >= 0):
         t = min(poss[0], poss[1])
      elif (poss[0] < 0 and poss[1] < 0):
         return None
      elif (poss[0] >= 0 and poss[1] < 0) or (poss[0] < 0 and poss[1] >= 0):
         if poss[0] >= 0:
            t = poss[0]
         else:
            t = poss[1]
      else:
         if poss[0] >= 0:
            t = poss[0]
         else:
            return None

   point = vector_math.translate_point(ray.pt, vector_math.scale_vector(
      ray.dir, t))

   return point


def find_intersection_points(sphere_list, ray):
   groups = []
   for sphere in sphere_list:
      point = sphere_intersection_point(ray, sphere)
      if point != None:
         groups.append((sphere, point))
      else:
         pass

   return groups

def sphere_normal_at_point(sphere, point):
   vector_of_one = vector_math.vector_from_to(sphere.center, point)
   fin_vector = vector_math.normalize_vector(vector_of_one)

   return fin_vector
