from collisions import *
from vector_math import *

def cast_ray(ray,sphere_list,amb_color,light,point):
   search = find_intersection_points(sphere_list,ray)
   if(search == []):
      return Color(1.0,1.0,1.0)
   neardex = 0
   for e in range(1,len(search)):
      e_dist = length_vector(difference_point(ray.pt,search[e][1]))
      near_dist = length_vector(difference_point(ray.pt,search[neardex][1]))
      if(e_dist < near_dist):
         neardex = e
   near_sphere = search[neardex][0]
   N = sphere_normal_at_point(search[neardex][0],search[neardex][1])
   Pe = translate_point(search[neardex][1],scale_vector(N,0.01))
   Ldir = normalize_vector(vector_from_to(Pe,light.pt))
   dprod = dot_vector(N,Ldir)
   block = find_intersection_points(sphere_list,Ray(Pe,Ldir))
   scalar = near_sphere.finish.ambient*amb_color
   new_r = near_sphere.color.r*scalar
   new_g = near_sphere.color.g*scalar
   new_b = near_sphere.color.b*scalar
   lightr = light.color.r*dprod*near_sphere.finish.diffuse*near_sphere.color.r
   lightg = light.color.g*dprod*near_sphere.finish.diffuse*near_sphere.color.g
   lightb = light.color.b*dprod*near_sphere.finish.diffuse*near_sphere.color.b
   reflection = vector_from_to(scale_vector(N,dprod*2),Ldir)
   Vdir = normalize_vector(vector_from_to(point,Pe))
   spec_int = dot_vector(reflection,Vdir)
   spec_r = (light.color.r*near_sphere.finish.specular*
              (spec_int**(1/near_sphere.finish.roughness)))
   spec_g = (light.color.g*near_sphere.finish.specular*
              (spec_int**(1/near_sphere.finish.roughness)))
   spec_b = (light.color.b*near_sphere.finish.specular*
              (spec_int**(1/near_sphere.finish.roughness)))
   part_four = Color(new_r+lightr,new_g+lightg,new_b+lightb)
   part_five = Color(part_four.r+spec_r,part_four.g+spec_g,part_four.b+spec_b)
   if(part_five.r > 1):
      part_five.r = 1
   if(part_five.g > 1):
      part_five.g = 1
   if(part_five.b > 1):
      part_five.b = 1
   if(dprod > 0 and block == []):
      if(spec_int > 0):
         return part_five
      else:
         return part_four
   return Color(new_r,new_g,new_b)   

def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,Color,light,point):
   dx = (max_x-min_x)/float(width)
   dy = (max_y-min_y)/float(height)
   for j in range(height):
      for i in range(width):
         x = min_x + i*dx
         y = max_y - j*dy
         z = 0
         ray = Ray(eye_point,difference_point(Point(x,y,z),eye_point))
         new_color = cast_ray(ray,sphere_list,Color,light,point)
         print int(new_color.r*255),int(new_color.g*255),int(new_color.b*255)
      
