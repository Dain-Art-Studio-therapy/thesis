import sys
import math

def main(argv):
   if len(argv) != 5:
      print 'usage: python fade.py image row col radius'
      exit(1)

   infile = open_with(argv[1], 'r')
   outfile = open_with('faded.ppm', 'w')

   unorganized = read_file(infile)
   header = unorganized[0 : 4]

   width = int(header[1])
   height = int(header[2])

   row = validity(int(argv[2]), height)
   col = validity(int(argv[3]), width)
   radius = int(argv[4])

   if radius <= 0:
      print 'Radius needs to be positive'
      exit(1)

   organized = unorganized[4 : len(unorganized)]
   organized_1 = str_to_float(organized)
   organized_2 = list_splicer(organized_1, 3)
   organized_3 = list_splicer(organized_2, int(header[1]))

   header_writer(header, outfile)
   blurrer(organized_3, row, col, radius, width, outfile)

   infile.close()
   outfile.close()

def open_with(name, method):
   try:
      return open(name, method)

   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      
def read_file(file):
   newList = []
   for line in file:
      p = line.split()
      for n in p:
         newList.append(n)
   return newList

def validity(number, max):
   if 0 < number < max:
      return number
   else:
      print 'Number is out of bounds'
      exit(1)

def str_to_float(list):
   try:
      return [float(v) for v in list]
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

def list_splicer(list, number):
   newList = []
   for i in range(0, len(list), number):
      newList.append(list[i : i + number])
   return newList

def header_writer(header, file):
   file.write(header[0] + '\n')
   file.write(header[1] + ' ' + header[2] + '\n')
   file.write(header[3] + '\n')

def blurrer(list, r, c, rad, width, outfile):
   counter_w = 0
   counter_h = 0
   for i in range(len(list)):
      for j in range(len(list[i])):
         scale = scale_function(r, c, rad, j, i)
         pixel = list[i][j]
         red = min(255, int(pixel[0] * scale))
         green = min(255, int(pixel[1] * scale))
         blue = min(255, int(pixel[2] * scale))
         outfile.write(str(red) + '\n')
         outfile.write(str(green) + '\n')
         outfile.write(str(blue) + '\n')

def scale_function(r, c, rad, x, y):
   distance = math.sqrt((x - c) ** 2 + (y - r) ** 2)
   scale = (rad - distance) / float(rad)

   if scale < .2:
      scale = .2

   return scale

if __name__ == '__main__':
   main(sys.argv)
