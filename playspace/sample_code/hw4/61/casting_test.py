from data import *
from cast import *

print "P3"
print "1024 768"
print "255"

eye = Point(0.0,0.0,-14.0)
Light = Light(Point(-100.0,100.0,-100.0),Color(1.5,1.5,1.5))
s1 = Sphere(Point(1.0,1.0,0.0),2.0,Color(0,0,1.0),Finish(0.2,0.4,0.5,0.05))
s2 = Sphere(Point(0.5,1.5,-3.0),0.5,Color(1.0,0,0),Finish(0.4,0.4,0.5,0.05))
sphere_list = [s1,s2]

cast_all_rays(-10,10,-7.5,7.5,1024,768,eye,sphere_list,Color(1.0,1.0,1.0),Light)
