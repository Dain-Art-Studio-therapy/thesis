import sys
from data import *
def sphere_from_file(data):
   try:
      f_data=[]
      for i in data:
         f_data.append(float(i))
   except:
      print 'Please enter numbers for the spheres' 
   point=Point(f_data[0],f_data[1],f_data[2])
   radius=f_data[3]
   color=Color(f_data[4],f_data[5],f_data[6])
   finish=Finish(f_data[7],f_data[8],f_data[9],f_data[10])
   sphere=Sphere(point,radius,color,finish)
   return sphere

def sphere_list_from_file(argv):
   try:
      f=open(argv[1],'rb')
   except:
      print 'Please enter a valid file name.'
      exit(1)
   sphere_list=[]
   c=0
   for line in f:
      c+=1
      data=line.split()
      try:
         s=sphere_from_file(data)
         sphere_list.append(s)
      except:
         print "Malformed sphere on line " 
         print c
   f.close()
   return sphere_list

def eye_from_file(argv,location):
   try:
      x=float(argv[location+1])
   except:
      print '[-eye x]'
      x=0
   try:
      y=float(argv[location+2])
   except:
      print '[-eye y]'
      y=0
   try:
      z=float(argv[location+3])
   except:
      print '[-eye z]'
      z=-140
   return Point(x,y,z)

def light_from_file(argv,location):
   try:
      x=float(argv[location+1])
   except:
      print '[-light x]'
      x=-100
   try:
      y=float(argv[location+2])
   except:
      print '[-light y]'
      y=100
   try:
      z=float(argv[location+3])
   except:
      print '[-light x]'
      z=-100
   try:
      r=float(argv[location+4])
   except:
      print '[-light r]'
      r=1.5
   try:
      g=float(argv[location+5])
   except:
      print '[-light g]'
      g=1.5
   try:
      b=float(argv[location+6])
   except:
      print '[-light b]'
      b=1.5
   return Light(Point(x,y,z),Color(r,g,b))

def ambient_from_file(argv,location):
   try:
      r=float(argv[location+1])
   except:
      print '[-ambient r]'
      r=1
   try:
      g=float(argv[location+2])
   except:
      print '[-ambient g]'
      g=1
   try:
      b=float(argv[location+3])
   except:
      print '[-ambient b]'
      b=1
   return Color(r,g,b)

def read_arguments(argv):
   min_x=-10
   max_x=10
   min_y=-7.5
   max_y=7.5
   wid=1024
   hei=768
   eye=Point(0,0,-14.0)
   s=sphere_list_from_file(argv)
   ambient=Color(1,1,1)
   light=Light(Point(-100,100,-100),Color(1.5,1.5,1.5))
   if len(argv)>2:
      current=2
      while current<=len(argv)-1:
         if argv[current]=='-eye':
            eye=eye_from_file(argv,current)
            current+=4
         elif argv[current]=='-view':
            try:
               min_x=int(argv[current+1])
            except:
               print '[-view min_x]'
            try:
               max_x=int(argv[current+2])
            except:
               print '[-view max_x]'
            try:
               min_y=int(argv[current+3])
            except:
               print '[-view min_y]'
            try:
               max_y=int(argv[current+4])
            except:
               print '[-view max_y]'
            try:
               wid=int(argv[current+5])
            except:
               print '[-view width]'
            try:
               hei=int(argv[current+6])
            except:
               print '[-view hei]'
            current+=7
         elif argv[current]=='-light':
            light=light_from_file(argv,current)
            current+=7
         elif argv[current]=='-ambient':
            ambient=ambient_from_file(argv,current)
            current+=4
         else:
            print 'Please enter the correct number of arguments'
            current+=1
   return [min_x,max_x,min_y,max_y,wid,hei,eye,s,ambient,light]
