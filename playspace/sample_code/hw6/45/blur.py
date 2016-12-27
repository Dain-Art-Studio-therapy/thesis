import sys
import math

def main(argv):
   #try:
      with open(argv[1], 'rb') as f:
         file_list = make_list(f)
         color_list = grouper(file_list)
         matrix = make_matrix(color_list, int(file_list[1]))
         width = int(file_list[1])
         height = int(file_list[2])
         colors = pixel_list(argv, matrix, width, height)
         writer(file_list, colors)
   #except:
      #print 'file not provided'

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

def make_matrix(colorlist, width):
   newlist = []
   for i in range(0, len(colorlist), width):
      newlist.append(colorlist[i:i + width])
   return newlist

def get_start_pts(x, y, blur):
   startx = x
   starty = y
   for x in range(blur):
      if startx > 0:
         startx -= 1
      if starty > 0:
         starty -= 1
   return (startx, starty)

def get_avg_mat(startx, starty, pix_x, pix_y, width, height, matrix, blur):
   newlist = []
   x = startx
   y = starty
   stopy = pix_y + blur
   stopx = pix_x + blur
   if stopy >= height:
      stopy = height - 1
   if stopx >= width:
      stopx = width - 1
   while y <= stopy:
      while x <= stopx:
         newlist.append(matrix[y][x])
         x += 1
      y += 1
      x = startx
   return newlist

def get_color(matrix):
   rsum = 0
   gsum = 0
   bsum = 0
   total = len(matrix)
   for n in matrix:
      rsum += int(n[0])
      gsum += int(n[1])
      bsum += int(n[2])
   r = rsum / total
   g = gsum / total
   b = bsum / total
   return (r, g, b)

def pixel_list(argv, matrix, width, height):
   newlist = []
   try:
      blur = int(argv[2])
   except:
      blur = 4
   for row in range(len(matrix)):
      for col in range(len(matrix[row])):
         start_pt = get_start_pts(col, row, blur)
         box_matrix = get_avg_mat(start_pt[0], start_pt[1], col, row, width, height, matrix, blur)
         color = get_color(box_matrix)
         newlist.append(color)
   return newlist

def writer(text, threes):
   with open('blurred.ppm', 'w') as f:
      print >>f, 'P3'
      print >>f, text[1], text[2]
      print >>f, text[3]
      for n in threes:
         print >>f, n[0], n[1], n[2]

if __name__=='__main__':
   main(sys.argv)
