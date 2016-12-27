import sys
import data
import cast

def spheres(file):
   opened_file = open(file,'r')
   lines = opened_file.readlines()   
   sphere_list = []
   failed = []
   for x in lines:         
      str_list = x.split()
      if len(str_list) == 11:
         list = []
         for x in str_list:
            list.append(float(x))
         point = data.Point(list[0],list[1],list[2]) 
         radius = list[3]
         color = data.Color(list[4],list[5],list[6])
         finish = data.Finish(list[7],list[8],list[9],list[10])
         sphere = data.Sphere(point,radius,color,finish)
         sphere_list.append(sphere)
      else:
         failed.append(lines.index(x)+1)
   
   return (sphere_list,failed)

      
