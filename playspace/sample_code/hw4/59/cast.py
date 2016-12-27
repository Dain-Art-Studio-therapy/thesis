import data
from vector_math import *
from collisions import *
from utility import *

def cast_ray(ray, sphere_list, color, light, point):
   N = find_intersection_points(sphere_list, ray)
   if N != []:
      return true_color(N, ray.pt, color, light, sphere_list, point)
   else:
      return data.Color(1.0, 1.0, 1.0)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, 
sphere_list, color, light):
   dx = (max_x - min_x) / float(width)
   dy = (max_y - min_y) / float(height)
   print_header(width, height)
   for y in range(height):
      for x in range(width):
         valx = min_x + (x * dx)
         valy = max_y - (y * dy)
         pixpt = data.Point(valx, valy, 0)
         edir = vector_from_to(eye_point, pixpt)
         eray = data.Ray(eye_point, edir)
         
         pcolor = cast_ray(eray, sphere_list, color, light, eye_point)
         r = int(pcolor.r * 255)
         if r > 255:
            r = 255

         g = int(pcolor.g * 255)
         if g > 255:
            g = 255

         b = int(pcolor.b * 255)
         if b > 255:
            b = 255
         print r, g, b

def print_header(width, height):
   print 'P3'
   print width, height
   print 255

def true_color(list, eye_point, color, light, sphere_list, point):
   mindex = 0
   for i in range(1, len(list)):
      n = dist_from_eye(list[mindex][1], eye_point)
      m = dist_from_eye(list[i][1], eye_point)
      if m < n:
         mindex = i

   r1 = list[mindex][0].color.r * list[mindex][0].finish.ambient * color
   g1 = list[mindex][0].color.g * list[mindex][0].finish.ambient * color
   b1 = list[mindex][0].color.b * list[mindex][0].finish.ambient * color
   color_with_finish = data.Color(r1, g1, b1)

   M = scale_vector(sphere_normal_at_point(list[mindex][0], list[mindex][1])\
   , 0.01)
   pe = translate_point(list[mindex][1], M)
   N = scale_vector(M, 100)
   ldir = normalize_vector(vector_from_to(pe, light.pt))

   dot = dot_vector(N, ldir)
   if dot > 0: #light is visible
      lray = data.Ray(pe, ldir)
      if is_closer_sphere(sphere_list, lray) == True:
         dr = dot * light.color.r * list[mindex][0].color.r * \
         list[mindex][0].finish.diffuse
         dg = dot * light.color.g * list[mindex][0].color.g * \
         list[mindex][0].finish.diffuse
         db = dot * light.color.b * list[mindex][0].color.b * \
         list[mindex][0].finish.diffuse

         rvec = difference_vector(ldir, scale_vector(N, 2 * dot))
         vdir = normalize_vector(vector_from_to(point, pe))
         spec = dot_vector(rvec, vdir)
         
         if spec > 0: #specular intensity contributes
            sr = light.color.r * list[mindex][0].finish.specular * \
            (spec ** (1 / float(list[mindex][0].finish.roughness)))
            sg = light.color.g * list[mindex][0].finish.specular * \
            (spec ** (1 / float(list[mindex][0].finish.roughness)))
            sb = light.color.b * list[mindex][0].finish.specular * \
            (spec ** (1 / float(list[mindex][0].finish.roughness)))

            return data.Color((r1 + dr + sr), (g1 + dg + sg), (b1 + db + sb))

         else: #specular intensity does not contribute
            return data.Color((r1 + dr), (g1 + dg), (b1 + db))

      else: #another sphere in way
         return color_with_finish

   else: #light is behind
      return color_with_finish

def dist_from_eye(spherept, eye):
   return math.sqrt(((eye.x - spherept.x) ** 2) + ((eye.y - spherept.y) ** 2) \
   + ((eye.z - spherept.z) ** 2))

def is_closer_sphere(sphere_list, lightray):
   S = find_intersection_points(sphere_list, lightray)
   if S == []:
      return True
   else:
      return False
