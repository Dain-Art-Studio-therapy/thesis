from vector_math import *
from data import *
from cast import *
import utility
from collisions import *


eye_point = Point(0.0, 0.0, -14.0)
color1 = Color(0, 0, 1.0)
color2 = Color(1.0, 0, 0)
s1_finish = Finish(0.2, 0.4, 0.5, 0.05)
s2_finish = Finish(0.4, 0.4, 0.5, 0.05)
sphere1 = Sphere(Point(1.0, 1.0, 0.0), 2.0, color1, s1_finish)
sphere2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, color2, s2_finish)
spheres = [sphere1, sphere2]
finish = Color(1.0, 1.0, 1.0)
light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
cast_all_rays(-10, 10, -7.5, 7.5, 1024, 768, eye_point, spheres, finish, light)
