from sys import *



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
   print >> outfile, list[0]
   print >> outfile, list[1],list[2]
   print >> outfile, list[3]

def color_adj(list,outfile):
   for color in list:
      R = min(int(color[0])*3,255)
      R_solved = str(R)
      B = R_solved
      G = R_solved
      print >> outfile, R_solved, G, B

def main():
   try:
      opened = open(argv[1], "r")
      image = open("hidden.ppm", "w")
   except:
      print "Invalid File"

   split_list = list_splitter(opened)
   header(split_list,image)
   L = triples(split_list)
   color_adj(L,image)


if __name__ =="__main__":
   main()
   
