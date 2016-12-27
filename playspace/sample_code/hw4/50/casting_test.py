from cast import *
from data import *

#sphere1 data
cnt1 = Point(1.0,1.0,0.0)
color1 = Color(0.0, 0.0, 1.0)
s1 = Sphere(cnt1, 2.0, color1, Finish(0.2, 0.4, 0.5, 0.05))

#sphere2 data
cnt2 = Point(0.5,1.5,-3.0)
color2 = Color(1.0,0.0,0.0)
s2 = Sphere(cnt2, 0.5, color2, Finish(0.4, 0.4, 0.5, 0.05))

sList = [s1,s2]
eye = Point(0.0,0.0,-14.0)
ambient_color = Color(1.0, 1.0, 1.0)
point_light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))

cast_all_rays(-10, 10, -7.5, 7.5, 1024, 768, eye, sList, ambient_color,\
point_light)

#cast_all_rays(0.05859357, 0.44921857, 2.03125, 2.421875, 20, 20, eye, sList,\
#ambient_color, point_light)
