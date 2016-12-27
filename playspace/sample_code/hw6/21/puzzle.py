import sys

OUTFILE_NAME = "hidden.ppm"
NUM_ARGS = 2
FILE_ARG_IDX = 1


def main(argv):
   if (len(argv) < NUM_ARGS):
      print >> sys.stderr, "file name missing"
      sys.exit(1)
      
   with open_file(argv[1]) as f:
      build_pixels((list_of_groups(argv, open_outfile(OUTFILE_NAME))),
        argv, open_outfile(OUTFILE_NAME))
      
def open_file(name):
   try:
      infile = open(name, "r")
      return infile
   except IOError as e:
      print >> sys.stderr, e
      sys.exit(1)

def open_outfile(name):
   try:
      outfile = open(name, "w")
      return outfile
   except IOError as e:
      print >> sys.stderr, e
      sys.exit(1)

def groups_of_3(list):
   newList = []
   for i in range(0, len(list), 3):
      newList.append(list[i : i + 3])
   return newList

def list_of_groups(in_file, out_file): 
   new_list = []  
   with open_file(in_file[1]) as f:
      for line in f:
         pix = line.split(' ')
         for e in int_list(pix):
            new_list.append(e)
      return groups_of_3(int_list(new_list))
   
def build_pixels(groups, in_file, out_file):
   with open_file(in_file[1]) as f:
      lines = f.read().splitlines()
      for i in range(len(lines)):
         if i < 3:
            out_file.write(lines[i])
            out_file.write('\n')
                  
   for e in groups:
      try:
         (out_file.write(str(cap_value(e[0]*10))), 
          out_file.write(' '), 
          out_file.write(str(cap_value(e[0]*10))), 
          out_file.write(' '), 
          out_file.write(str(cap_value(e[0]*10))),
          out_file.write('\n')) 
      except:
         pass  
    

def int_list(list):
   new = []
   for e in list:
      try:
         new.append(int(e))
      except:
         pass
   return new 
   
def cap_value(c):
   cap = 255
   if c > cap:
      return cap
   else:
      return c  
      
if __name__ == "__main__":
   main(sys.argv)
