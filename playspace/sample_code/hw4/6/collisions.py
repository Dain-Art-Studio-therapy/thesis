import math
import vector_math
import data 

def quad_formula_1root(A,B,C):
   return (-B/(2*A))

def quad_formula_2rootA(A,B,C):
   return ((- B + (math.sqrt(B**2 - (4*A*C))))/(2*A))

def quad_formula_2rootB(A,B,C):
   return ((- B - (math.sqrt(B**2 - (4*A*C))))/(2*A))

def sphere_intersection_point(ray,sphere):
   A = vector_math.dot_vector(ray.dir,ray.dir)
   B = 2 * (vector_math.dot_vector((vector_math.difference_point(ray.pt,sphere.center)),ray.dir))
   C = vector_math.dot_vector((vector_math.difference_point(ray.pt,sphere.center)),(vector_math.difference_point(ray.pt,sphere.center))) - (sphere.radius * sphere.radius)

   if (B**2 - (4* A * C)) < 0: 
       return None
   elif (B**2 - (4 * A * C))==0:
       t = quad_formula_1root(A,B,C)
       return vector_math.translate_point(ray.pt,(vector_math.scale_vector(ray.dir,t)))
   else:
       t1 = quad_formula_2rootA(A,B,C)
       t2 = quad_formula_2rootB(A,B,C)
       if t1 >= t2 and t2 > 0:
          return (vector_math.translate_point(ray.pt,(vector_math.scale_vector(ray.dir,t2))))
       elif t1 > 0:
          return (vector_math.translate_point(ray.pt,(vector_math.scale_vector(ray.dir,t1))))
       else:
          return None

def find_intersection_points(sphere_list,ray):
   if sphere_list == []:
       return None
   int_list = []
   for i in sphere_list:
      pt = sphere_intersection_point(ray,i)
      if pt != None:
         int_list.append((i,pt))
   return int_list
       


def sphere_normal_at_point(sphere,point):
   return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center,point))
