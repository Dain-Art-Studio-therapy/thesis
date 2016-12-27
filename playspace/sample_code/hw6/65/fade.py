import sys
from math import *

def groups_of_3(input):
    newList = []
    for i in range(0, len(input), 3):
        if i+3>len(input):
            if ((i+3) - len(input) == 1):
                newList.append(input[i:i+2])
            elif ((i+3) - len(input) == 2):
                newList.append([input[i]])
        else:
            newList.append(input[i:i+3])
    return newList

def open_file(filename, mode):
   try:
     return open(filename, mode)
   except IOError as e:
      print>>sys.stderr, '{0}:{1}'.format(filename, e.strerror)

def distance(x1,y1,x2,y2):
   dy = y2-y1
   dx = x2-x1
   dy2 = dy**2
   dx2 = dx**2
   return sqrt(dy2 + dx2)

def cap_color_values(number):
   if number>255:
      return 255
   else:
      return int(number)

def validate_args(argv, length):
   if len(argv) != length:
      print>>sys.stderr, 'not enough arguments'
      exit(1)

def process_file(in_file, out_file, py, px, pr):
   line_counter = 0
   print_counter = 0
   cur_x = 0
   cur_y = 0
   pr = int(pr)
   px = int(px)
   py = int(py)
   extra = []
   for line in in_file:
      if line_counter < 3:
         print>>out_file, line
         if line_counter == 1:
            stringer = line.split()
            width = int(stringer[0])
      if line_counter >= 3:
         stringer = line.split()
         if extra == []:
            list_of_line_in_3 = groups_of_3(stringer)
            for l in list_of_line_in_3:
               if len(l) == 3:
                  try:
                     d = distance(cur_x, cur_y, px, py)
                     scalar = (pr - d) / pr
                     if scalar < 0.2:
                        scalar = 0.2
                     r = int(l[0]) * scalar	
                     g = int(l[1]) * scalar
                     b = int(l[2]) * scalar
                     new_r = cap_color_values(r)
                     new_g = cap_color_values(g)
                     new_b = cap_color_values(b)
                     extra = []
                     print_counter += 1
                     cur_x += 1
                     cur_y = print_counter / width
                     if cur_x == width:
                        cur_x = 0
                     print>>out_file, new_r, new_g, new_b
                  except:
                     print>>sys.stderr, 'Line', line_counter, 'unable to convert'
               else:
                  extra = l                 
         else:
            for i in stringer:
               extra.append(i)
            list_of_line_in_3 = groups_of_3(extra)
            for l in list_of_line_in_3:
               if len(l) == 3:
                  try:  
                     d = distance(cur_x, cur_y, px, py)
                     scalar = (pr-d) / pr
                     if scalar < 0.2:
                        scalar = 0.2
                     r = int(l[0]) * scalar
                     g = int(l[1]) * scalar
                     b = int(l[2]) * scalar
                     new_r = cap_color_values(r)
                     new_g = cap_color_values(g)
                     new_b = cap_color_values(b)
                     extra = []
                     print_counter += 1
                     cur_x += 1
                     cur_y = print_counter / width
                     if cur_x == width:
                        cur_x = 0
                     print>>out_file, new_r, new_g, new_b
                  except:
                     print>>sys.stderr, 'Line', line_counter, 'unable to convert'
                     exit(1)
               else:
                  extra = l                   
      line_counter += 1            
   
def main(argv):
   validate_args(argv, 5)
   OUT_FILE = open_file('faded.ppm', 'wb')
   with open_file(argv[1], 'rb') as f:
      process_file(f, OUT_FILE, argv[2], argv[3], argv[4]) 
   OUT_FILE.close()

if __name__ == '__main__':
   main(sys.argv)
