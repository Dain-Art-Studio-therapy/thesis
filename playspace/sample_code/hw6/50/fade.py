import sys
import math
def main(argv):
   try:
      infile = argv[1]  
      output = open('faded.ppm','w')
      row = int(argv[2])
      column = int(argv[3])
      radius = float(argv[4])
      width = Get_width(infile)
   except IOError:
      print "Invalid Input File"
      sys.exit()
   except IndexError:
      print "Usage: Python fade.py 'filename' 'row' 'column' 'radius'" 
      sys.exit()
   except ValueError:
      print 'row and column must be Int type values'
      sys.exit()

   Pixels_raw = make_pixel_list(infile,output)
   Pixels = groups_of_three(Pixels_raw)
   Fade_pixels(Pixels,radius,row,column,output,width)
         
            
 


def groups_of_three(L):
   q = []
   if len(L)%3 == 0:
      l = len(L)/3
      for i in range(l):
         z = []
         for k in range((i*3),(i*3)+3):
             z.append(L[k])
         q.append(z)
   else:
      l = len(L)/3 +1
      
      for i in range(l):
         z = []
         if i < len(L)/3:
            for k in range((i*3),(i*3)+3):
                z.append(L[k])
         else:
            for k in range((i*3),(i*3)+len(L)%3):
                z.append(L[k])
         q.append(z)
   return q

def make_pixel_list(filein,output):
      Pixels = []
      with open(filein) as puzzle:
         currentline = 0
         for line in puzzle:
            if currentline <= 2:
               print >> output, line
            else:
               L = line.split()
               for characters in L:
                  if characters.isdigit():
                     Pixels.append(characters)
            currentline += 1
      return Pixels      

def Fade_pixels(Pixels,radius,row,column,output,width):
   for pixel in range(len(Pixels)):
      y = pixel/width
      x = pixel - (y*width)
      scalar = max(.2,Scalar(radius,row,column,x,y))
      Pixels[pixel][0] = min(255,scalar*float(Pixels[pixel][0]))
      Pixels[pixel][1] = min(255,scalar*float(Pixels[pixel][1]))
      Pixels[pixel][2] = min(255,scalar*float(Pixels[pixel][2]))   
      print >> output, int(Pixels[pixel][0]),int(Pixels[pixel][1]),int(Pixels[pixel][2])

def Scalar(radius,row,column,x,y):
   return ((radius-(Distance(column,row,x,y)))/radius)

def Distance(x1,y1,x2,y2):
   return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

def Get_width(infile):
   with open(infile,'r') as source:
      source.readline()
      width = int((source.readline().split())[0])
   return width


if __name__ == '__main__':
   main(sys.argv)
