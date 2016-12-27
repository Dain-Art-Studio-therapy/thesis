import data
import collisions
import vector_math

 
def cast_ray(ray, sphere_list, a_color, light, eye_point):
   list = collisions.find_intersection_points(sphere_list, ray)
   sphere_color = data.Color(1.0, 1.0, 1.0)
   if list != []:
      sphere = list[0][0]
      point = list[0][1]
      distance = vector_math.length_vector(vector_math.vector_from_to(ray.pt,
         list[0][1]))
      for i in range(len(list)):
         if vector_math.length_vector(vector_math.vector_from_to(ray.pt,
            list[i][1])) < distance:
            sphere = list[i][0]
            distance = vector_math.length_vector(vector_math.vector_from_to(
               ray.pt, list[i][1]))
            point = list[i][1]
      n = collisions.sphere_normal_at_point(sphere, point)
      p_e = vector_math.translate_point(point, vector_math.scale_vector(n,
         0.01))
      l_dir = vector_math.normalize_vector(vector_math.vector_from_to(p_e,
         light.pt))
      vis = vector_math.dot_vector(n, l_dir)
      reflect_vector = vector_math.difference_vector(l_dir,
         vector_math.scale_vector(n, (2 * vis)))
      v_dir = vector_math.normalize_vector(vector_math.vector_from_to(eye_point,
         p_e))
      specular_intensity = vector_math.dot_vector(reflect_vector, v_dir)
 
      red = sphere.color.r * sphere.finish.ambient * a_color.r
      green = sphere.color.g * sphere.finish.ambient * a_color.g
      blue = sphere.color.b * sphere.finish.ambient * a_color.b 

      coll_to_light = collisions.find_intersection_points(sphere_list, data.Ray(
         p_e, l_dir))
      
      if vis <= 0:
         sphere_color = data.Color(red, green, blue)
      elif coll_to_light != []:
         close = vector_math.length_vector(vector_math.vector_from_to(p_e,
            light.pt))
         for i in range(len(coll_to_light)):
            if vector_math.length_vector(vector_math.vector_from_to(p_e,
               coll_to_light[i][1])) < close:
               sphere_color = data.Color(red, green, blue)
            else:
               red = red + (vis * light.color.r * sphere.color.r *
                  sphere.finish.diffuse)
               green = green + (vis * light.color.g * sphere.color.g *
                  sphere.finish.diffuse)
               blue = blue + (vis * light.color.g * sphere.color.g *
                  sphere.finish.diffuse)

               if specular_intensity <= 0:
                  pass
               else:
                  spec_cont_r = light.color.r * sphere.finish.specular * \
                     (specular_intensity ** (1.0/sphere.finish.roughness))
                  spec_cont_g = light.color.g * sphere.finish.specular * \
                     (specular_intensity ** (1.0/sphere.finish.roughness))
                  spec_cont_b = light.color.b * sphere.finish.specular * \
                     (specular_intensity ** (1.0/sphere.finish.roughness))

                  red = red + spec_cont_r
                  green = green + spec_cont_g
                  blue = blue + spec_cont_b

               sphere_color = data.Color(red, green, blue)
      else:
         red = red + (vis * light.color.r * sphere.color.r *
            sphere.finish.diffuse)
         green = green + (vis * light.color.g * sphere.color.g *
            sphere.finish.diffuse)
         blue = blue + (vis * light.color.b * sphere.color.b *
            sphere.finish.diffuse)
         
         if specular_intensity <= 0:
            pass
         else:      
            spec_cont_r = light.color.r * sphere.finish.specular * \
               (specular_intensity ** (1.0/sphere.finish.roughness))
            spec_cont_g = light.color.g * sphere.finish.specular * \
               (specular_intensity ** (1.0/sphere.finish.roughness))
            spec_cont_b = light.color.b * sphere.finish.specular * \
               (specular_intensity ** (1.0/sphere.finish.roughness))

            red = red + spec_cont_r
            green = green + spec_cont_g
            blue = blue + spec_cont_b
      
         
         sphere_color = data.Color(red, green, blue)
   return sphere_color
   
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point,
   sphere_list, a_color, light, f):
   
   x_interval = (float(max_x) - float(min_x))/float(width)
   y_interval = (float(max_y) - float(min_y))/float(height)

   x = min_x
   y = max_y

   while y > min_y:
      while x < max_x:
         color = cast_ray(data.Ray(eye_point, vector_math.vector_from_to(
            eye_point, data.Point(x, y, 0.0))), sphere_list, a_color, light,\
            eye_point)
         print >> f, min(int(color.r * 255), 255), min(int(color.g * 255),\
            255) ,min(int(color.b * 255), 255)
         x += x_interval
      x = min_x
      y -= y_interval


