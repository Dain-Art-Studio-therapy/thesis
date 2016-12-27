import sys

def main(argv):
   fin= []
   try:
      open(argv[1], "r")
   except:
      print 'file does not exist'
      sys.exit()
   with open(argv[1], "r") as lf:
      listfile = []
      lf.readline()
      w_h= lf.readline()
      w_h= str.split(w_h)
      lf.readline()
      for line in lf:
         line=line.strip()
         listfile.append(line)
      groupedfile= groups_of_3(listfile)
      #print groupedfile
      for i in range(1, len(groupedfile)-1):
         #print groupedfile[i][0]
         result= pixel_manipulation(groupedfile[i])
         #print result
         fin.append(result)
      write_to_file(w_h, fin)
      
        
   

def write_to_file(w_h, pixel):
   with open('image.ppm', 'w') as file:
      file.write('P3\n'+str(w_h[0])+' '+str(w_h[1])+'\n255\n')
      file.write(''.join(pixel))

def groups_of_3(numlist):
 newlist =[ numlist[i:i+3] for i in range(0, len(numlist), 3)]
 return newlist

def pixel_manipulation(pixellist):
   #print pixellist
   r= int(pixellist[0])*10
   if r> 255:
      r= 255
   g=r
   b=r
   return str(r)+' '+str(g)+' '+str(b)+'\n'

if __name__=='__main__':
   main(sys.argv)