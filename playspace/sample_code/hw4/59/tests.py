import unittest
import data
import vector_math
import math
import collisions
import cast

class TestData(unittest.TestCase):
   def test_cast_ray(self):
      sph1 = data.Sphere(data.Point(0, 3, 3), 5, data.Color(1.0, 1.0, 0.0), \
      data.Finish(0.5, 0.4, 0.5, 0.05))
      sph2 = data.Sphere(data.Point(5, 1, 2), 2, data.Color(0.0, 1.0, 1.0), \
      data.Finish(0.9, 0.4, 0.5, 0.05))
      sph3 = data.Sphere(data.Point(2, 2, 2), 4, data.Color(1.0, 0.0, 1.0), \
      data.Finish(0.8, 0.4, 0.5, 0.05))
      N = [sph1, sph2, sph3]

      ray1 = data.Ray(data.Point(4, 4, 4), data.Vector(-2, -2, -2))
      self.assertTrue(cast.cast_ray(ray1, N, 0.8, data.Light(data.Point(-100.0, \
      100.0, -100.0), data.Color(1.5, 1.5, 1.5)), data.Point(0.0, 0.0, -14.0)), \
      data.Color(0.8, 0.8, 0.8))

      ray2 = data.Ray(data.Point(3, 5, 1), data.Vector(-3, 1, 4))
      self.assertTrue(cast.cast_ray(ray2, N, 0.5, data.Light(data.Point(-100.0, \
      100.0, -100.0), data.Color(1.5, 1.5, 1.5)), data.Point(0.0, 0.0, -14.0)), \
      data.Color(1.0, 1.0, 1.0)) 

        
# Run unit tests
if __name__ == '__main__':
   unittest.main()
