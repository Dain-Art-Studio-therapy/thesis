import collisions
import data
import vector_math
import math

#calculates distance of a ray's point and any point
def find_distance(ray, intersect_pt):
   x2 = intersect_pt.x
   x1 = ray.pt.x
   y2 = intersect_pt.y
   y1 = ray.pt.y
   z2 = intersect_pt.z
   z1 = ray.pt.z
   d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
   return d

#casts a ray and determines if it hits a sphere
def cast_ray(ray, sphere_list, Color, Light, Point):
   white = data.Color(1.0, 1.0, 1.0)
   intersection_list = collisions.find_intersection_points(sphere_list, ray)
   if intersection_list == []:
      return white
   else:
      point_color = find_point_color(ray, sphere_list, intersection_list,
                                       Color, Light, Point)
      return point_color

#finds the color of individual pixels on a sphere
def find_point_color(ray, sphere_list, list_of_intersections, Color, Light, Point):
      mindex = 0
      for e in range(1, len(list_of_intersections)):
         if (find_distance(ray, list_of_intersections[e][1]) < 
            find_distance(ray, list_of_intersections[mindex][1])):
            mindex = e
      
      near_sphere = list_of_intersections[mindex][0]
      intersect_pt = list_of_intersections[mindex][1]
      diffuse_value = light_visible(near_sphere, intersect_pt,
                                    Light, sphere_list)
      specular_value = is_specular_contribution(near_sphere,
                                                intersect_pt, Light, Point)
      ambience_value = near_sphere.finish.ambient
      sphere_color = near_sphere.color

      red_value = (sphere_color.r * Color.r * ambience_value
                   + diffuse_value[0]  + specular_value[0])
      green_value = (sphere_color.g * Color.g * ambience_value
                     + diffuse_value[1] + specular_value[1])
      blue_value = (sphere_color.b * Color.b * ambience_value
                    + diffuse_value[2] + specular_value[2])
      sphere_color_finish = data.Color(red_value, green_value, blue_value)                    
      return sphere_color_finish

#creates a scene
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, Color, Light):
   x_list = range(width)
   y_list = range(height)
   x_inc = ((max_x - min_x) / float(width))
   y_inc = ((max_y - min_y) / float(height))
   with open('image.ppm', 'wb') as f:
      print >> f, "P3"
      print >> f, width, height
      print >> f, 255
      for y in y_list:
         y_step = max_y - (y_inc * y)
         for x in x_list:
            x_step = min_x + (x_inc * x)
            single_ray = data.Ray(eye_point, 
                         vector_math.vector_from_to(eye_point,
                         data.Point(x_step, y_step, 0.0)))
            sphere_color = cast_ray(single_ray, sphere_list,
                                    Color, Light, eye_point)
            red_value = min(int(255 * sphere_color.r), 255)
            green_value = min(int(255 * sphere_color.g), 255)
            blue_value = min(int(255 * sphere_color.b), 255)
            print >> f, (red_value), (green_value), (blue_value)

#computes the normal vector from the sphere's center to the intersect pt
def find_N(sphere, intersect_pt):
   N = collisions.sphere_normal_at_point(sphere, intersect_pt)
   return N

#translates intersect point so it is outside of sphere indefinitely
def find_px(sphere, intersect_pt):
   N = find_N(sphere, intersect_pt)
   small_vector = vector_math.scale_vector(N, 0.01)
   px = vector_math.translate_point(intersect_pt, 
                                    small_vector)
   return px

#computes a normal vector from px to the light
def find_Ldir(sphere, intersect_pt, Light):
   px = find_px(sphere, intersect_pt)
   long_vector = vector_math.vector_from_to(px, Light.pt)
   Ldir = vector_math.normalize_vector(long_vector)
   return Ldir

#checks if the light is visible
def light_visible(sphere, intersect_pt, Light, sphere_list):
   LdotN = find_LdotN(sphere, intersect_pt, Light)
   if LdotN > 0:
      if is_light_obscured(sphere, intersect_pt, Light, sphere_list) == False:
         diffuse_value = light_contribution(sphere, intersect_pt, Light)
         return diffuse_value
      else:
         diffuse_value = [0.0,0.0,0.0]
         return diffuse_value
   else:
      diffuse_value = [0.0,0.0,0.0]
      return diffuse_value


