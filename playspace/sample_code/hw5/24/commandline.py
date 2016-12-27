import data
import sys

default_eye_point = data.Point(0.0, 0.0, -14.0)
default_view = [-10.0, 10.0, -7.5, 7.5, 1024, 768]
default_light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
default_ambient_light = data.Color(1.0, 1.0, 1.0)

def arguments(argv):
   try:
      exist = does_it_exist(argv)
      arguments = default_or_not(exist, argv)
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)
      
   return arguments

def does_it_exist(argv):
   it_exists = [-1, -1, -1, -1]
   eye_counter = 0
   view_counter = 0
   light_counter = 0
   ambient_counter = 0

   for i in range(len(argv)):
      if argv[i] == '-eye': 
         if eye_counter == 0:
            it_exists[0] = i
            eye_counter = 1
         elif eye_counter == 1:
            print 'Too Many Flags of the Same Kind'
            exit(1)

      elif argv[i] == '-view':
         if view_counter == 0:
            it_exists[1] = i
            view_counter = 1
         elif view_counter == 1:
            print 'Too Many Flags of the Same Kind'
            exit(1)

      elif argv[i] == '-light':
         if light_counter == 0:
            it_exists[2] = i
            light_counter = 1
         elif light_counter == 1:
            print 'Too Many Flags of the Same Kind'
            exit(1)

      elif argv[i] == '-ambient':
         if ambient_counter == 0:
            it_exists[3] = i
            ambient_counter = 1
         elif ambient_counter == 1:
            print 'Too Many Flags of the Same Kind'
            exit(1)

   return it_exists

def default_or_not(exist_list, argv):
   arguments = []
   try:
      if exist_list[0] != -1:
         arguments.append(make_eye_point(exist_list[0], argv))
      else:
         arguments.append(default_eye_point)

      if exist_list[1] != -1:
         arguments.append(make_view(exist_list[1], argv))
      else:
         arguments.append(default_view)

      if exist_list[2] != -1:
         arguments.append(make_light(exist_list[2], argv))

      else:
         arguments.append(default_light)

      if exist_list[3] != -1:
         arguments.append(make_ambient_light(exist_list[3], argv))
      else:
         arguments.append(default_ambient_light)
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

   return arguments

def make_eye_point(index, argv):
   try:
      eye_point = data.Point(float(argv[index + 1]), float(argv[index + 2]), float(argv[index + 3]))
      return eye_point
   except IOError in e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

def make_view(index, argv):
   try:
      view_str = [argv[index + 1], argv[index + 2], argv[index + 3], argv[index + 4], 0, 0]
      view_float = list_str_to_float(view_str)
      view_float[4] = int(argv[index + 5])
      view_float[5] = int(argv[index + 6])
      return view_float
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

def make_light(index, argv):
   try:
      light_point = data.Point(float(argv[index + 1]), float(argv[index + 2]), float(argv[index + 3]))
      light_color = data.Color(float(argv[index + 4]), float(argv[index + 5]), float(argv[index + 6]))
      light = data.Light(light_point, light_color)
      return light
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

def make_ambient_light(index, argv):
   try:
      ambient_light = data.Color(float(argv[index + 1]), float(argv[index + 2]), float(argv[index + 3]))
      return ambient_light
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit

def list_str_to_float(list):
   float_list = []
   for n in list:
      try:
         float_list.append(float(n))
      except IOError as e:
         print IOError, e
   return float_list

def usage(argv):
   exists = does_it_exist(argv)
   try: 
      if exists == [-1, -1, -1, -1]:
         return 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
      else:
         return ''
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)
