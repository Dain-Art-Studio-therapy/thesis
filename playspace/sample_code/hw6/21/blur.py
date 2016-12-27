import sys
import math

OUTFILE_NAME = "blurred.ppm"
NUM_ARGS = 2
FILE_ARG_IDX = 1
REACH_IDX = 2


def main(argv):
   if (len(argv) < NUM_ARGS):
      print >> sys.stderr, "file name missing"
      sys.exit(1)
      
   with open_file(argv[FILE_ARG_IDX]) as f:
      build_pixels((list_of_groups(argv, open_outfile(OUTFILE_NAME))),
        argv, open_outfile(OUTFILE_NAME))
        
def reach_flag(list):
   if (len(list) == NUM_ARGS):
      try:
         return int(list[2])
      except:
         return 4
   else:
      return 4

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
            out_file.write(str(blur(groups, in_file, out_file)))
         except:
            pass
            
def blur(groups, in_file, out_file):
   for y in range(1, in_file.get_height() -1):
      for x in range(1, in_file.get_width() - 1):
         centerP = get_pixel(x, y, groups)
         left = get_pixel(x-1, y, groups)
         right = get_pixel(x+1, y, groups)
         top = get_pixel(x, y-1, groups)
         bottom = get_pixel(x, y+1, groups)
         sums = (sum_pixels[centerP, left, right, top, bottom])
         averages = get_avg(sums)
   return (x, y, averages)

def get_pixel(x, y, groups):
   for i in range(len(groups)):   
      if groups[i] == y:
         for j in range(len(groups[i])):
             if groups[i][j] == x:
                return  groups[i] 
    return None
            
   
def get_height(in_file, out_file):
   with open_file(in_file[FILE_ARG_IDX]) as f:
      lines = f.read().splitlines()
      for i in range(len(lines)):
         size = i.split(' ')
         if i == 1:
            return int(size[1])
      return None
 
 def get_width(in_file, out_file):
   with open_file(in_file[FILE_ARG_IDX]) as f:
      lines = f.read().splitlines()
      for i in range(len(lines)):
         size = i.split(' ')
         if i == 1:
            return int(size[0])
      return None   
        
def sum_pixels(list):
   red = 0
   green = 0
   blue = 0
   for (r, g, b) in list:
      return red += r, green + g, blue += b

def get_avg(c):
   new_r = c[0] / 5
   new_g = c[1] / 5
   new_b = c[2] / 5
   return new_r, new_g, new_b
             
if __name__ == "__main__":
   main(sys.argv)

