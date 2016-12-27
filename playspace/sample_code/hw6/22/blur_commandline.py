import sys

NUM_ARGS = 2
OPTIONAL_IDX = 2
DEFAULT_BLUR = 4


def check_args(argv):
   if len(argv) < NUM_ARGS:
      print >> sys.stderr, 'usage: python blur.py <filename> ' + \
         '[optional blur]'
      sys.exit(1)

   return None


def open_file(name, mode):
   try:
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0}: {1}'.format(name, e.strerror)
      sys.exit(1)


def init_blur(argv):
   if len(argv) > NUM_ARGS:
      try:
         return int(argv[OPTIONAL_IDX])
      except:
         print >> sys.stderr, 'Invalid blur value; using default'

   return DEFAULT_BLUR
