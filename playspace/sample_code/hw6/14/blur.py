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


def read_header(list, output_file):
   print >> output_file, list[0]
   print >> output_file, list[1],list[2]
   print >> output_file, list[3]

def two_d_list(c_list,file_out, width,height,neighbor_reach):
   list = [[]]
   row = 0
   column = 0
   for i in c_list:
      if column == width:
         row += 1
         column = 0
         list.append([])
      #print len(list)
      list[row].append(i)
      column += 1
   for z in range(len(list)):
       #print range(len(list[z])), "r len list z"
      for p in range(len(list[z])):
         red = 0
         green = 0
         blue = 0
         tally = 0
      
         for ypixels in range(max(0,(int(z) - int(neighbor_reach))), min(height,(int(p) + int(neighbor_reach)))):
            for xpixels in range(max(0,(int(p) - int(neighbor_reach))), min(width,(int(z) + int(neighbor_reach)))):
               pix = list[ypixels][xpixels]
               #print pix , "pix"
               red   += int(pix[0])
               green += int(pix[1])
               blue  += int(pix[2])
               tally += 1
      
    
                     
         pix_red = str(int(red/tally))
         
         pix_green = str(int(green/tally))
       
         pix_blue = str(int(blue/tally))
       
        
         print >> file_out,pix_red,pix_green,pix_blue
                     
def write_out(c_list, width,height,neighbor_reach):
   try:
      out = open('blurred.ppm', 'w')
   except:
      print 'error, tis but a scratch'
      exit()
   two_d_list(c_list, out, width, height, neighbor_reach)
                     
                     
                    
def main():
   try:
      f = open(argv[1], 'r')
   except:
      print 'error'

   A = open('blurred.ppm', 'w')
   read = read_through(f)
   read_header(read, A)
   three = groups_of_3(read)
   write_out(three, int(read[1]), int(read[2]), argv[2])
                     
                     
                     
                     
                    
                     
if __name__ == '__main__':
   main()
    
                     
                     
                     
                     
