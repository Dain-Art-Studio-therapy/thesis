from collisions import *
from vector_math import *
import data

def color_mult(color1,color2,finish):
   r=color1.r*color2.r*finish
   g=color1.g*color2.g*finish
   b=color1.b*color2.b*finish
   return data.Color(r,g,b)

def scale_color(color,scale):
   r=color.r*scale
   g=color.g*scale
   b=color.b*scale
   return data.Color(r,g,b)

def distance(P1,P2):
   return length_vector(difference_vector(P1,P2))

def diffuse_light(intersection,light):
   N=sphere_normal_at_point(intersection[0],intersection[1])
   PE=translate_point(intersection[1],scale_vector(N,.01))
   L_dir=normalize_vector(vector_from_to(PE,light.pt))
   dot=dot_vector(N,L_dir)
   if dot>0:
      color1=color_mult(light.color,intersection[0].color,dot)
      return scale_color(color1,intersection[0].finish.diffuse)
   else:
      return None

def specular_intensity(intersection,light,eye_point):
   N=sphere_normal_at_point(intersection[0],intersection[1])
   PE=translate_point(intersection[1],scale_vector(N,.01))
   L_dir=normalize_vector(vector_from_to(PE,light.pt))
   fakeN=sphere_normal_at_point(intersection[0],PE)
   dot=dot_vector(N,L_dir)
   reflection_vector=difference_vector(L_dir,scale_vector(N,(2*dot)))
   V_dir=normalize_vector(vector_from_to(eye_point,PE))
   return dot_vector(reflection_vector,V_dir)

def specular_color(light,sphere,intensity):
   r=light.color.r*sphere.finish.specular*intensity
   g=light.color.g*sphere.finish.specular*intensity
   b=light.color.b*sphere.finish.specular*intensity
   return data.Color(r,g,b)

def cast_ray(ray,sphere_list,ambient_color,light,point):
   nearest_intersection=find_closest_sphere(sphere_list,ray)
   if nearest_intersection != []:
      light_ray=Ray(light.pt,vector_from_to(light.pt,nearest_intersection[1]))
      light_intersection=find_closest_sphere(sphere_list,light_ray)
      ambient= color_mult(nearest_intersection[0].color,ambient_color,nearest_intersection[0].finish.ambient)
      if nearest_intersection==light_intersection:
         diffuse=diffuse_light(nearest_intersection,light)
         intensity=specular_intensity(nearest_intersection,light,point)
         if diffuse !=None:
            ambient_diffuse=add_colors(ambient,diffuse)
            if intensity>0:
               adjust_intensity=intensity**(1/nearest_intersection[0].finish.roughness)
               spec_color=specular_color(light,nearest_intersection[0],adjust_intensity)
               return add_colors(ambient_diffuse,spec_color)
            else:
               return ambient_diffuse
         else:
            return ambient
      else:
         return ambient
   else:
      return data.Color(1,1,1)

def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,ambient_color,light):
   print 'P3'
   print width,height
   print '255'
   w_increase=(max_x-min_x)/float(width)
   h_increase=(max_y-min_y)/float(height)
   for h in range(height):
      for w in range(width):
         x=min_x+(w_increase*w)
         y=max_y-(h_increase*h)
         ray=data.Ray(eye_point,vector_from_to(eye_point,data.Point(x,y,0)))
         color=convert_color(cast_ray(ray,sphere_list,ambient_color,light,eye_point))
         print color.r,color.g,color.b

def convert_color(color):
   r=int(color.r*255)
   g=int(color.g*255)
   b=int(color.b*255)
   if color.r>1:
      r=255
   if color.g>1:
      g=255
   if color.b>1:
      b=255
   return data.Color(r,g,b)
