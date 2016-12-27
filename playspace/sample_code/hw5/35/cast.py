from collisions import *
from vector_math import *

DEFAULT_COLOR = Color(1, 1, 1)
NO_COLOR = Color(0, 0, 0)
MAX_OUTPUT_COLOR = 255

def cast_ray(ray, sphere_list, ambient, light):
   point_tuple = find_closest_sphere(sphere_list, ray)
   if point_tuple:
      sphere = point_tuple[0]
      point = point_tuple[1]
      reflected = get_reflected_color(sphere.color, ambient, sphere.finish.ambient)
      diffuse = get_color_diffusion_and_intensity(sphere, point, light, sphere_list, ray.pt)
      return add_colors(reflected, diffuse)

   return DEFAULT_COLOR


def cast_all_rays(view, eye_point, sphere_list, ambient, light):
   # min_x, max_x, min_y, max_y, width, height
   current_x = view.min_x
   current_y = view.max_y
   xstep = (view.max_x - view.min_x) / float(view.width)
   ystep = (view.min_y - view.max_y) / float(view.height)
   pixels = []
   while current_y > view.min_y:
      while current_x < view.max_x:
         ray = Ray(eye_point, vector_from_to(eye_point, Point(current_x, current_y, 0)))
         color = cast_ray(ray, sphere_list, ambient, light)
         pixels.append(get_color_string(color))
         current_x += xstep
      current_y += ystep
      current_x = view.min_x
      if current_y % 10 == 0:
         print "PART DONE!"
   print_p3(view.width, view.height, pixels)


def print_p3(width, height, pixels):
   with open('image.ppm', 'w') as f:
      f.write('P3\n' + str(width) + ' ' + str(height) + '\n255\n')
      f.write(''.join(pixels))


def get_color_string(color):
   r = int(color.r * MAX_OUTPUT_COLOR) if color.r < 1 else MAX_OUTPUT_COLOR
   g = int(color.g * MAX_OUTPUT_COLOR) if color.g < 1 else MAX_OUTPUT_COLOR
   b = int(color.b * MAX_OUTPUT_COLOR) if color.b < 1 else MAX_OUTPUT_COLOR
   return '%s %s %s ' % (r, g, b)


def get_reflected_color(color, ambient, percent):
   r = color.r * ambient.r * percent
   g = color.g * ambient.g * percent
   b = color.b * ambient.b * percent
   return Color(r, g, b)


def get_color_diffusion_and_intensity(sphere, point, light, sphere_list, eye_point):
   normal_point = sphere_normal_at_point(sphere, point)
   pe = translate_point(point, scale_vector(normal_point, 0.01))
   ldir = normalize_vector(vector_from_to(pe, light.pt))
   ldotn = dot_vector(normal_point, ldir)

   if ldotn <= 0:
      return NO_COLOR

   if find_closest_sphere(sphere_list, Ray(pe, ldir)):
      return NO_COLOR

   part = sphere.finish.diffuse * ldotn
   r = part * light.color.r * sphere.color.r
   g = part * light.color.g * sphere.color.g
   b = part * light.color.b * sphere.color.b
   reflection = difference_vector(scale_vector(normal_point, ldotn * 2), ldir)
   vdir = normalize_vector(difference_point(eye_point, pe))
   intensity = dot_vector(reflection, vdir)
   if intensity > 0:
      part = sphere.finish.specular * intensity ** (1 / sphere.finish.roughness)
      r += part * light.color.r
      g += part * light.color.g
      b += part * light.color.b
   return Color(r, g, b)


def add_colors(color1, color2):
   return Color(color1.r + color2.r, color1.g + color2.g, color1.b + color2.b)
