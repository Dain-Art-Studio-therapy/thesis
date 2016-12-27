import sys

def main():

   try:
      input = open(sys.argv[1], 'r')
   except:
      print "usage: python puzzle.py <filename>"
      exit()
 
   process_puzzle()

def groups_of_3(list):

   # Groups pixel values
   n = 0
   new_list = []

   while n < len(list):
      new_list.append(list[n:n+3])
      n += 3
   return new_list


def process_puzzle():

   output = open("hidden.ppm", 'w')
   input = open(sys.argv[1], 'r')
   
   header_line = 0
   pix_list = []

   # Regroups pixel values
   for line in input:
      if header_line < 3:
         output.write(line,)
         header_line += 1
      else:
         all_lines = line.split()
         for values in all_lines: 
            pix_list.append(values)

   grouped_values = groups_of_3(pix_list)

   # Converts each pixel
   for pixel in grouped_values:
      r = int(pixel[0]) * 10
      if r > 255:
         r = 255
      g = r
      b = r
      output.write(str(r) + ' ' +
                   str(g) + ' ' +
                   str(b) + '\n') 
 
   
if __name__ == "__main__":
   main()
           
