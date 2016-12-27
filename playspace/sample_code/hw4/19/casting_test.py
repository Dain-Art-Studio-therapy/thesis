from cast import *

test1 = cast_all_rays(-10,10,-7.5,7.5,1024,768,Point(0.0,0.0,-14.0),
   [Sphere(Point(1,1,0),2,Color(0,0,1.0),Finish(0.2, 0.4, 0.5, 0.05)), Sphere(Point(0.5,1.5,-3.0),0.5,Color(1.0,0,0), Finish(0.4, 0.4, 0.5, 0.05))], 
   Color(1.0,1.0,1.0), Light(Point(-100,100,-100), Color(1.5,1.5,1.5)))
