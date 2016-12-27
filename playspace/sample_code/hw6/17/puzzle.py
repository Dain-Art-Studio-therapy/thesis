import sys
from puzzle_processes import *

def main(argv):
   pixels = []
   size = (1024, 768)
   maxColor = 255

   with open_file(argv[1], 'rb') as f:
      size, maxColor = read_header_info(f)
      pixels = process_file(f, size[0])
   
   with open_file('decoded.ppm', 'wb') as output:
      print_header(size, maxColor, output)
      print_pixels(pixels, output)

def read_header_info(f):
   f.readline()
   size = f.readline().split()
   maxColor = f.readline()
   return ((int(size[0]), int(size[1])), int(maxColor))


def open_file(name, mode):
   try:
      return open(name, mode)
   except IOError as e:
      print >> sys.stderror, '{0}:{1}'.format(name, e.strerror)
      print 'File could not be opened'
      exit(1)

if __name__=='__main__':
   main(sys.argv)
