from vector_math import *
import math
import data

def sphere_intersection_point(ray,sphere):
   A=dot_vector(ray.dir,ray.dir)
   B=(2*dot_vector(difference_vector(ray.pt,sphere.center),ray.dir))
   C=(dot_vector(difference_point(ray.pt,sphere.center),difference_point(ray.pt,sphere.center))-sphere.radius**2)
   root=(B**2)-(4*A*C)
   if root>=0:
      sroot=math.sqrt(root)
      t1=((-1*B)+sroot)/(2*A)
      t2=((-1*B)-sroot)/(2*A)
      if t1>=0 and t2>=0:
         if t1<=t2:
            return (translate_point(ray.pt,scale_vector(ray.dir,t1)))
         else:
            return (translate_point(ray.pt,scale_vector(ray.dir,t2)))
      elif t1>=0:
         return (translate_point(ray.pt,scale_vector(ray.dir,t1)))
      elif t2>=0:
         return (translate_point(ray.pt,scale_vector(ray.dir,t2)))

def find_intersection_points(sphere_list,ray):
   newlist=[]
   for s in sphere_list:
      intersection=sphere_intersection_point(ray,s)
      if intersection != None:
         newlist.append((s,intersection))
   return newlist

def sphere_normal_at_point(sphere,point):
   return normalize_vector(vector_from_to(sphere.center,point))

def distance(P1,P2):
   return length_vector(difference_vector(P1,P2))

def distance_squared(P1,P2):
   return length_squared_vector(difference_vector(P1,P2))

def find_closest_sphere(sphere_list,ray):
   points=find_intersection_points(sphere_list,ray)
   if points != []:
      nearest=0
      for s in range(len(points)):
         if distance_squared(ray.pt,points[s][1])<distance_squared(ray.pt,points[nearest][1]):
            nearest=s
      return points[nearest]
   else:
      return []

def add_colors(c1,c2):
   r=c1.r+c2.r
   g=c1.g+c2.g
   b=c1.b+c2.b
   return data.Color(r,g,b)
