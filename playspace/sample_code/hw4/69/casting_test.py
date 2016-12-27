from cast import *
from data import *

print 'P3'
print 1024, 768
print 255

#def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, amcolor, light)

eye = Point(0.0, 0.0, -14.0)

sphere1 = Sphere(Point(1.0, 1.0, 0.0), 2.0, Color(0, 0, 1.0), Finish(0.2, 0.4, 0.5, 0.05))
sphere2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0, 0), Finish(0.4, 0.4, 0.5, 0.05))

spheres = [sphere1, sphere2]

ambient_light = Color(1.0, 1.0, 1.0)

cast_all_rays(-10.0, 10.0, -7.5, 7.5, 1024, 768, eye, spheres, ambient_light, Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5)))