import data
import vector_math
import math

def sphere_intersection_point(ray, sphere):
   a = vector_math.dot_vector(ray.dir, ray.dir)
   b = 2 * (vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), ray.dir))
   c = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), vector_math.difference_point(ray.pt, sphere.center)) - sphere.radius**2 
   # dis_t = math.sqrt(b ** 2 - (4 * a * c))
   # pos_t = - b + dis_t
   # neg_t = - b - dis_t
   if ((4 * a * c) > (b ** 2)):
       return None

   pos_t = (- b + math.sqrt(b ** 2 - (4 * a * c)))/(2 * a)
   neg_t = (- b - math.sqrt(b ** 2 - (4 * a * c)))/(2 * a)
   


   if (pos_t >= 0 and neg_t >= 0):
       pointp = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, pos_t))
       pointn = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, neg_t))
       return pointn 

   elif (pos_t >= 0 and neg_t < 0):
       pointp = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, pos_t))
       return pointp

   elif (pos_t < 0 and neg_t >= 0):
       pointn = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, pos_t))
       return pointn

   else:
       return None

def find_intersection_points(sphere_list, ray):
   v = []
   for sphere in sphere_list:
      if (sphere_intersection_point(ray, sphere) is not None):
         v.append((sphere, sphere_intersection_point(ray, sphere)))     
   return v
    

def sphere_normal_at_point(sphere, point):
   return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, point))
