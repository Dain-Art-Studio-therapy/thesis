# Test Update

import data
import utility
import cast
import unittest
import vector_math
import collisions


class TestCase(unittest.TestCase):
   def test_case1(self):
      color1 = data.Color(0.0, 0.0, 1.0)
      color2 = data.Color(1.0, 0.0, 0.0)
      sp1_amb = data.Finish(0.2, 0.4, 0.5, 0.5)
      sp2_amb = data.Finish(0.4, 0.4, 0.5, 0.5)
      scene_amb = data.Color(1.0, 1.0, 1.0)
      point_light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
      sphere_list = [data.Sphere(data.Point(1.0, 1.0, 0), 2, color1, sp1_amb), data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, color2, sp2_amb)]

      min_x = 0.05859357
      max_x = 0.44921857
      min_y = 2.03125
      max_y = 2.421875
      width = 20
      height = 20
      eye_point = data.Point(0.0, 0.0, -14.0)
      
      del_x = (max_x - min_x)/float(width)
      del_y = (max_y - min_y)/float(height)
      z = 0
      # Find the ray from eye_point to each pixel on the rectangle
      for i in range(height): # enter each row
         y = max_y - i*del_y
         for j in range(width):  # enter each column
            x = min_x + j*del_x
            pixel_pt = data.Point(x, y, z)
            vec_eye_pixel = vector_math.difference_point(pixel_pt, eye_point)
            ray = data.Ray(eye_point, vec_eye_pixel)
            result = cast.cast_ray(ray, sphere_list, scene_amb, point_light, eye_point)
            print result.r, '\t', result.g, '\t ', result.b 

if __name__ == '__main__':
   unittest.main()
