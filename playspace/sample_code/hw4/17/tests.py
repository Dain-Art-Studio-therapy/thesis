import unittest
import data
import vector_math
import math
import collisions
import cast

class TestData(unittest.TestCase):
   
      
   def test_cast_ray_one(self):
      sphere_list = []
      pt = data.Point(0.0, 0.0, -14.0)
      dir = data.Point(4, 2, 3)
      center = data.Point(3, 6, 4)
      ray = data.Ray(pt, dir)
      sphere = data.Sphere(center, 2, data.Color(0, 0, 1.0), data.Finish(0.2, 0.4, 0.5, 0.5))
      
      center2 = data.Point(6, 6, 5)
      sphere2 = data.Sphere(center2, 6, data.Color(1.0, 0, 0), data.Finish(0.4, 0.4, 0.5, 0.5))
      sphere_list.append(sphere)
      sphere_list.append(sphere2)
      colorambient = data.Color(1.0, 1.0, 1.0)
      light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
      eye_point = data.Point(0.0, 0.0, -14.0)
      checklist = cast.cast_ray(ray, sphere_list, colorambient, light, eye_point)
      self.assertEqual(checklist, data.Color(1.0, 1.0, 1.0))
      

   def test_cast_ray_two(self):
      sphere_list = []
      pt = data.Point(1, 2, 3)
      center = data.Point(2, 8, 7)
      dir = data.Point(3, 5, 10)
      ray = data.Ray(pt, dir)
      sphere = data.Sphere(center, 5, data.Color(0, 1.0, 1.0), data.Finish(0.2, 0.4, 0.5, 0.5))
      sphere_list.append(sphere)
      center2 = data.Point(3, 3, 5)
      sphere2 = data.Sphere(center2, 8, data.Color(1.0, 1.0, 0.0), data.Finish(0.2, 0.4, 0.5, 0.5))
      colorambient = data.Color(1.0, 1.0, 1.0)
      light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
      sphere_list.append(sphere2)
      eye_point = data.Point(0.0, 0.0, -14.0)
      checklist = cast.cast_ray(ray, sphere_list, colorambient, light, eye_point)
      self.assertEqual(checklist, data.Color(0.0, 0.20000000000000001, 0.20000000000000001))

if __name__ == '__main__':
   unittest.main()
