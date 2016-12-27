from collisions import *
from vector_math import *
from utility import *

def cast_ray(ray,sphere_list,ambient_light,light,pt):
   list = find_intersection_points(sphere_list,ray) 
   if list != []:
      close_sphere = list[0][0]
      close_point = list[0][1]
      min_dist = length_vector(vector_from_to(ray.pt,close_point))
      for i in list:
         length = length_vector(vector_from_to(ray.pt,i[1]))
         if (length<min_dist):
            close_sphere = i[0]
            close_point = i[1]
            min_dist = length
      N = sphere_normal_at_point(close_sphere,close_point)
      PE2 = scale_vector(N,.01)
      PE = translate_point(close_point,PE2)
      Ldir = normalize_vector(vector_from_to(PE,light.pt))
      dot = dot_vector(N,Ldir)
      diffr = (dot*light.color.r*close_sphere.color.r*close_sphere.finish.diffuse)
      diffg = (dot*light.color.g*close_sphere.color.g*close_sphere.finish.diffuse)
      diffb = (dot*light.color.b*close_sphere.color.b*close_sphere.finish.diffuse)
      diff_finish = Color(diffr,diffg,diffb)
      PEray = Ray(PE,Ldir)
      find = find_intersection_points(sphere_list,PEray)
      #print dot,len(find)
      reflection_vector1 = scale_vector(N,2*dot)
      reflection_vector = difference_vector(Ldir,reflection_vector1)
      Vdir = normalize_vector(vector_from_to(ray.pt,PE))
      specular = dot_vector(reflection_vector,Vdir)
      RR = light.color.r*close_sphere.finish.specular*(specular**(1/close_sphere.finish.roughness))
      GG = light.color.g*close_sphere.finish.specular*(specular**(1/close_sphere.finish.roughness))
      BB = light.color.b*close_sphere.finish.specular*(specular**(1/close_sphere.finish.roughness))
      my_new_color = Color(RR,GG,BB)
      if specular > 0 and dot > 0 and find == []:
         return color_add(color_add(diff_finish,(color_multiply(color_scale(close_sphere.color, close_sphere.finish.ambient), ambient_light))),my_new_color)
   
      elif dot > 0 and find == []:
         return color_add(diff_finish,(color_multiply(color_scale(close_sphere.color, close_sphere.finish.ambient), ambient_light)))
      else:
         return (color_multiply(color_scale(close_sphere.color, close_sphere.finish.ambient), ambient_light))
   else:
      return Color(1.0,1.0,1.0)
           
 

def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,ambient_light,light):
   dx = (max_x - min_x)/float(width)
   dy = (max_y - min_y)/float(height)
   for j in range(height):
      for i in range(width):
         x = min_x + i*dx
         y = max_y - j*dy
         z = 0
         ray = Ray(eye_point,difference_point(Point(x,y,z),eye_point))
         
         color = cast_ray(ray,sphere_list,ambient_light,light,ray.pt)
         if color.r>1:
            color.r = 1
         if color.g>1:
            color.g = 1
         if color.b>1:
            color.b = 1
         print 255*color.r, 255*color.g, 255*color.b

def find_closest_sphere(ray,sphere_list):
   list = find_intersection_points(sphere_list,ray)
   if list != []:
      close_sphere = list[0][0]
      close_point = list[0][1]
      min_dist = length_vector(vector_from_to(ray.pt,close_point))
      for i in list:
         length = length_vector(vector_from_to(ray.pt,i[1]))
         if (length<min_dist):
            close_sphere = i[0]
            close_point = i[1]
            min_dist = length
         return (close_sphere,close_point)

            
       
            
