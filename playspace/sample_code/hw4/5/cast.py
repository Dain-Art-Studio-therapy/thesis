import math
from vector_math import *
from collisions import *
import data

def distance_difference(origin, intersection):
   return math.sqrt((intersection.x-origin.x)**2\
    + (intersection.y-origin.y)**2 + (intersection.z-origin.z)**2)

def compare_distances_sphere(input_list, ray):
   closest = 0
   for i in range(1,len(input_list)):
      nearest = distance_difference(ray.pt, input_list[closest][1])
      current = distance_difference(ray.pt, input_list[i][1])
      if current < nearest:
         closest = i
   return input_list[closest]

def normal_sphere_vector(sphere_intersect):
   if sphere_intersect != []:
      create_vector = vector_from_to(sphere_intersect[0].center,sphere_intersect[1])
      normalized_vector = normalize_vector(create_vector)
      return normalized_vector

def point_light(normalized_vector, sphere_intersect):
   if normalized_vector is not None:
      scaled_normal_v = scale_vector(normalized_vector,0.01)
      pt_e = translate_point(sphere_intersect[1],scaled_normal_v)
      return pt_e 

def light_direction_vector(pt_e, light):
   if pt_e is not None:
      light_dir = normalize_vector(vector_from_to(pt_e, light.pt))
      return light_dir

def check_light_path(sphere_intersect, sphere_list, normalized_vector, pt_e, light_dir):
   #normalized_vector = normalize_vector(vector_from_to(\
   #sphere_intersect[0].center,sphere_intersect[1]))
   #scaled_normal_v = scale_vector(normalized_vector, 0.01)  
   #pt_e = translate_point(sphere_intersect[1], scaled_normal_v)
   #light_dir = normalize_vector(vector_from_to(pt_e, light.pt))
   visible_check = dot_vector(light_dir,normalized_vector)
   if visible_check <= 0:
      diffuse = 0.0
      return diffuse
   else:
      test_ray = data.Ray(pt_e,light_dir)
      for sphere in sphere_list:
         collision_test = find_intersection_points(sphere_list, test_ray)
         if collision_test != []:
            return 0.0
      return sphere_intersect[0].finish.diffuse * visible_check

def check_specular_intensity(sphere_intersect, point, normalized_vector, pt_e, light_dir):
   #normalized_vector = normalize_vector(vector_from_to(\
   #sphere_intersect[0].center,sphere_intersect[1]))
   #scaled_normal_v = scale_vector(normalized_vector, 0.01)
   #pt_e = translate_point(sphere_intersect[1], scaled_normal_v)
   #light_dir = normalize_vector(vector_from_to(pt_e, light.pt))
   light_dot_norm = dot_vector(light_dir, normalized_vector)
   reflection_vector = difference_vector(light_dir,scale_vector(normalized_vector,(2 * light_dot_norm)))
   view_dir = normalize_vector(vector_from_to(point, pt_e))
   spec_intensity = dot_vector(reflection_vector, view_dir)
   if spec_intensity <= 0:
      specular = 0.0
      return specular
   else:
      specular = sphere_intersect[0].finish.specular * \
      (spec_intensity ** (1/sphere_intersect[0].finish.roughness))
      return specular
  
def color_convert(sphere, color, light, sphere_list, point, normalized_vector, pt_e, light_dir): 
   if sphere != []:
      diffuse = check_light_path(sphere, sphere_list, normalized_vector, pt_e, light_dir)
      specular = check_specular_intensity(sphere, point, normalized_vector, pt_e, light_dir)
      red = int(((sphere[0].color.r * sphere[0].finish.ambient\
      * color.r) + (diffuse * sphere[0].color.r * light.color.r) + (specular * light.color.r)) * 255)
      green = int(((sphere[0].color.g * sphere[0].finish.ambient\
      * color.g) + (diffuse * sphere[0].color.g * light.color.g) + (specular * light.color.g)) * 255)
      blue = int(((sphere[0].color.b * sphere[0].finish.ambient\
      * color.b) + (diffuse * sphere[0].color.b * light.color.b) + (specular * light.color.b)) * 255)
      return (red, green, blue)

def cast_ray(ray, sphere_list, color, light, point):
   intersect_test = find_intersection_points(sphere_list,ray)
   if intersect_test != []:
      closest_sphere = compare_distances_sphere(intersect_test, ray)
      normalized_vector = normal_sphere_vector(closest_sphere)
      pt_e = point_light(normalized_vector, closest_sphere)
      light_dir = light_direction_vector(pt_e, light)
      return color_convert(closest_sphere, color, light, sphere_list, point, normalized_vector, pt_e, light_dir)
   else:
      color = data.Color(1.0, 1.0, 1.0)
      red = int(color.r * 255)
      green = int(color.g * 255)
      blue = int(color.b * 255)
      return (red, green, blue)

def iteration_floats(start,end,increment):
   result = []
   if start < end:
      while start < end:
         result.append(start)
         start += increment
      return result
   elif start > end:
      while start > end:
         result.append(start)
         start += increment
      return result

def cast_all_rays(min_x, max_x, min_y, max_y, width, height,\
   eye_point, sphere_list, color, light):
   width_increment = (max_x - min_x) / float(width)
   height_increment = (min_y - max_y) / float(height)
   print "P3"
   print width, height
   print 255
   for height_point in iteration_floats(max_y,min_y,height_increment):
      for width_point in iteration_floats(min_x,max_x,width_increment):
         pixel = data.Point(width_point,height_point,0.0)
         create_ray = data.Ray(eye_point,\
         vector_math.difference_point(pixel,eye_point))
         colors = cast_ray(create_ray, sphere_list, color, light, eye_point)
         print colors[0], colors[1], colors[2]
