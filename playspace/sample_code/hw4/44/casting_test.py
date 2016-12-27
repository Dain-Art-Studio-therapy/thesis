from data import *
from cast import *

eye_point = Point(0, 0 , -14)
sphere_list = [Sphere(Point(1, 1, 0), 2, Color(0,0,1), Finish(0.2, 0.4, .5, .05)), Sphere(Point(.5, 1.5, -3), .5, Color(1,0,0), Finish(0.4, 0.4, .5, .05))]
max_x = 10
min_x = -10
max_y = 7.5
min_y = -7.5
width = 1024
height = 768
ambient = Color(1.0, 1.0, 1.0)
Light = Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5))
cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, Light)
