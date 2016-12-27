import sys
import cast
import collisions
import data
import vector_math
import math
# x y z radius r g b ambient diffuse specular roughness

DEFAULT_EYE = data.Point(0.0,0.0,-14.0)
DEFAULT_VIEW = [-10.0, 10.0, -7.5, 7.5, 1024, 768]
DEFAULT_LIGHT = data.Light(data.Point(-100.0,100.0,-100.0), 
                           data.Color(1.5,1.5,1.5))
DEFAULT_AMBIENT = data.Color(1.0,1.0,1.0)


def get_eye(argv):
   try:
      if '-eye' not in argv:
         return DEFAULT_EYE
      else:
         for i in range(2, len(argv)):
            if argv[i] == '-eye':
               x = float(argv[i+1])
               y = float(argv[i+2])
               z = float(argv[i+3])
               eye = data.Point(x,y,z)
               return eye
   except:
      return DEFAULT_EYE

def get_view(argv):
   try:
      if '-view' not in argv:
         return DEFAULT_VIEW
      else:
         for i in range(2, len(argv)):
            if argv[i] == '-view':
               min_x = float(argv[i+1])
               max_x = float(argv[i+2])
               min_y = float(argv[i+3])
               max_y = float(argv[i+4])
               width = float(argv[i+5])
               height = float(arg[i+6])
               view = [min_x, max_x, min_y, max_y, width, height]
               return view
   except:
      return DEFAULT_VIEW

def get_light(argv):
   try:
      if '-light' not in argv:
         return DEFAULT_LIGHT
      else:
         for i in range(2, len(argv)):
            if argv[i] == '-light':
               light_pos = data.Point(float(argv[i+1]),float(argv[i+2]),float(argv[i+3]))
               light_color = data.Color(float(argv[i+4]),float(argv[i+5]),float(argv[i+6]))
               light = data.Light(light_pos, light_color)
               return light      
   except:
      return DEFAULT_LIGHT


def get_ambient(argv):
   try:
      if '-ambient' not in argv:
         return DEFAULT_AMBIENT
      else:         
         for i in range(2, len(argv)):
            if argv[i] == '-ambient':
               ambient_light = data.Color(float(argv[i+1]),float(argv[i+2]),float(argv[i+3]))
               return ambient_light
   except:
      return DEFAULT_AMBIENT




if __name__ == '__main__':
   main(sys.argv)



