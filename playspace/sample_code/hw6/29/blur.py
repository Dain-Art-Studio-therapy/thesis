import math
import sys
import groups

OUTFILE = 'blurred.ppm'

def main(argv):
   if len(argv) < 2:
      print 'no file provided'
      sys.exit(1)
   elif len(argv) < 3:
      reach = 4
   else:
      reach = int(argv[2])

   infile = openfile(argv[1], 'r')
   outfile = openfile(OUTFILE, 'w')
   
   read = infile.read()
   nums = read.split()
   
   print_head(nums[1], nums[2], outfile)
   print_body(nums, outfile, float(nums[1]), float(nums[2]), reach)

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

def print_body(nums, outfile, width, height, reach):
   num_list = []
   for i, e in enumerate(nums):
      if i <= 3:
         pass
      else:
         num_list.append(float(e))

   list_of_nums = groups.groups_of_3(num_list)
   blur(list_of_nums, outfile, width, height, reach)

def blur(nums_list, outfile, width, height, reach):
   grid = make_grid(nums_list, width, height)

   for i in range(len(grid)):
      for j in range(len(grid[i])):
         total_r = 0
         total_g = 0
         total_b = 0
         for k in range(-reach, reach+1):
            for l in range(-reach, reach+1):
               try:
                  total_r += grid[i+k][j+l][0]
                  total_g += grid[i+k][j+l][1]
                  total_b += grid[i+k][j+l][2]
               except:
                  pass
         red = int(total_r / ((2*reach + 1)**2))
         green = int(total_g / ((2*reach + 1)**2))
         blue = int(total_b / ((2*reach + 1)**2))
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
