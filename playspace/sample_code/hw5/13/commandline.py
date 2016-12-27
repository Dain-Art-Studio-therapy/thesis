from convert import float_default
from data import *
import sys

def find_flag(argv):
   for i in range(len(argv)):
      if argv[i] == 'cat':
         print 'yes'
     

def find_next_flag(argv, flag):
   for i in range(len(argv)):
      if argv[i] is not flag and argv[i] in [-eye, -view, -light, -ambient]:
         return i
         
def set_eye(argv):
   x, y, z = 0, 0, -14
   eye_point = Point(x, y, z)
   for i in range(len(argv)):
      if argv[i] == '-eye':
         x = float_default(argv[(i + 1)], 0)
         y = float_default(argv[(i + 2)], 0)
         z = float_default(argv[(i + 3)], -14)
   return eye_point

def set_view(argv):
   min_x, max_x, min_y, max_y = -10, 10, -7.5, 7.5
   width, height = 1024, 768
   for i in range(len(argv)):
      if argv[i] == '-view':
         min_x = float_default(argv[i + 1], -10)
         max_x = float_default(argv[i + 2], 10)
         min_y = float_default(argv[i + 3], -7.5)
         max_y = float_default(argv[i + 4], 7.5)
         width = int(float_default(argv[i + 5], 1024))
         height = int(float_default(argv[i + 6], 768))
   return min_x, max_x, min_y, max_y, width, height

def set_light(argv):
   x, y, z, r, g, b = -100, 100, -100, 1.5, 1.5, 1.5
   light = Light(Point(x, y, z), Color(r, g, b))
   for i in range(len(argv)):
      if argv[i] == '-light':
         x = float_default(argv[i + 1], 100)
         y = float_default(argv[i + 2], 100)
         z = float_default(argv[i + 3], 100)
         r = float_default(argv[i + 4], 1.5)
         g = float_default(argv[i + 5], 1.5)
         b = float_default(argv[i + 6], 1.5)
   return light

def set_ambient(argv):
   r, g, b = 1.0, 1.0, 1.0
   color = Color(r, g, b)
   for i in range(len(argv)):
      if argv[i] == '-ambient':
         r = float_default(argv[i + 1], 1.0)
         g = float_default(argv[i + 2], 1.0)
         b = float_default(argv[i + 3], 1.0)
   return color

