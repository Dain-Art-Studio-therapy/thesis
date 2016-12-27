import sys
import math
def main(argv):
   try:
      infile = argv[1]  
      output = open('blurred.ppm','w')
      try:
         blur = int(argv[2])
      except IndexError:
         blur = 4
      except ValueError:
         print "blur factor must be Int type value"
         sys.exit()
      width = Get_width(infile)
   except IOError:
      print "Invalid Input File"
      sys.exit()
   except IndexError:
      print "Usage: Python fade.py [blur factor]" 
      sys.exit()
   Pixels_raw = make_pixel_list(infile,output)
   Pixels = groups_of_three(Pixels_raw)
   blur_pixels(Pixels,blur,width,output)
   output.close()
            
 


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

def blur_pixels(Pixels,blur,width,output):
   for pixel in range(len(Pixels)):
      Neighbors = find_neighbors(Pixels,pixel,blur,width)
      r = average_color(Neighbors,0)
      g = average_color(Neighbors,1)
      b = average_color(Neighbors,2)
  
      print >> output, int(r),int(g),int(b)

def Get_width(infile):
   with open(infile,'r') as source:
      source.readline()
      width = int((source.readline().split())[0])
   return width

def locations(Pixels,width):
   Locations = []
   for i in range(len(Pixels)):
      y = i/width
      x = i - (y*width)
      Locations.append((x,y))
   return Locations

def find_neighbors(Pixels,pixel,blur,width):
   Neighbors = []
   y = pixel/width
   x = pixel - (y*width)
   for y2 in range(y-(blur),y+(blur+1)):
      for x2 in range(x-blur,x+(blur+1)):
         index = y2*width + x2
         if x2>=0 and y2>=0 and x2<width:
            try:
               Neighbors.append(Pixels[index])
            except IndexError:
               pass
   return Neighbors
   

def average_color(Pixels,index):
   total = 0
   for pixel in Pixels:
      total += int(pixel[index])
   return int(total)/len(Pixels)


if __name__ == '__main__':
   main(sys.argv)
