import unittest
import math
import cast

import data


class TestData(unittest.TestCase):
   def test_case_ray_1(self):
       ray = data.Ray(data.Point(-3,0,0),data.Vector(3,0,0))
       sphere1 = data.Sphere(data.Point(0,0,0), 1, data.Color(255,0,0))
       sphere2 = data.Sphere(data.Point(0,3,0), 3, data.Color(0,0,255))
       spherelist = [sphere1, sphere2]
       color = cast.cast_ray(ray, spherelist)

       self.assertEqual(color, data.Color(255,0,0 ))

   def test_case_ray_2(self):
       ray = data.Ray(data.Point(-5,1,0),data.Vector(10,0,0))
       sphere1 = data.Sphere(data.Point(-1,0,0), 1, data.Color(0,255,0))
       sphere2 = data.Sphere(data.Point(3,3,0), 2, data.Color(0,0,255))
       spherelist = [sphere1, sphere2]
       color = cast.cast_ray(ray, spherelist)


if __name__ == "__main__":
     unittest.main()