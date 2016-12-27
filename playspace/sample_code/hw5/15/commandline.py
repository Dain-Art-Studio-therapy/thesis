import sys
from data import *
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

 
def eye_flag(argv):
   try:
      flag_index = 0
      for i in range(2, len(argv)):
         if argv[i] == '-eye':
            flag_index = i
      if flag_index == 0:
         return Point(0.0, 0.0, -14.0)
      else:
         x = float(argv[flag_index + 1])
         y = float(argv[flag_index + 2])
         z = float(argv[flag_index + 3])
         return Point(x, y, z)
   except:
      return Point(0.0, 0.0, -14.0)

def view_flag(argv):
   try:
      flag_index = 0
      for i in range(2, len(argv)):
         if argv[i] == '-view':
            flag_index = i
      if flag_index == 0:
         return [-10.0, 10.0, -7.5, 7.5, 1024, 768]
      else:
         min_x = float(argv[flag_index + 1])
         max_x = float(argv[flag_index + 2])
         min_y = float(argv[flag_index + 3])
         max_y = float(argv[flag_index + 4])
         width = int(argv[flag_index + 5])
         height = int(argv[flag_index + 6])
         return [min_x, max_x, min_y, max_y, width, height]
   except:
      return [-10.0, 10.0, -7.5, 7.5, 1024, 768]

def light_flag(argv):
   try:
      flag_index = 0
      for i in range(2, len(argv)):
         if argv[i] == '-light':
            flag_index = i
      if flag_index == 0:
         return Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      else:
         x = float(argv[flag_index + 1])
         y = float(argv[flag_index + 2])
         z = float(argv[flag_index + 3])
         r = float(argv[flag_index + 4])
         g = float(argv[flag_index + 5])
         b = float(argv[flag_index + 6])
         return Light(Point(x, y, z), Color(r, g, b))
   except:
      return Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))

def ambient_flag(argv):
   try:
      flag_index = 0
      for i in range(2, len(argv)):
         if argv[i] == '-ambient':
            flag_index = i
      if flag_index == 0:
         return Color(1.0, 1.0, 1.0)
      else:
         r = float(argv[flag_index + 1])
         g = float(argv[flag_index + 2])
         b = float(argv[flag_index + 3])
         return Color(r, g, b)
   except:
      return Color(1.0, 1.0, 1.0)

if __name__=='__main__':
   main(sys.argv)
