import sys
def main(argv):
   output = open('hidden.ppm','w')
   try:
      Pixels_raw = make_pixel_list(argv[1],output)
      Pixels = groups_of_three(Pixels_raw)
      Solve_pixels(Pixels,output)
         
            
   except IOError:
      print "Invalid Input"
   except IndexError:
      print "Usage: Python puzzle.py 'filename'"  


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

def Solve_pixels(Pixels,output):
   for pixel in Pixels:
      pixel[0] = min(255,10*int(pixel[0])) 
      print >> output, pixel[0],pixel[0],pixel[0]

if __name__ == '__main__':
   main(sys.argv)
