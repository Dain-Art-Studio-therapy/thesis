from cast import *
from data import *

width = 1024
height = 768
min_x = -10.0 
max_x = 10.0
min_y = -7.5
max_y = 7.5
amb_light = Color(1.0, 1.0, 1.0)
light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))

s1 = Sphere(Point(1.0, 1.0, 0.0), 2.0, Color(0.0, 0.0, 1.0), Finish(0.2, 0.4, 0.5, 0.05))
s2 = Sphere(Point(.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0), Finish(0.4, 0.4, 0.5, 0.05))

sphere_list = [s1, s2]
eye_point = Point(0.0, 0.0, -14.0)


print 'P3'
print width, height
print 255


cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, amb_light, light)
