import sys
from blur_process import *

DEFAULT_BLUR = 4

def main(argv):
   blurReach = handle_argv(argv)
   size = (1024,768)
   maxColor = 255
   pixels = []
   
   with open_file(argv[1], 'rb') as f:
      size, maxColor = read_header_info(f)
      pixels = process_file(f, size[0])
  
   blurPx = pixels

   with open_file('blurred.ppm','wb') as output:
      print_header(size, maxColor, output)
      blur_pixels(pixels,blurPx, blurReach, size[0], size[1])
      print_pixels(blurPx, output, maxColor)

def open_file(name, mode):
   try:
      return open(name,mode)
   except IOError as e:
      print >> sys.stderror, '{0}:{1}'.format(name, e.strerror)
      print 'Program now exiting'
      exit(1)

def read_header_info(f):
   f.readline()
   size = f.readline().split()
   maxColor = f.readline()
   return ((int(size[0]), int(size[1])), int(maxColor))

def handle_argv(argv):
   if len(argv) > 3:
      print >> 'Commandline Format: Input-File [Blur-Factor]'
      exit(1)
   elif len(argv) == 3:
      return max(try_int(argv[2]),0)
   else:
      return DEFAULT_BLUR   

def try_int(v):
   try:
      return int(v)
   except:
      print 'The value was not convertable to an int'
      print 'Now exiting'
      exit(1)


if __name__=='__main__':
   main(sys.argv)
