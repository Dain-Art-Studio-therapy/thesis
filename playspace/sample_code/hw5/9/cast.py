import math
import data
import vector_math
import collisions
from utility import convert_float
from utility import nearest_to_point
import utility
import commandline

def cast_ray(ray,sphere_list,ambient_light,light,point):
   sphere_pts = collisions.find_intersection_points(sphere_list,ray)
    
   if sphere_pts == []:
      return data.Color(1.0,1.0,1.0)
   else:
      pts  = [t[1] for t in sphere_pts]
      index_of_nearest_pt = nearest_to_point(pts,ray.pt)

      intersection_pt = sphere_pts[index_of_nearest_pt][1]
      intersection_sphere = sphere_pts[index_of_nearest_pt][0]
      color_of_sphere = intersection_sphere.color
      sphere_ambience = data.Color(intersection_sphere.finish.ambient * ambient_light.r * color_of_sphere.r, 
                                   intersection_sphere.finish.ambient * ambient_light.g * color_of_sphere.g,
                                   intersection_sphere.finish.ambient * ambient_light.b * color_of_sphere.b)
      sphere_diffuse = intersection_sphere.finish.diffuse
      N = collisions.sphere_normal_at_point(intersection_sphere,intersection_pt)
      short_vector = vector_math.scale_vector(N,0.01)
      pE = vector_math.translate_point(intersection_pt,short_vector)
      Ldir = vector_math.normalize_vector(vector_math.vector_from_to(pE,light.pt))
      LdotN = vector_math.dot_vector(N,Ldir)
      reflection_vector = vector_math.difference_vector(Ldir,vector_math.scale_vector(N,(2*LdotN)))
      Vdir = vector_math.normalize_vector(vector_math.vector_from_to(point,pE))
      specular_intensity = vector_math.dot_vector(reflection_vector,Vdir)

      if specular_intensity > 0:
         specular_contrib_r = light.color.r*intersection_sphere.finish.specular*specular_intensity**(1/intersection_sphere.finish.roughness)
       	 specular_contrib_g = light.color.g*intersection_sphere.finish.specular*specular_intensity**(1/intersection_sphere.finish.roughness)
       	 specular_contrib_b = light.color.b*intersection_sphere.finish.specular*specular_intensity**(1/intersection_sphere.finish.roughness)
      elif specular_intensity <= 0:
         specular_contrib_r = 0
         specular_contrib_g = 0
         specular_contrib_b = 0
      
      if LdotN <= 0:
         diffuse_light_r = 0
         diffuse_light_g = 0
         diffuse_light_b = 0
         specular_contrib_r = 0
         specular_contrib_g = 0
         specular_contrib_b = 0

      else:
         check_sphere_int = collisions.find_intersection_points(sphere_list,data.Ray(pE,Ldir)) 
         if check_sphere_int == []:
            diffuse_light_r = LdotN * light.color.r * color_of_sphere.r * sphere_diffuse
            diffuse_light_g = LdotN * light.color.g * color_of_sphere.g * sphere_diffuse
            diffuse_light_b = LdotN * light.color.b * color_of_sphere.b * sphere_diffuse 
         elif check_sphere_int != []:
            for i in range(len(check_sphere_int)):
               ray_hits = [check_sphere_int[i][1] for t in check_sphere_int]
               for h in ray_hits:
                  if utility.distance_from_a_point(h.x,h.y,h.z,pE) < utility.distance_from_a_point(light.pt.x,light.pt.y,light.pt.z,pE):
                     diffuse_light_r = 0
                     diffuse_light_g = 0
                     diffuse_light_b = 0
                     specular_contrib_r = 0
                     specular_contrib_g = 0
                     specular_contrib_b = 0
                  else:
                     diffuse_light_r = LdotN * light.color.r * color_of_sphere.r * sphere_diffuse 
                     diffuse_light_g = LdotN * light.color.g * color_of_sphere.g * sphere_diffuse
                     diffuse_light_b = LdotN * light.color.b * color_of_sphere.b * sphere.diffuse
   
      red_value = diffuse_light_r + sphere_ambience.r + specular_contrib_r
      green_value = diffuse_light_g + sphere_ambience.g + specular_contrib_g
      blue_value = diffuse_light_b + sphere_ambience.b + specular_contrib_b

      return data.Color(red_value,green_value,blue_value)

def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,ambient_light,light):
   
   file_object = commandline.open_file('image.ppm','w')

   print >> file_object, 'P3'
   print >> file_object, width, height
   print >> file_object, '255'

   dx = (max_x-min_x)/float(width)
   dy = (max_y-min_y)/float(height)
   for h in range(height): 
      for w in range(width):
         x = min_x + (dx*w)
         y = max_y - (dy*h)
         ray_cast = cast_ray(data.Ray(eye_point,vector_math.vector_from_to(eye_point,data.Point(x,y,0))),
                    sphere_list,ambient_light,light,eye_point)

         r = ray_cast.r
         g = ray_cast.g
         b = ray_cast.b
         
 
   
         print >> file_object, convert_float(r),convert_float(g),convert_float(b)
