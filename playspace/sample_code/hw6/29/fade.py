import math
import sys
import groups

OUTFILE = 'faded.ppm'

def main(argv):
   if len(argv) < 2:
      print 'no file provided'
      sys.exit(1)
   elif len(argv) < 5:
      print 'not enough arguments provided'
      sys.exit(1)

   infile = openfile(argv[1], 'r')
   outfile = openfile(OUTFILE, 'w')
   
   read = infile.read()
   read2 = read.split()

   print_head(read2[1], read2[2], outfile)
   print_body(read2, outfile, float(read2[1]), float(read2[2]), float(argv[2]), float(argv[3]), float(argv[4]))

   infile.close()
   outfile.close()      

def openfile(name, mode):
   try:
      return open(name, mode)
   except:
      print 'cannot open file'
      sys.exit(1)

def print_head(width, height, outfile):
   print >> outfile, 'P3'
   print >> outfile, width, height
   print >> outfile, 255

def print_body(nums, outfile, width, height, row, col, rad):
   num_list = []
   for i, e in enumerate(nums):
      if i <= 3:
         pass
      else:
         num_list.append(float(e))

   list_of_nums = groups.groups_of_3(num_list)
   fade(list_of_nums, outfile, width, height, row, col, rad)

def fade(nums_list, outfile, width, height, row, col, rad):
   grid = make_grid(nums_list, width, height)
   for i in range(len(grid)):
      for j in range(len(grid[i])):
         scale = max(0.2, ((rad - distance(i, j, row, col))/rad))
         red = int(scale * grid[i][j][0])
         green = int(scale * grid[i][j][1])
         blue = int(scale * grid[i][j][2])
         print >> outfile, red, green, blue

def make_grid(nums_list, width, height):
   grid = []
   counter = 1
   newlist = []
   for i, e in enumerate(nums_list):
      newlist.append(e)
      if counter <  width:
         counter += 1
      else:
         grid.append(newlist)
         newlist = []
         counter = 1
   return grid

def distance(r, c, row, col):
   return math.sqrt((r - row)**2 + (c - col)**2)

if __name__ == "__main__":
   main(sys.argv)
