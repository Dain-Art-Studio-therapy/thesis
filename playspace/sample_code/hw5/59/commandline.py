import sys
from data import *


# Point object
EYE_POINT = [0.0, 0.0, -14.0]

# [min_x, max_x, min_y, max_y, width, height]
VIEW = [-10, 10, -7.5, 7.5, 1024, 768]

# Light object
LIGHT = [-100.0, 100.0, -100.0, 1.5, 1.5, 1.5]

# Color object
AMBIENT = [1.0, 1.0, 1.0]


DEFAULT = [EYE_POINT, VIEW, LIGHT, AMBIENT]
FLAGS = ['-eye', '-view', '-light', '-ambient']


def open_file(name, mode):
   if name == None:
      print >> sys.stderr, 'usage: python ray_caster.py <filename>' + \
        '[-eye x y z] [-view min_x max_x min_y max_y width height]' + \
        '[-light x y z r g b] [-ambient r g b]'
      exit(1)

   try:
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0}: {1}'.format(name, e.strerror)
      exit(1)


def check_flags(argv):
   flag_values = DEFAULT

   for i in range(2, len(argv)):
      for j in range(len(FLAGS)):
         if argv[i] == FLAGS[j]:
            flag_values[j] = initialize_flag(argv, i + 1, DEFAULT[j])

   return flag_values   


def initialize_flag(argv, first, default):
   num_components = len(default)
   components = [0] * num_components
   last = first + num_components

   if last > len(argv):
      components = default
   else:
      for i in range(first, last):
         if argv[i] in FLAGS:
            return default

      for n in range(num_components):
         try:
            components[n] = float(argv[n + first])
         except:
            components[n] = default[n]

   return components
