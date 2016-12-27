from sys import *
from groups import *
from math import *

def main(argv):
   try:
      f = open(argv[1],'r')
      out = open('faded.ppm','w')
   except:
      print 'Error: Cannot Read File'
      exit()


   d = write_p3(f,out)
   list = group_pixels(f)
   fade_pixels(f,list,d,out)


def write_p3(f,out):
   for i in range(3):
      header = f.readline()
      if(i == 1):
         d = header
         dimen = d.split()
      print header
      print >> out, header
   return dimen

def group_pixels(f):
   a = f.read()
   b = a.split()
   groups = groups_of_3(b)
   return groups

def fade_pixels(f,list,dimensions,out):
   width = int(dimensions[0])
   height = int(dimensions[1])
   radius = float(argv[4])
   row = int(argv[2])
   col = int(argv[3])
   for j in range(height):
      for i in range(width):
         dist = pythag(row-j,col-i)
         scalar = (radius-dist)/radius
         if(scalar < .2): 
            scalar = .2
         pixel = list[i+width*j]
         r = int(pixel[0])*scalar
         g = int(pixel[1])*scalar
         b = int(pixel[2])*scalar
         #print [r,g,b]
         print >> out, r,g,b

def pythag(a,b):
   return sqrt(a**2 + b**2)


if __name__ == '__main__':
   main(argv)
