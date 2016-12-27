import sys
import fade_help

def main(argv):
   if len(argv) != 5:
      print 'program must take four command-line arguments'
      exit()
   else:
      with fade_help.open_file(argv[1],"rb") as f:
         return fade_help.process_file(f,argv[2],argv[3],argv[4])   
      






if __name__ == '__main__':
   main(sys.argv)
