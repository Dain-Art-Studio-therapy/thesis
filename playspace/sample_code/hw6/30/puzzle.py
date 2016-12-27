import sys

def open_infile(f):
   try:
      return open(f,'rb')
   except:
      print 'File cannot be opened.\nuasge: python puzzle.py <filename>'
      exit(1)

def groups_of_3(list):
   new_list = []
   for i in range(0,len(list),3):
      new_list.append(list[i:i+3])
   return new_list

def write_header(infile,outfile):
   header = [next(infile) for x in xrange(3)]
   for line in header:
      outfile.write(line + '\n')

def get_input_pixels(infile):
   pixels = []
   for i in xrange(3):
      infile.next()
   for line in infile:
      split = line.split()
      for e in split:
         pixels.append(e)
   return groups_of_3(pixels)

def write_pixels(infile,outfile):
   grouped_pixels = get_input_pixels(infile)
   for e in grouped_pixels:
      r = str(min(255,int(e[0])*10)) + ' '
      col = r * 3
      outfile.write(col)

def main(argv):
   infile = open_infile(argv[1])
   outfile = open('hidden.ppm','w')
   write_header(infile,outfile)
   write_pixels(infile,outfile)
   infile.close()
   outfile.close()

if __name__ == "__main__":
   main(sys.argv)
      
   
   
