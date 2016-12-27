import unittest
import math
from data import *
from vector_math import *
from collisions import *
from cast import *

class TestData(unittest.TestCase):

   def test_single_ray_cast1(self):
      ray = Ray(Point(1,0,0),Vector(1,0,0))
      sphere1 = Sphere(Point(0,0,0),2,Color(1,1,1),Finish(.1,.1,.1,.01))
      sphere2 = Sphere(Point(10,0,0),1,Color(1,1,1),Finish(.1,.1,.1,.01))
      sphere3 = Sphere(Point(100,100,100),5,Color(1,1,1),Finish(.1,.1,.1,.01))
      h = (cast_ray(ray,[sphere1,sphere2,sphere3],.4,.4,.4))
      self.assertEqual(cast_ray(ray,[sphere1,sphere2,sphere3],.4,.4,.4),h)

   def test_single_ray_cast2(self):
      ray = Ray(Point(0,0,0), Vector(1,0,0))
      sphere1 = Sphere(Point(2,2,2),1,Color(1,1,1),Finish(.1,.1,.1,.01))
      sphere2 = Sphere(Point(-5,-5,-5),3,Color(1,1,1),Finish(.1,.1,.1,.01))
      h = (cast_ray(ray,[sphere1,sphere2],.4,.4,.4))
      self.assertEqual(cast_ray(ray,[sphere1,sphere2],.4,.4,.4),h)

if __name__ == "__main__":
   unittest.main()
