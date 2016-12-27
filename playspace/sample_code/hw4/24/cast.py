import data
import vector_math
import collisions
import utility
import math



#returns color or closest sphere intersected, or the color white
def cast_ray(ray, sphere_list, ambient_color, light, eye_point):
   reslist = collisions.find_intersection_points(sphere_list, ray)

   if reslist == []:
      return data.Color(1.0, 1.0, 1.0)

   closest_sphere_pair = find_closest_sphere(ray.pt, reslist)
   sphere_color = closest_sphere_pair[0].color
   
   l_dot_n = vector_math.dot_vector(
         collisions.sphere_normal_at_point(closest_sphere_pair[0],
            closest_sphere_pair[1]),
         vector_math.normalize_vector(vector_math.difference_point(light.pt,
            closest_sphere_pair[1])))

   specular_intensity = find_specular_intensity(closest_sphere_pair, light,
      eye_point, l_dot_n)
   
   ambient_component = find_ambient_component(closest_sphere_pair[0], ambient_color)
   light_on_point = light_hits_point(closest_sphere_pair, sphere_list, light)
   
   
   if specular_intensity > 0 and light_on_point:
      diffuse_component = find_diffuse_component(l_dot_n, light,
         closest_sphere_pair[0])
      specular_component = find_specular_component(light, closest_sphere_pair[0],
         specular_intensity)
      
      newr = specular_component.r + diffuse_component.r + ambient_component.r
      newg = specular_component.g + diffuse_component.g + ambient_component.g
      newb = specular_component.b + diffuse_component.b + ambient_component.b
      
      
      pixelcolor = data.Color(newr, newg, newb)
      pixelcolor = fix_specular_color(pixelcolor, ambient_component, diffuse_component)
      
      
   
   elif light_on_point:
      diffuse_component = find_diffuse_component(l_dot_n, light,
         closest_sphere_pair[0])
      
      newr = diffuse_component.r + ambient_component.r
      newg = diffuse_component.g + ambient_component.g
      newb = diffuse_component.b + ambient_component.b
   
      pixelcolor = data.Color(newr, newg, newb)
      pixelcolor = fix_color_issues(pixelcolor, ambient_component)  
      # if color is past max/min, sets it to the max/min
      
   else: # light doesn't hit ray
      newr = ambient_component.r
      newg = ambient_component.g
      newb = ambient_component.b
      
      pixelcolor = data.Color(newr, newg, newb)
      pixelcolor = fix_color_issues(pixelcolor, ambient_component)
   
   
   
   return pixelcolor


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient_color, light):
   y_interval = (max_y - min_y) / float(height)
   x_interval = (max_x - min_x) / float(width)
   
   
   print "P3"
   print "%d %d" % (width, height)
   print "255"
   
   
   for i in range(height):
      for j in range(width):
         y = max_y - (i * y_interval)
         x = min_x + (j * x_interval)
         viewpoint = data.Point(x, y, 0)
         ray_dir = vector_math.difference_point(viewpoint, eye_point)
         ray_to_cast = data.Ray(eye_point, ray_dir)
         spherecolor = cast_ray(ray_to_cast, sphere_list, ambient_color, light,
            eye_point)
         print "%d %d %d" % (spherecolor.r * 255,
                             spherecolor.g * 255,
                             spherecolor.b * 255)


# helper functions
# returns the sphere pair with the closest point to the given point
def find_closest_sphere(point, sphere_pair_list):
   if sphere_pair_list == []:
      return None
   closest = sphere_pair_list[0]
   distance = vector_math.distance(point, closest[1])
   for i in range(len(sphere_pair_list)):
      if vector_math.distance(point, sphere_pair_list[i][1]) < distance:
         closest = sphere_pair_list[i]
         distance = vector_math.distance(point, sphere_pair_list[i][1])
   return closest


# for computing light rays stuff
# finds point 0.01 off the sphere at the given point.
# used to prevent errors due to floating points
def find_point_near_sphere(sphere, point):
   normal_vector = collisions.sphere_normal_at_point(sphere, point)
   translate_vec = vector_math.scale_vector(normal_vector, 0.01)
   return vector_math.translate_point(point, translate_vec)


