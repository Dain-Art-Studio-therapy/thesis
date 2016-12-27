# Han Tran || CPE101-01,02 || Assignment 6 
# blur_image_output.py

import sys
import blur_image_reading

def image_output(headerVal, colorsVal):
   with open('blur.ppm', 'w') as f:
      print_header(headerVal, f)
      for i in range(len(colorsVal)):
         for j in range(len(colorsVal[i])):
            print_color(colorsVal[i][j], f)
            #print_color(colorsVal[i], f)


# ---- Supportive Functions ---- #
def print_header(lst, f):
   f.write(str(lst[0]) + '\n')   # P3
   f.write(str(lst[1]) + '\n')   # w + h
   f.write(str(lst[2]) + '\n')   # Color Type


def print_color(lst, f):
   f.write(str(int(min(lst[0], 255))) + ' ')
   f.write(str(int(min(lst[1], 255))) + ' ')
   f.write(str(int(min(lst[2], 255))) + '\n')
   
