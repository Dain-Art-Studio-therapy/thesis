import sys
from sys import *

def sphere_read():
   try:
      f = open(sys.argv[4], 'r')
   except:
      if (len(sys.argv) == 0):
         print ('could not open file')
         exit()
      
   for i in f:
      values = i.split()
      if len(values) == 11:
         try:
            print usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]
         except:
         print('malformed sphere...skipping')
            