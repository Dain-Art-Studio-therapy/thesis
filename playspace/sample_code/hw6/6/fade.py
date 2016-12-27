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

def distance(x1,y1,x2,y2):
   d = math.sqrt((x2-x1)**2+(y2-y1)**2)
   return d


def color_adjust(list,row,col,rad,width,height,outfile):
   counter = 0
   for color in list:
      pix_x = counter % width
      pix_y = counter/width
      dist = distance(pix_x,pix_y,col,row)
      scale = max(0.2,((rad - dist)/rad))
      R = int(float(color[0])*scale)
      B = int(float(color[1])*scale)
      G = int(float(color[2])*scale)
      print >> outfile, R, G, B
      counter = counter +1
   

def main():
   try:
      opened = open(argv[1], "r")
      image = open("faded.ppm", "w")
   except:
      print "Invaid File"
   try:
      row = int(argv[2])
      col = int(argv[3])
      rad = int(argv[4])
   except:
      print "Invalid Inputs"

   split_list = list_splitter(opened)
   width = int(split_list [1])
   height = int(split_list [2])
   header(split_list,image)
   L = triples(split_list)
   color_adjust(L,row,col,rad,width,height,image)



if __name__ =="__main__":
   main()
