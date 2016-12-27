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
   file = open('image.ppm', 'w')
   print_header(width, height, file)
   for y in range(height):
      for x in range(width):
         valx = min_x + (x * dx)
         valy = max_y - (y * dy)
         pixpt = data.Point(valx, valy, 0)
         edir = vector_from_to(eye_point, pixpt)
         eray = data.Ray(eye_point, edir)
         
         pcolor = cast_ray(eray, sphere_list, color, light, eye_point)
         r = check_max(int(pcolor.r * 255))
         g = check_max(int(pcolor.g * 255))
         b = check_max(int(pcolor.b * 255))
         
         
         print >> file, r, g, b
   file.close()

def print_header(width, height, file):
   print >> file, 'P3'
   print >> file, width, height
   print >> file, 255

def check_max(color_comp):
   if color_comp > 255:
      return 255
   return color_comp

def true_color(list, eye_point, color, light, sphere_list, point):
   mindex = 0
   for i in range(1, len(list)):
      n = dist_from_eye(list[mindex][1], eye_point)
      m = dist_from_eye(list[i][1], eye_point)
      if m < n:
         mindex = i
   
   first = list[mindex][0].color
   finish = list[mindex][0].finish
   color_with_finish = default_color(first, finish, color)

   M = scale_vector(sphere_normal_at_point(list[mindex][0], list[mindex][1])\
       , 0.01)
   pe = translate_point(list[mindex][1], M)
   N = scale_vector(M, 100)
   ldir = normalize_vector(vector_from_to(pe, light.pt))

   dot = dot_vector(N, ldir)
   if dot > 0: #light is visible
      lray = data.Ray(pe, ldir)
      if is_closer_sphere(sphere_list, lray, light):
         rvec = difference_vector(ldir, scale_vector(N, 2 * dot))
         vdir = normalize_vector(vector_from_to(point, pe))
         spec = dot_vector(rvec, vdir)

         if spec > 0: #specular intensity contributes
            return spec_color(color_with_finish, first, dot, finish, light, spec)

         else: #specular intensity does not contribute
            return diff_color(color_with_finish, first, dot, finish, light)

   return color_with_finish

def dist_from_eye(spherept, eye):
   return math.sqrt(((eye.x - spherept.x) ** 2) + ((eye.y - spherept.y) ** 2) \
          + ((eye.z - spherept.z) ** 2))

def default_color(color, finish, amb_light):
   return data.Color((color.r * finish.ambient * amb_light.r), (color.g * \
          finish.ambient * amb_light.g), (color.b * finish.ambient * \
          amb_light.b))

def diff_color(defcolor, first, dot, finish, light):
   r = defcolor.r + (first.r * finish.diffuse * dot * light.color.r)
   g = defcolor.g + (first.g * finish.diffuse * dot * light.color.g)
   b = defcolor.b + (first.b * finish.diffuse * dot * light.color.b)
   return data.Color(r, g, b)

def spec_color(defcolor, first, dot, finish, light, spec):
   s = finish.specular * (spec ** (1 / finish.roughness))
   d_color = diff_color(defcolor, first, dot, finish, light)
   return data.Color((d_color.r + (s * light.color.r)), (d_color.g + (s * \
          light.color.g)), (d_color.b + (s * light.color.b)))

def is_closer_sphere(sphere_list, lray, light):
   S = find_intersection_points(sphere_list, lray)
   if S == []:
      return True
   else:
      mindex = 0
      for i in range(1, len(S)):
         n = dist_from_light(S[mindex][1], light.pt)
         m = dist_from_light(S[i][1], light.pt)
         if m < n:
            mindex = i
      j = dist_from_light(lray.pt, light.pt)
      if j >= dist_from_light(S[mindex][1], light.pt):
         return False
      else:
         return True

def dist_from_light(s_pt, l_pt):
   return math.sqrt(((s_pt.x - l_pt.x) ** 2) + ((s_pt.y - l_pt.y) ** 2) + \
          ((s_pt.z - l_pt.z) ** 2))
