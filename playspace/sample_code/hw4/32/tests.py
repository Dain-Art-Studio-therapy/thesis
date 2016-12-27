import unittest
from data import *
from vector_math import *
from collisions import *
from cast import *
from utility import *

class Tests(unittest.TestCase):
   """def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_sphere_intersection_point_1(self):
      sphere1 = Sphere(Point(9, 0, 0), 5.0)
      ray1 = Ray(Point(2, 0, 0), Vector(6, 0, 0))
      intersect = Point(4, 0, 0)
      self.assertTrue(intersect == sphere_intersection_point(ray1, sphere1))   

   def test_sphere_intersection_2(self):
      sphere1 = Sphere(Point(0, 9, 0), 3.0)
      ray1 = Ray(Point(0, 5, 0), Vector(0, 5, 0))
      intersect = Point(0, 6, 0)
      self.assertTrue(intersect == sphere_intersection_point(ray1, sphere1))

   def test_find_intersection_points_1(self):
      sphere1 = Sphere(Point(0, 35, 0), 2.0)
      sphere2 = Sphere(Point(5, 0, 0), 3.0)
      ray1 = Ray(Point(1, 0, 0), Vector(3, 0, 0))
      intersect = Point(2, 0, 0)
      spheres = [sphere1, sphere2]
      list = find_intersection_points(spheres, ray1)
      self.assertTrue(list == [(sphere2, intersect)])
      
   def test_find_intersection_points_2(self):
      sphere1 = Sphere(Point(0, 0, 7), 3.0)
      sphere2 = Sphere(Point(0, 4, 0), 2.0)
      spheres = [sphere1, sphere2]
      ray1 = Ray(Point(0, 0, 2), Vector(0, 0, 5))
      intersect = Point(0, 0, 4)
      self.assertTrue([(sphere1, intersect)] == 
      find_intersection_points(spheres, ray1))

   def test_sphere_normal_1(self):
      sphere1 = Sphere(Point(0, 0, 0), 5.0)
      point = Point(5, 5, 5)
      self.assertTrue(sphere_normal_at_point(sphere1, point) == 
      Vector(.577350269, .577350269, .577350269))

   def test_sphere_normal_2(self):
      sphere1 = Sphere(Point(2, 3, 4), 3.0)
      point = Point(5, 6, 7)
      self.assertTrue(sphere_normal_at_point(sphere1, point) == 
      Vector(.577350269, .577350269, .577350269))"""

   def test_cast_ray_1(self):
      color = Color(1.0, 0, 0)
      color1 = Color(1.0, 0, 0)
      color2 = Color(0, 0, 1.0)
      f1 = Finish(0.2, 0.4, 0.5, 0.05)
      f2 = Finish(0.2, 0.4, 0.5, 0.05)
      sphere1 = Sphere(Point(0, 9, 0), 5.0, color1, f1)
      sphere2 = Sphere(Point(3, 0, 0), 2.0, color2, f2)
      finish = Color(1.0, 1.0, 1.0)
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      eye_point = Point(0.0, 0.0, -14.0)
      ray = Ray(Point(0, 3, 0), Vector(1, 2, 0))
      spheres = [sphere1, sphere2]
      self.assertTrue(cast_ray(ray, spheres, finish, light, eye_point) == color)

   def test_cast_ray_2(self):
      pass
      color = Color(1.0, 1.0, 1.0)
      color1 = Color(1.0, 0, 0)
      color2 = Color(0, 0, 1.0)
      sphere1 = Sphere(Point(75, 14, 3), 2.0, color1)
      sphere2 = Sphere(Point(41, 2, 78), 5.0, color2)
      spheres = [sphere1, sphere2]
      ray = Ray(Point(2, 4, 7), Vector(4, 0, 0))
      self.assertTrue(cast_ray(ray, spheres) == color)
      

if __name__ == "__main__":
   unittest.main()

