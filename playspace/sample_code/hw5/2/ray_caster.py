import sys
from cast import *
from commandline import *
from data import *

def main(argv):
   if len(argv) < 2:
      print 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
   else:
      eye_point = Point(0.0, 0.0, -14.0)
      min_x = -10
      max_x = 10
      min_y = -10
      max_y = 7.5
      width = 1024
      height = 768
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      ambient = Color(1.0, 1.0, 1.0)
      with open_file(argv[1], 'rb') as f:
         spheres = process_file(f)

      eye_index = index_of_eye(argv)
      view_index = index_of_view(argv)
      light_index = index_of_light(argv)
      amb_index = index_of_ambient(argv) 

      for flag in argv:
         if flag == '-eye':
            eye_point = Point(float(argv[eye_index+1]),
            float(argv[eye_index+2]), float(argv[eye_index+3]))
         elif flag == '-view':
            min_x = float(argv[view_index+1])
            max_x = float(argv[view_index+2])
            min_y = float(argv[view_index+3])
            max_y = float(argv[view_index+4])
            height = float(argv[view_index+5])
            width = float(argv[view_index+6])
         elif flag == '-light':
            light = Light(Point(float(argv[light_index+1]),
            float(argv[light_index+2]), float(argv[light_index+3])),
            Color(float(argv[light_index+4]), float(argv[light_index+5]),
            float(argv[light_index+6])))
         elif flag == '-ambient':
            ambient = Color(float(argv[amb_index+1]),
            float(argv[amb_index+2]), float(argv[amb_index+3]))

   cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point,
   spheres, ambient, light)

if __name__ == '__main__':
   main(sys.argv)
