import sys
from data import Color
from math import sqrt


def main(argv):
   #try:
      with open(argv[1], 'rb') as f:
         color_list = fade_process_file(f, argv)
      fade_print_to_file(color_list)
   #except:
   #   print 'Given file could not be found'


def fade_process_file(f, argv):
   new_list = fade_file_to_list(f)
   return fade_set_fade(new_list, argv)

def fade_file_to_list(f):
   global width
   global height
   input_list = [x.strip('\n') for x in f.readlines()]
   line_2 = input_list[1].split(' ')
   width, height = int(line_2[0]), int(line_2[1])
   color_list = []
   for x in range(3, len(input_list), 3):
      color = Color(int(input_list[x]), int(input_list[x + 1]), 
                    int(input_list[x + 2]))
      color_list.append(color)
   return color_list
      
def fade_set_fade(list, argv):
   row = int(argv[2])
   col = int(argv[3])
   rad = int(argv[4])
   for i in range(len(list)):
      x = i % width
      y = i / height
      dist = fade_dist(row, col, y, x)
      fade = max((rad-dist)/rad, 0.2)
      list[i] = fade_color(list[i], fade)
   return list 

def fade_color(color, fade):
   return Color(color.r * fade, color.g * fade, color.b * fade)

def fade_dist(a, b, c, d):
   return sqrt(((a - c) ** 2) + ((b - d) ** 2))
   

def fade_print_to_file(new_list):
   output_file = open('faded.ppm', 'w')
   print >> output_file, 'P3'
   print >> output_file, width, height
   print >> output_file, '255'
   for color in new_list:
      print >> output_file, color.r, color.g, color.b

main(sys.argv)
