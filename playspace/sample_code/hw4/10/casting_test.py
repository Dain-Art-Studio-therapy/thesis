from cast import *
from data import *

pt = Point(0, 0, -14)
center1 = Point(1, 1, 0)
color1 = Color(0, 0, 1)
finish1 = Finish(0.2)
sph1 = Sphere(center1, 2.0, color1, finish1)
center2 = Point(0.5, 1.5, -3.0)
color2 = Color(1, 0, 0)
finish2 = Finish(0.4)
sph2 = Sphere(center2, 0.5, color2, finish2)
sphs = [sph1, sph2]

ambient_light = Color(1.0,1.0,1.0)

cast_all_rays(-10.0, 10.0, -7.5, 7.5, 1024, 768, pt, sphs, ambient_light)
#cast_all_rays(0.05859357, 0.44921857, 2.03125, 2.421875, 20, 20, pt, sphs, ambient_light)

