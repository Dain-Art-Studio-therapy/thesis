
import collisions
import data
import vector_math
   

#The meat and bulk of it all, creates rays from eye_point to every pixel on the 'image' and decides to color the pixel white or send it along to color_of_sphere to determine it's color.
def cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,color,light):
   dx = (max_x-min_x)/float(width)
   dy = (max_y-min_y)/float(height)
   n = ''
   for y in range(0,height):
      for x in range(0,width):
         pt = data.Point(min_x + (dx*x), max_y - (dy*y),0)
         vector = vector_math.vector_from_to(eye_point,pt)
         ray = data.Ray(eye_point, vector)
         if cast_ray(ray, sphere_list)== False:
            n += '255 255 255\n'
         else:
            n += ' '.join(map(str, color_of_sphere(closest_sphere(ray, sphere_list, eye_point), color, ray, sphere_list, eye_point, light))) 
   return n

#Checks if the ray has hit any spheres, if it hasn't, the list will be empy, and cast_all_rays can go ahead and print a white pixel.         
def cast_ray(ray, sphere_list):
   if collisions.find_intersection_points(ray, sphere_list) == []:
      return False
   else:
      return True   


#Returns the closest sphere in the case the ray has hit more than 1 sphere
def closest_sphere(ray, sphere_list, eye_point):
   new_sphere_list_of_success = collisions.find_intersection_points(ray, sphere_list)
   starting_point = new_sphere_list_of_success[0][0]
   starting_sphere = new_sphere_list_of_success[0][1]
   for i in new_sphere_list_of_success:
      if vector_math.length_vector(vector_math.vector_from_to(i[0], eye_point)) < vector_math.length_vector(vector_math.vector_from_to(starting_point, eye_point)):
         starting_point = i[0]
         starting_sphere = i[1]
   return starting_sphere 

#Returns the intersection point on the closest sphere in the case the ray has hit more than 1 sphere 
def closest_intersection_point(ray, sphere_list, eye_point):
   new_sphere_list_of_success = collisions.find_intersection_points(ray, sphere_list)
   starting_point = new_sphere_list_of_success[0][0]
   starting_sphere = new_sphere_list_of_success[0][1]
   for i in new_sphere_list_of_success:
      if vector_math.length_vector(vector_math.vector_from_to(i[0], eye_point)) < vector_math.length_vector(vector_math.vector_from_to(starting_point, eye_point)):
         starting_point = i[0]
         starting_sphere = i[1]
   return starting_point


#Determines the color that the pixel should be
def color_of_sphere(sphere, color, ray, sphere_list, eye_point, light):

#Data needed for brightness component
   the_intersection_point = closest_intersection_point(ray, sphere_list, eye_point)
   the_normal = vector_math.normalize_vector(vector_math.vector_from_to(sphere.center,  the_intersection_point))
   the_scaled_normal = vector_math.scale_vector(the_normal, 0.01)
   point_e = vector_math.translate_point(the_intersection_point, the_scaled_normal) 
   light_vector = vector_math.normalize_vector(vector_math.vector_from_to(point_e, light.point))
   how_bright = vector_math.dot_vector(the_normal, light_vector)

#Data needed for specular component
   reflection_vector = vector_math.normalize_vector(vector_math.difference_vector(light_vector, vector_math.scale_vector(the_normal, (2*how_bright))))
   view_direction = vector_math.normalize_vector(vector_math.vector_from_to(eye_point, point_e))
   specular_intensity = vector_math.dot_vector(reflection_vector, view_direction)

#Specular Intensity colors
   super_red = (255 * sphere.color.r * sphere.finish.ambient * color.ambient.r) + (255 * light.color.r * sphere.color.r * sphere.finish.diffuse * how_bright) + (255 * (specular_intensity**(1.0/sphere.finish.roughness)) * light.color.r * sphere.finish.specular)
   super_blu = (255 * sphere.color.b * sphere.finish.ambient * color.ambient.b) + (255 * light.color.b * sphere.color.b * sphere.finish.diffuse * how_bright) + (255 * (specular_intensity**(1.0/sphere.finish.roughness)) * light.color.b * sphere.finish.specular)
   super_gre = (255 * sphere.color.g * sphere.finish.ambient * color.ambient.g) + (255 * light.color.g * sphere.color.g * sphere.finish.diffuse * how_bright) + (255 * (specular_intensity**(1.0/sphere.finish.roughness)) * light.color.g * sphere.finish.specular)

#Brightness colors  
   red = (255 * sphere.color.r * sphere.finish.ambient * color.ambient.r) + (255 * light.color.r * sphere.color.r * sphere.finish.diffuse * how_bright)
   blu = (255 * sphere.color.b * sphere.finish.ambient * color.ambient.b) + (255 * light.color.b * sphere.color.b * sphere.finish.diffuse * how_bright)
   gre = (255 * sphere.color.g * sphere.finish.ambient * color.ambient.g) + (255 * light.color.g * sphere.color.g * sphere.finish.diffuse * how_bright)

#Ambient light colors
   shade_r = 255 * sphere.color.r * sphere.finish.ambient * color.ambient.r
   shade_b = 255 * sphere.color.b * sphere.finish.ambient * color.ambient.b
   shade_g = 255 * sphere.color.g * sphere.finish.ambient * color.ambient.g
   if how_bright > 0 and all_clear(sphere_list, point_e, light_vector) == True:
      if specular_intensity > 0: 
         return int(super_red), int(super_gre), int(super_blu),'\n'
      else:
         return int(red), int(gre), int(blu),'\n'
   else:
      return int(shade_r), int(shade_g), int(shade_b),'\n' 



#Checks to see if there are any spheres blocking the light
def all_clear(sphere_list, point_e, light_vector):
   light_ray = data.Ray(point_e, light_vector)
   if len(collisions.find_intersection_points(light_ray, sphere_list)) == 0:
      return True
   else:
      return False
   
  
     
