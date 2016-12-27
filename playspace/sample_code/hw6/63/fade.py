# Fade.py
import sys
import math
import re
from fade_commandline import *
from fade_canvas import *

OUT_NAME = 'faded.ppm'

def main(args):
   
   # Check if a valid file name is produced
   f_m = 'usage: python puzzle.py <file name> <(int)x-coord> <(int)y-coord> <(int)radius>'
   file_info = get_file_info(args, f_m, 4)
   
   
   # Received info
   file_name = file_info[0]
   y_coord = file_info[1]
   x_coord = file_info[2]
   radius = file_info[3]
   

   # Open and use file
   with open(file_name, 'r') as in_f:
      vals_string = in_f.read().strip()
      vals = re.split(' |\n', vals_string)
      f_info = vals[0:4]
      del vals[0:4]
      pixels = groups_of_3(vals)
      
      # Create a canvas
      canv = Canvas(Point(x_coord, y_coord), int(f_info[1]), int(f_info[2]))
      
      # Actually print the pixels
      with open_file(OUT_NAME, 'w+') as out_f:
         out_f.write('{0}\n{1} {2}\n{3}'.format(f_info[0],
                                                f_info[1],
                                                f_info[2],
                                                f_info[3]))
         for pixel in pixels:
            pix_tup = (float(pixel[0]), float(pixel[1]), float(pixel[2]))
            pix_str = get_px_color_str(pix_tup, canv.cur_pt, canv.f_pt, radius)
            out_f.write(pix_str)
            canv.updateCur()


def get_px_color_str(pixel, p_pt, f_pt, rad):
   # Calculate distance of px from focus point
   dist = calc_dist(p_pt, f_pt)
   factor = (rad - dist) / rad
   if factor < 0.2:
      factor = 0.2
   
   return '\n{0} {1} {2}'.format(int(pixel[0] * factor),
                                 int(pixel[1] * factor),
                                 int(pixel[2] * factor))


def calc_dist(pt1, pt2):
   return math.sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2)

def groups_of_3(vals):
   
   # Find number of full slices and remainder
   input_len = len(vals)
   full_group_count = input_len / 3
   remainder = input_len % 3
   
   # Groups to return
   groups = []
   
   # Add full groups
   for i in range(full_group_count):
      groups.append(vals[i * 3: (i + 1) * 3])
   
   # Add remainder for group
   if remainder > 0:
      groups.append(vals[input_len - remainder : input_len + 1])
   
   # Return
   return groups


def open_file(name, mode):
   try:
      # Successful opening
      return open(name, mode)
   except IOError as e:
      # Unsuccessful, print error and exit
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

if __name__ == '__main__':
   main(sys.argv)
