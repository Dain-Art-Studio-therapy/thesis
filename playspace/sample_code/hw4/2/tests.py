import unittest
import data
import cast

class TestCases(unittest.TestCase):
   def test_cast_ray1(self):
      list = [data.Sphere(data.Point(2.0, 4.0, 8.0), float(30.0), data.Color(0, 0, 255), data.Finish(0.4, 0.4, 0.5, 0.5)), data.Sphere(data.Point(9.0, 3.0, 3.0), float(90.0), data.Color(255, 0, 0), data.Finish(0.4, 0.4, 0.3, 0.3))]
      n = cast.cast_ray(data.Ray(data.Point(3.0, 2.0, 6.0), data.Vector(1.0, 3.0, 6.0)), list, data.Color(1.0, 1.0, 1.0), data.Light(data.Point(4.0, 7.0, 10.0), data.Color(1.5, 1.5, 1.5)), data.Point(7.0, 7.0, 9.0))
      self.assertEquals(n, data.Color(2.8, 140.3, 190.9))

   def test_cast_ray2(self):
      list = [data.Sphere(data.Point(1.0, 1.0, 0.0), 20.0, data.Color(255, 0, 0), data.Finish(0.2, 0.2, 1.0, 1.0)), data.Sphere(data.Point(0.5, 1.5, -3.0), 40.0, data.Color(0, 0, 255), data.Finish(0.4, 1.0, 1.0, 0.2))]
      ray = data.Ray(data.Point(0.05859357, 2.421875, 0), data.Vector(0.05859357, 2.421875, -14.0))
      n = cast.cast_ray(ray, list, data.Color(1.0, 1.0, 1.0), data.Light(data.Point(5.0, 1.0, 1.0), data.Color(1.0, 1.0, 1.0)), data.Point(2.0, 4.0, 10.0))
      self.assertEqual(n, data.Color(255, 255, 255))

   def test_case_distance(self):
      distance = cast.distance(data.Point(1.0, 1.0, 0.0), data.Point(0.5, 1.5, -3.0))
      self.assertEqual(distance, 3.082207001484488)
   
   def test_case_distance2(self):
      distance = cast.distance(data.Point(1.0, 2.0, 3.0), data.Point(0.0, 0.0, 5.0))
      self.assertEqual(distance, 3.0)

   def test_case_mult(self):
      p = cast.multiply(data.Vector(1.0, 2.0, 3.0), 7.0)
      self.assertEqual(p, data.Vector(7.0, 14.0, 21.0))
   
   def test_case_mult1(self):
      p = cast.multiply(data.Vector(1.0, 1.0, 5.0), 2.0)
      self.assertEqual(p, data.Vector(2.0, 2.0, 10.0))

   def test_case_subt(self):
      p = cast.vec_subt(data.Vector(1.0, 3.0, 1.0), data.Vector(1.0, 2.0, 1.0))
      self.assertEqual(p, data.Vector(0.0, 1.0, 0.0))
   
   def test_case_subt1(self):
      p = cast.vec_subt(data.Vector(5.0, 4.0, 3.0), data.Vector(2.0, 2.0, 1.0))
      self.assertEqual(p, data.Vector(3.0, 2.0, 2.0))
if __name__ == '__main__':
   unittest.main()
