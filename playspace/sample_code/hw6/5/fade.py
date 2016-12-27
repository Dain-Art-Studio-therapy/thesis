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

def group_pixels(input_file):
   pixel_group = []
   for i in range(0,len(input_file),3):
      increment = i + 3
      pixel_group.append(input_file[i:increment])
   return pixel_group

def read_image(infile):
   full_read = infile.read()
   full_split = full_read.split()
   return full_split

def distance_pt(position1, position2):
   return math.sqrt((position1[0]-position2[0])**2 + \
          (position1[1]-position2[1])**2)

def scale_pixel_color(pixel, scalar):
   new_pixel = []
   if scalar <= 0.2:
      scalar = 0.2
   for color_comp in pixel:
      scaled_color = int(color_comp) * scalar
      new_pixel.append(int(scaled_color))
   return new_pixel 

def find_pixel_position(pixel_index, width):
   if pixel_index >= width:
      row = int(pixel_index / width)
      col = int(pixel_index % width)
   elif pixel_index < width:
      row = 0
      col = pixel_index
   return (int(row), int(col)) 

def output_transformed_pixels(width, pixel_group, fade_point, radius, outfile):
   for i in range(len(pixel_group)):
      pixel_pos = find_pixel_position(i, width)
      distance = distance_pt(pixel_pos, fade_point)
      color_scalar = (radius - distance)/radius
      scaled_pixel = scale_pixel_color(pixel_group[i],\
                     color_scalar)
      print >> outfile, scaled_pixel[0], scaled_pixel[1],\
            scaled_pixel[2]

def output_pixels(split_file, fade_point, radius, outfile):
   p3_header = split_file[0]
   width = int(split_file[1])
   height = int(split_file[2])
   max_color = split_file[3]
   print >> outfile, p3_header
   print >> outfile, width, height
   print >> outfile, max_color
   pixel_groups = group_pixels(split_file[4:])
   output_transformed_pixels(width, pixel_groups, fade_point, \
                      radius, outfile)

def main(argv):
   infile = open_infile(argv)
   outfile = open_outfile("faded.ppm")
   fade_point = (int(argv[2]), int(argv[3]))
   fade_radius = int(argv[4])
   split_file = read_image(infile)
   output_pixels(split_file, fade_point, fade_radius, outfile)
   outfile.close()

if __name__ == '__main__':
   main(sys.argv)
