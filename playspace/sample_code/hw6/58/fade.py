import commandline
import sys
import math

def main():
   cmdline = commandline.process(sys.argv)
   outfile = open('faded.ppm', 'w')
  
   print_header(cmdline[0][0], outfile)
   pixels = cmdline[0][1]
   row = cmdline[1][0]
   col = cmdline[1][1]
   radius = cmdline[1][2]
   width = int(cmdline[0][0][1])
   height = int(cmdline[0][0][2])

   print_pixels(pixels, row, col, radius, width, height, outfile) 
   outfile.close()

def print_header(list, outfile):
   print >> outfile, list[0]
   print >> outfile, list[1], list[2]
   print >> outfile, list[3]

def print_pixels(pixels, row, col, radius, width, height, file):
   p_count = 0
   for y in range(height):
      for x in range(width):
         dist = calc_distance_scale(row, col, radius, x, y)
         r = int(pixels[p_count][0]) * dist
         g = int(pixels[p_count][1]) * dist
         b = int(pixels[p_count][2]) * dist
         print >> file, int(r), int(g), int(b)
         p_count += 1

def calc_distance_scale(row, col, radius, x, y):
   d = distance(row, col, x, y)
   scale = (radius - d) / radius
   if scale <= 0.2:
      return 0.2
   return scale

def distance(row, col, x, y):
   return math.sqrt(((row - y) ** 2) + ((col - x) ** 2))

if __name__ == '__main__':
   main()
