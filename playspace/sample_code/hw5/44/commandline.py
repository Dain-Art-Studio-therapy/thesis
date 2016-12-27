import cast
import sys
import data
   
EYE = data.Point(0.0, 0.0, -14.0)
MIN_X = -10
MIN_Y = -7.5
MAX_X = 10
MAX_Y = 7.5
WIDTH = 1024
HEIGHT = 768
LIGHT = data.Light(data.Point(-100.0,100.0,-100.0),data.Color(1.5,1.5,1.5))
AMB = data.Color(1.0,1.0,1.0)
   
# python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]
#4, 6
#7, 9
#44,10
#47,13
#77,16
#447,17
#774,20
#4477,24
POS_LENS = [2,6,9,10,13,16,17,20,24]

def cmd_processing(argv):
   
   eye = EYE
   min_x = MIN_X
   min_y = MIN_Y
   max_x = MAX_X
   max_y = MAX_Y
   width = WIDTH
   height = HEIGHT
   light = LIGHT
   amb = AMB
   length = len(argv)
   if not(length in POS_LENS) :
      print "Incorrect amount of arguments"
      print "usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]"
      sys.exit(0)
   else:
      i = 2
      while i < len(argv):
         if argv[i] == '-eye':
            eye = data.Point(float(argv[i+1]),float(argv[i+2]),float(argv[i+3]))
            i += 4
         elif argv[i] == '-view':
            min_x = float(argv[i+1])
            max_x = float(argv[i+2])
            min_y = float(argv[i+3])
            max_y = float(argv[i+4])
            width = float(argv[i+5])
            height = float(argv[i+6])
            i += 7
         elif argv[i] == '-light':
            light = data.Light(data.Point(float(argv[i+1]),
               float(argv[i+2]),float(argv[i+3])),
               data.Color(float(argv[i+4]),float(argv[i+5]),float(argv[i+6])))
            i += 7
         elif argv[i] == '-ambient':
            amb = data.Color(float(argv[i+1]),float(argv[i+2]),float(argv[i+3]))
            i += 4
         else:
            print 'Flags are not properly formatted'
            print 'Format: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
            sys.exit(0)
   return [argv[1],eye,min_x,max_x,min_y,max_y,width,height,light,amb]
#Finish implementing actual function call and input file
