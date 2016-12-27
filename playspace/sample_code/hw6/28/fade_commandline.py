# Han Tran || CPE101-01,02 || Assignment 6
# fade_commandline 

import sys


def parse_commandline(argv):
   if len(argv) != 5:
      print >> sys.stderr, 'Usage: python puzzle.py <filename> row col radius'
      sys.exit()
   else:
      if not argv[2].isdigit() and argv[3].isdigit() and argv[4].isdigit():
         print >> sys.stderr, 'row col radius must be integer'
         sys.exit()
   return None 
