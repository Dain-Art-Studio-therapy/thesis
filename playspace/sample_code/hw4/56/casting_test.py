import data
import cast
import vector_math
import math

eye = data.Point(0.0, 0.0, -14.0)
sphere1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2, data.Color(0.0, 0.0, 1.0), data.Finish(.2, .4, .5, .05))
sphere2 = data.Sphere(data.Point(.5, 1.5, -3.0), .5, data.Color(1.0, 0.0, 0.0), data.Finish(.4, .4, .5, .05))
sphere_list = [sphere1, sphere2]
ambient_light = data.Color(1.0, 1.0, 1.0)
light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
minx = -10
maxx = 10
miny = -7.5
maxy = 7.5
width = 1024
height = 768

cast.cast_all_rays(minx, maxx, miny, maxy, width, height, eye, sphere_list, ambient_light, light)

