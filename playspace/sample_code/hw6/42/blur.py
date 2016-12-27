import sys
from convert import float_default
from data import Color

def main(argv):
   #try:
      with open(argv[1], 'rb') as f:
         color_list = blur_process_file(f, argv)
      blur_print_to_file(color_list)
   #except:
   #   print 'Given file could not be found'

def blur_process_file(f, argv):
   matrix = blur_list_to_matrix(blur_file_to_list(f))
   color_list = blur_set_blur(matrix, argv)
   return color_list

def blur_file_to_list(f):
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
   

def blur_list_to_matrix(new_list):
   counter = 0
   row = []
   matrix = []
   for i in range(len(new_list)):
      if counter < width:
         row.append(new_list[i])
      else:
         matrix.append(row)
         row = [new_list[i]]
         counter = 0
      counter += 1  
   print len(matrix), len(matrix[1])
   return matrix

def blur_set_blur(matrix, argv):
   global reach
   try:
      reach = int(float_default(argv[2], 4))
   except:
      reach = 4
   for row in range(height - 1):
      for col in range(width):
         matrix[row][col] = blur_pixel(matrix, row, col, reach)
   return matrix

def blur_pixel(matrix, row, col, reach):
   red, green, blue, total = 0, 0, 0, 0
   for y in range(max((row - reach), 0), min((row + reach + 1), height - 1)):
      for x in range(max((col - reach), 0), min((col + reach + 1), width)):
            red += matrix[y][x].r
            green += matrix[y][x].g
            blue += matrix[y][x].b
            total += 1
   return Color(red/total, green/total, blue/total)


def blur_print_to_file(new_list):
   output_file = open('blurred.ppm', 'w')
   print >> output_file, 'P3'
   print >> output_file, width, height
   print >> output_file, '255' 
   for row in new_list:
      for color in row:
         print >> output_file, color.r, color.g, color.b


main(sys.argv)
