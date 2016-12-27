import math
import cast
import data
import collisions
import vector_math
import sys

def open_file():
   try:
      f = open(sys.argv[1], 'rb')
      return f
   except:
      print 'Error: file doesn\'t exist'
      exit()
  
   
def get_sphere(f):
   sphere_list = []
   for line in f:  
      try: 
         arg = line.split()
         center = data.Point(float(arg[0]), float(arg[1]), float(arg[2]))
         radius = float(arg[3])
         color = data.Color(float(arg[4]), float(arg[5]), float(arg[6]))
         finish = data.Finish(float(arg[7]), float(arg[8]), float(arg[9]), float(arg[10]))
         isphere = data.Sphere(center, radius, color, finish)
         sphere_list.append(isphere)
      except:
         print 'Malformed sphere on line... skipping'
         continue
   return sphere_list
          


def check_eye():

   arg = sys.argv

   for i in range(len(arg)):
      if arg[i] == '-eye':
         
         try:
   
            return data.Point(float(arg[i+1]), float(arg[i+2]), float(arg[i+3]))
   
         except:
            return data.Point(0.0, 0.0, -14.0)
   
   return data.Point(0.0, 0.0, -14.0)   

   
def check_view():

   view_list = []
   arg = sys.argv
  
   for i in range(len(arg)):
      
      if arg[i] == '-view':
         try:
            return [float(arg[i+1]), float(arg[i+2]), float(arg[i+3]), float(arg[i+4]), float(arg[i+5]), float(arg[i+6])]
               
         except:
            return [-10.0, 10.0, -7.5, 7.5, 1024, 768]

   return [-10.0, 10.0, -7.5, 7.5, 1024, 768]
   

def check_light():
   arg = sys.argv

   for i in range(len(arg)):
      if arg[i] == '-light':
         try:
               
            lightpoint = data.Point(float(arg[i+1]), float(arg[i+2]), float(arg[i+3]))
            lightcolor = data.Color(float(arg[i+4]), float(arg[i+5]), float(arg[i+6]))
            return data.Light(lightpoint, lightcolor)
        
         except:
            return data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
   return data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))


def check_ambience():

   arg = sys.argv

   for i in range(len(arg)):
      if arg[i] == '-ambience':
         try:
            return data.Color(float(arg[i+1]), float(arg[i+2]), float(arg[i+3]))
         except:
            return data.Color(1.0, 1.0, 1.0)
            

   return data.Color(1.0, 1.0, 1.0)
      
      
       

      

      

      



