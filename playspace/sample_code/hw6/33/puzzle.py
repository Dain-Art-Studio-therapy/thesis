from sys import *
from groups import *


def main(argv):
   try:
      f = open(argv[1],'r')
      out = open('hidden.ppm','w')
   except:
      print 'Error: Cannot read file'
      exit()
   read_p3(f,out)
   group = group_pixels(f)
   convert_color(group,out)

def convert_color(list,out):
   for i in list:
      red = str(int(i[0])*10)
      if int(red) > 255:
         red = str(255)
      green = red
      blue = red
      print >> out,red,green,blue

def group_pixels(f):
   a = f.read()
   b = a.split()
   groups = groups_of_3(b)
   return groups


def read_p3(f,out):
   for i in range(3):
      head = f.readline()
      print head
      print >> out,head
   

if __name__ == '__main__':
   main(argv)
