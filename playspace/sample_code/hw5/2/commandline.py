from data import *

def process_file(f):
   spheres = []
   line_index = 0
   for line in f:
      line_index += 1
      s = line.split()
      try:
         spheres.append(Sphere(Point(float(s[0]), float(s[1]), float(s[2])), 
         float(s[3]), Color(float(s[4]), float(s[5]), float(s[6])),
         Finish(float(s[7]), float(s[8]), float(s[9]), float(s[10]))))
      except IndexError:
         print 'malformed sphere on line ' + str(line_index) + ' ...skipping'
      except ValueError:              
         print 'malformed sphere on line ' + str(line_index) + ' ...skipping'
      except len(s) != 11:              
         print 'malformed sphere on line ' + str(line_index) + ' ...skipping'

   return spheres

def open_file(name, mode):
   try:
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0}:{1}'.format(name, e.strerror)
      exit(1)

def index_of_eye(list):
   index = 0
   for i in range(len(list)):
      if list[i] == '-eye':
         index = i
   return index

def index_of_view(list):
   index = 0
   for i in range(len(list)):
      if list[i] == '-view':
         index = i
   return index

def index_of_light(list):
   index = 0
   for i in range(len(list)):
      if list[i] == '-light':
         index = i
   return index

def index_of_ambient(list):
   index = 0
   for i in range(len(list)):
      if list[i] == '-ambient':
         index = i
   return index

