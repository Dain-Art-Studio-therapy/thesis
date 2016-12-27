#commandline
#define what raycaster uses for cast_all_rays

import data
import cast
import collisions
import utility
import vector_math
import sys


#for the main file defining spheres:
def open_file(file_name, mode):
  try:
    return open(file_name, mode)
  except IOError as e:
    print >> sys.stderr, 'Error: Cannot Open File'. format(file_name,
       e.strerror)
    exit(1)

def process_file(file):
  n = 0
  b = []
  for line in file:
    n = n+1
    try: b.append(process_line(line))
    except: print 'malformed sphere on line', n, '... skipping' 
  return b

def process_line(line):
  n = line.split( )
  if len(n) == 11: 
    try: return data.Sphere(data.Point(float(n[0]),float(n[1]),float(n[2])),
           float(n[3]),data.Color(float(n[4]),float(n[5]),float(n[6])),
           data.Finish(float(n[7]),float(n[8]),float(n[9]),float(n[10])))
    except: raise Exception
  else:
    raise Exception

def main(argv):
  if len(argv) < 2:
    print 'Error: usage: python ray_caster.py <filename> [-eye x y z]'
    print '	[-view min_x max_x min_y max_y width height]'
    print '	[-light x y z r g b] [-ambient r g b]'
  else:
    with open_file(argv[1], 'rb') as file:
      return process_file(file)



def is_float(value):
  try: float(value)
  except: return 'Fail'

def is_float3(v1, v2, v3):
  if (is_float(v1)=='Fail' or is_float(v2)=='Fail' or is_float(v3)=='Fail'):
   return 'Fail'

def is_float6(v1, v2, v3, v4, v5, v6):
  if (is_float3(v1, v2, v3) == 'Fail' or is_float3(v4, v5, v6) == 'Fail'):
    return 'Fail'

def cmdline_eye(cmdline):
  eye = data.Point(0.0, 0.0, -14.0)
  for i in range(len(cmdline)):
    if cmdline[i] == '-eye':
      if is_float3(cmdline[i+1], cmdline[i+2], cmdline[i+3]) == 'Fail':
        pass
      else:
	eye = data.Point(float(cmdline[i+1]), float(cmdline[i+2]),
                         float(cmdline[i+3]))
  return eye

def cmdline_view(argv):
  view = [-10, 10, -7.5, 7.5, 512, 384]
  for i in range(len(argv)):
    if argv[i] == '-view':
      if is_float6(argv[i+1], argv[i+2], argv[i+3], argv[i+4],
                   argv[i+5], argv[i+6]) == 'Fail':
        pass
      else: view = [int(argv[i+1]),int(argv[i+2]),int(argv[i+3]),
                    int(argv[i+4]),int(argv[i+5]),int(argv[i+6])]
  return view

def cmdline_light(argv):
  light = data.Light(data.Point(-100.0, 100.0, -100.0),
              data.Color(1.5, 1.5, 1.5))
  for i in range(len(argv)):
    if argv[i] == '-light':
      if is_float6(argv[i+1], argv[i+2], argv[i+3], argv[i+4],
                   argv[i+5], argv[i+6]) == 'Fail':
        pass
      else:
        light = data.Light(data.Point(float(argv[i+1]), float(argv[i+2]),
                          float(argv[i+3])), data.Color(float(argv[i+4]), 
                                     float(argv[i+5]), float(argv[i+6])))
  return light

def cmdline_ambient(argv):
  ambient = data.Color(1.0, 1.0, 1.0)
  for i in range(len(argv)):
    if argv[i] == '-ambient':
      if is_float3(argv[i+1], argv[i+2], argv[i+3]) == 'Fail':
          pass
      else:
        ambient = data.Color(float(argv[i+1]),
                             float(argv[i+2]), float(argv[i+3]))
  return ambient








if __name__ == '__main__':
   main(sys.argv)

