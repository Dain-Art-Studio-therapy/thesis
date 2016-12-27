# puzzle.py
import sys
from puzzle_commandline import *
import re

OUT_NAME = 'hidden.ppm'

def main(args):

   # Check if a valid file name is produced
   f_m = 'usage: python puzzle.py <file name>'
   file_name = get_file_name(args, f_m)

   # Open and use file
   with open(file_name, 'r') as in_f:
      vals_string = in_f.read().strip()
      vals = re.split(' |\n', vals_string)
      f_info = vals[0:4]
      del vals[0:4]
      pixels = groups_of_3(vals)
      
      # Actually print the pixels
      with open_file(OUT_NAME, 'w+') as out_f:
         out_f.write('{0}\n{1} {2}\n{3}'.format(f_info[0],
                                                 f_info[1],
                                                 f_info[2],
                                                 f_info[3]))
         for pixel in pixels:
            r = float(pixel[0])
            r = int(min(r*10, 255))
            out_f.write('\n{0} {1} {2}'.format(r, r, r))


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
