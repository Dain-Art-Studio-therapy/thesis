import sys

def command_file():
   if (len(sys.argv) < 1):
      print "file name missing"
      sys.exit()
      
def groups_of_3(values):
   return [values[i:i+3] for i in range(0, len(values), 3)]
   
def main():
   command_file()
   inputfile = open(file, 'r')
   pixels = inputfile.readlines()  
   for i in pixels:
      values = i.split()
      outputfile.write(groups_of_3(values)) 

   inputfile.close()
   outputfile.close()

      
if __name__ == "__main__":
   main(sys.argv)