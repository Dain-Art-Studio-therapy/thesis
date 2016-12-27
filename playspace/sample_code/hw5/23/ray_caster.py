import data
import collisions
import vector_math
import math
import sys
import cast
import commandline
# x y z radius r g b ambient diffuse specular roughness
# min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, Color, Light


def main(argv):
   try:
      with open(argv[1], 'rb') as f:
         sphere_list  = convert_file_to_spheres(f)
      eye_point = commandline.get_eye(argv)
      view = commandline.get_view(argv)
      ambient_light = commandline.get_ambient(argv)
      light = commandline.get_light(argv)
      cast.cast_all_rays(view[0], view[1], view[2], view[3], view[4], view[5], 
                         eye_point, sphere_list, ambient_light, light)         
   except:
      print >> sys.stderr, """usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]"""



def make_sphere(floats):
   center = data.Point(floats[0], floats[1], floats[2])
   radius = floats[3]
   color = data.Color(floats[4], floats[5], floats[6])
   finish = data.Finish(floats[7], floats[8], floats[9], floats[10])
   sphere = data.Sphere(center, radius, color, finish)
   return sphere

def convert_file_to_spheres(sphere_file):
   sphere_list = []
   counter = 0
   for line in sphere_file:
      values = line.split()
      counter += 1
      if len(values) == 11:
         float_values = []
         try:
            for e in values:
               float_values.append(float(e))
            new_sphere = make_sphere(float_values)
            sphere_list.append(new_sphere)
         except:
            print "malformed sphere on line {0}...skipping".format(counter)
      else:
         print "malformed sphere on line {0}...skipping".format(counter)
   return sphere_list


if __name__ == '__main__':
   main(sys.argv)
