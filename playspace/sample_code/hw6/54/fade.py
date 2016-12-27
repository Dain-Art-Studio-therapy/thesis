#takes 4 command-line arguments
#   - input file      ARGV[1]
#   - y-coord integer ARGV[2]
#   - x-coord integer ARGV[3]
#   - radius  integer ARGV[4]
import sys
import math

def main(argv):
   try:
      with open(argv[1], 'rb') as f:
         dimensions = find_dim(f)
         width = dimensions[0]
         height = dimensions[1]
         columns = dimensions[0]
         pixel_list = file_to_list(f)
         color_lists = list_to_colors(pixel_list)
         grid = make_grid(color_lists, columns)
         center = get_center_index(argv)
         faded_grid = fade_pixels(grid, center, columns, argv)
         output_file(faded_grid, width, height)
   except:
      print >> sys.stderr, "Valid file was not provided"

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
   counter = 0
   f.readline()    
   lines_after_header = f.readlines()
   for line in lines_after_header:
      counter += 1
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
      

def get_center_index(argv):
   y_coord = int(argv[2])
   x_coord = int(argv[3])
   center_index = [y_coord, x_coord]
   return center_index


def fade_pixels(grid, center, columns, argv):
   new_pixel_list = []
   radius = int(argv[4])
   for i in range(len(grid)):
      for j in range(len(grid[i])):
         point = [i,j]
         d = find_distance(point, center)
         scalar = (radius - d)/(radius)
         if scalar < 0.2:
            scalar = 0.2
         pixel = grid[i][j]
         pixel = scale_pixel(pixel, scalar)
         new_pixel_list.append(pixel)
   new_grid = make_grid(new_pixel_list, columns)
   return new_grid


def scale_pixel(pixel,scalar):
   scaled_pixel = []
   for e in pixel:
      scaled_pixel.append(int(e * scalar))
   return scaled_pixel      
         

def find_distance(l1,l2):
   d = math.sqrt((l2[0]-l1[0])**2 + (l2[1]-l1[1])**2)
   return d
   

def output_file(grid, width, height):
   with open('faded.ppm', 'wb') as f:
      print >> f, 'P3'
      print >> f, width, height
      print >> f, 255
      for row in grid:
         for [r, g, b] in row:
            print >> f, r, g, b



if __name__ == '__main__':
   main(sys.argv)




