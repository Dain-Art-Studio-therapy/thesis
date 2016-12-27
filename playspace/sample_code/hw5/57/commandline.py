from data import *

def float_default(string,default):
   try:
      return float(string)
   except:
      return default

def eye_argument(string):
   try:
      for i in range(len(string)):
         if string[i] == '-eye':
            x = float_default(string[i+1],0.0)
            y = float_default(string[i+2],0.0) 
            z = float_default(string[i+3],-14.0)
            return Point(x,y,z)
         else:
            return Point(0.0,0.0,-14.0) 
   except:
      return Point(0.0,0.0,-14.0)

def view_argument(string):
   try:
      for i in range(len(string)):
       	 if string[i] == '-view':
   	    min_x = float_default(string[i+1],-10)
   	    max_x = float_default(string[i+2],10)
       	    min_y = float_default(string[i+3],-7.5)
            max_y = float_default(string[i+4],7.5)
            width = float_default(string[i+5],1024)
            height = float_default(string[i+6],768)
       	    return (min_x,max_x,min_y,max_y,width,height)
         else:
            return (-10, 10, -7.5, 7.5, 1024, 768)
   except:
      return (-10,10,-7.5,7.5,1024,768)

def light_argument(string):
   try:
      for i in range(len(string)):
       	 if string[i] == '-light':
   	    x = float_default(string[i+1],-100.0)
   	    y = float_default(string[i+2],100.0)
       	    z = float_default(string[i+3],-100.0)
            r = float_default(string[i+4],1.5)
            g = float_default(string[i+5],1.5)
            b = float_default(string[i+6],1.5)
       	    return Light(Point(x,y,z),Color(r,g,b))
         else:
            return Light(Point(-100.0,100.0,-100.0),Color(1.5,1.5,1.5))
   except:
      return Light(Point(-100.0,100.0,-100.0),Color(1.5,1.5,1.5))

def ambient_argument(string):
   try:
      for i in range(len(string)):
       	 if string[i] == '-ambient':
   	    r = float_default(string[i+1],1.0)
   	    g = float_default(string[i+2],1.0)
       	    b = float_default(string[i+3],1.0)
       	    return Color(r,g,b)
         else:
            return Color(1.0,1.0,1.0)
   except:
      return Color(1.0,1.0,1.0)

