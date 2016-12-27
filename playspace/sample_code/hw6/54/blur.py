# Takes 2 command-line arguments
#    - 1st is input file
#    - ***OPTIONAL 2nd is integer "neighbor reach"

import sys

DEFAULT_REACH = 4

def main(argv):
   try:
      with open(argv[1], 'rb') as f:
         reach = get_reach(argv)
         dimensions = find_dim(f)
         length = dimensions[0]
         height = dimensions[1]
         columns = dimensions[0]
         pixel_list = file_to_list(f)
         color_lists = list_to_colors(pixel_list)
         grid = make_grid(color_lists, columns)
         blurred_grid = blur_image(grid, columns, argv, height, length)
         output_file(blurred_grid, length, height)
   except:
      print >> sys.stderr, "Valid file was not provided"


def get_reach(argv):
   if len(argv) == 2:
      return DEFAULT_REACH
   else:
      reach = int(argv[2])
      return reach


def find_dim(f):
   f.readline()
   line = f.readline()
   nums = line.split()
   dimensions = []
   for e in nums:
      dimensions.append(int(e))
   return dimensions


def file_to_list(f):
   pixel_list = []
   f.readline()    
   lines_after_header = f.readlines()
   for line in lines_after_header:
      nums = line.split()
      for e in nums:
         pixel_list.append(int(e))
   return pixel_list


def list_to_colors(pixels):
   color_lists = []
   for i in range(0, len(pixels), 3):
      if i + 2 < len(pixels):
         color_lists.append([pixels[i], pixels[i+1], pixels[i+2]])     
   return color_lists


def make_grid(values, columns):
   row_list = []
   column_list = []
   for value in values:
      if len(row_list) < columns:
         row_list.append(value)
      else:
         column_list.append(row_list)
         row_list = [value]
   column_list.append(row_list)
   return column_list


def find_neighbors(grid, pt_index, reach, height, length):
   grid_height = height
   grid_length = length
   neighbors = []
   y = pt_index[0]
   x = pt_index[1]

   right_x = x + reach
   if right_x >= grid_length:
      right_x = grid_length - 1
   right_x = [y,right_x]
   left_x = x - reach
   if left_x <= 0:
      left_x = 0
   left_x = [y,left_x]

   top_y = y - reach
   if top_y <= 0:
      top_y = 0
   top_y = [top_y, x]
   bottom_y = y + reach
   if bottom_y >= grid_height:
      bottom_y = grid_height - 1
   bottom_y = [bottom_y, x]

   top_left = [top_y[0], left_x[1]]
   bottom_right = [bottom_y[0], right_x[1]]

   for i in range(top_left[0], bottom_right[0] + 1):
      for j in range(top_left[1], bottom_right[1] + 1):
         neighbor_pt = grid[i][j]
         neighbors.append(neighbor_pt)
   return neighbors
   

def blur_image(grid, columns, argv, height, length):
   reach = get_reach(argv)
   blurred_pixels = []
   for i in range(len(grid)):
      for j in range(len(grid[i])):
         point = [i,j]
         neighbors = find_neighbors(grid, point, reach, height, length)
         blurred_color = average_color(neighbors)
         blurred_pixels.append(blurred_color)
   new_grid = make_grid(blurred_pixels, columns)
   return new_grid
   

def average_color(colors):
   total_colors = len(colors)
   total_red = 0
   total_green = 0
   total_blue = 0
   for [r, g, b] in colors:
      total_red += r
      total_green += g
      total_blue += b
   avg_red = total_red/total_colors
   avg_green = total_green/total_colors
   avg_blue = total_blue/total_colors
   blurred_color = [avg_red, avg_green, avg_blue]
   return blurred_color
      

def output_file(grid, width, height):
   with open('blurred.ppm', 'wb') as f:
      print >> f, 'P3'
      print >> f, width, height
      print >> f, 255
      for row in grid:
         for [r, g, b] in row:
            print >> f, r, g, b

if __name__ == '__main__':
   main(sys.argv)



