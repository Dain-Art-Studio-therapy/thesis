import sys
from groups import groups_of_3

def main(argv):
   #try:
      with open(argv[1], 'rb') as f:
         color_list = puzzle_process_file(f)
      puzzle_print_file(color_list)
   #except:
   #   print 'Given file could not be found'

def puzzle_process_file(f):
   red_list = puzzle_file_to_list(f)
   return puzzle_set_color(puzzle_cap_red(puzzle_set_red(red_list)))
 
def puzzle_file_to_list(f):
   global width 
   global height
   red_values = []
   input_list = f.readlines()
   input_list = [x.strip('\n') for x in input_list]
   line_2 = input_list[1].split(' ')
   width, height = line_2[0], line_2[1]
   for x in range(3, len(input_list), 3):
      red_values.append(input_list[x])
   return red_values
   
def puzzle_set_red(red_list):
   return [10 * int(red) for red in red_list]

def puzzle_cap_red(list):
   new_list = []
   for red in list:
      if red > 255:
         red = 255
      new_list.append(red)
   return new_list

def puzzle_set_color(list):
   color_list = []
   for red in list:
      color = [red, red, red]
      color_list.append(color)
   return color_list

def puzzle_print_file(color_list):
   output_file = open('hidden.ppm', 'w')
   print >> output_file, 'P3'
   print >> output_file, width, height
   print >> output_file, '255'
   for color in color_list:
      print >> output_file, color[0], color[1], color[2]


main(sys.argv)
