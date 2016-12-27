import sys
import math

def open_infile(f):
   try:
      return open(f,'rb')
   except:
      print ('File cannot be opened.\nuasge: python fade.py <filename>' +
             ' point_row point_column radius')            
      exit(1)

def groups_of_3(list):
   new_list = []
   for i in range(0,len(list),3):
      new_list.append(list[i:i+3])
   return new_list

def write_header(input_file,outfile):
   infile = open_infile(input_file)
   header = [next(infile) for x in xrange(3)]
   for line in header:
      outfile.write(line + '\n')
   infile.close()

def get_width(input_file):
   infile = open_infile(input_file)
   for i, line in enumerate(infile):
      if i == 1:
         split = line.split()
         return int(split[0])
      elif i > 1:
         break
   infile.close()

def get_distance(pos1,pos2):
   distance = math.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2)
   return distance

def get_scale_val(radius,pos1,pos2):
   distance = get_distance(pos1,pos2)
   scale = (radius - distance)/radius
   return max(scale,0.2)

def get_row_col(idx,width):
   row = idx / width
   col = idx % width
   return (row,col)

def get_input_pixels(input_file):
   pixels = []
   infile = open_infile(input_file)
   for i in xrange(3):
      infile.next()
   for line in infile:
      split = line.split()
      for e in split:
         pixels.append(e)
   grouped_pixels = groups_of_3(pixels)
   infile.close()
   return grouped_pixels

def write_pixels(input_file,outfile,width,point,radius):
   grouped_pixels = get_input_pixels(input_file)
   for i, e in enumerate(grouped_pixels):
      pix_pos = get_row_col(i,width)
      scale = get_scale_val(radius,pix_pos,point)
      r = int(int(e[0])*scale)
      g = int(int(e[1])*scale)
      b = int(int(e[2])*scale)
      col = str(r) + ' ' + str(g) + ' ' + str(b) + ' '  
      outfile.write(col)

def main(argv):
   outfile = open('faded.ppm','w')
   width = get_width(argv[1])
   point = (int(argv[2]),int(argv[3]))
   radius = int(argv[4])
   write_header(argv[1],outfile)
   write_pixels(argv[1],outfile,width,point,radius)
   outfile.close()

if __name__ == "__main__":
   main(sys.argv)
