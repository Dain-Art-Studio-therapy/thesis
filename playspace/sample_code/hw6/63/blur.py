# Fade.py
import sys
import re
from blur_commandline import *
from blur_grid import *

OUT_NAME = 'blurred.ppm'

def main(args):
   
   # Check if a valid file name is produced
   f_m = 'usage: python puzzle.py <file name> [(int)blur radius]'
   file_info = get_file_info(args, f_m, 4)
   
   
   # Received info
   file_name = file_info[0]
   blur_rad = file_info[1]
   
   
   # Open and use file
   with open(file_name, 'r') as in_f:
      vals_string = in_f.read().strip()
      vals = re.split(' |\n', vals_string)
      f_info = vals[0:4]
      del vals[0:4]
      pixels = groups_of_3(vals)
      
      # Create a grid
      pix_grid = PixelGrid(pixels, int(f_info[1]), int(f_info[2]))
      
      # Actually print the pixels
      with open_file(OUT_NAME, 'w+') as out_f:
         out_f.write('{0}\n{1} {2}\n{3}'.format(f_info[0],
                                                f_info[1],
                                                f_info[2],
                                                f_info[3]))
         for pixel in pixels:
            all_pix = pix_grid.get_surrounding_pix_of_cur(blur_rad)
            pix_str = average_color_string(all_pix)
            out_f.write(pix_str)
            pix_grid.updateCur()


def average_color_string(pixels):
   pix_amt = float(len(pixels))
   r = 0
   g = 0
   b = 0
   
   # Add all components
   for p in pixels:
      r += int(p[0])
      g += int(p[1])
      b += int(p[2])

   # Get average
   r /= pix_amt
   g /= pix_amt
   b /= pix_amt

   return '\n{0} {1} {2}'.format(int(r), int(g), int(b))

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
