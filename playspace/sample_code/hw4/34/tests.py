# Contains test cases
import unittest
from data import *
import utility
from vector_math import *
from collisions import *
from math import *
from cast import *

class TestData(unittest.TestCase):
   def test_sphere_intersection_point1(self):
      newRay = Ray(Point(-4,0,0), Vector(3,0,0))
      newSphere = Sphere(Point(0,0,0), 2)
      self.assertEqual(sphere_intersection_point(newRay, newSphere), Point(-2,0,0))

   def test_sphere_intersection_point2(self):
      newRay = Ray(Point(10,4,4), Vector(-10,0,0))
      newSphere = Sphere(Point(4,0,4), 4)
      self.assertEqual(sphere_intersection_point(newRay, newSphere), Point(4,4,4))



   def test_find_intersection_points1(self):
      ray1 = Ray(Point(0,0,0), Vector(5,5,0))
      sphere1 = Sphere(Point(-1,0,0), 1)
      sphere2 = Sphere(Point(7,5,0), 2)
      sphere_list = [sphere1, sphere2]
      self.assertEqual(find_intersection_points(sphere_list, ray1), [(sphere2, sphere_intersection_point(ray1,sphere2))])

   def test_find_intersection_points2(self):
      ray1 = Ray(Point(5,5,0), Vector(-5,-5,0))
      sphere1 = Sphere(Point(0,0,1), 1)
      sphere2 = Sphere(Point(10,3,-5), 4)
      sphere3 = Sphere(Point(3,3,-3), 3)
      sphere_list = [sphere1, sphere2, sphere3]
      self.assertEqual(find_intersection_points(sphere_list, ray1), [(sphere1, sphere_intersection_point(ray1,sphere1)), (sphere3, sphere_intersection_point(ray1,sphere3))])

   def test_find_intersection_points3(self):
      ray1 = Ray(Point(0,0,0), Vector(20,0,0))
      sphere1 = Sphere(Point(2,0,0), 1)
      sphere2 = Sphere(Point(10,0,0), 5)
      sphere3 = Sphere(Point(7,0,0), 2)
      sphere_list = [sphere1, sphere2, sphere3]
      self.assertEqual(find_intersection_points(sphere_list, ray1), [(sphere1, sphere_intersection_point(ray1,sphere1)), (sphere2, sphere_intersection_point(ray1,sphere2)), (sphere3, sphere_intersection_point(ray1,sphere3))])



   def test_sphere_normal_at_point1(self):
      sphere1 = Sphere(Point(2,0,0), 1)
      intersection_point = Point(1,0,0)
      self.assertEqual(sphere_normal_at_point(sphere1, intersection_point), Vector(-1,0,0))
  
   def test_sphere_normal_at_point2(self):
      sphere1 = Sphere(Point(2,2,2), 4)
      intersection_point = Point(2,2,6)
      self.assertEqual(sphere_normal_at_point(sphere1, intersection_point), Vector(0,0,1))

   def test_cast_ray(self):
      ray1 = Ray(Point(0,0,0), Vector(20,0,0))
      sphere1 = Sphere(Point(2,0,0), 1)
      sphere2 = Sphere(Point(10,0,0), 5)
      sphere3 = Sphere(Point(7,0,0), 2)
      sphere_list = [sphere1, sphere2, sphere3]
      self.assertEqual(cast_ray(ray1,sphere_list), True)
      ray1 = Ray(Point(0,0,0), Vector(5,5,0))
      sphere1 = Sphere(Point(-1,0,0), 1)
      sphere2 = Sphere(Point(7,5,0), 2)
      sphere_list = [sphere1, sphere2]
      self.assertEqual(cast_ray(ray1,sphere_list), True)























if __name__ == "__main__":
   unittest.main()
