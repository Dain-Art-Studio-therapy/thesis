from collisions import *
from data import *

def cast_ray(ray, sphere_list, color, Light, point):
   new_list = find_intersection_points(sphere_list, ray)
   if  new_list == []:
      return Color(1, 1, 1)
   else:
      index = nearest_point(new_list, ray.pt)
      sphere = new_list[index][0]
      collision_point = new_list[index][1]
      N = sphere_normal_at_point(sphere, collision_point)
      P = translate_point(collision_point, scale_vector(N, 0.01)) 
      vector = vector_from_to(P, Light.pt)
      ray = Ray(P, vector)
      L = normalize_vector(vector)
      D_P = light_visible(N, L, sphere_list, ray)
      diffuse = color_diffuse(D_P, Light, sphere)
      refl_vector = difference_vector(L, scale_vector(N, (2 * D_P)))
      vdir = normalize_vector(vector_from_to(point, P))
      s_c = dot_vector(refl_vector, vdir)
      part_4_color = color_add(diffuse,finish_color(sphere.color,sphere.finish.ambient))
      part_5_color = final_color(s_c, Light, sphere)
      return color_add(part_5_color, part_4_color)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, Color, Light):
   distance = max_x - min_x
   delta_x = distance/float(width)
   delta_y = (max_y - min_y)/float(height)
   y_start = max_y
   print 'P3'
   print '1024 768'
   print '255'
   for y in range(height):
      x_start = min_x
      for x in range(width):
         point = Point(x_start, y_start, 0)
         ray = Ray(eye_point, vector_from_to(eye_point, point))
         sphere_color = cap_color(scale_color(cast_ray(ray, sphere_list, Color, Light, eye_point)))
         print '%s %s %s' % (sphere_color.r, sphere_color.g, sphere_color.b)
         x_start += delta_x
      y_start -= delta_y               
    
def nearest_point(List, point):
   index = 0
   for s in range(len(List)):
      if length_vector(difference_point(List[s][1], point)) < length_vector(difference_point(List[index][1], point)):
         index = s
   return index

def scale_color(color):
   return Color(color.r * 255, color.g * 255, color.b * 255)

def finish_color(color, finish):
   return Color(color.r * float(finish), color.g * float(finish), color.b * float(finish))

def light_visible(N, L, sphere_list, ray):
   pos = dot_vector(N, L)
   if pos < 0:
      return 0
   elif find_intersection_points(sphere_list, ray) == []:
      return pos
   else:
      return 0

def color_diffuse(d_p, light, sphere):
   return Color(d_p * light.color.r * sphere.color.r * sphere.finish.diffuse, d_p * light.color.g * sphere.color.g * sphere.finish.diffuse, d_p * light.color.b * sphere.color.b * sphere.finish.diffuse)

def color_add(c1, c2):
   return Color(c1.r + c2.r, c1.g + c2.g, c1.b + c2.b)

def final_color(s_c, light, sphere):
   return Color((light.color.r * sphere.finish.specular * (s_c**(1/sphere.finish.roughness))), (light.color.g * sphere.finish.specular * (s_c**(1/sphere.finish.roughness))), (light.color.b * sphere.finish.specular *(s_c**(1/sphere.finish.roughness))))

def cap_color(color):
   if color.r > 255:
      color.r = 255
   if color.g > 255:
      color.g = 255
   if color.b > 255:
      color.b = 255
   return color
