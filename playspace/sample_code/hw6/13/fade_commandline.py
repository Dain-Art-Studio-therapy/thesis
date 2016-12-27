#Command line functions
import sys


def open_file(file, mode):
   try:
      return open(file, mode)
   except IOError as e:
      print >> sys.stderr, "{0}:{1}".format(file, e.strerror)
      exit(1)

def set_pos_rad(argv):
   list = []
   list.append(int(argv[2]))
   list.append(int(argv[3]))
   list.append(float(argv[4]))

   return list

def set_width_height(list):
   p_width_height = []

   p_width_height.append(list[0][0])
   p_width_height.append(list[0][1])
   p_width_height.append(list[0][2])

   return p_width_height


