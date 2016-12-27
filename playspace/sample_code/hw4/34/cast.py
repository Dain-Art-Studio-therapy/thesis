from collisions import *
from data import *
from utility import *
from vector_math import *

def cast_ray(ray, sphere_list):
   return find_intersection_points(sphere_list, ray) != []

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
   dy = float(max_y - min_y)/float(height) 
   dx = float(max_x - min_x)/float(width)
   for h in range(height):
      y = max_y - h*dy
      for w in range(width):
         x = min_x + w*dx
         eye_ray = Ray(eye_point, difference_point(Point(x,y,0), eye_point))
   if cast_ray(eye_ray, sphere_list):
      print 0, 0, 0
   else:
      print 255, 255, 255







