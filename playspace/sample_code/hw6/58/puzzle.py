import commandline
import sys

def main():
   cmdline = commandline.process(sys.argv)
   outfile = open('image.ppm', 'w')

   print_header(cmdline[0], outfile)
   pixels = cmdline[1]
   print_pixels(pixels, outfile)

   outfile.close()

def print_header(list, outfile):
   print >> outfile, list[0]
   print >> outfile, list[1], list[2]
   print >> outfile, list[3]

def print_pixels(pixels, file):
   r = 0
   g = 0
   b = 0
   for p in pixels:
       r = float(p[0]) * 10
       g = r
       b = r
       print >> file, r, g, b

if __name__ == '__main__':
   main()
