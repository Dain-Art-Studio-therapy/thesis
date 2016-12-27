import sys
import blur_help

def main(argv):
   if len(argv) == 3:
      with blur_help.open_file(argv[1],"rb") as f:
         return blur_help.process_file(f,argv[2])   
   elif len(argv) == 2:
      with blur_help.open_file(argv[1],'rb') as f:
         return blur_help.process_file(f,4)   
   else:
      print 'program must take one or two command-line arguments'
      exit()






if __name__ == '__main__':
   main(sys.argv)
