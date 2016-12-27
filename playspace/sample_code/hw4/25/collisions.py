import math
import data
import vector_math
def sip_a(ray):
   A= (vector_math.dot_vector(ray.dir, ray.dir))
   return A

def sip_b(ray, sphere):
   B= (2 * vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), ray.dir))
   return B

def sip_c(ray, sphere):
   C= (vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center),vector_math.difference_point(ray.pt, sphere.center)) - ((sphere.radius) ** 2))
   return C

def sip_discriminant(ray, sphere):
   root_exists= ((sip_b(ray, sphere)**2) - 4 * (sip_a(ray)) * (sip_c(ray, sphere)))
   return root_exists
def sip_smaller_root(ray, sphere):
   root1= ((-sip_b(ray, sphere) + math.sqrt((sip_b(ray, sphere)**2) - 4*(sip_a(ray)) * (sip_c(ray, sphere))))/(2*(sip_a(ray))))
   root2= ((-sip_b(ray, sphere) - math.sqrt((sip_b(ray, sphere)**2) - 4*(sip_a(ray)) * (sip_c(ray, sphere))))/(2*(sip_a(ray))))
   if root1 >=0 and root2 >=0:
      return min(root1, root2)
   elif root1 <0 and root2 <0:
      return None
   elif root1 <0 or root2 <0:
      if root1 <0:
         return root2
      elif root2 <0:
         return root1

def sip_point_t(ray, sphere):
   if sip_smaller_root(ray, sphere) == None:
      return None
   else:
      point_t= vector_math.translate_point(ray.pt, (vector_math.scale_vector(ray.dir, sip_smaller_root(ray, sphere))))
      return point_t

def sphere_intersection_point(ray, sphere):
   if sip_discriminant(ray,sphere) < 0:
      return None
   else:
      return sip_point_t(ray, sphere)

def find_intersection_points(sphere_list, ray):
   newlist= []
   for s in sphere_list:
      sip= sphere_intersection_point(ray, s)
      if sip != None:
         newlist.append((s, sip))
   return newlist

def sphere_normal_at_point(sphere, point):
   sphere_vector= vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, point))
   return sphere_vector
