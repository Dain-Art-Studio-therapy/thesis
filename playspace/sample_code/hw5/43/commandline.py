from sys import *
import data


def flags():
   for index in argv:
      i = argv.index(index)      
      if "-eye" == index:
         try: 
            eye = data.Point(float(argv([i+1])),float(argv([i+2])),float(argv([i+3])))
         except: 
            eye = data.Point(0.0,0.0,-14.0)
      else:
         eye = data.Point(0.0,0.0,-14.0)


      if "-view" == index:
         try:
            view = [float(argv[i+1]),float(argv[i+2]),float(argv[i+2]),float(argv[i+3])] 
         except:
            view = [-10.0,10.0,-7.5,7.5,1024,768]
      else:
         view = [-10.0,10.0,-7.5,7.5,1024,768]


      if '-light' == index:
         try:
            light = data.Point(data.Point(float(argv[i+1]),float(argv[i+2]),float(argv[i+3])), data.Color(float(argv[i+4]),float(argv[i+5]),float(argv[i+6])))
         except:
            light = data.Light(data.Point(-100.0,100.0,-100.0), data.Color(1.5,1.5,1.5))        
      else:
         light = data.Light(data.Point(-100.0,100.0,-100.0), data.Color(1.5,1.5,1.5))
      

      if "-ambient" == index:
         try:
            ambient = data.Color(float(argv[i+1]), float(argv[i+2]), float(argv[1+3]))
         except:
            ambient = data.Color(1.0,1.0,1.0)
      else: 
         ambient = data.Color(1.0,1.0,1.0)


   return [view[0],view[1],view[2],view[3],view[4],view[5],eye,ambient,light]



