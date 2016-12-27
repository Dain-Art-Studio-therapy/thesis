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
   blur_factor = find_blur_factor()
 
   pixel_list = groups_of_3(new_file_list[3:len(new_file_list)+1])
   pixel_grid = make_grid(pixel_list, width, height)

   for p_row, row in enumerate(pixel_grid, 1):
      for p_col, pixel in enumerate(row, 1):
         neighbor_list = find_neighbors(pixel_grid, blur_factor, p_row, p_col)
         new_pixel = average_of_pixels(neighbor_list)
         print >> output_file, new_pixel[RED], new_pixel[GREEN], new_pixel[BLUE]

def make_grid(pixel_list, width, height):
   grid = []
   for row in range(height):
      row_list = []
      for col in range(width):
         row_list.append(pixel_list[row*width + col])
      grid.append(row_list)
   return grid

def find_neighbors(pixel_grid, blur_factor, p_row, p_col):
   neighbor_list = []
   for row in range(p_row - blur_factor, p_row + blur_factor + 1):
      for col in range(p_col - blur_factor, p_col + blur_factor + 1):
         if row >= 0 and row < len(pixel_grid) and \
            col >= 0  and col < len(pixel_grid[row]): 
            neighbor_list.append(pixel_grid[row][col])
         else:
            pass
   return neighbor_list

def find_blur_factor():
   try:
      blur_factor = int(sys.argv[1])
   except:
      blur_factor = 4
   return blur_factor

def average_of_pixels(neighbor_list):
   red_sum = 0
   green_sum = 0
   blue_sum = 0
   for pixel in neighbor_list:
      red_sum += int(pixel[RED])
      green_sum += int(pixel[GREEN])
      blue_sum += int(pixel[BLUE])
   total = len(neighbor_list)
   avg_pixel = [red_sum/total, green_sum/total, blue_sum/total]
   return avg_pixel

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

def find_distance(col, row, p_col, p_row):
   return math.sqrt((col-p_col)*(col-p_col) + (row-p_row)*(row-p_row))

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

def main():
   input_file = open_file(sys.argv[1], 'rb')
   output_file = open_file('blurred.ppm', 'w')
   process_file(input_file, output_file)   
   input_file.close()
   output_file.close()


if __name__ ==  '__main__':
   main()