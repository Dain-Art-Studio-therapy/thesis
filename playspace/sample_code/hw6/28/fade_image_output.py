# Han Tran || CPE101-01,02 || Assignment 6 
# fade_image_output.py

import sys
import fade_image_reading

def image_output(headerVal, colorsVal):
   with open('fade.ppm', 'w') as f:
      print_header(headerVal, f)
      for i in range(len(colorsVal)):
         print_color(colorsVal[i], f)


# ---- Supportive Functions ---- #
def print_header(lst, f):
   f.write(str(lst[0]) + '\n')   # P3
   f.write(str(lst[1]) + '\n')   # w + h
   f.write(str(lst[2]) + '\n')   # Color Type


def print_color(lst, f):
   f.write(str(int(min(lst[0], 255))) + ' ')
   f.write(str(int(min(lst[1], 255))) + ' ')
   f.write(str(int(min(lst[2], 255))) + '\n')
   
