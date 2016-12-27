from cast import *
from data import *

print 'P3'
print 1024,768
print 255
sphere_list = [Sphere(Point(1.0,1.0,0.0), 2.0), Sphere(Point(0.5,1.5,-3.0), 0.5)]
cast_all_rays(-10.0,10.0,-7.5,7.5,1024,768,Point(0.0,0.0,-14.0),sphere_list)
