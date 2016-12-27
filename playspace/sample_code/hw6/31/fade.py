import sys
from fade_helper import *


def main(argv):
   arg_check(argv)
   img_out(argv[1], argv[2], argv[3], argv[4])

if __name__ == "__main__":
   main(sys.argv)

