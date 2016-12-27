import math
import data
import vector_math

def quadratic(a,b,c):
   descriminant = b**2 - 4*a*c
   if descriminant >= 0:
        ans1 = (-b)/(2*a) + ((math.sqrt(descriminant))/(2*a))
        ans2 = (-b)/(2*a) - ((math.sqrt(descriminant))/(2*a))
        tlist = [ans1, ans2]
        return tlist
   else:
        return None

def tvalue(t_in):
      if t_in == None:
          return None
      elif t_in[0]>=0:
         if t_in[1]>=0:            
             if t_in[0]>=t_in[1]:
                 return t_in[1]
             else:
                 return t_in[0]
         else:
             return t_in[0]
      elif t_in[1]>=0:
         return t_in[1]
      else:
         return None

def sphere_intersection_point(ray, sphere):
      A = vector_math.dot_vector(ray.dir,ray.dir)
      B = 2 * vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), ray.dir)
      C = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), vector_math.difference_point(ray.pt, sphere.center)) - (sphere.radius * sphere.radius)
      poss_t_val = quadratic(A,B,C)
      t = tvalue(poss_t_val)
      if t == None:
          return None
      else:
          needed_point = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t))
          return needed_point

def find_intersection_points(sphere_list, ray):
      L = []
      for i in range(len(sphere_list)):
          pt = sphere_intersection_point(ray, sphere_list[i])
          if pt!=None:
              L.append((sphere_list[i], pt))
      return L

def sphere_normal_at_point(sphere, point):
     NewVector = vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, point))
     return NewVector
