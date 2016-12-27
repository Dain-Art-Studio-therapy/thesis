import sys
import math


def main(argv):
   fin= []
   len_check(argv, 1)
   with open(argv[1], "r") as lf:
      listfile = []
      res= p3_spec(lf)
      width= int(res[0]) 
      height= int(res[1])
      reach= correct_arg(argv)
      for line in lf:
         line=line.strip()
         listfile.append(line)
      pixelsrgb= groups_of_3(listfile)
      num_of_pixels=len(pixelsrgb)
      grid= d2_grid(pixelsrgb, width)
      fin= color_loop(grid, reach, height, width)
      write_to_file(width, height, fin)
      

def d2_grid(pixels, width):
   y=[]
   x=[]
   for i in range(len(pixels)):
      x.append(pixels[i])
      if (i+1)%width==0:
         y.append(x)
         x =[]
   return y

def color_loop(grid, reach, height, width):
   newpixels= []
   for y in range(len(grid)):
      for x in range(len(grid[y])):
         avgcolor= average(grid, reach, y, x, height, width)
         newpixels.append(avgcolor)
   return newpixels

def average(grid, reach, y, x, height, width):
   localpixels=[]
   for ly in range(y-reach, y+reach+1):
      if ly >= 0 and ly <= height-1:
         for lx in range(x-reach, x+reach+1):
            if lx >= 0 and lx < width:
               #print ly, lx 
               localpixels.append(grid[ly][lx])
          
   return average_math(localpixels)

#test2= average([[[0,0,0],[1,1,1], [2,2,2]], [[3,3,3], [4,4,4], [5,5,5]], [[6,6,6], [7,7,7], [8,8,8]]], 1, 0, 0, 3, 3)       
#print test2

def average_math(localpixels):
   r =0
   g =0
   b =0
   length= len(localpixels)
   for n in range(length):
      r+= float(localpixels[n][0])
      g+= float(localpixels[n][1])
      b+= float(localpixels[n][2])

   r= r/float(length) 
   g= g/float(length) 
   b= b/float(length) 
   return str(int(r))+' '+str(int(g))+' '+str(int(b))+'\n'
   

   

def len_check(argv, argnums):
   if (len(argv) <= argnums):
      print >> sys.stderr, "file name missing"
      sys.exit(1)

def correct_arg(argv):
      try:
         radius= int(argv[2])
         return radius
      except:
         print 'Error: incorrect/missing values for reach'
         return 4
            
def p3_spec(rfile):
   rfile.readline()
   w_h= rfile.readline()
   w_h= str.split(w_h)
   return w_h
      

def write_to_file(width, height, pixel):
   with open('image.ppm', 'w') as file:
      file.write('P3\n'+str(width)+' '+str(height)+'\n255\n')
      file.write(''.join(pixel))

def groups_of_3(numlist):
 newlist =[ numlist[i:i+3] for i in range(1, len(numlist), 3)]
 return newlist

if __name__== '__main__':
   main(sys.argv)