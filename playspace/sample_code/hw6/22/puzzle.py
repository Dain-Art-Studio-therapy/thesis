import sys
from puzzle_computations import *

NUM_ARGS = 2
FILE_IDX = 1
OUTFILE_NAME = 'hidden.ppm'

WIDTH_IDX = 1
HEIGHT_IDX = 2
MAX_COLOR = 255
PIX_START = 3


def check_args(argv):
   if len(argv) < NUM_ARGS:
      print >> sys.stderr, 'No file provided'
      sys.exit(1)

   return None


def open_file(name, mode):
   try:
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0}: {1}'.format(name, e.strerror)
      sys.exit(1)


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
      print >> sys.stderr, 'Invalid pixel value(s) in input file'
      sys.exit(1)

   return groups_of_three(pixels)


def process_pixel(pixels, position, image):
   pixel = convert_pixel(pixels[position])

   for i in pixel:
      print >> image, i

   return None


def print_header(width, height, image):
   print >> image, 'P3'
   print >> image, width, height
   print >> image, MAX_COLOR

   return None


def print_image(pixels, width, height, image):
   print_header(width, height, image)

   for i in range(len(pixels)):
      process_pixel(pixels, i, image)

   return None


def main(argv):
   check_args(argv)

   full = process_file(argv[FILE_IDX])
   pixels = find_pixels(full)
   width, height = file_dimensions(full)

   with open_file(OUTFILE_NAME, 'w') as image:
      print_image(pixels, width, height, image)


if __name__ == '__main__':
   main(sys.argv)

