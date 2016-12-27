from cast import *
from data import *


def convert_spheres(f):
   list_of_spheres = []
   for line in f:
      q = line.split()
      sphere = Sphere(Point(float(q[0]),float(q[1]),float(q[2])),float(q[3]),Color(float(q[4]),float(q[5]),float(q[6])),Finish(float(q[7]),float(q[8]),float(q[9]),float(q[10])))
      list_of_spheres.append(sphere)
   return list_of_spheres

def change(sphere_list, list):
   eye_point = Point(0.0,0.0,-14.0)
   min_x = -10
   max_x = 10
   min_y = -7.5
   max_y = 7.5
   width = 1024
   height = 768
   light = Light(Point(-100,100,-100), Color(1.5,1.5,1.5))
   ambient = Color(1.0,1.0,1.0)
   for i in range(2,len(list)):
      if list[i] == '-eye':
         eye_point = Point(float(list[i+1]),float(list[i+2]),float(list[i+3]))
      if list[i] == '-view':
         min_x = float(list[i+1])
         max_x = float(list[i+2])
         min_y = float(list[i+3])
         max_y = float(list[i+4])
         width = float(list[i+5])
         height = float(list[i+6])
      if list[i] == '-light':
         light = Light(Point(float(list[i+1]),float(list[i+2]),float(list[i+3])), Color(float(list[i+4]),float(list[i+5]),float(list[i+6])))
      if list[i] == '-ambient':
         ambient = Color(float(list[i+1]),float(list[i+2]),float(list[i+3]))
   cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,ambient,light,eye_point)
