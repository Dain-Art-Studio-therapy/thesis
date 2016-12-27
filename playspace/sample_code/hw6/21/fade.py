import sys
import math

OUTFILE_NAME = "fade.ppm"
NUM_ARGS = 2
FILE_ARG_IDX = 1
ROW_IDX = 2
COL_IDX = 3
RAD_IDX = 4


def main(argv):
   if (len(argv) < NUM_ARGS):
      print >> sys.stderr, "file name missing"
      sys.exit(1)
      
   with open_file(argv[FILE_ARG_IDX]) as f:
      build_pixels((list_of_groups(argv, open_outfile(OUTFILE_NAME))),
        argv, open_outfile(OUTFILE_NAME))
      
def open_file(name):
   try:
      infile = open(name, "r")
      return infile
   except IOError as e:
      print >> sys.stderr, e
      sys.exit(1)

def open_outfile(name):
   try:
      outfile = open(name, "w")
      return outfile
   except IOError as e:
      print >> sys.stderr, e
      sys.exit(1)

def groups_of_3(list):
   newList = []
   for i in range(0, len(list), 3):
      newList.append(list[i : i + 3])
   return newList

def list_of_groups(in_file, out_file): 
   new_list = []  
   with open_file(in_file[FILE_ARG_IDX]) as f:
      for line in f:
         pix = line.split(' ')
         for e in int_list(pix):
            new_list.append(e)
      return groups_of_3(int_list(new_list))
   
def build_pixels(groups, in_file, out_file):
   with open_file(in_file[FILE_ARG_IDX]) as f:
      lines = f.read().splitlines()
      for i in range(len(lines)):
         if i < 3:
            out_file.write(lines[i])
            out_file.write('\n')

   
   for y in range(len(groups)):
      for x in range(len(groups[y])):
         try:
            out_file.write(str(cap_value(get_color(groups[y][x], 
               int(in_file[COL_IDX]), groups[y][x], 
               int(in_file[ROW_IDX]), groups[y][x+1], 0, 
               groups[y][x+2], int(in_file[RAD_IDX])))))
            out_file.write(' ')
            out_file.write(str(cap_value(get_color(groups[y][x+1],
               int(in_file[COL_IDX]), groups[y][x], 
               int(in_file[ROW_IDX]), groups[y][x+1], 0, 
               groups[y][x+2], int(in_file[RAD_IDX])))))
            out_file.write(' ')
            out_file.write(str(cap_value(get_color(groups[y][x+2], 
               int(in_file[COL_IDX]), groups[y][x], 
               int(in_file[ROW_IDX]), groups[y][x+1], 0, 
               groups[y][x+2], int(in_file[RAD_IDX])))))
            out_file.write('\n')
         except:
            pass
                  
def int_list(list):
   new = []
   for e in list:
      try:
         new.append(int(e))
      except:
         pass
   return new 

def scale_value(c):
   return max(0.2, c)
   
def scalar(radius, dist):
   return (radius - dist) / (radius)
   
def square(x):
   return x ** 2
   
def distance(x1, x2, y1, y2, z1, z2):
   return float(math.sqrt(square(x1 - x2) + square(y1 -y2) +
          square(z1 - z2)))

def get_color(c, row_y, x1, col_x, y1, z, z1, radius):
   return int(scale_value(abs(scalar(radius, distance
      (col_x, x1, row_y, y1, z, z1)))) * c)

    
def cap_value(c):
   cap = 255
   if c > cap:
      return cap
   else:
      return c 
             
           
if __name__ == "__main__":
   main(sys.argv)

