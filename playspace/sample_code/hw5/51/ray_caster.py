from cast import *
from sys import *
from commandline import *
from collisions import *
from vector_math import *

def main():
   try:
      f = open(argv[1])
   except:
      print 'Error'
      exit()

   l = convert_spheres(f)

   change(l,argv)

if __name__ == '__main__':
   main()
