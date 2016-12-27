import sys
import math

def open_infile(argv):
   try:
      infile = open(argv[1], "rb")
      return infile
   except IOError as e:
      print "File is missing or does not exist"
      exit(1)

def open_outfile(output_file):
   try:
      outfile = open(output_file, "w")
      return outfile
   except IOError as e:
      print "File cannot be opened for writing"
      exit(1)

def get_neighbor_reach(argv):
   try:
      neighbor_reach = int(argv[2])
   except:
      neighbor_reach = 4
   return neighbor_reach

def find_pixel_position(pixel_index, width):
   row = int(pixel_index / width)
   col = int(pixel_index % width)
   return (row, col)

def group_pixels(split_file):
   pixel_group = []
   for i in range(0,len(split_file),3):
      increment = i + 3
      pixel_group.append(split_file[i:increment])
   return pixel_group

def read_image(infile):
   full_read = infile.read()
   full_split = full_read.split()
   return full_split

def average_color(color_comp):
   total_sum = 0
   for comp in color_comp:
      total_sum += comp
   ave_color = total_sum/len(color_comp)
   return ave_color

def obtain_new_pixel(neighbor_pixels):
   red_c = []
   green_c = []
   blue_c = []
   for pixel in neighbor_pixels:
      red_c.append(int(pixel[0]))
      green_c.append(int(pixel[1]))
      blue_c.append(int(pixel[2]))
   ave_red = average_color(red_c)
   ave_green = average_color(green_c)
   ave_blue = average_color(blue_c)
   new_pixel = [ave_red, ave_green, ave_blue]
   return new_pixel

def top_limit(current_pix, reach):
   row = max(0,(current_pix[0] - reach))
   col = max(0,(current_pix[1] - reach))
   return (row,col)

def bottom_limit(current_pix, reach, height, width):
   row = min(height, (current_pix[0] + (reach + 1)))
   col = min(width, (current_pix[1] + reach + 1))
   return (row,col)

def find_pixel_index(pixel_row, pixel_col, width):
   index = (pixel_row * width) + pixel_col
   return index

def find_neighbors(pixel_pos, pixel_group, width, height, reach):
   neighbors = []
   top_l = top_limit(pixel_pos, reach)
   bottom_l = bottom_limit(pixel_pos, reach, height, width)
   for row in range(top_l[0],bottom_l[0]):
      for col in range(top_l[1],bottom_l[1]):
         neighbor_index = find_pixel_index(row, col, width)
         n_pixel = pixel_group[neighbor_index]
         neighbors.append(n_pixel)
   return neighbors

def output_blurred_pixels(width, height, pixel_group, reach, outfile):
   for i in range(len(pixel_group)):
      pixel_pos = find_pixel_position(i, width)
      pix_neighbors = find_neighbors(pixel_pos, pixel_group, width, height, reach)
      blurred_pixel = obtain_new_pixel(pix_neighbors)
      print >> outfile, blurred_pixel[0], blurred_pixel[1],\
            blurred_pixel[2]

def output_pixels(split_file, neighbor_reach, outfile):
   p3_header = split_file[0]
   width = int(split_file[1])
   height = int(split_file[2])
   max_color = split_file[3]
   print >> outfile, p3_header
   print >> outfile, width, height
   print >> outfile, max_color
   pixel_group = group_pixels(split_file[4:])
   output_blurred_pixels(width, height, pixel_group, neighbor_reach, outfile)

def main(argv):
   infile = open_infile(argv)
   outfile = open_outfile("blurred.ppm")
   neighbor_reach = get_neighbor_reach(argv)
   split_file = read_image(infile)
   output_pixels(split_file, neighbor_reach, outfile)
   outfile.close()

if __name__ == '__main__':
   main(sys.argv)
