import unittest
from data import *
from collisions import *
import math
from cast import *

class CollisionTests(unittest.TestCase):
   def test_handle_lighting(self):
      pixel = handle_lighting(Color(1,1,0), Finish(.4,.4,.5,.05), Color(1,1,1),
         Color(1,1,1), Color(0,0,0))
      self.assertEqual(pixel, Color(1.4,1.4,1.0))
      
      pixel2 = handle_lighting(Color(0,1,1), Finish(.1,1,1,1), Color(1,1,1),
         Color(.5,.5,.5), Color(0,0,1))
      self.assertEqual(pixel2, Color(.5, .6, 1.6))

   def test_pseudo_dist(self):
      self.assertEqual(pseudo_dist(Point(2,2,2), Point(0,0,0)), 12)
   
   def test_computerPE(self):
      point = Point(1,1,1)
      normalV = Vector(1,0,0)
      self.assertEqual(compute_point_epsilon(point, normalV), Point(1.01,1,1))
      
      pt2 = Point(-2,0,1)
      normalV2 = Vector(0,-1,0)
      self.assertEqual(compute_point_epsilon(pt2, normalV2), Point(-2,-.01, 1))

   def test_spec_light(self):
      self.assertEqual(compute_spec_light(Color(0,0,0), .5,-1,.2), Color(0,0,0))
      self.assertEqual(compute_spec_light(Color(1,1,1), .2, 1, .5), 
         Color(.2,.2,.2))

if __name__ == "__main__":
   unittest.main() 
