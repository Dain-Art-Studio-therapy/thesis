import sys
from data import *

def comi_eye(argv, defaulteye):
   for i in range(len(argv)):
      if argv[i] == '-eye':
         try:
            x = float(argv[i+1])
            y = float(argv[i+2])
            z = float(argv[i+3])
            return Point(x,y,z)
         except:
            return defaulteye
   return defaulteye

def comi_view(argv,dminx,dmaxx,dminy,dmaxy,dwidth,dheight):
   for i in range(len(argv)):
      if argv[i] == '-view':
         try:
            minx = float(argv[i+1])
            maxx = float(argv[i+2])
            miny = float(argv[i+3])
            maxy = float(argv[i+4])
            width = int(argv[i+5])
            height = int(argv[i+6])
            return [minx,maxx,miny,maxy,width,height]
         except Exception as e:
            print>>sys.stderr, e
            return [dminx,dmaxx,dminy,dmaxy,dwidth,dheight]
   return [dminx,dmaxx,dminy,dmaxy,dwidth,dheight]

def comi_light(argv, defaultlight):
   for i in range(len(argv)):
      if argv[i] == '-light':
         try:
            x = float(argv[i+1])
            y = float(argv[i+2])
            z = float(argv[i+3])
            r = float(argv[i+4])
            g = float(argv[i+5])
            b = float(argv[i+6])
            return Light(Point(x,y,z),Color(r,g,b))
         except:
            return defaultlight
   return defaultlight

def comi_ambient(argv, defaultambient):
   for i in range(len(argv)):
      if argv[i] == '-ambient':
         try:
            r = float(argv[i+1])
            g = float(argv[i+2])
            b = float(argv[i+3])
            return Color(r,g,b)
         except:        
            return defaultambient
   return defaultambient
