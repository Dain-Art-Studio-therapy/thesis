import data
import vector_math
import collisions 


def cast_ray(ray, sphere_list, ambient_light_color, light): 
   cast = collisions.find_intersection_points(sphere_list, ray)

   if len(cast) > 0:
      first_sphere = cast[0] 
      for i in range(len(cast)):
      #this looks through the index of the list of collided spheres 
         if vector_math.length_vector(vector_math.difference_point(cast[i][1], ray.pt)) < \
            vector_math.length_vector(vector_math.difference_point(first_sphere[1], ray.pt)): 
           #this says if the next index has a smaller 'difference point' ie is closer to initial ray point then it will move/replace that number in that spot
            first_sphere = cast[i]
             
      sphere_norm = collisions.sphere_normal_at_point(first_sphere[0], first_sphere[1])
      scaled_vec = vector_math.scale_vector(sphere_norm, 0.01)
      pe = vector_math.translate_point(first_sphere[0].center, scaled_vec)
      ldir = vector_math.normalize_vector(vector_math.difference_point(light.pt, pe))
      light_visible = vector_math.dot_vector(sphere_norm, ldir) 
           
      second_sphere = first_sphere
      newray = data.Ray(pe, ldir)
      cast2 = collisions.find_intersection_points(sphere_list, newray)
      
      for i in range(len(cast2)):     
         if vector_math.length_vector(vector_math.difference_point(cast2[i][1], newray.pt)) < \
            vector_math.length_vector(vector_math.difference_point(second_sphere[1], newray.pt)):
            second_sphere = cast2[i]
             
      if light_visible > 0 and second_sphere[1] == first_sphere[1]:
         return data.Color(light_visible * light.color.r * first_sphere[0].color.r * first_sphere[0].finish.diffuse + 
                              first_sphere[0].color.r * first_sphere[0].finish.ambient * ambient_light_color.r, 
                           light_visible * light.color.g * first_sphere[0].color.g * first_sphere[0].finish.diffuse + 
                              first_sphere[0].color.g * first_sphere[0].finish.ambient * ambient_light_color.g, 
                           light_visible * light.color.b * first_sphere[0].color.b * first_sphere[0].finish.diffuse + 
                              first_sphere[0].color.b * first_sphere[0].finish.ambient * ambient_light_color.b)
      else:
         return data.Color(first_sphere[0].color.r * first_sphere[0].finish.ambient * ambient_light_color.r, 
                           first_sphere[0].color.g * first_sphere[0].finish.ambient * ambient_light_color.g, 
                           first_sphere[0].color.b * first_sphere[0].finish.ambient * ambient_light_color.b)                        
         
   return data.Color(1.0,1.0,1.0)
   
   

   #translate the intersection point along the vector (using sphere_normal_at_point) SCALE THE NORMALIZED VECTOR BY .01
       
     
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient_light_color, light): 
                  
   rectwidth = (max_x - min_x)/float(width) 
   rectheight = (max_y - min_y)/float(height)
  
   def ray_point(x,y):
      return data.Point(min_x + x * rectwidth, max_y - y * rectheight, 0.0)
      #this returns the point at which the ray intersects the pixel 
         
   for y in range(height):
      for x in range(width):
        #cast the rays
         the_ray = data.Ray(eye_point, vector_math.vector_from_to(eye_point, ray_point(x,y)))
         newcolor = cast_ray(the_ray, sphere_list, ambient_light_color, light) 
         
         newcolor_list = []
         if newcolor is not data.Color(1.0,1.0,1.0):      
            newcolor_list.append( (min(int(newcolor.r*255), 255),
                                   min(int(newcolor.g*255), 255),
                                   min(int(newcolor.b*255), 255)) )    
                 
         else:
            newcolor_list.append( (int(255), int(255), int(255)) )

            
            
            
            
            
            
            
            
