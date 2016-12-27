import sys
from fade_processing import *

def main(argv):
   fadeArgs = handle_argv(argv)
   size = (1024,768)
   maxColor = 255
   pixels = []
   
   with open_file(argv[1], 'rb') as f:
      size, maxColor = read_header_info(f)
      pixels = process_file(f, size[0])

   with open_file('faded.ppm','wb') as output:
      print_header(size, maxColor, output)
      fade_pixels(pixels, fadeArgs[0], fadeArgs[1], fadeArgs[2])
      print_pixels(pixels, output, maxColor)

def open_file(name, mode):
   try:
      return open(name,mode)
   except IOError as e:
      print >> sys.stderror, '{0}:{1}'.format(name, e.strerror)
      print >> 'Program now exiting'
      exit(1)

def read_header_info(f):
   f.readline()
   size = f.readline().split()
   maxColor = f.readline()
   return ((int(size[0]), int(size[1])), int(maxColor))

def handle_argv(argv):
   if len(argv) != 5:
      print >> 'Please supply the right arguments: file2open row col radius'
      exit(1)
   else: 
      return (try_int(argv[2]), try_int(argv[3]), try_int(argv[4]))

def try_int(v):
   try:
      return int(v)
   except:
      print >> 'The value you put in was not convertable to an int'
      print >> 'Format is: file row col radius'
      exit(1)


if __name__=='__main__':
   main(sys.argv)
