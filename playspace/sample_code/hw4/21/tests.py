import unittest
import data
import utility
import vector_math
import collisions
import cast
class TestData(unittest.TestCase):
   def test_point_1(self):
      p1 = data.Point(1,3,5)
      self.assertAlmostEqual(p1.x, 1)
      self.assertAlmostEqual(p1.y, 3)
      self.assertAlmostEqual(p1.z, 5)
   def test_point_2(self):
      p2 = data.Point(2,4,6)
      self.assertAlmostEqual(p2.x, 2)
      self.assertAlmostEqual(p2.y, 4)
      self.assertAlmostEqual(p2.z, 6)
   def test_vector_1(self):
      v1 = data.Vector(1.3,0,3.6)
      self.assertAlmostEqual(v1.x, 1.3)
      self.assertAlmostEqual(v1.y, 0)
      self.assertAlmostEqual(v1.z, 3.6)
   def test_vector_2(self):
      v2 = data.Vector(2.4,1.1,5.7)
      self.assertAlmostEqual(v2.x, 2.4)
      self.assertAlmostEqual(v2.y, 1.1)
      self.assertAlmostEqual(v2.z, 5.7)
   def test_ray_1(self): 
      r1 = data.Ray(data.Point(1,2,3),data.Vector(0,4,5))
      self.assertAlmostEqual(r1.pt.x, 1)
      self.assertAlmostEqual(r1.pt.y, 2)
      self.assertAlmostEqual(r1.pt.z, 3)
      self.assertAlmostEqual(r1.dir.x, 0)
      self.assertAlmostEqual(r1.dir.y, 4)
      self.assertAlmostEqual(r1.dir.z, 5)
   def test_ray_2(self):
      r2 = data.Ray(data.Point(3,1,8),data.Vector(1.2,6.4,2.3))
      self.assertAlmostEqual(r2.pt.x, 3)
      self.assertAlmostEqual(r2.pt.y, 1)
      self.assertAlmostEqual(r2.pt.z, 8)
      self.assertAlmostEqual(r2.dir.x, 1.2)
      self.assertAlmostEqual(r2.dir.y, 6.4)
      self.assertAlmostEqual(r2.dir.z, 2.3)
   def test_sphere_1(self):
      s1 = data.Sphere(data.Point(0,5,2), 3.2, data.Color(0.0,0.0,0.0),0.2)
      self.assertAlmostEqual(s1.center.x, 0)
      self.assertAlmostEqual(s1.center.y, 5)
      self.assertAlmostEqual(s1.center.z, 2)
      self.assertAlmostEqual(s1.radius, 3.2)
      self.assertAlmostEqual(s1.color.r, 0.0)
      self.assertAlmostEqual(s1.color.g, 0.0)
      self.assertAlmostEqual(s1.color.b, 0.0)
      self.assertAlmostEqual(s1.finish, 0.2)
   def test_sphere_2(self):
      s2 = data.Sphere(data.Point(1,4,6), 1.2, data.Color(1.0,0.0,0.0),0.6)
      self.assertAlmostEqual(s2.center.x, 1)
      self.assertAlmostEqual(s2.center.y, 4)
      self.assertAlmostEqual(s2.center.z, 6)
      self.assertAlmostEqual(s2.radius, 1.2)
      self.assertAlmostEqual(s2.color.r, 1.0)
      self.assertAlmostEqual(s2.color.g, 0.0)
      self.assertAlmostEqual(s2.color.b, 0.0)
      self.assertAlmostEqual(s2.finish, 0.6)
   def test_color_1(self):
      c1 = data.Color(1.0,1.0,1.0)
      self.assertAlmostEqual(c1.r, 1.0)
      self.assertAlmostEqual(c1.g, 1.0)
      self.assertAlmostEqual(c1.b, 1.0)
   def test_color_2(self):
      c2 = data.Color(0.0,0.0,0.0)
      self.assertAlmostEqual(c2.r, 0.0)
      self.assertAlmostEqual(c2.g, 0.0)
      self.assertAlmostEqual(c2.b, 0.0)
   def test_finish_1(self):
      f1 = data.Finish(0.2,0.4,0.6,0.8)
      self.assertAlmostEqual(f1.ambient, 0.2)
      self.assertAlmostEqual(f1.diffuse, 0.4)
      self.assertAlmostEqual(f1.specular, 0.6)
      self.assertAlmostEqual(f1.roughness, 0.8)
   def test_finish_2(self):
      f2 = data.Finish(0.6,0.3,0.1,0.2)
      self.assertAlmostEqual(f2.ambient, 0.6)
      self.assertAlmostEqual(f2.diffuse, 0.3)
      self.assertAlmostEqual(f2.specular, 0.1)
      self.assertAlmostEqual(f2.roughness, 0.2)
   def test_light_1(self):
      l1 = data.Light(data.Point(1,1,1), data.Color(1.0,1.0,1.0))
      self.assertAlmostEqual(l1.pt.x, 1)
      self.assertAlmostEqual(l1.pt.y, 1)
      self.assertAlmostEqual(l1.pt.z, 1)
      self.assertAlmostEqual(l1.color.r, 1.0)
      self.assertAlmostEqual(l1.color.g, 1.0)
      self.assertAlmostEqual(l1.color.b, 1.0)
   def test_light_2(self):
      l2 = data.Light(data.Point(0,0,0), data.Color(0.0,0.0,0.0))
      self.assertAlmostEqual(l2.pt.x, 0)
      self.assertAlmostEqual(l2.pt.y, 0)
      self.assertAlmostEqual(l2.pt.x, 0)
      self.assertAlmostEqual(l2.color.r, 0.0)
      self.assertAlmostEqual(l2.color.g, 0.0)
      self.assertAlmostEqual(l2.color.b, 0.0)
   def test_point_equality_1(self):
      self.assertTrue(data.Point(1,2,3) == data.Point(1,2,3))
      self.assertFalse(data.Point(3,5,7) == data.Point(9,0,2))
   def test_point_equality_2(self):
      self.assertTrue(data.Point(5,8,3) == data.Point(5,8,3))
      self.assertFalse(data.Point(0,3,0) == data.Point(6,4,5))
   def test_vector_equality_1(self):
      self.assertTrue(data.Vector(1,4,3) == data.Vector(1,4,3))
      self.assertFalse(data.Vector(5,3,8) == data.Vector(9,9,9))
   def test_vector_equality_2(self):
      self.assertTrue(data.Vector(0,0,0) == data.Vector(0,0,0))
      self.assertFalse(data.Vector(4,2,1) == data.Vector(8,4,0))
   def test_ray_equality_1(self):
      self.assertTrue(data.Ray(data.Point(1,2,3),data.Vector(4,5,6)) == data.Ray(data.Point(1,2,3),data.Vector(4,5,6)))
      self.assertFalse(data.Ray(data.Point(7,4,2),data.Vector(1,5,3)) == data.Ray(data.Point(5,0,9),data.Vector(1,1,1)))
   def test_ray_equality_2(self):
      self.assertTrue(data.Ray(data.Point(5,5,5),data.Vector(4,4,4)) == data.Ray(data.Point(5,5,5),data.Vector(4,4,4)))
      self.assertFalse(data.Ray(data.Point(3,2,4),data.Vector(9,8,7)) == data.Ray(data.Point(5,3,7),data.Vector(9,3,0)))
   def test_sphere_equality_1(self):
      self.assertTrue(data.Sphere(data.Point(1,2,3), 6.5, data.Color(0.0,0.0,0.0),0.1) == data.Sphere(data.Point(1,2,3), 6.5, data.Color(0.0,0.0,0.0),0.1))
      self.assertFalse(data.Sphere(data.Point(9,4,6), 1.1, data.Color(0.0,1.0,0.0),0.9) == data.Sphere(data.Point(3,3,3), 9.6, data.Color(1.0,0.0,0.0),0.4))
   def test_sphere_equality_2(self):
      self.assertTrue(data.Sphere(data.Point(6,2,1), 2.3, data.Color(0.0,0.0,0.0),0.5) == data.Sphere(data.Point(6,2,1), 2.3, data.Color(0.0,0.0,0.0),0.5))
      self.assertFalse(data.Sphere(data.Point(1,6,8), 4.4, data.Color(1.0,0.0,0.0),0.3) == data.Sphere(data.Point(9,4,5), 1.2, data.Color(0.0,0.0,1.0),0.7))
   def test_color_equality_1(self):
      self.assertTrue(data.Color(0.0,0.0,0.0) == data.Color(0.0,0.0,0.0))
      self.assertFalse(data.Color(1.0,0.0,0.0) == data.Color(0.0,1.0,0.0))
   def test_color_equality_2(self):
      self.assertTrue(data.Color(1.0,0.0,1.0) == data.Color(1.0,0.0,1.0))
      self.assertFalse(data.Color(0.0,0.0,0.0) == data.Color(0.4,0.2,0.0))
   def test_finish_equality_1(self):
      self.assertTrue(data.Finish(0.2,0.2,0.2,0.2) == data.Finish(0.2,0.2,0.2,0.2))
      self.assertFalse(data.Finish(0.4,0.1,0.0,0.0) == data.Finish(0.8,0.9,0.0,0.0))
   def test_finish_equality_2(self):
      self.assertTrue(data.Finish(0.1,0.9,0.0,0.0) == data.Finish(0.1,0.9,0.0,0.0))
      self.assertFalse(data.Finish(0.9,0.2,0.0,0.0) == data.Finish(0.2,0.6,0.0,0.0))
   def test_light_equality_1(self):
      self.assertTrue(data.Light(data.Point(0,0,0), data.Color(0.0,0.0,0.0)) == data.Light(data.Point(0,0,0), data.Color(0.0,0.0,0.0)))
      self.assertFalse(data.Light(data.Point(1,1,1), data.Color(1.0,0.0,0.0)) == data.Light(data.Point(3,1,7), data.Color(0.0,1.0,0.0)))
   def test_light_equality_2(self):
      self.assertTrue(data.Light(data.Point(4,5,6), data.Color(1.0,1.0,1.0)) == data.Light(data.Point(4,5,6), data.Color(1.0,1.0,1.0)))
      self.assertFalse(data.Light(data.Point(9,9,9), data.Color(0.0,0.0,0.0)) == data.Light(data.Point(2,0,0), data.Color(1.0,0.0,0.0)))
   def test_scale_vector(self):
      vector1 = data.Vector(1,2,3)
      vector2 = data.Vector(4,0,1)
      self.assertEqual(vector_math.scale_vector(vector1, 2), data.Vector(2,4,6))
      self.assertEqual(vector_math.scale_vector(vector2, 3), data.Vector(12,0,3))
   def test_dot_vector(self):
      self.assertEqual(vector_math.dot_vector(data.Vector(1,1,1),data.Vector(2,2,2)), 6)
      self.assertEqual(vector_math.dot_vector(data.Vector(5,3,0),data.Vector(1,3,2)), 14)
   def test_length_vector(self):
      self.assertEqual(vector_math.length_vector(data.Vector(1,2,2)), 3)
      self.assertEqual(vector_math.length_vector(data.Vector(0,4,0)), 4)
   def test_normalize_vector(self):
      self.assertEqual(vector_math.normalize_vector(data.Vector(9,0,0)), data.Vector(1,0,0))
      self.assertEqual(vector_math.normalize_vector(data.Vector(0,4,0)), data.Vector(0,1,0))
   def test_difference_point(self):
      self.assertEqual(vector_math.difference_point(data.Point(5,5,5),data.Point(1,1,1)), data.Point(4,4,4))
      self.assertEqual(vector_math.difference_point(data.Point(3,2,6),data.Point(0,2,1)), data.Point(3,0,5))
   def test_difference_vector(self):
      self.assertEqual(vector_math.difference_point(data.Vector(8,8,8),data.Vector(3,3,3)), data.Vector(5,5,5))
      self.assertEqual(vector_math.difference_point(data.Vector(9,6,1),data.Vector(2,5,0)), data.Vector(7,1,1))
   def test_translate_point(self):
      self.assertEqual(vector_math.translate_point(data.Point(2,1,0),data.Vector(5,3,1)), data.Point(7,4,1))
      self.assertEqual(vector_math.translate_point(data.Point(3,1,5),data.Vector(1,1,1)), data.Point(4,2,6))
   def test_vector_from_to(self):
      self.assertEqual(vector_math.vector_from_to(data.Point(0,0,0),data.Point(2,2,2)), data.Vector(2,2,2))
      self.assertEqual(vector_math.vector_from_to(data.Point(0,2,6),data.Point(9,3,7)), data.Vector(9,1,1))
   def test_sphere_intersection_point_1(self):
      r1 = data.Ray(data.Point(0,0,0), data.Vector(3,0,0))
      s1 = data.Sphere(data.Point(3,0,0), 2, data.Color(0.0,0.0,0.0),0.3)
      self.assertEqual(collisions.sphere_intersection_point(r1,s1), data.Point(1,0,0))
   def test_sphere_intersection_point_2(self):
      r2 = data.Ray(data.Point(1,4,2), data.Vector(0,6,0))
      s2 = data.Sphere(data.Point(3,3,3), 5, data.Color(0.0,0.0,0.0),0.2)
      self.assertEqual(collisions.sphere_intersection_point(r2,s2), data.Point(1,7.472135,2))
   def test_find_intersection_points_1(self):
      r1 = data.Ray(data.Point(0,0,0), data.Vector(8,0,0))
      sl1 = [data.Sphere(data.Point(3,0,0), 1, data.Color(0.0,0.0,0.0),0.1), data.Sphere(data.Point(0,8,2), 2, data.Color(0.0,0.0,0.0),0.5), data.Sphere(data.Point(8,0,0), 4, data.Color(0.0,0.0,0.0),0.8)]
      self.assertEqual(collisions.find_intersection_points(sl1,r1), [(data.Sphere(data.Point(3,0,0), 1, data.Color(0.0,0.0,0.0),0.1),data.Point(2,0,0)), (data.Sphere(data.Point(8,0,0), 4, data.Color(0.0,0.0,0.0),0.8), data.Point(4,0,0))])
   def test_find_intersection_points_2(self):
      r2 = data.Ray(data.Point(4,0,0), data.Vector(0,4,0))
      sl2 = [data.Sphere(data.Point(4,4,0), 2, data.Color(0.0,0.0,0.0),0.2), data.Sphere(data.Point(20,45,2), 2, data.Color(0.0,0.0,0.0),0.9)]
      self.assertEqual(collisions.find_intersection_points(sl2,r2), [(data.Sphere(data.Point(4,4,0), 2, data.Color(0.0,0.0,0.0),0.2),data.Point(4,2,0))])
   def test_sphere_normal_at_point_1(self):
      s1 = data.Sphere(data.Point(0,0,0), 3, data.Color(0.0,0.0,0.0),0.5)
      p1 = data.Point(3,0,0)
      self.assertEqual(collisions.sphere_normal_at_point(s1,p1), data.Vector(1,0,0))
   def test_sphere_normal_at_point_2(self):
      s2 = data.Sphere(data.Point(0,0,0), 4, data.Color(0.0,0.0,0.0),0.3)
      p2 = data.Point(0,4,0)
      self.assertEqual(collisions.sphere_normal_at_point(s2,p2), data.Vector(0,1,0))
   def test_cast_ray_1(self):
      r1 = data.Ray(data.Point(0,0,0), data.Vector(4,0,0))
      sl1 = [data.Sphere(data.Point(2,0,0), 1, data.Color(0.0,0.0,0.0),0.2), data.Sphere(data.Point(4,6,5), 2, data.Color(0.0,0.0,0.0),0.4)]
      c1 = data.Color(0.0,0.0,0.0)
      l1 = data.Light(data.Point(4,0,4),data.Color(1.0,1.0,1.0))
      ep1 = data.Point(0.0,0.0,-4.0)
      self.assertEqual(cast.cast_ray(r1,sl1,c1,l1,ep1), data.Sphere(data.Point(2,0,0), 1, data.Color(0.0,0.0,0.0),0.2))
   def test_cast_ray_2(self):
      r2 = data.Ray(data.Point(0,0,0), data.Vector(0,4,0))
      sl2 = [data.Sphere(data.Point(8,0,0), 2, data.Color(0.0,0.0,0.0),0.7), data.Sphere(data.Point(6,7,9), 1, data.Color(0.0,0.0,0.0),0.1)]
      self.assertEqual(cast.cast_ray(r2,sl2,data.Color(1.0,1.0,1.0)), data.Sphere(data.Point(8,0,0), 2, data.Color(0.0,0.0,0.0)))


if __name__ == "__main__":
     unittest.main()
