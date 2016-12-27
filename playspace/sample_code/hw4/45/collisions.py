from vector_math import *

# check if discriminant is negative initially


def sphere_intersection_point(ray,sphere):

    a = dot_vector(ray.dir,ray.dir)
    diff = difference_point(ray.pt,sphere.center)
    b =  dot_vector(diff,ray.dir) *2
    c = dot_vector(diff,diff) - sphere.radius**2


    d = (b**2)-(4*a*c)

    if d>=0:
       t1 = (-b + math.sqrt(d))/(2*a)
       t2 = (-b - math.sqrt(d))/(2*a)

       if t1>=0 and t1<t2:
          V1 = scale_vector(ray.dir,t1)
          return translate_point(ray.pt,V1)

       elif t2>=0 and t1>t2:
          V2 = scale_vector(ray.dir,t2)
          return translate_point(ray.pt,V2)

       elif t1>=0:
         V3 = scale_vector(ray.dir,t1)
         return translate_point(ray.pt,V3)

       elif t2>=0:
         V4 = scale_vector(ray.dir,t2)
         return translate_point(ray.pt,V4)


    else:
      return None



def find_intersection_points(sphere_list,ray):
   new_list=[]
   for sphere in sphere_list:
      point = sphere_intersection_point(ray,sphere)
      if point != None:
         new_list.append((sphere,point))
   return new_list



def sphere_normal_at_point(sphere,point):
   new_vector = vector_from_to(sphere.center,point)
   return normalize_vector(new_vector)



