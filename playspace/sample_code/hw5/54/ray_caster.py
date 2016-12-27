import sys
from cast import *
from commandline import *
from data import *

# Project Defaults are in commandline.py

def main(argv):
   sphere_list = []

   with open_file(argv[1], 'rb') as f:
      sphere_list = process_file(f)
   
   cast_args = process_flags(argv)   

   # cast_args = [eyePoint, ViewTuple(minX, maxX, minY, maxY, width, height), 
   #              light, ambient]
   with open_file('image.ppm', 'wb') as output:
      cast_all_rays(cast_args[1][0], cast_args[1][1], cast_args[1][2],
         cast_args[1][3], cast_args[1][4], cast_args[1][5], cast_args[0], 
         sphere_list, cast_args[3], cast_args[2], output)


def open_file(name, mode):
   try: 
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0}:{1}'.format(name, e.strerror)
      print 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x',
      print 'max_x min_y max_y width height] [-light x y z r g b] [-ambient r',
      print 'g b]'
      exit(1)



if __name__=='__main__':
   main(sys.argv)
