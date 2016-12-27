import vector_math
import math
import data

def sphere_intersection_point(ray,sphere):
   def point_t(t):
      return vector_math.translate_point(ray.pt,
                                         vector_math.scale_vector(ray.dir,t))
   diff_pt = vector_math.difference_point(ray.pt,sphere.center)
   a = vector_math.dot_vector(ray.dir, ray.dir)
   b = vector_math.dot_vector(vector_math.scale_vector(diff_pt,2),
                              ray.dir)
   c = vector_math.dot_vector(diff_pt,diff_pt) - sphere.radius ** 2
   disc = b ** 2 - 4 * a * c
   if disc < 0:
      return None
   elif disc == 0:
      t3 = (-b / (2 * a))
      if t3 >= 0:
         return point_t(t3)
      else:
         return None 
   else:
      disc_root = math.sqrt(disc)
      t1 = (-b + disc_root) / (2 * a)
      t2 = (-b - disc_root) / (2 * a)
      if t1 >= 0 and t2 >= 0:
         return point_t(min(t1,t2))
      elif t1 < 0 and t2 < 0:
         return None
      else:
         if t1 >= 0:
            return point_t(t1)
         elif t2 >= 0:
            return point_t(t2)


def find_intersection_points(sphere_list,ray):
   res = []
   for x in sphere_list:
      sip = sphere_intersection_point(ray,x)
      if isinstance(sip,data.Point):
         res.append((x,sip))
   return res
      
   
def sphere_normal_at_point(sphere,point):
   return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center,
                                                                  point))
