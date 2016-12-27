import sys
from blur_commandline import *
from blur_computations import *

FILE_IDX = 1
OUTFILE_NAME = 'blurred.ppm'

WIDTH_IDX = 1
HEIGHT_IDX = 2
MAX_COLOR = 255
PIX_START = 3


def process_file(name):
   with open_file(name, 'rb') as f:
      full = f.read()

   full = full.strip()
   return full.split()


def file_dimensions(file_str):
   try:
      width = int(file_str[WIDTH_IDX])
      height = int(file_str[HEIGHT_IDX])
      return [width, height]
   except:
      print >> sys.stderr, 'Invalid width or height'
      sys.exit(1)

   return None


def find_pixels(file_str):
   try:
      pixels = [int(file_str[i]) for i in range(len(file_str)) 
         if i > PIX_START]
   except:
      print >> sys.stderr, 'Invalid pixel value(s) in file)'
      sys.exit(1)

   return groups_of_three(pixels)


def process_pixel(pixels, width, height, row, column, radius, image):
   neighbors = find_neighbors(pixels, width, height, row, column, radius)
   pixel = average_pixels(neighbors)

   for i in pixel:
      print >> image, i

   return None


def print_header(width, height, image):
   print >> image, 'P3'
   print >> image, width, height
   print >> image, MAX_COLOR

   return None


def print_image(pixels, width, height, radius, image):
   print_header(width, height, image)

   for y in range(height):
      for x in range(width):
         process_pixel(pixels, width, height, y, x, radius, image)
 
   return None


def main(argv):
   check_args(argv)

   full = process_file(argv[FILE_IDX])
   pixels = find_pixels(full)
   width, height = file_dimensions(full)
   radius = init_blur(argv)

   with open_file(OUTFILE_NAME, 'w') as image:
      print_image(pixels, width, height, radius, image)

   return None


if __name__ == '__main__':
   main(sys.argv)
