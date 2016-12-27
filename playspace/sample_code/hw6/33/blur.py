from sys import *
from groups import *

def main(argv):
   try:
      f = open(argv[1],'r')
      out = open('blurred.ppm','w')
   except:
      print 'Error: Cannot open file'
      exit()

   d = write_p3(f,out)
   list = group_pixels(f)
   if(len(argv)>2):
      reach = int(argv[2])
   else:
      reach = 4
   blur_pixels(list,d,reach,out)

def write_p3(f,out):
   for i in range(3):
      header = f.readline()
      if(i == 1):
         d = header
         dimen = d.split()
      print header
      print >> out,header
   return dimen

def group_pixels(f):
   a = f.read()
   b = a.split()
   groups = groups_of_3(b)
   return groups

def blur_pixels(list,dimensions,reach,out):
   width = int(dimensions[0])
   height = int(dimensions[1])
   grid = [[0 for x in range(width)] for x in range(height)]
   for j in range(height):
      for i in range(width):
         grid[j][i] = list[i + int(width)*j]

   for j in range(height):
      for i in range(width):
         rsum = 0.0
         gsum = 0.0
         bsum = 0.0
         counter = 0
         for y in range(-reach,reach+1):
            for x in range(-reach,reach+1):
               if( (0 < j+y < int(height)) and (0 < i+x < int(width)) ):
                  counter +=1
                  rsum += float(grid[j+y][i+x][0])
                  gsum += float(grid[j+y][i+x][1])
                  bsum += float(grid[j+y][i+x][2])
         r = rsum/(counter)
         g = gsum/(counter)
         b = bsum/(counter)
         print >> out,r,g,b


if __name__ == '__main__':
   main(argv)
