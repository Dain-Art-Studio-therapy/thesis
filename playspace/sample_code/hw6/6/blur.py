from sys import *
import math

def list_splitter(file):
   read_list = file.read()
   split_list = read_list.split()
   return split_list

def triples(list):
   L = []
   for x in range(4,len(list),3):
      L.append(list[x:x+3])
   return L

def header(list,outfile):
   print >> outfile,list[0]
   print >> outfile,list[1],list[2]
   print >> outfile,list[3]


def average(list):
   tot = 0
   counter = 0
   for i in list:
      tot = tot + (list[counter])
      counter = counter + 1
   return tot/(counter+1)


def color_adjust(list,width,height,reach,outfile):
   counter = 0
   for i in list:

      pix_x = counter % width
      pix_y = counter/ width

      pix_in_reach = []

      x_min = max(pix_x - reach,0)
      x_max = min(pix_x + reach,width)
      y_min = max(pix_y - reach,0)
      y_max = min(pix_y + reach,height)

      for y in range(x_min,x_max):
         for x in range(y_min,y_max):
            index = (x * width)+y
            pix_in_reach.append(list[index])

      r_list = []
      g_list = []
      b_list = []

      counter2 = 0
      for color in pix_in_reach:  
         r_list.append(int(pix_in_reach[counter2][0]))
         g_list.append(int(pix_in_reach[counter2][1]))
         b_list.append(int(pix_in_reach[counter2][2]))
         counter2 = counter2 + 1
     
 
      R = average(r_list)
      G = average(g_list)
      B = average(b_list)
      print >> outfile, R,G,B
      counter = counter + 1


def main():
   try:
      opened = open(argv[1], "r")
      image = open("blurred.ppm", "w")
   except:
      print "Invalid File"

   try:
      reach = int(argv[2])
   except:
      print "No reach specified. 4 will be used."
      reach = 4

   split_list = list_splitter(opened)
   width = int(split_list [1])
   height = int(split_list [2])
   header(split_list,image)
   L = triples(split_list)
   color_adjust(L,width,height,reach,image)
 

if __name__ =="__main__":
   main()

 
