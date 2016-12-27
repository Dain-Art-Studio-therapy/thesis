import unittest
import cast
from data import *


min_x=-10
max_x=10
min_y=-7.5
max_y=7.5
width=1024
height=768
eye_point=Point(0.0,0.0,-14.0)
p1=Point(1.0, 1.0, 0.0)
r1=0
g1=0
b1=225
co1=Color(r1,g1,b1)
fin1=Finish(0.2, 0.4, 0.5, 0.05)
s1=(p1,2.0,co1,fin1)
p2=Point(0.5, 1.5, -3.0)
r2=225
g2=0
b2=0
co2=Color(r2,g2,b2)
fin2=Finish(0.4, 0.4, 0.5, 0.05)
s2=(p2,0.5,co2,fin2)
sphere_list=[s1,s2]
lightpt=Point(-100, 100, -100)
lightcolor=Color(1.5, 1.5, 1.5)
ambientColor=Light(lightpt,lightcolor)
print "P3"
cast.cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,
                ambientColor)

