#Command-line functions
import sys


def open_file(file, mode):
   try:
      return open(file, mode)
   except IOError as e:
      print >> sys.stderr, "{0};{1}".format(file, e.strerror)
      exit(1)





