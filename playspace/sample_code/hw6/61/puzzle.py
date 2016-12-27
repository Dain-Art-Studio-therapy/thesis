import sys
from sys import *

outfile = 'hidden.ppm' 


def open_file(fname): 
   try: 
      return open(fname)
   except: 
      print "cannot open file" 
      exit(1)

def open_out(fname, cmd): 
   return open(fname, cmd) 


def read_pixels(string):
   pixel_color_list = [] 
   for i in range(0,len(string),3): 
      pixel_color_list.append(string[i:i+3])
   return pixel_color_list


def test_for_int(string):
   l = []
   for i in string: 
      try:
         l.append(int(i))
      except: 
          pass
   return l
      
      

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
            number_line = pixels.split( )
         except: 
            print 'incomplete pixel' 
            exit(1)
            
         pixel_string =read_pixels(test_for_int(number_line))
         
         for pix in pixel_string: 
        
            out.write(str(min(255, pix[0] * 10)))
            out.write(' ')
            out.write(str(min(255, pix[0] * 10))) 
            out.write(' ') 
            out.write(str(min(255, pix[0] * 10)))
            out.write(' ')



if __name__ == '__main__': 
   main(sys.argv)
   
#define a pixel
#have the file go through and read each pixel (which is a group of three numbers) 
#print the pixels TO EACH lINE
#DO NOT INCLUDE FIRST 3 LINES 
 
 
 
'''
readline -> P3 
readline -> width height 
readline -> 255 

(this is the header) 

then it is Pixels = read() this reads what has not been read yet 

read.split 

replace all values with red value and mult by 10
max of 255
''' 
