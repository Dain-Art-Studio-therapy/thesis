
import unittest      # import the module that supports writing unit tests
import data
import collisions
import vector_math
import math
import cast
import utility

class TestData(unittest.TestCase):
   def test_ray_cast(self):
      self.assertEqual(cast.cast_ray(data.Ray(data.Point(0,0,0),data.Vector(1,3,5)),
                      [data.Sphere(data.Point(-10,-10,-10), 5,data.Color(0.0,0.0,0.0),data.Finish(0.2,0.1,0.2,0.1)),
                       data.Sphere(data.Point(-20,-10,-5),5,data.Color(1.0,1.0,1.0),data.Finish(0.2,0.1,0.2,0.1))],data.Color(0.1,0.1,0.1),
                       data.Light(data.Point(-1,-1,0),data.Color(0.5,0.5,0.5)),data.Point(-1,-1,-1)), data.Color(1.0,1.0,1.0))
     

   def test_float_conv(self):
      self.assertEqual(utility.convert_float(1.5),255)

      self.assertEqual(utility.convert_float(0.0),0)

   def test_mindex(self):
      self.assertEqual(utility.nearest_to_point([data.Point(4,2,0),data.Point(-1,5,0)],data.Point(0,0,0)),0)

      self.assertEqual(utility.nearest_to_point([data.Point(0,1,0),data.Point(2,3,0)],data.Point(0,0,0)),0)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()


