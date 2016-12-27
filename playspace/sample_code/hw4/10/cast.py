from utility import *
from collisions import *
from vector_math import *
from data import *
import math

def cast_ray(ray, sphere_list, color):
   spheres = find_intersection_points(sphere_list, ray)
   if spheres == []:
      return Color(1.0, 1.0, 1.0)
   else:
      initz = ray.pt.z
      nearestz = 0
      closest_delta = abs(initz)
      nearest_sphere = 0
      for i in range(0, len(spheres)):
         near = spheres[i]
         sphere = near[0]
         delta = abs(initz - sphere.center.z)
         if delta <= closest_delta :
            closest_delta = delta
            nearest_sphere = sphere
            
      return computeFinish(nearest_sphere.color, nearest_sphere.finish, color)

def computeFinish(color, finish, light):
   return Color(color.r * finish.ambient * light.r, color.g * finish.ambient * light.g, color.b * finish.ambient * light.b)
   
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, 
                                                             sphere_list, color):
   print 'P3'
   print width, height
   print '255'
   rayendstepX = float (max_x - min_x) / width
   rayendstepY = float (max_y - min_y) / height
   for i in range((height/2), ((height/2)*-1), -1):
      for j in range(((width/2)*-1), (width/2)):
         pt = Point(j * rayendstepX, i * rayendstepY, 0)
         dir = vector_from_to(eye_point, pt)
         ray = Ray(eye_point, dir)
         intersecting_color = cast_ray(ray, sphere_list, color)
         printColor2rgb(intersecting_color)

def printColor2rgb(color):
   print int (color.r * 255), int (color.g * 255), int (color.b * 255),
