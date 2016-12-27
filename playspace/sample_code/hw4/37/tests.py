import data
import unittest
import math
from vector_math import *
import collisions
import cast

class TestPoint(unittest.TestCase):
   def test_cast_rays_1(self):
       ray = data.Ray(data.Point(0, 0, 0), data.Vector(1, 0, 0))
       s1 = data.Sphere(data.Point(10, 0, 0), 2, 
       data.Color(1.0, 0.0, 1.0), data.Finish(1.0))
       s2 = data.Sphere(data.Point(1582, 28, -3842), 12, 
       data.Color(0.0, 1.0, 0.0), data.Finish(0.5))
       s3 = data.Sphere(data.Point(-42, 0, 12.86), 2.4, 
       data.Color(0.0, 0.0, 1.0), data.Finish(0.2))
       sphere_list = [s1, s2, s3]
       ambient_light = data.Color(1.0, 1.0, 1.0)
       self.assertEqual(cast.cast_ray(ray, sphere_list, ambient_light), 
       data.Color(1.0, 0.0, 1.0))

   def test_cast_rays_2(self):
       ray = data.Ray(data.Point(0, 0, 0), data.Vector(1, 0, 0))
       s1 = data.Sphere(data.Point(-80, 2, 5), 2, 
       data.Color(0.0, 1.0, 1.0), data.Finish(0.45))
       s2 = data.Sphere(data.Point(-62, -10, 40), 8, 
       data.Color(0.0, 1.0, 0.0), data.Finish(0.3))
       sphere_list = [s1, s2]
       ambient_light = data.Color(0.3, 0.6, 0.9)
       self.assertEqual(cast.cast_ray(ray, sphere_list, ambient_light), 
       data.Color(1.0, 1.0, 1.0))

   def test_add_finish(self):
       color = data.Color(0.5, 1.0, 0.0)
       sphere = data.Sphere(data.Point(0, 0, 0), 1, 
       data.Color(0.0, 0.0, 0.0), data.Finish(0))
       ambient_light = data.Color(0.5, 0.2, 0.1)
       self.assertEqual(cast.add_finish(color, sphere, ambient_light), 
       data.Color(0.0, 0.0, 0.0))
   
   
   
if __name__ == "__main__":
     unittest.main()