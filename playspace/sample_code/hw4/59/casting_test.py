import unittest
import data
import vector_math
import collisions
import cast

def create_picture():
   eyept = data.Point(0.0, 0.0, -14.0)
   sph1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0.0, 0.0, \
   1.0), data.Finish(0.2, 0.4, 0.5, 0.05))
   sph2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1.0, 0.0, \
   0.0), data.Finish(0.4, 0.4, 0.5, 0.05))
   S = [sph1, sph2]
   
   min_x = -10
   max_x = 10
   min_y = -7.5
   max_y = 7.5
   width = 1024
   height = 768
   ambient = 1.0
   light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, \
   1.5))
   
   cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eyept, S, \
   ambient, light)

if __name__ == '__main__':
   create_picture()
