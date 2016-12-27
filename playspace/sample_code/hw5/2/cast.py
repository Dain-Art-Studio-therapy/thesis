from vector_math import *
from data import *
from collisions import *
from utility import *

def cast_ray(ray, sphere_list, finish, light, eye_point):
   if find_intersection_points(sphere_list, ray) != []:  
      list = find_intersection_points(sphere_list, ray)
      x = 0
      nearest = distance(ray.pt, list[0][1])
      for i in range(len(list)):
         if distance(ray.pt, list[i][1]) < nearest:
            nearest = distance(ray.pt, list[i][1])
            x = i
      color = mod_color(scale_color(list[x][0].color, list[x][0].finish.ambient),
      finish)
      pe = translate_point(list[x][1],
      scale_vector(sphere_normal_at_point(list[x][0], list[x][1]), .01))
      n = sphere_normal_at_point(list[x][0], list[x][1])
      l_dir = normalize_vector(vector_from_to(pe, light.pt))
      visible = dot_vector(n, l_dir)
      vis_ray = Ray(pe, l_dir)
      pairs = find_intersection_points(sphere_list, vis_ray)
      reflection = difference_vector(l_dir, scale_vector(n, 2*visible))
      v_dir = normalize_vector(vector_from_to(eye_point, pe))
      intensity = dot_vector(reflection, v_dir)
      if pairs != [] or visible < 0:
         diffuse = Color(0, 0, 0)
      elif visible > 0:
         diffuse = scale_color(mod_color(light.color, list[x][0].color),   
         visible*list[x][0].finish.diffuse)
      if intensity < 0:
         specular = Color(0, 0, 0)
      elif intensity > 0:
         specular = scale_color(light.color, 
         list[x][0].finish.specular*(intensity**(1/list[x][0].finish.roughness)))
      color = Color(color.r+diffuse.r+specular.r, color.g+diffuse.g+specular.g,
      color.b+diffuse.b+specular.b)
   else:
      color = Color(1.0, 1.0, 1.0)
   return color

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point,
sphere_list, finish, light):
   f = open('image.ppm', 'wb')

   f.write('P3\n')
   f.writelines((str(width), ' ', str(height), '\n'))
   f.write('255\n')
   
   dy = max_y
   for y in range(height):
      dx = min_x
      for x in range(width):
         ray = Ray(eye_point, vector_from_to(eye_point,
         Point(dx, dy, 0)))
         color = cast_ray(ray, sphere_list, finish, light, eye_point)
         f.writelines((str((int)(cap_value(color.r) * 255)), ' ', str((int)(cap_value(color.g)*255)), ' ',str((int)(cap_value(color.b)*255)), ' '))
         dx += (max_x - min_x) / float(width)
      dy += (min_y - max_y) / float(height)
