import sys

NUM_ARGS = 2
MIN_ARGS = 5
ROW_IDX = 2
COL_IDX = 3
RADIUS_IDX = 4


def check_args(argv):
   if len(argv) < NUM_ARGS:
      print >> sys.stderr, 'usage: python fade.py <filename> ' + \
         '[row] [col] [radius]'
      sys.exit(1)


def open_file(name, mode):
   try:
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0}: {1}'.format(name, e.strerror)
      sys.exit(1)


def init_arguments(argv):
   if len(argv) < MIN_ARGS:
      print >> sys.stderr, 'Missing input'
      sys.exit(1)

   try:
      return [int(argv[ROW_IDX]), int(argv[COL_IDX]), int(argv[RADIUS_IDX])]
   except:
      print >> sys.stderr, 'Invalid input'
      sys.exit(1)

   return None
