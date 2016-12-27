import sys
import puzzle_help

def main(argv):
   if len(argv) != 2:
      print 'program must take single command-line argument'
      exit()
   else:
      with puzzle_help.open_file(argv[1],"rb") as f:
         return puzzle_help.process_file(f)   
      






if __name__ == '__main__':
   main(sys.argv)
