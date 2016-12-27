# Han Tran | CPE101-01,02 | Assignment 4--Part 2 | Professor: Aaron Keen

import unittest
import cast
import data
import collisions
import vector_math


class TestCase(unittest.TestCase):
	# ---- Part V ---- #
   def test_case1(self):
      cast.print_header(1024, 768)
      color1 = data.Color(0.0, 0.0, 1.0)
      color2 = data.Color(1.0, 0.0, 0.0)
      sp1_amb = data.Finish(0.2, 0.4, 0.5, 0.05)
      sp2_amb = data.Finish(0.4, 0.4, 0.5, 0.05)
      scene_amb = data.Color(1.0, 1.0, 1.0)
      point_light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
      sphere_list = [data.Sphere(data.Point(1.0, 1.0, 0), 2, color1, sp1_amb), data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, color2, sp2_amb)]
      cast.cast_all_rays(-10.0, 10.0, -7.5, 7.5, 1024, 768, data.Point(0.0, 0.0, -14.0) ,sphere_list, scene_amb, point_light)


if __name__ == '__main__':
	unittest.main()
