# Han Tran || CPE101-01,02 || Assignment 6
# blur_commandline - take in 2 command-line argv. The second argv is
#                    optional.  

import sys


def parse_commandline(argv):
   if len(argv) < 2:
      print >> sys.stderr, ' Usage: python blur.py <filename> \
                                          blurFactor'
      sys.exit()
   elif len(argv) < 3:
      blurFactor = 4
   elif len(argv) >= 3: 
      if not argv[2].isdigit():
         print >> sys.stderr, '-blurFactor must be of type int'
         sys.exit()
      else:
         blurFactor = argv[2]
   else:
      print >> sys.stderr, ' Usage: python blur.py <filename> \
                                          blurFactor'
      sys.exit()
   return blurFactor


