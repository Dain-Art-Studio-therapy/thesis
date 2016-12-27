import sys

def main(argv):
   if len(argv) != 2:
      print 'Not Enough/Too Many Command Arguments'
      exit(1)

   infile = open_file(argv[1], 'r')
   outfile = open_file('hidden.ppm', 'w')
   old_pixels = read_file(infile)
   header = old_pixels[0 : 4]
   pixel_list = old_pixels[4 : len(old_pixels)]
   old_pixels_list = groups_of_three(pixel_list)
   new_pixels = change_pixels(old_pixels_list)

   header_writer(header, outfile)
   pixel_writer(new_pixels, outfile)

   infile.close()
   outfile.close()

def open_file(name, method):
   try:
      return open(name, method)

   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

def read_file(infile):
   old_pixels = []

   for line in infile:
      line_string = line.split()
      for n in line_string:
         old_pixels.append(n)
   return old_pixels
         
def change_pixels(list):
   new_pixels = []
   for n in list:
      try:
         old_red = float(n[0])
      except IOError as e:
         print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
         exit(1)

      new_red = min(255, int(old_red * 10))
      new_pixels.append([new_red]*3)
   return new_pixels

def pixel_writer(pixel_list, outfile):
   for p in pixel_list:
      for n in p:
         outfile.write(str(n) + '\n')

def header_writer(list, file):
   file.write(list[0] + '\n')
   file.write(list[1] + ' ' + list[2] + '\n')
   file.write(list[2] + '\n')

def groups_of_three(list):
   newList = []

   for i in range(0, len(list), 3):
      newList.append(list[i : i + 3])
   return newList

if __name__ == '__main__':
   main(sys.argv)
