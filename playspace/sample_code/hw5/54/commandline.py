from data import *

# Project Defaults 
dEye = Point(0.0, 0.0, -14.0) 
dView = (-10.0, 10.0, -7.5, 7.5, 1024, 768)# view: minX, maxX, minY, maxY, w, h
dLight = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5)) 
dAmb = Color(1.0, 1.0, 1.0) 


def process_file(f):
   sphere_list = []
   i = 1
   for line in f:
      vals = sanitize_vals(line.split())
      if vals is False:
         print 'Malformed Sphere on line' , i
         i += 1
      else: 
         sphere_list.append(create_sphere_using(float_all(vals)))
         i += 1
   return sphere_list


def sanitize_vals(vals):
   if len(vals) != 11: 
      return False
   for i in range(len(vals)):
      f = check_float(vals[i])
      if f is False:
         return False
      elif 4 <= i < 10:
         if 0 <= float(vals[i]) <= 1 is False:
             return False
         if float(vals[10]) <= 0:
             return False
   return vals

def float_all(vals):
   stuff = []
   for v in vals:
      stuff.append(float(v))
   return stuff

def create_sphere_using(v):
   # input if correctly sanitized would be x y z radi r g b amb diff spec rghns
   return Sphere(Point(v[0], v[1], v[2]), v[3], Color(v[4],v[5],v[6]), 
      Finish(v[7], v[8], v[9], v[10]))


def process_flags(argv):
   cast_args = [dEye, dView, dLight, dAmb]
   argLen = len(argv)
   if argLen > 2:
      for i in range(1, argLen):
         if argv[i] == '-eye':
            cast_args[0] = process_eye_flag(argv, argLen, i)
         if argv[i] == '-view':
            cast_args[1] = process_view_flag(argv, argLen, i)
         if argv[i] == '-light':
            cast_args[2] = process_light_flag(argv, argLen, i)
         if argv[i] == '-ambient':
            cast_args[3] = process_amb_flag(argv, argLen, i)
   return cast_args


def check_float(f):
   try:
      return float(f)
   except:
      return False


def float_default(s, f):
   try: 
      return float(s)
   except: 
      return f
      print 'hmmm, one of the supplied values was not a float, but this is a'
      print 'very forgiving program so it will still run! However, be sure to'
      print 'check your commandline arguments!'


def all_true_huh(arb): # takes in a collection of values and sees if all of 
   for v in arb:       # them are true. returns appropriate result
      if v is False:
         return False
   return True


# p_e_f takes in the arguments and the index of where the eye flag was found
# also takes in argLen so that it doesn't have to recalculate it. 
# returns results as a point. defaults to default point 
# sole purpose of these process functions is decomposition
def process_eye_flag(argv, argLen, i):
   if argLen - i >= 4:
      x = float_default(argv[i+1], dEye.x)
      y = float_default(argv[i+2], dEye.y)
      z = float_default(argv[i+3], dEye.z)
      return Point(x,y,z)
   else:
      print_error('eye')


def process_view_flag(argv, argLen, i):
   if argLen - i >= 7:
      minX = float_default(argv[i+1], dView[0])
      maxX = float_default(argv[i+2], dView[1])
      minY = float_default(argv[i+3], dView[2])
      maxY = float_default(argv[i+4], dView[3])
      w = float_default(argv[i+5], dView[4])
      h = float_default(argv[i+6], dView[5])
      return (minX, maxX, minY, maxY, w, h)
   else:
      print_error('view')


def process_light_flag(argv, argLen, i):
   if argLen - i >= 7:
      x = float_default(argv[i+1], dLight.pt.x)
      y = float_default(argv[i+2], dLight.pt.y)
      z = float_default(argv[i+3], dLight.pt.z)
      r = float_default(argv[i+4], dLight.color.r)
      g = float_default(argv[i+5], dLight.color.g)
      b = float_default(argv[i+6], dLight.color.b)
      return Light(Point(x,y,z), Color(r,g,b))
   else: 
      print_error('light')


def process_amb_flag(argv, argLen, i):
   if argLen - i >= 4:
      r = float_default(argv[i+1], dAmb.r)
      g = float_default(argv[i+2], dAmb.g)
      b = float_default(argv[i+3], dAmb.b)
      return Color(r, g, b)
   else:
      print_error('ambient')


def print_error(s):
   print 'You have made an error in the number of arguments supplied. '
   print 'Please double check your arguments after the', s, 'flag'
   print 'Thank you.'
   print 'Now exiting.'
   exit(1)
