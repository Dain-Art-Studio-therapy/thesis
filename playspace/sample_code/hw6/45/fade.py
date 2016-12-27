import sys
import math

def main(argv):
   try:
      with open(argv[1], 'rb') as f:
         file_list = make_list(f)
         color_list = grouper(file_list)
         matrix = make_matrix(color_list, int(file_list[1]))
         colors = get_pixel_color(argv, matrix)
         writer(file_list, colors)
   except:
      print 'file not provided'

def make_list(fil):
   newlist = []
   for line in fil:
      s = line.split()
      for n in s:
         newlist.append(n)
   return newlist

def grouper(l):
   newlist = []
   for i in range(4, len(l), 3):
      newlist.append((l[i], l[i+1], l[i+2]))
   return newlist

#colorlist is a list of colors made from grouper [[r,b,g],...]
#width is from ppm header; text[1]
def make_matrix(colorlist, width):
   newlist = []
   for i in range(0, len(colorlist), width):
      newlist.append(colorlist[i:i + width])
   return newlist

def get_pixel_color(argv, matrix):
   newlist = []
   radius = float(argv[4])
   y = int(argv[2])
   x = int(argv[3])
   for row in range(len(matrix)):
      for col in range(len(matrix[row])):
         distance = math.sqrt((y - row) ** 2 + (x - col) ** 2)
         scale = (radius - distance) / radius
         if scale <= 0.2:
            scale = 0.2
         r = int(matrix[row][col][0]) * scale
         g = int(matrix[row][col][1]) * scale
         b = int(matrix[row][col][2]) * scale
         newlist.append((int(r), int(g), int(b)))
   return newlist

def writer(text, threes):
   with open('faded.ppm', 'w') as f:
      print >>f, 'P3'
      print >>f, text[1], text[2]
      print >>f, text[3]
      for n in threes:
         print >>f, n[0], n[1], n[2]

if __name__=='__main__':
   main(sys.argv)
