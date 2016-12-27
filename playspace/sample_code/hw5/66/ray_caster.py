import sys
import commandline
import cast

def main(argv):
   s = commandline.readfile(argv)
   
   v = commandline.options(argv)

   cast.cast_all_rays(v[0][0], v[0][1], v[0][2], v[0][3], v[0][4], v[0][5], v[1], s, v[2], v[3])

if __name__ == '__main__':
   main(sys.argv)
