import sys
import data
import cast

DEFAULT_EYE = data.Point(0.0, 0.0, -14.0)
DEFAULT_VIEW = (-10, 10, -7.5, 7.5, 1024, 768)
DEFAULT_LIGHT = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, \
                1.5, 1.5))
DEFAULT_AMB = data.Color(1.0, 1.0, 1.0)

def main(argv):
   validate_cmdline(argv)
   spheres = []
   with open_file(argv[1], 'rb') as f:
      spheres = process_file(f)
   flags = command_flags(argv)
   return [spheres, flags]

def validate_cmdline(argv):
   if len(argv) >= 2:
      pass
   else:
      print 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x \
      max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
      exit(1)

def open_file(name, mode):
   try: 
      return open(name, mode)
   except IOError as e:
      print >> sys.stderr, '{0}:{1}'.format(name, e.strerror)
      exit(1)

def process_file(f):
   spheres = []
   i = 1
   for line in f:
      input = line.split()
      if len(input) == 11:
         spheres.append(create_sphere(input, i))
         i += 1
      else:
         print 'malformed sphere on line', i, ' ... skipping'
         i += 1

   return spheres

def create_sphere(list, i):
   try:
      cen = data.Point(float(list[0]), float(list[1]), float(list[2]))
      rad = float(list[3])
      color = data.Color(float(list[4]), float(list[5]), float(list[6]))
      finish = data.Finish(float(list[7]), float(list[8]), float(list[9]), \
      float(list[10]))
      return data.Sphere(cen, rad, color, finish)
   except:
      print 'malformed sphere in line', i, '... skipping'

def command_flags(argv):
   if len(argv) == 2:
      return (DEFAULT_EYE, DEFAULT_VIEW, DEFAULT_LIGHT, DEFAULT_AMB)
   else:
      flags = [DEFAULT_EYE, DEFAULT_VIEW, DEFAULT_LIGHT, DEFAULT_AMB]
      for i in range(len(argv)):
         if argv[i] == '-eye':
            flags[0] = validate_eye(argv, i)

         elif argv[i] == '-view':
            flags[1] = validate_view(argv, i)

         elif argv[i] == '-light':
            flags[2] = validate_light(argv, i)

         elif argv[i] == '-ambient':
            flags[3] = validate_amb(argv, i)

      return (flags[0], flags[1], flags[2], flags[3])
 
def validate_eye(argv, i):
   try:
      return data.Point(float(argv[i+1]), float(argv[i+2]), float(argv[i+3]))
   except:
      return DEFAULT_EYE

def validate_view(argv, i):
   try:
      return (float(argv[i+1]), float(argv[i+2]), float(argv[i+3]), \
      float(argv[i+4]), float(argv[i+5]), float(argv[i+6]))
   except:
      return DEFAULT_VIEW

def validate_light(argv, i):
   try:
      return data.Light(data.Point(float(argv[i+1]), float(argv[i+2]), \
      float(argv[i+3])), data.Color(float(argv[i+4]), float(argv[i+5]), \
      float(argv[i+6])))
   except:
      return DEFAULT_LIGHT

def validate_amb(argv, i):
   try:
      return data.Color(float(argv[i+1]), float(argv[i+2]), float(argv[i+3]))
   except:
      return DEFAULT_AMB    

if __name__ == '__main__':
   main(sys.argv)
