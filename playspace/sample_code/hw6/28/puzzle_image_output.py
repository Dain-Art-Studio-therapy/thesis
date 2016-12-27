# Han Tran || CPE101-01,02 || Assignment 6 
# puzzle_image_output.py

import sys
import puzzle_image_reading

def image_output(lst):
   # Note: List of color output from puzzle_image_reading
   #        is [[r,g,b], [r,g,b], [ect.]]['P3', 'width height', '255'].
   #        Thus, len(lst) == 2. Therefore, header = lst[1] and 
   #        color = lst[0]
   headerVal = lst[1]
   colorsVal = lst[0]
   with open('hidden.ppm', 'w') as f:
      print_header(headerVal, f)
      for i in range(len(colorsVal)):
         print_color(colorsVal[i], f)


def print_header(lst, f):
   f.write(str(lst[0]) + '\n')   # P3
   f.write(str(lst[1]) + '\n')   # w + h
   f.write(str(lst[2]) + '\n')   # Color Type


def print_color(lst, f):
   r = lst[0]*10  # New red
   f.write(str(min(r, 255)) + ' ')
   f.write(str(r) + ' ')   # Set new r as g
   f.write(str(r) + '\n')  # Set new r as b
   
