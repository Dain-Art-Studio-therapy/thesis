from cast import *
from data import *
from commandline import *
import sys

eye_default = Point(0.0, 0.0, -14.0)
default_ambient = Color(1.0, 1.0, 1.0)
default_light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
default_view_tuple = (-10.0, 10.0, -7.5, 7.5, 1024, 768)

try:
   sphere_file = sys.argv[1]
   open(sphere_file, 'read')
except:
   if len(sys.argv) > 0:
      print 'file', sys.argv[1], 'cannot be open'
   else:
      print 'no sphere file given'
   sys.exit()


def save_picture(tuple_with_view, eye_point, sphere_list, amcolor, light):

   with open('image.ppm', 'w+')as image:
      image.write('P3''\n')
      image.write(str(default_view_tuple[4])+","+str(default_view_tuple[5])+'\n')
      image.write('255''\n')
      view_arguments = []
      for item in tuple_with_view:
         view_arguments.append(item)
      cast_all_rays(view_arguments[0], view_arguments[1], view_arguments[2], 
         view_arguments[3], int(view_arguments[4]), int(view_arguments[5]), 
         eye_point, sphere_list, amcolor, light, image)

def read_spheres(given_file):
   # x y z radius r g b ambient diffuse specular roughness
   with open(given_file, 'rw')as thefile:
      return_list = []
      line_number = 0
      for line in thefile:
         line_number += 1
         try:
            parts = line.split()
            return_list.append(Sphere(Point(float(parts[0]), float(parts[1]), 
               float(parts[2])), float(parts[3]), Color(float(parts[4]), 
               float(parts[5]), float(parts[6])), Finish(float(parts[7]), 
               float(parts[8]), float(parts[9]), float(parts[10]))))
         except:
            if len(parts) == 0:
               print 'line', line_number, 'blank ... skipping'
               pass
            elif len(parts) != 11:
               print "malformed sphere on line:", line_number,  '... skipping'
               pass
            else:
               print "something isnt working"
               sys.exit()
      return return_list


if __name__ == '__main__':
   stuff = command_line(eye_default, default_view_tuple, default_light, 
      default_ambient)
   save_picture(stuff[1], stuff[0], read_spheres(sphere_file), stuff[3], 
      stuff[2])






