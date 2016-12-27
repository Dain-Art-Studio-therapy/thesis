import sys
from cast import *
from data import *
from commandline import *

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def main(argv):
  try:
      with open(argv[1], 'rb') as f:
         spherelist = make_sphere_list(f)
         eye = eye_flag(argv)
         view = view_flag(argv)
         light = light_flag(argv)
         ambient = ambient_flag(argv)
         cast_all_rays(view[0], view[1], view[2], view[3], view[4], view[5],
                       eye, spherelist, ambient, light)
  except:
      print 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b] '

def make_sphere_list(f):
   sphere_list = []
   index = 0
   for n in f:
      sphere = n.split()
      index += 1
      try:
         center = Point(float(sphere[0]), float(sphere[1]),
                        float(sphere[2]))
         radius = float(sphere[3])
         color = Color(float(sphere[4]), float(sphere[5]),
                       float(sphere[6]))
         finish = Finish(float(sphere[7]), float(sphere[8]), 
                         float(sphere[9]), float(sphere[10]))
         sphere_list.append(Sphere(center, radius, color, finish))
      except:
         print 'malformed sphere on line {0} ...skipping'.format(index)
   return sphere_list

if __name__=='__main__':
   main(sys.argv)
