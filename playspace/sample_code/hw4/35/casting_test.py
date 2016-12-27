from data import *
from cast import *
print 'P3'
print 1024
print 768
print 255

min_x = -10
max_x = 10
min_y = -7.5
max_y = 7.5
width = 1024
height = 768
eye_point = Point(0.0,0.0,-14.0)
ambient = 1.0
light = Light(Point(-100.0,100.0,-100.0),Color(1.5,1.5,1.5))
slist = [Sphere(Point(1.0,1.0,0.0),2.0,Color(0,0,1.0),Finish(.2,.4,.5,.05)),
         Sphere(Point(.5,1.5,-3.0),.5,Color(1.0,0,0),Finish(.4,.4,.5,.05))]
cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,slist,ambient,light,eye_point)