# returns true if the point is on the same side of the sphere
# as the light
def point_light_same_side(point, sphere, light):
   normal = collisions.sphere_normal_at_point(sphere, point)
   pt_light_vec = vector_math.normalize_vector(
      vector_math.difference_point(light.pt, point))
   dot_product = vector_math.dot_vector(normal, pt_light_vec)
   if dot_product <= 0:
      return False
   else:
      return True


# returns true if there are no objects between the point and light
# including the sphere that contains the point
def point_unobstructed(point, light, sphere_list):
   light_dir = vector_math.normalize_vector(vector_math.difference_point(
      light.pt, point))
   ray_to_light = data.Ray(point, light_dir)
   spheres_intersected = collisions.find_intersection_points(sphere_list,
      ray_to_light)
   if spheres_intersected == []:
      return True
   else:
      return False



def light_hits_point(spherepair, sphere_list, light):
   close_point = find_point_near_sphere(spherepair[0], spherepair[1])
   return (point_light_same_side(close_point, spherepair[0], light) and
           point_unobstructed(close_point, light, sphere_list))


def fix_color_issues(init_color, ambient_component):
   maxn = 1
   minr = min(ambient_component.r, 1)
   ming = min(ambient_component.g, 1)
   minb = min(ambient_component.b, 1)
         
   r = init_color.r
   g = init_color.g
   b = init_color.b
         
   if r > maxn:
      r = maxn
   elif r < minr:
      r = minr
   
   if g > maxn:
      g = maxn
   elif g < ming:
      g = ming
    
   if b > maxn:
      b = maxn
   elif b < minb:
      b = minb
      
   return data.Color(r, g, b)


def fix_specular_color(color, ambient_component, diffuse_component):
   r = color.r
   g = color.g
   b = color.b
   
   maxn = 1
   minr = min(ambient_component.r + diffuse_component.r, 1)
   ming = min(ambient_component.g + diffuse_component.g, 1)
   minb = min(ambient_component.b + diffuse_component.b, 1)
   
   if r > maxn:
      r = maxn
   elif r < minr:
      r = minr
      
   if g > maxn:
      g = maxn
   elif g < ming:
      g = ming
   
   if b > maxn:
      b = maxn
   elif b < minb:
      b = minb
      
   return data.Color(r, g, b)


def find_specular_intensity(spherepair, light, eye_point, l_dot_n):
   light_dir = vector_math.normalize_vector(vector_math.difference_point(
      light.pt, spherepair[1]))
      
   sphere_normal = collisions.sphere_normal_at_point(spherepair[0], spherepair[1])
   
   reflection_vector = vector_math.difference_vector(light_dir,
      vector_math.scale_vector(sphere_normal, 2 * l_dot_n))
      
   view_dir = vector_math.normalize_vector(vector_math.difference_point(
      spherepair[1], eye_point))
      
   specular_intensity = vector_math.dot_vector(view_dir, reflection_vector)
   return specular_intensity


def find_ambient_component(sphere, ambient_color):
   r = sphere.color.r * sphere.finish.ambient * ambient_color.r
   g = sphere.color.g * sphere.finish.ambient * ambient_color.g
   b = sphere.color.b * sphere.finish.ambient * ambient_color.b
   return data.Color(r, g, b)


def find_diffuse_component(l_dot_n, light, sphere):
   r = l_dot_n * light.color.r * sphere.color.r * sphere.finish.diffuse
   g = l_dot_n * light.color.g * sphere.color.g * sphere.finish.diffuse
   b = l_dot_n * light.color.b * sphere.color.b * sphere.finish.diffuse
   return data.Color(r, g, b)


def find_specular_component(light, sphere, specular_intensity):
   r = light.color.r * sphere.finish.specular * (specular_intensity ** (
      1.0 / sphere.finish.roughness))
   g = light.color.g * sphere.finish.specular * (specular_intensity ** (
      1.0 / sphere.finish.roughness))
   b = light.color.b * sphere.finish.specular * (specular_intensity ** (
      1.0 / sphere.finish.roughness))
   return data.Color(r, g, b)
