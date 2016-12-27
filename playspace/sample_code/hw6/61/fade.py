import sys
from sys import *
import math

outfile = 'faded.ppm' 


def open_file(fname): 
   try: 
      return open(fname)
   except: 
      print "cannot open file" 
      exit(1)
      
      
def open_out(fname, cmd): 
   return open(fname, cmd) 

def scale(rad, dist):
   scaled =(rad - dist)/rad  
   #return max(scaled, 0.2)
   if scaled < 0.2:
      return 0.2
   return scaled
   
def find_loc(row, col, argv): 
   radx = float(argv[3])
   rady = float(argv[2])
   distance = ((rady - row)**2 + (radx - col)**2)**0.5
   return distance  

def make_grid(pixel_string, header2, argv): 
   header2.split()
   pixel_color_list = [] 
   for i in range(len(pixel_string)/3):
      row = i // int(header2[0]) 
      col = i % int(header2[0]) 
      scalar = scale(float(argv[4]), find_loc(row, col, argv))
      #print scalar
      try: 
      
         pixel_color_list.append((str(min(float(pixel_string[i * 3])*scalar, 255)) ,
                                 str(min(float(pixel_string[i * 3 + 1])*scalar, 255)),
                                 str(min(float(pixel_string[i * 3 + 2])*scalar, 255)) ))
                                 
        # print pixel_color_list[i][0], pixel_color_list[i][1], pixel_color_list[i][2]
      except: 
         print "can't do it, but oh how it tries"
         
   return pixel_color_list
    
          

 

def main(argv): 
   with open_file(argv[1]) as f:
      with open_out(outfile, 'w') as out: 
         header1 = f.readline()
         header2 = f.readline()
         header3 = f.readline() 
         
         out.write(header1) 
         out.write(header2) 
         out.write(header3)
         
         pixels = f.read()
         
         try: 
            pixel_string= pixels.split( )
         except: 
            print 'incomplete pixel' 
            exit(1)
         
         pixel_list = make_grid(pixel_string, header2, argv)    
         
         for pix in pixel_list: 
         
            out.write(pix[0])
            out.write(' ')
            out.write(pix[1])
            out.write(' ') 
            out.write(pix[2])
            out.write(' ')
#works with a small image not a large image... 


if __name__ == '__main__': 
   main(sys.argv)
   