#check if anything is in the path of the light
def is_light_obscured(sphere, intersect_pt, Light, sphere_list):
   px = find_px(sphere, intersect_pt)
   Ldir = find_Ldir(sphere, intersect_pt, Light) 
   ray_to_light = data.Ray(px, Ldir)
   intersection_list = collisions.find_intersection_points(sphere_list, 
                                                           ray_to_light)
   if intersection_list == []:
      return False
   elif intersection_list != []:
      for (sphere, intersect_pt) in intersection_list:
         if (find_distance(ray_to_light, intersect_pt) < 
             find_distance(ray_to_light, Light.pt)):
            return True
   else:
      return False


#finds the contribution of light to color of point on sphere
def light_contribution(sphere, intersect_pt, Light):
   a = find_LdotN(sphere, intersect_pt, Light)
   b_red = Light.color.r
   b_green = Light.color.g
   b_blue = Light.color.b
   c_red = sphere.color.r
   c_green = sphere.color.g
   c_blue = sphere.color.b
   d = sphere.finish.diffuse
  
   red_diffuse = a * b_red * c_red * d
   green_diffuse = a * b_green * c_green * d
   blue_diffuse = a * b_blue * c_blue * d
   return [red_diffuse, green_diffuse, blue_diffuse]


#checks if the specular contributes to the sphere's color
def is_specular_contribution(sphere, intersect_pt, Light, Point):
   if find_specular_intensity(sphere, intersect_pt, Light, Point) > 0:
      specular_value = find_specular_value(sphere, intersect_pt, Light, Point)
      return specular_value
   else:
      specular_value = [0.0,0.0,0.0]
      return specular_value

#computes the specular value
def find_specular_value(sphere, intersect_pt, Light, Point):
   specular_intensity = find_specular_intensity(sphere, intersect_pt,
                                                Light, Point)
   sphere_roughness = sphere.finish.roughness
   power = 1.0/sphere_roughness

   light_red = Light.color.r
   light_green = Light.color.g
   light_blue = Light.color.b
   sphere_specular = sphere.finish.specular
   sphere_specular_new = specular_intensity**power

   red_specular = light_red * sphere_specular * sphere_specular_new
   green_specular = light_green * sphere_specular * sphere_specular_new
   blue_specular = light_blue * sphere_specular * sphere_specular_new
   specular_contribution = [red_specular, green_specular, blue_specular]
   return specular_contribution


#computes the intensity of the specular
def find_specular_intensity(sphere, intersect_pt, Light, Point):
   Ldir = find_Ldir(sphere, intersect_pt, Light)
   LdotN = find_LdotN(sphere, intersect_pt, Light)
   reflection_vector = find_reflection_vector(sphere, intersect_pt, Light)
   Vdir = find_Vdir(sphere, intersect_pt, Point)
   specular_intensity = vector_math.dot_vector(reflection_vector, Vdir)
   return specular_intensity
   
#computes dot product of N and Ldir (abstracted for any sphere, intersect, light)
def find_LdotN(sphere, intersect_pt, Light):
   N = find_N(sphere, intersect_pt)
   Ldir = find_Ldir(sphere, intersect_pt, Light)
   LdotN = vector_math.dot_vector(N, Ldir)
   return LdotN


#finds the reflection vector (intermediate step)
def find_reflection_vector(sphere, intersect_pt, Light):
   N = find_N(sphere, intersect_pt)
   Ldir = find_Ldir(sphere, intersect_pt, Light)
   LdotN = find_LdotN(sphere, intersect_pt, Light)
   scaled_N = vector_math.scale_vector(N, (2 * LdotN))
   reflection_vector = vector_math.difference_vector(Ldir, scaled_N)
   return reflection_vector


#finds normal vector from eye point to the light
def find_Vdir(sphere, intersect_pt, Point):
   px = find_px(sphere, intersect_pt)
   eye_point = Point
   long_vector = vector_math.vector_from_to(eye_point, px)
   Vdir = vector_math.normalize_vector(long_vector)
   return Vdir








