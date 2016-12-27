import sys
import math

RED = 0
GREEN = 1
BLUE = 2


#In process_file, you want to read the heading, write it to the output file, process the pixels by groups of three. 
def process_file(input_file, output_file):
   file_list = input_file.readlines()

   new_file_list = []
   for e in file_list:
      new = e.strip('\n')
      new_file_list.append(new)
   header = find_header(new_file_list)
   print_header(header, output_file)

   width = find_img_width(header)
   height = find_img_height(header)
   row = int(sys.argv[2])
   col = int(sys.argv[3])
   radius = int(sys.argv[4])

   pixel_list = groups_of_3(new_file_list[3:len(new_file_list)+1])
   for index, pixel in enumerate(pixel_list, 1):
      new_pixel = process_pixel(pixel_list, index, pixel, width, height, \
         col, row, radius)
      print >> output_file, new_pixel[RED], new_pixel[GREEN], new_pixel[BLUE]

def process_pixel(pixel_list, index, pixel, width, height, col, row, radius):
   p_col = find_pixel_col(pixel_list, index, pixel, width)
   p_row = find_pixel_row(pixel_list, index, pixel, width, height)

   distance = find_distance(col, row, p_col, p_row)
   scale = compute_scale(radius, distance)
   new_pixel = fade_pixel(pixel, row, col, scale)
   return new_pixel

def fade_pixel(pixel, row, col, scale): 
   red = int(float(pixel[RED])*scale)
   green = int(float(pixel[GREEN])*scale)
   blue = int(float(pixel[BLUE])*scale)
   processed_pixel = [red, green, blue]
   return processed_pixel

def compute_scale(radius, distance):
   scale = (radius-distance)/float(radius)
   if scale < 0.2:
      scale = 0.2
   return scale

def print_header(header, output_file):
   print >> output_file, header[0]
   print >> output_file, header[1]
   print >> output_file, header[2]

def find_header(file_list):
   header = file_list[:3]
   return header

def find_img_width(PPM_header):
   try:
      width = int(PPM_header[1].split()[0])
   except:
      width is None
   return width

def find_img_height(PPM_header):
   try:
      height1 = int(PPM_header[1].split()[1])
   except:
      height1 is None
   return height1

def find_pixel_col(pixel_list, index, pixel, width):
   col = (index%(width))
   return col

def find_pixel_row(pixel_list, index, pixel, width, height):
   col = find_pixel_col(pixel_list, index, pixel, height)
   row = (index - col)/(width)
   return row

def find_distance(col, row, p_col, p_row):
   return math.sqrt((col-p_col)*(col-p_col) + (row-p_row)*(row-p_row))

def groups_of_3(list):
    return_list = []
    for i in range(int(math.ceil(len(list)/3.0))):       
        if len(list) <= (3*i+1):
            subgroup = [list[3*i]]
        elif len(list) <= (3*i+2):
            subgroup = [list[3*i], list[3*i+1]]
        else:
            subgroup =[list[3*i], list[3*i+1], list[3*i+2]] 
        return_list.append(subgroup)
    return return_list

def string_to_pixel_list(line_string, extras):
   line_list = line_string.split()
   for i in range(len(extras)):
      line_list.insert(i, extras[i])
   pixel_list = groups.groups_of_3(line_list)
   return pixel_list

def open_file(argv, mode):
   try:
      f = open(argv, mode)
      return f
   except:
   	  print >> sys.stderr, "Cannot open file provided."
   	  exit(1)

def main():
   input_file = open_file(sys.argv[1], 'rb')
   output_file = open_file('faded.ppm', 'w')
   process_file(input_file, output_file)   
   input_file.close()
   output_file.close()


if __name__ ==  '__main__':
   main()