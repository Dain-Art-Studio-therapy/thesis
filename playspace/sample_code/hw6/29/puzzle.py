import sys
import groups

OUTFILE = 'hidden.ppm'

def main(argv):
   if len(argv) < 2:
      print 'no file provided'
      sys.exit(1)

   infile = openfile(argv[1], 'r')
   outfile = openfile(OUTFILE, 'w')
   
   read = infile.read()
   nums = read.split()
   
   print_head(nums, outfile)
   print_body(nums, outfile)

   infile.close()
   outfile.close()      

def openfile(name, mode):
   try:
      return open(name, mode)
   except:
      print 'cannot open file'
      sys.exit(1)

def print_head(words, outfile):
   print >> outfile, 'P3'
   print >> outfile, words[1], words[2]
   print >> outfile, 255

def print_body(nums, outfile):
   num_list = []
   for i, e in enumerate(nums):
      if i <= 3:
         pass
      else:
         num_list.append(float(e))

   list_of_nums = groups.groups_of_3(num_list)
   solve_puzzle_1(list_of_nums, outfile)

def solve_puzzle_1(l1, outfile):
   for e in l1:
      value = int(min(e[0]*10, 255))
      print >> outfile, value, value, value

if __name__ == "__main__":
   main(sys.argv)
