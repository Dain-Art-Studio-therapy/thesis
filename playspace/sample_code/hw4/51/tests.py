import unittest
import data
import utility
import vector_math
import math
import collisions
import cast

class TestData(unittest.TestCase):


   def test_cast_ray_1(self):
      R = data.Ray(data.Point(0,0,0),data.Vector(20,20,0))
      L = [data.Sphere(data.Point(6,7,0),4,data.Color(1.0,1.0,1.0),data.Finish(1.0,1.0,1.0,1.0)),data.Sphere(data.Point(11,11,0),1,data.Color(1.0,1.0,1.0),data.Finish(1.0,1.0,1.0,1.0))]
      C = data.Color(0.0,0.0,0.0)
      l = data.Light(data.Point(0,0,0),data.Color(0.0,0.0,0.0))
      self.assertEqual(cast.cast_ray(R,L,C,l,data.Point(0,0,0)),data.Color(0.0,0.0,0.0))

   def test_cast_ray_2(self):
      R = data.Ray(data.Point(0,0,0),data.Vector(1,1,0))
      L = [data.Sphere(data.Point(15,15,0),4,data.Color
(1.0,1.0,1.0),data.Finish(1.0,1.0,1.0,1.0)),data.Sphere(data.Point(11,11,0),5,data.Color(1.0,1.0,1.0),data.Finish(1.0,1.0,1.0,1.0))]
      C = data.Color(1.0,1.0,1.0)
      l = data.Light(data.Point(0,0,0),data.Color(1.0,1.0,1.0))
      self.assertEqual(cast.cast_ray(R,L,C,l,data.Point(0,0,0)),data.Color(3.0,3.0,3.0))
      

if __name__ == "__main__":
     unittest.main()
