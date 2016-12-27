from cast import *
from data import *

width = 1024
height = 768
#width = 20
#height = 15
print 'P3'
print width
print height
print '255'

eye = Point(0.0,0.0,-14.0)
spherelist = [Sphere(Point(1.0,1.0,0.0),2.0,Color(0,0,1),Finish(0.2,0.4,0.5,0.05)), Sphere(Point(0.5,1.5,-3.0), 0.5,Color(1,0,0),Finish(0.4,0.4,0.5,0.05))]
cast_all_rays(-10,10,-7.5,7.5,width,height,eye,spherelist,Color(1,1,1),Light(Point(-100.0,100.0,-100.0),Color(1.5,1.5,1.5)))
