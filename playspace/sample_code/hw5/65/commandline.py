# Han Tran || CPE101-01,02 || Assignment 5
# commandine.py - contains implementations of command-line processing functions

import sys
import ray_caster


# values = [x, y, z, min_x, max_x, min_y, max_y, width, height, light_x,
#           light_y, light_z, light_r, light_g, light_b, ambient_r,
#           ambient_g, ambient_b]



def read_commandline(argv):
   if len(argv) < 2:
      print 'usage: python ray_caster.py <filename> [-eye x y z]' + \
            ' [-view min_x max_x min_y max_y width height]' + \
            ' [-light x y z r g b] [-ambient r g b]'
      exit

   else:
      index = 2
      values = [0.0, 0.0, -14.0, -10, 10, -7.5, 7.5, 1024, 768,                            -100.0, 100.0, -100.0, 1.5, 1.5, 1.5, 1.0, 1.0, 1.0]
      while index < len(argv):
         command = argv[index]
         # check flag -eye
         if command == '-eye':
            if (index + 3) >= len(argv):
               print 'Not enough arguments for [-eye x y z]'
               print 'Using default value for [-eye]'
               break
            if ray_caster.list_is_numeric(argv, index + 1, index + 3):   
               values[0:3] = map(float, argv[index+1:index+4])
            index = skip_to_flag(argv, index + 1, index + 3)
         
         # check flag -view
         elif command == '-view':
            if (index + 6) >= len(argv):
               print 'Not enough arguments for [-view min_x max_x \
                        [min_y max_y width height]'
               print 'Using default value for [-view]'
               break
            if ray_caster.list_is_numeric(argv, index + 1, index + 6):
               #values[3:9] = map(float, argv[index+1:index+7])
               values[3:7] = map(float, argv[index+1:index+5])
               values[7:9] = map(int, argv[index+5:index+7])
            index = skip_to_flag(argv, index + 1, index + 6)
         
         # check flag -light
         elif command == '-light': 
            if (index + 6) >= len(argv):
                print 'Not enough arguments for [-light x y z r g b]'
                print 'Using default value for [-light]'
                break
            if ray_caster.list_is_numeric(argv, index + 1, index + 6):
               values[9:15] = map(float, argv[index+1:index+7])
            index = skip_to_flag(argv, index + 1, index + 6)
         
         # check flag -ambient
         elif command == '-ambient':
            if (index + 3) >= len(argv):
                print 'Not enough arguments for [-ambient r g b]'
                print 'Using default value for [-ambient]'
                break
            if ray_caster.list_is_numeric(argv, index + 1, index + 3):
               values[15:18] = map(float, argv[index+1:index+4])
            index = skip_to_flag(argv, index + 1, index + 3)
      return values




# ----- DECOMPOSITION ----- #
def skip_to_flag(L, start, end):
   include = ['-eye', '-view', '-light', '-ambient']
   for i in range(start, end+1):
      if L[i] in include:
         print >> sys.stdout.write('Flag has insufficient arguments. Skip to the next flag \n')
         return i
   return end + 1

