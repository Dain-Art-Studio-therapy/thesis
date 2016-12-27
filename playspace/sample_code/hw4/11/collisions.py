import math
from data import *
from vector_math import * 
def sphere_intersection_point(ray,sphere):
   
    A=dot_vector(ray.dir,ray.dir)
   
    B= ( dot_vector( (difference_point(ray.pt,sphere.center) ), ray.dir ) * 2 )
    
    C=( ( dot_vector( difference_point(ray.pt,sphere.center),
    difference_point(ray.pt,sphere.center)) -(sphere.radius **2) ))

    
    dis  = B**2 - 4*A*C  
    
    if dis<0:
       return None 
   
    neg_quad =( -B - math.sqrt(dis))/(2*A)
    
    pos_quad = (-B + math.sqrt(dis))/(2*A)
   
    t=neg_quad
    t1=pos_quad
   
    y=translate_point(ray.pt, scale_vector(ray.dir,t))
    y1=translate_point(ray.pt,scale_vector(ray.dir,t1))

    
    
    if (t<0 and t1>=0):
      
      return y1

    elif (t>=0 and t<0):
      return y

    
    elif (t>=0 and t1>=0):
      if t<t1:
         return y
      else: 
         return y1
 
    else: 
        
       return None

   
def find_intersection_points(sphere_list,ray):
    sph_pt =[  ]
    
    for sphere in sphere_list:
      if sphere_intersection_point(ray,sphere) is not None:
         sph_pt.append((sphere,sphere_intersection_point(ray,sphere)))

    return sph_pt



def sphere_normal_at_point(sphere,point):
    A = normalize_vector( vector_from_to(sphere.center,point))  

    return A  
















