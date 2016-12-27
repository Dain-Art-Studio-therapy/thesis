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
      rcr= correct_arg(argv)
      for line in lf:
         line=line.strip()
         listfile.append(line)
      groupedfile= groups_of_3(listfile)
      #print groupedfile
      num_of_pixels= range(len(groupedfile))
      currentrow= 0
      currentcol= 0
      for i in num_of_pixels:
         currentcol= (i%width)
         currentrow= ((i-currentcol)/width)
         #print currentrow, currentcol
         #result = str(currentrow)+' '+str(currentcol)+'\n'
         dis= distance_to_pixel(rcr[0], rcr[1], currentrow, currentcol)
         if dis < 0:
            print "ERROR"
         result= pixel_manipulation(groupedfile[i], rcr[2], dis)
         #print result
         fin.append(result)
      write_to_file(width, height, fin)
      
        
def len_check(argv, argnums):
   if (len(argv) <= argnums):
      print >> sys.stderr, "file name missing"
      sys.exit(1)

def correct_arg(argv):
      try:
         row= float(argv[2])
         col= float(argv[3])
         radius= int(argv[4])
         return [row, col, radius]
      except:
         print 'Error: incorrect/missing values for: row col radius'
         sys.exit()
            
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

def distance_to_pixel(row, col, cury, curx):
   x = curx - col
   y = cury - row
   return math.sqrt((x**2) + (y**2))
   #return str(math.sqrt((x**2) + (y**2)))+'\n'
   

def pixel_manipulation(rgb, radius, distance):
   scalar= float((radius - distance)/ radius)
   #print scalar
   if scalar < 0.2:
      scalar= 0.2
      r= float(rgb[0]) * scalar
      g= float(rgb[1]) * scalar
      b= float(rgb[2]) * scalar
   else:
      r= int(rgb[0]) * scalar
      g= int(rgb[1]) * scalar
      b= int(rgb[2]) * scalar
   return str(int(r))+' '+str(int(g))+' '+str(int(b))+'\n'

if __name__=='__main__':
   main(sys.argv)