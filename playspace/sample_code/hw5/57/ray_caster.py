import sys
from data import *
from cast import *
from commandline import *

def open_file(name,mode):
   try:
      return open(name,mode)
   except:
      print >> sys.stderr, '{0}:{1}'.format(name,'File does not exist')

def main(argv):
   try:
      with open_file(argv[1],'rb') as f:
         spheres = []
         for line in f:
            s = line.split()
            if len(s) != 11:
               print >> sys.stderr, 'Wrong number of sphere values'            
            spheres.append(Sphere(Point(float(s[0]),float(s[1]),float(s[2])),float(s[3]),Color(float(s[4]),float(s[5]),float(s[6])),Finish(float(s[7]),float(s[8]),float(s[9]),float(s[10]))))
      eye = eye_argument(argv)
      v = view_argument(argv)
      l = light_argument(argv)
      a = ambient_argument(argv)
      cast_all_rays(v[0],v[1],v[2],v[3],v[4],v[5],eye,spheres,a,l)
   except:
      print >> sys.stderr, "usage: python ray_caster.py <filename> [-eye x y z] \
                       [-view min_x max_x min_y max_y width height] \
                       [-light x y z r g b] [-ambient r g b]"


if __name__ == '__main__':
   main(sys.argv)
