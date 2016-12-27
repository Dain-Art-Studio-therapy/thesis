import collisions
import vector_math
import data

def ambient_color(color, sphere):
   ambient= sphere.finish.ambient
   r= sphere.color.r * ambient * color.r
   g= sphere.color.g * ambient * color.g
   b= sphere.color.b * ambient * color.b
   return data.Color(r, g, b)

def light_color_diffused(light, sphere, visible_value):
   diffuse_visibility= sphere.finish.diffuse * visible_value
   r= light.color.r * diffuse_visibility * sphere.color.r
   g= light.color.g * diffuse_visibility * sphere.color.g
   b= light.color.b * diffuse_visibility * sphere.color.b
   return data.Color(r, g, b)

def ambient_light_color_diffused(ambcolor, lcolor):
   r= ambcolor.r + lcolor.r
   g= ambcolor.g + lcolor.g
   b= ambcolor.b + lcolor.b
   return data.Color(r, g, b)

def specular_light_roughness(light, sphere, specular_intensity):
   exponent_roughness= 1/sphere.finish.roughness
   spec= sphere.finish.specular
   spec_roughness= spec * (specular_intensity ** exponent_roughness)
   r= light.color.r * spec_roughness
   g= light.color.g * spec_roughness
   b= light.color.b * spec_roughness
   return data.Color(r, g, b)

def specular_ambient_diffuse(ambdiff, specrough):
   r= ambdiff.r + specrough.r
   g= ambdiff.g + specrough.g
   b= ambdiff.b + specrough.b
   return data.Color(r, g, b)

def move_point(sphere, point):
   normalized_vector= collisions.sphere_normal_at_point(sphere, point)
   scaled_vector= vector_math.scale_vector(normalized_vector, 0.01)
   translated_point= vector_math.translate_point(point, scaled_vector)
   return translated_point


def cast_ray(ray, sphere_list, color, light, eye_point):
   sip= collisions.find_intersection_points(sphere_list,ray)
   if sip == []:
      return data.Color(1.0, 1.0, 1.0)
   else:
      min= vector_math.length_vector(vector_math.vector_from_to(ray.pt, sip[0][1]))
      object= sip[0]
      for s in sip:
         if vector_math.length_vector(vector_math.vector_from_to(ray.pt, s[1])) < min:
            min=s[1]
            object= s
      closer_sphere= object[0]
      closer_sphere_point= object[1]
      ambient_colored= ambient_color(color, closer_sphere)
      N= collisions.sphere_normal_at_point(closer_sphere, closer_sphere_point)
      Pe= move_point(closer_sphere, closer_sphere_point)
      Ldir= vector_math.normalize_vector(vector_math.vector_from_to(Pe, light.pt))
      visible_value= vector_math.dot_vector(N, Ldir)
      lighting= True
      spec_light= True
      ambient_color_diffused_visibility= light_color_diffused(light, closer_sphere, visible_value)
      ambient_diffuse= ambient_light_color_diffused(ambient_colored, ambient_color_diffused_visibility)
      reflection_vector= vector_math.difference_vector(Ldir, vector_math.scale_vector(N ,(2 * visible_value)))
      Vdir= vector_math.normalize_vector(vector_math.vector_from_to(eye_point, Pe))
      specular_intensity= vector_math.dot_vector(reflection_vector, Vdir)
      specular_diffusion= specular_light_roughness(light, closer_sphere, specular_intensity)
      speculated_color= specular_ambient_diffuse(ambient_diffuse ,specular_diffusion)
      if visible_value >0:
         off_ray= data.Ray(Pe, Ldir)
         sip_off= collisions.find_intersection_points(sphere_list, off_ray)
         if sip_off != []:
            light_sip_off= vector_math.vector_from_to(Pe, light.pt)
            for pt in range(len(sip)):
               vector_sphere_collision= vector_math.vector_from_to(Pe, sip_off[pt][1])
               if vector_math.length_vector(vector_sphere_collision) < vector_math.length_vector(light_sip_off):
                  lighting= False
         else:
            lighting= True
      else:
         lighting= False
      if specular_intensity > 0:
         spec_light= True
      else:
         spec_light=False
      if spec_light == True and lighting ==True:
         return speculated_color
      elif lighting == True:
         return ambient_diffuse
      else:
         return ambient_colored

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light):
   change_x= (max_x-min_x)/ float(width)
   change_y= (max_y-min_y)/ float(height)
   for y in range(0, height):
      y= max_y - y*change_y
      for x in range(0, width):
         x= min_x + x*change_x
         vector= vector_math.vector_from_to(eye_point, data.Point(x,y,0.0))
         color_sphere= cast_ray(data.Ray(eye_point, vector), sphere_list, color, light, eye_point)
         red_color= color_sphere.r * 255
         blue_color= color_sphere.b * 255
         green_color= color_sphere.g * 255
         if red_color > 255:
            red_color= 255
         if blue_color > 255:
            blue_color = 255
         if green_color > 255:
            green_color = 255
         sphere_color= data.Color(int(red_color), int(green_color), int(blue_color))
         print sphere_color.r, sphere_color.g, sphere_color.b
