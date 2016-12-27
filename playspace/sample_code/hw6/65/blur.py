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

def determine_comm(argv, length, init):
   if len(argv) < length:
      comm = init
   else:
      comm = argv[2]
   return comm

def compute_new_vals(ylist, d, row, col, output_file):
   dist = int(d)
   r_tot = 0
   g_tot = 0
   b_tot = 0
   num_to_div = 0
   dx = dist
   dy = dist
   for value in range((2*dist + 1)**2):
      cont = [0,0,0]
      try:
         if row - dy >= 0 and col - dx >=0:
               cont = ylist[row-dy][col-dx]
               num_to_div += 1
      except:
         pass
      r_tot += int(cont[0])
      g_tot += int(cont[1])
      b_tot += int(cont[2])
      dx -= 1
      if dx == -(dist + 1):
         dx = dist
         dy -= 1
   r_tot = r_tot/num_to_div
   g_tot = g_tot/num_to_div
   b_tot = b_tot/num_to_div
   print>>output_file, r_tot, g_tot, b_tot

def make_list(in_file, out_file):
   line_counter = 0
   extra = []
   width = 0
   y_list = []
   temp_list = []
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
                  if len(temp_list) < width:
                     try:
                        temp_list.append(l)
                        extra = []
                     except:
                        print>>sys.stderr, 'Line', line_counter, 'unable to convert'
                  else:
                     y_list.append(temp_list)
                     temp_list = []
               else:
                  extra = l                 
         else:
            for i in stringer:
               extra.append(i)
            list_of_line_in_3 = groups_of_3(extra)
            for l in list_of_line_in_3:
               if len(l) == 3:
                  if len(temp_list) < width:
                     try:  
                        temp_list.append(l)
                        extra = []
                     except:
                        print>>sys.stderr, 'Line', line_counter, 'unable to convert'
                  else:
                     y_list.append(temp_list)
                     temp_list = []
               else:
                  extra = l                   
      line_counter += 1            
   return y_list   

def main(argv):
   comm = determine_comm(argv, 3, 4)
   OUT_FILE = open_file('blurred.ppm', 'wb')
   with open_file(argv[1], 'rb') as f:
      y_list = make_list(f, OUT_FILE) 
   for row in range(len(y_list)):
      for col in range(len(y_list[row])):
         compute_new_vals(y_list, comm, row, col, OUT_FILE)
   OUT_FILE.close()

if __name__ == '__main__':
   main(sys.argv)
