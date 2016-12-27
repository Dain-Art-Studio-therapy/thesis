import data
import vector_math
from utility import *
import unittest
import collisions
import cast
import math

red = data.Color(1.0, 0, 0)
blue = data.Color(0, 0, 1.0)
eye_point = data.Point(0.0,0.0,-14.0)
s0 = data.Sphere(data.Point(1.0,1.0,0.0), 2.0,
                            blue, data.Finish(0.2, 0.4, 0.5, 0.05))
s1 = data.Sphere(data.Point(0.5,1.5,-3.0), 0.5,
                 red, data.Finish(0.4, 0.4, 0.5, 0.05))
list_of_spheres = [s0, s1]
min_x = -10.0
max_x = 10.0
min_y = -7.5
max_y = 7.5
width = 1024
height = 768
ambient_light = data.Color(1.0,1.0,1.0)
light_pt = data.Point(-100.0, 100.0, -100.0)
light_color = data.Color(1.5, 1.5, 1.5)
Light = data.Light(light_pt, light_color)
cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height,
                   eye_point, list_of_spheres, ambient_light, Light)



