import unittest
from data import *
from vector_math import *
from collisions import *
from cast import *

class Tests(unittest.TestCase):

   def test_singlecast1(self):
      r = Ray(Point(0,0,0),Vector(4,4,4))
      color = 1.0,1.0,1.0
      finish = Finish(.25,.5,1)
      s = Sphere(Point(2,2,-2),4,color,finish)
      s2 = Sphere(Point(1,-2,1),3,color,finish)
      slist = [s,s2]
      Color = .5
      Light = 1.0
      Point = Point(0,0,0)
      self.assertTrue(cast_ray(r,slist,Color,Light,Point),True)
   def test_singlecast2(self):
      r = Ray(Point(0,0,-14),Vector(1,0,0))
      color = 1.0,1.0,1.0
      finish = Finish(.25,.5,1)
      s = Sphere(Point(2,2,2),1,color,finish)
      s2 = Sphere(Point(-5,-5,-5),3,color,finish)
      slist = [s,s2]
      Color = .5
      Light = 1.0
      Point = Point(0,0,0)
      self.assertTrue(cast_ray(r,slist,Color,Light,Point),False)

   

if __name__ == "__main__":
      unittest.main() 
