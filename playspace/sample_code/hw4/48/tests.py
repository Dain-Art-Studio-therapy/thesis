import unittest
import data
import vector_math
import cast
import collisions

class TestData(unittest.TestCase):
   def test_cast_ray_1(self):
      r1 = data.Ray(data.Point(0,0,0), data.Vector(3,0,0))
      s1 = data.Sphere(data.Point(4,0,0), 1, data.Color(0,0,0), data.Finish(0,0,0,0))
      self.assertAlmostEqual((collisions.sphere_intersection_point(r1,s1)),True)
      #answer = data.Point(3,0,0)
      #self.assertAlmostEqual((collisions.sphere_intersection_point(r1,s1)).x,answer.x)
      #self.assertAlmostEqual((collisions.sphere_intersection_point(r1,s1)).y,answer.y)
      #self.assertAlmostEqual((collisions.sphere_intersection_point(r1,s1)).z,answer.z)

   def test_sphere_intersection_point_2(self):
      r2 = data.Ray(data.Point(1,1,1), data.Vector(4,6,9))
      s2 = data.Sphere(data.Point(-4,-7,-9), 1, data.Color(0,0,0), data.Finish(0,0,0,0))
      self.assertEqual(collisions.sphere_intersection_point(r2,s2), None)
   
   def test_closest_sphere(self):
      sphere_list = [(data.Sphere(data.Point(0.0,0.0,0.0), 2.0, data.Color(1.0, 0.0, 0.0), data.Finish(0.0,0.0,0.0,0.0)))]
      ray = data.Ray(data.Point(5.0,5.0,5.0), data.Vector(0.0,0.0,0.0))
      eye_point = data.Point(5.0,5.0,5.0)
      answer = [(data.Sphere(data.Point(0.0,0.0,0.0), 2.0, data.Color(1.0, 0.0, 0.0), data.Finish(0.0,0.0,0.0,0.0)))]
      self.assertEqual(cast.closest_sphere(ray, sphere_list, eye_point), answer)
      #self.assertEqual(data.Sphere.center.y, 0)
      #self.assertEqual(data.Sphere.center.z, 0)
   
   #def test_sphere_intersection_point_3(self):
      #r3 = data.Ray(data.Point(0.0,0.0,-14.0), data.Vector(0.5,1.5,-3.0))
      #s3 = data.Sphere(data.Point(0.5,1.5,-3.0), 0.5)
      #self.assertEqual(collisions.sphere_intersection_point(r3,s3),True)

  
      
if __name__ == '__main__':
   unittest.main()
      
