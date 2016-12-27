# Name: Allison Lee
# Instructor: Aaron Keen
# Section: 09

import unittest
import data
import vector_math
import collisions
import cast

light = data.Light(data.Point(-100.0,100.0,-100.0),data.Color(1.5,1.5,1.5))
color = data.Color(1.0,1.0,1.0)
eye_point = data.Point(0.0,0.0,-14.0)
sphere1 = data.Sphere(data.Point(1.0,1.0,0.0),2.0,data.Color(0.0,0.0,1.0),data.Finish(0.2,0.4,0.5,.05))
sphere2 = data.Sphere(data.Point(.5,1.5,-3.0),.5,data.Color(1.0,0.0,0.0),data.Finish(0.4,0.4,0.5,.05))
min_x = -10
max_x = 10
min_y = -7.5
max_y = 7.5
width = 1024
height = 768
sphere_list = [sphere1,sphere2]

cast.cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,color,light)

if __name__ == '__main__':
    unittest.main()
