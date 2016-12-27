from collisions import *
from data import *
from vector_math import *
import math

def getColor(sphere, pt, ambientColor, light, sphere_list, eye_point):
   N = sphere_normal_at_point(sphere, pt)
   P_E = translate_point(pt, scale_vector(N, 0.01))
   L_dir = normalize_vector(vector_from_to(P_E, light.pt))

   shadowColor = Color(sphere.color.r * sphere.finish.ambient * ambientColor.r, 
                       sphere.color.g * sphere.finish.ambient * ambientColor.g, 
                       sphere.color.b * sphere.finish.ambient * ambientColor.b)

   colorFromLight = Color(0, 0, 0)
   specularColor = Color(0, 0, 0)

   if dot_vector(N, L_dir) > 0:
      if not find_intersection_points(sphere_list, Ray(P_E, L_dir)):
         L_dot_N = dot_vector(N, L_dir)
         colorFromLight = Color(L_dot_N * light.color.r * sphere.color.r * sphere.finish.diffuse, 
                                L_dot_N * light.color.g * sphere.color.g * sphere.finish.diffuse, 
                                L_dot_N * light.color.b * sphere.color.b * sphere.finish.diffuse)

         reflection = difference_vector(L_dir, scale_vector(N, 2 * L_dot_N))
         V_dir = normalize_vector(vector_from_to(eye_point, P_E))
         specularIntensity = dot_vector(reflection, V_dir)
         if specularIntensity > 0:
            specularColor = Color(light.color.r * sphere.finish.specular * specularIntensity**(1.0/sphere.finish.roughness), 
                                  light.color.g * sphere.finish.specular * specularIntensity**(1.0/sphere.finish.roughness), 
                                  light.color.b * sphere.finish.specular * specularIntensity**(1.0/sphere.finish.roughness))

   return Color(shadowColor.r + colorFromLight.r + specularColor.r, 
                shadowColor.g + colorFromLight.g + specularColor.g, 
                shadowColor.b + colorFromLight.b + specularColor.b)

def cast_ray(ray, sphere_list, ambientColor, light, eye_point):
   color = Color(1.0, 1.0, 1.0)
   points = find_intersection_points(sphere_list, ray)
  
   if points:
      closest = length_vector(difference_point(points[0][1], ray.pt))
      color = getColor(points[0][0], points[0][1], ambientColor, 
                       light, sphere_list, eye_point)

      for point in points:
         length = length_vector(difference_point(point[1], ray.pt))
         if length < closest:
            closest = length
            
            color = getColor(point[0], point[1], ambientColor, light, 
                             sphere_list, eye_point)

   return color


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, 
                  sphere_list, ambientColor, light):
   print "P3" 
   print width, height 
   print 255

   dx = (max_x - min_x) / float(width)
   dy = (max_y - min_y) / float(height)

   for h in xrange(height):
      y = max_y - (h*dy)

      for w in xrange(width):
         x = min_x + (w*dx)

         ray = Ray(eye_point, vector_from_to(eye_point, Point(x, y, 0)))

         color = cast_ray(ray, sphere_list, ambientColor, light, eye_point)
         print int(color.r*255), int(color.g*255), int(color.b*255)
