from sys import *
from math import *


def read_through(file_name):
   f = file_name.read()
   list = f.split()
   return list

def groups_of_3(list_of_values):
   groups = []
   current_group = []
   cur_group_length = 3
   for i in range(4,len(list_of_values),cur_group_length):
      groups = list_of_values[i:i+cur_group_length]
      current_group.append(groups)
   return current_group

def open_file2(file_name):
   try:
      f = open(file_name, "w")
   except:
      print 'Error couldnt open faded.ppm'
      exit()



def read_header(list, output_file):
   print >> output_file, list[0]
   print >> output_file, list[1],list[2]
   print >> output_file, list[3]


def two_d_list(c_list,file_out,x, y, width,height,radius):
   list = [[]]
   row = 0
   column = 0
   for i in c_list:
      if column == width:
         row += 1
         column = 0
         list.append([])
      column += 1
      list[row].append(i)
   for z in range(height):
      for p in range(width):
         dist = sqrt(((y-z)**2) + ((x-p)**2))
         scalar = ((radius-dist)/radius)
         if scalar < .2:
            scalar = .2


         r = str(int(float(list[z][p][0]) * scalar))
         g = str(int(float(list[z][p][1]) * scalar))
         b = str(int(float(list[z][p][2]) * scalar))
         print >> file_out,r,g,b






def main():
   try:
      f = open(argv[1], 'r')
   except:
      print 'error'
   A = open('faded.ppm','w')
   read = read_through(f)
   read_header(read,A)
   three = groups_of_3(read)
   two_d_list(three,A,int(argv[2]),int(argv[3]),int(read[1]),int(read[2]),int(argv[4]))



if __name__ == '__main__':
   main()


