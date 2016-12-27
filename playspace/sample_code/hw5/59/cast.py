from collisions import *
from data import *
from vector_math import *


def scale_color(color, scale):
   r = color.r * scale
   g = color.g * scale
   b = color.b * scale
   return Color(r, g, b)


def mult_color(color1, color2):
   r = color1.r * color2.r
   g = color1.g * color2.g
   b = color1.b * color2.b
   return Color(r, g, b)

  
def add_color(color1, color2):
   r = color1.r + color2.r
   g = color1.g + color2.g
   b = color1.b + color2.b
   return Color(r, g, b)


def external_color(color):
   r = int(color.r * 255)
   g = int(color.g * 255)
   b = int(color.b * 255)

   if r > 255:
      r = 255
   if b > 255:
      b = 255
   if g > 255:
      g = 255

   return Color(r, g, b)


def p_e(normal, intersection_pt):
   adjust_by = scale_vector(normal, 0.01)
   return translate_point(intersection_pt, adjust_by)


def l_dir(normal, intersection_pt, light):
   adjust = p_e(normal, intersection_pt)
   return normalize_vector(difference_point(light.pt, adjust))


def is_visible(normal, l_dir):
   if dot_vector(normal, l_dir) > 0:
      return True
   return False


def not_obscured(l_dir, p_e, sphere_list, light):
   light_ray = Ray(p_e, l_dir)
   intersections = find_intersection_points(sphere_list, light_ray)

   if intersections == []:
      return True

   dist = length_vector(difference_point(p_e, light.pt))
   find_closest = intersections[closest(p_e, light.pt, intersections)][1]
   closest_dist = length_vector(difference_point(p_e, find_closest))

   if closest_dist < dist:
      return False
   return True
   

def closest(compare_to, initial, list):
   closest_index = 0
   dist = length_vector(difference_point(compare_to, initial))

   for i in range(len(list)):
      current_dist = length_vector(difference_point(compare_to, list[i][1]))

      if current_dist < dist:
         closest_index = i
         dist = current_dist

   return closest_index


def diffuse(normal, l_dir, p_e, closest_sphere, sphere_list, light):
   total = Color(0.0, 0.0, 0.0)

   if is_visible(normal, l_dir) and not_obscured(l_dir, p_e, sphere_list, 
      light):

      total = dot_vector(normal, l_dir) * closest_sphere.finish.diffuse
      total = scale_color(mult_color(light.color, closest_sphere.color),
         total)

   return total


def spec_intensity(normal, l_dir, p_e, eye_pos):
   l_dot_n = dot_vector(normal, l_dir)
   reflection = difference_vector(l_dir, scale_vector(normal, (2 * l_dot_n)))
   v_dir = normalize_vector(vector_from_to(eye_pos, p_e))

   return dot_vector(reflection, v_dir)


def specular(s_i, l_dir, p_e, sphere_list, closest_sphere, light):
   specular_intensity = s_i ** (1 / closest_sphere.finish.roughness)
   total = Color(0.0, 0.0, 0.0)

   if s_i > 0 and not_obscured(l_dir, p_e, sphere_list, light):
      total = scale_color(light.color, closest_sphere.finish.specular)
      total = scale_color(total, specular_intensity)
  
   return total


def cast_ray(ray, sphere_list, color, light, point):
   intersections = find_intersection_points(sphere_list, ray)
  
   if intersections == []:
      return Color(1.0, 1.0, 1.0)

   loc = intersections[closest(ray.pt, intersections[0][1], intersections)]
   cast = loc[0]
   cast_intersection = loc[1]

   n = sphere_normal_at_point(cast, cast_intersection)
   l = l_dir(n, cast_intersection, light)
   p = p_e(n, cast_intersection)
   si = spec_intensity(n, l, p, point)

   d = diffuse(n, l, p, cast, sphere_list, light)
   s = specular(si, l, p, sphere_list, cast, light)

   cast_color = scale_color(cast.color, cast.finish.ambient)
   cast_color = mult_color(cast_color, color)
   cast_color = add_color(cast_color, d)
   cast_color = add_color(cast_color, s)

   return cast_color


def cast_all_rays(min_x, max_x, min_y, max_y, width, height,
   eye_point, sphere_list, color, light, point, image):

   print >> image, 'P3'
   print >> image, width, height
   print >> image, 255

   x = min_x
   y = max_y
   dx = (max_x - min_x) / float(width)
   dy = (max_y - min_y) / float(height)

   for i in range(height):
      for j in range(width):
         cast = Ray(eye_point, vector_from_to(eye_point, Point(x, y, 0.0)))
         cast_color = external_color(cast_ray(cast, sphere_list, color,
            light, point))
         print >> image, cast_color.r, cast_color.g, cast_color.b
         x += dx
      y -= dy
      x = min_x
