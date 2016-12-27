# Name: Audrey Chan
# Instructor: Aaron Keen
# Section: 09

import data
import vector_math
import unittest
import utility
import collisions
import cast

class DataTests(unittest.TestCase):
   def test_point1(self):
      self.assertEqual(data.Point(2, 35, -0.2), data.Point(2, 35, -0.2))
      pt = data.Point(2, 35, -0.2)
      self.assertAlmostEqual(pt.x, 2)
      self.assertAlmostEqual(pt.y, 35)
      self.assertAlmostEqual(pt.z, -0.2)

   def test_point2(self):
      self.assertEqual(data.Point(0, 0.45, 342), data.Point(0, 0.45, 342))
      pt = data.Point(0, 0.45, 342)
      self.assertAlmostEqual(pt.x, 0)
      self.assertAlmostEqual(pt.y, 0.45)
      self.assertAlmostEqual(pt.z, 342)

   def test_vector1(self):
      self.assertEqual(data.Vector(1.1, -0.2, 0), data.Vector(1.1, -0.2, 0))
      v = data.Vector(1.1, -0.2, 0)
      self.assertAlmostEqual(v.x, 1.1)
      self.assertAlmostEqual(v.y, -0.2)
      self.assertAlmostEqual(v.z, 0)

   def test_vector2(self):
      self.assertEqual(data.Vector(-2, 5.65, 23), data.Vector(-2, 5.65, 23))
      v = data.Vector(-2, 5.65, 23)
      self.assertAlmostEqual(v.x, -2)
      self.assertAlmostEqual(v.y, 5.65)
      self.assertAlmostEqual(v.z, 23)

   def test_ray1(self):
      self.assertEqual(data.Ray(data.Point(0, 5, 2), data.Vector(3, 0, -0.1)), data.Ray(data.Point(0, 5, 2), data.Vector(3, 0, -0.1)))
      rP = data.Point(0, 5, 2)
      rV = data.Vector(3, 0, -0.1)
      r = data.Ray(rP, rV)
      self.assertAlmostEqual(r.pt.x, 0)
      self.assertAlmostEqual(r.pt.y, 5)
      self.assertAlmostEqual(r.pt.z, 2)
      self.assertAlmostEqual(r.dir.x, 3)
      self.assertAlmostEqual(r.dir.y, 0)
      self.assertAlmostEqual(r.dir.z, -0.1)

   def test_ray2(self):
      self.assertEqual(data.Ray(data.Point(20, -3.3, 2), data.Vector(5, -0.2, 0)), data.Ray(data.Point(20, -3.3, 2), data.Vector(5, -0.2, 0)))
      rP = data.Point(20, -3.3, 2)
      rV = data.Vector(5, -0.2, 0)
      r = data.Ray(rP, rV)
      self.assertAlmostEqual(r.pt.x, 20)
      self.assertAlmostEqual(r.pt.y, -3.3)
      self.assertAlmostEqual(r.pt.z, 2)
      self.assertAlmostEqual(r.dir.x, 5)
      self.assertAlmostEqual(r.dir.y, -0.2)
      self.assertAlmostEqual(r.dir.z, 0)

   def test_sphere1(self):
      self.assertEqual(data.Sphere(data.Point(-1, 0, 0), 3.57, data.Color(0.0, 0.0, 0.0), data.Finish(0.4, 0.4, 0.5, 0.05)), data.Sphere(data.Point(-1, 0, 0), 3.57, data.Color(0.0, 0.0, 0.0), data.Finish(0.4, 0.4, 0.5, 0.05)))
      sphP = data.Point(-1, 0, 0)
      sphC = data.Color(0.0, 0.0, 0.0)
      sphF = data.Finish(0.4, 0.4, 0.5, 0.05)
      sph = data.Sphere(sphP, 3.57, sphC, sphF)
      self.assertAlmostEqual(sph.center.x, -1)
      self.assertAlmostEqual(sph.center.y, 0)
      self.assertAlmostEqual(sph.center.z, 0)
      self.assertAlmostEqual(sph.radius, 3.57)

   def test_sphere2(self):
      self.assertEqual(data.Sphere(data.Point(-0.4, 300, 1), 6.08, data.Color(1.0, 1.0, 1.0), data.Finish(0.4, 0.4, 0.5, 0.05)), data.Sphere(data.Point(-0.4, 300, 1), 6.08, data.Color(1.0, 1.0, 1.0), data.Finish(0.4, 0.4, 0.5, 0.05)))
      sphP = data.Point(-0.4, 300, 1)
      sphC = data.Color(1.0, 1.0, 1.0)
      sphF = data.Finish(0.4, 0.4, 0.5, 0.05)
      sph = data.Sphere(sphP, 6.08, sphC, sphF)
      self.assertAlmostEqual(sph.center.x, -0.4)
      self.assertAlmostEqual(sph.center.y, 300)
      self.assertAlmostEqual(sph.center.z, 1)
      self.assertAlmostEqual(sph.radius, 6.08)

   def test_scale_vector1(self):
      self.assertEqual(vector_math.scale_vector(data.Vector(1, 2, 3), 0), data.Vector(0, 0, 0))

   def test_scale_vector2(self):
      self.assertEqual(vector_math.scale_vector(data.Vector(-3, 4.5, 2), 2), data.Vector(-6, 9, 4))

   def test_dot_vector1(self):
      self.assertEqual(vector_math.dot_vector(data.Vector(0, 50, -1), data.Vector(-30, 1, 5)), 45)

   def test_dot_vector2(self):
      self.assertEqual(vector_math.dot_vector(data.Vector(2, -4, 21), data.Vector(-1, 0, 3)), 61)

   def test_length_vector1(self):
      self.assertAlmostEqual(vector_math.length_vector(data.Vector(1, 6, -2)), 6.403124237432)

   def test_length_vector2(self):
      self.assertEqual(vector_math.length_vector(data.Vector(0, -1, 0)), 1) 

   def test_normalize_vector1(self):
      self.assertEqual(vector_math.normalize_vector(data.Vector(1, 0, 0)), data.Vector(1, 0, 0))

   def test_normalize_vector2(self):
      self.assertEqual(vector_math.normalize_vector(data.Vector(3, 4, 5)), data.Vector(0.42426206, 0.56568542, 0.70710678))

   def test_difference_point1(self):
      self.assertEqual(vector_math.difference_point(data.Point(8, 0, -3), data.Point(1, 30, 0)), data.Vector(7, -30, -3))

   def test_difference_point2(self):
      self.assertEqual(vector_math.difference_point(data.Point(78, 31.2, 1), data.Point(4, 0.2, -3)), data.Vector(74, 31, 4))

   def test_difference_vector1(self):
      self.assertEqual(vector_math.difference_vector(data.Vector(12, -5, 0), data.Vector(1, 34, 1)), data.Vector(11, -39, -1))

   def test_difference_vector2(self):
      self.assertEqual(vector_math.difference_vector(data.Vector(-34, 17, 43), data.Vector(0, -4, 21)), data.Vector(-34, 21, 22))

   def test_translate_point1(self):
      self.assertEqual(vector_math.translate_point(data.Point(9, 0, 1), data.Point(1, 2, 3)), data.Point(10, 2, 4))

   def test_translate_point2(self):
      self.assertEqual(vector_math.translate_point(data.Point(-45, 9, 1), data.Point(0, 3, 12)), data.Point(-45, 12, 13))

   def test_vector_from_to1(self):
      self.assertEqual(vector_math.vector_from_to(data.Point(1, 0, 2), data.Point(0, 0, 3)), data.Vector(-1, 0, 1))

   def test_vector_from_to2(self):
      self.assertEqual(vector_math.vector_from_to(data.Point(45, 2, -1), data.Point(45, -1, 23)), data.Vector(0, -3, 24))

   def test_sphere_intersection_point1(self):
      self.assertEqual(collisions.sphere_intersection_point(data.Ray(data.Point(0, 2, 0), data.Vector(0, 1, 0)), data.Sphere(data.Point(0, 0, 0), 4, data.Color(0.2, 0.1, 0.2), data.Finish(0.4, 0.4, 0.5, 0.05))), data.Point(0, 4, 0))

   def test_sphere_intersection_point2(self):
      self.assertEqual(collisions.sphere_intersection_point(data.Ray(data.Point(0, 0, -15), data.Vector(0, 0, 1)), data.Sphere(data.Point(0, 0, 0),9.3, data.Color(0.0, 0.0, 0.3), data.Finish(0.4, 0.4, 0.5, 0.05))), data.Point(0, 0, -9.3))

   def test_sphere_intersection_point3(self):
      self.assertEqual(collisions.sphere_intersection_point(data.Ray(data.Point(5, 1, 9), data.Vector(1, 2, 0)), data.Sphere(data.Point(7, 4.3, 1), 2.4, data.Color(0.1, 0.1, 1.0), data.Finish(0.4, 0.4, 0.5, 0.05))), None)

   def test_sphere_intersection_point4(self):
      self.assertEqual(collisions.sphere_intersection_point(data.Ray(data.Point(4, 1, 0), data.Vector(-1, 1, 2)), data.Sphere(data.Point(-3, 8, 11), 7.5498344, data.Color(1.0, 1.0, 0.2), data.Finish(0.4, 0.4, 0.5, 0.05))), data.Point(1, 4, 6))

   def test_find_intersection_points1(self):
       s_list = [data.Sphere(data.Point(0, 0, 0), 0.1, data.Color(1.0, 1.0, 1.0), data.Finish(0.4, 0.4, 0.5, 0.05)), data.Sphere(data.Point(2, 3, 4), 2.4494897, data.Color(0.0, 0.2, 0.0), data.Finish(0.4, 0.4, 0.5, 0.05)), data.Sphere(data.Point(-3, 8, 11), 7.5498344, data.Color(0.1, 0.2, 0.3), data.Finish(0.4, 0.4, 0.5, 0.05))]
       self.assertEqual(collisions.find_intersection_points(s_list, data.Ray(data.Point(4, 1, 0), data.Vector(-1, 1, 2))), [(data.Sphere(data.Point(2, 3, 4), 2.4494897, data.Color(0.0, 0.2, 0.0), data.Finish(0.4, 0.4, 0.5, 0.05)), data.Point(3, 2, 2)), (data.Sphere(data.Point(-3, 8, 11), 7.5498344, data.Color(0.1, 0.2, 0.3), data.Finish(0.4, 0.4, 0.5, 0.05)), data.Point(1, 4, 6))])

   def test_find_intersection_points2(self):
      s_list = [data.Sphere(data.Point(0, 0, 0), 5, data.Color(0.0, 0.0, 0.0), data.Finish(0.4, 0.4, 0.5, 0.05)), data.Sphere(data.Point(-1, -1, 5), 1, data.Color(0.0, 0.0, 0.0), data.Finish(0.4, 0.4, 0.5, 0.05)), data.Sphere(data.Point(5, 5, 3), 2, data.Color(0.0, 0.0, 0.2), data.Finish(0.4, 0.4, 0.5, 0.05))]
      self.assertEqual(collisions.find_intersection_points(s_list, data.Ray(data.Point(0, 0, 0), data.Vector(1, 0, 0))), [(data.Sphere(data.Point(0, 0, 0), 5, data.Color(0.0, 0.0, 0.0), data.Finish(0.4, 0.4, 0.5, 0.05)), data.Point(5, 0, 0))])

   def test_sphere_normal_at_point1(self):
      self.assertEqual(collisions.sphere_normal_at_point(data.Sphere(data.Point(0, 0, 0), 1, data.Color(1.0, 0.3, 0.2), data.Finish(0.4, 0.4, 0.5, 0.05)), data.Point(0, 0, 1)), data.Vector(0, 0, 1))

   def test_sphere_normal_at_point2(self):
      self.assertEqual(collisions.sphere_normal_at_point(data.Sphere(data.Point(-3, 2, 5), 6, data.Color(0.0, 0.0, 0.0), data.Finish(0.4, 0.4, 0.5, 0.05)), data.Point(-3, -4, 5)), data.Vector(0, -1, 0))

   def test_cast_ray1(self):
        s_list = [data.Sphere(data.Point(0, 0, 0), 5, data.Color(0.3, 0.4, 0.2), data.Finish(0.4, 0.4, 0.5, 0.05)), data.Sphere(data.Point(-1, -1, 5), 1, data.Color(0.0, 0.0, 0.0), data.Finish(0.4, 0.0, 0.0, 0.05)), data.Sphere(data.Point(5, 5, 3), 2, data.Color(1.0, 0.3, 0.2), data.Finish(0.4, 0.4, 0.5, 0.05))]
        self.assertEqual(cast.cast_ray(data.Ray(data.Point(0, 0, 0), data.Vector(1, 0, 0)), s_list, data.Color(0.0, 0.0, 0.0), data.Light(data.Point(0.0, 0.0, 0.0), data.Color(0.0, 0.0, 0.0)), data.Point(0, 0, 0)), data.Color(0.0, 0.0, 0.0))

   def test_cast_ray2(self):
        s_list = [data.Sphere(data.Point(7, 4.3, 1), 2.4, data.Color(0.3, 0.3, 0.1), data.Finish(0.4, 0.4, 0.5, 0.05)), data.Sphere(data.Point(0, 0, 0), 1, data.Color(0.0, 0.0, 1.0), data.Finish(0.4, 0.4, 0.5, 0.05))]
        self.assertEqual(cast.cast_ray(data.Ray(data.Point(5, 1, 9), data.Vector(1, 2, 0)), s_list, data.Color(1.0, 0.0, 0.0), data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5)), data.Point(0, 0, -14)), data.Color(1.0, 1.0, 1.0))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

