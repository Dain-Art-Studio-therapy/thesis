import unittest
from data import *
from vector_math import *
from collisions import *
from cast import *

class TestData(unittest.TestCase):
   def test_point_1(self):
      pt = Point(1, 2, 3)
      self.assertEqual(pt.x, 1)
      self.assertEqual(pt.y, 2)
      self.assertEqual(pt.z, 3)

   def test_point_2(self):
      pt = Point(0, -1, 1)
      self.assertEqual(pt.x, 0)
      self.assertEqual(pt.y, -1)
      self.assertEqual(pt.z, 1)

   def test_equality_point_3(self):
      pt1 = Point(1,2,3)
      pt2 = Point(1,2,3)
      self.assertEqual(pt1, pt2)

   def test_equality_point_4(self):
      pt1 = Point(4,9,2)
      pt2 = Point(8,0,3)
      self.assertNotEqual(pt1, pt2)

   def test_vector_1(self):
      vc = Vector(1, 2, 3)
      self.assertEqual(vc.x, 1)
      self.assertEqual(vc.y, 2)
      self.assertEqual(vc.z, 3)

   def test_vector_2(self):
      vc = Vector(0, -4, 6)
      self.assertEqual(vc.x, 0)
      self.assertEqual(vc.y, -4)
      self.assertEqual(vc.z, 6)

   def test_equality_vector_3(self):
      vc1 = Vector(1,2,3)
      vc2 = Vector(1,2,3)
      self.assertEqual(vc1, vc2)

   def test_equality_vector_4(self):
      vc1 = Vector(-1,5,3)
      vc2 = Vector(9,2,0)
      self.assertNotEqual(vc1, vc2)

   def test_ray_1(self):
      ray = Ray(Point(1, 2, 3), Vector(3, 2, 1))
      self.assertEqual(ray.pt.x, 1)
      self.assertEqual(ray.pt.y, 2)
      self.assertEqual(ray.pt.z, 3)
      self.assertEqual(ray.dir.x, 3)
      self.assertEqual(ray.dir.y, 2)
      self.assertEqual(ray.dir.z, 1)

   def test_ray_2(self):
      ray = Ray(Point(4, -2, 9), Vector(0, 3, -1))
      self.assertEqual(ray.pt.x, 4)
      self.assertEqual(ray.pt.y, -2)
      self.assertEqual(ray.pt.z, 9)
      self.assertEqual(ray.dir.x, 0)
      self.assertEqual(ray.dir.y, 3)
      self.assertEqual(ray.dir.z, -1)

   def test_equality_ray_3(self):
      ray1 = Ray(Point(1, 2, 3), Vector(3, 2, 1))
      ray2 = Ray(Point(1, 2, 3), Vector(3, 2, 1))
      self.assertEqual(ray1, ray2)

   def test_equality_ray_4(self):
      ray1 = Ray(Point(8, 2, 3), Vector(3, 0, 1))
      ray2 = Ray(Point(-1, 2, 3), Vector(7, 2, 1))
      self.assertNotEqual(ray1, ray2)

   def test_sphere_1(self):
      sp = Sphere(Point(1, 2, 3), 2.654, Color(1,0,1))
      self.assertEqual(sp.center.x, 1)
      self.assertEqual(sp.center.y, 2)
      self.assertEqual(sp.center.z, 3)
      self.assertAlmostEqual(sp.radius, 2.654)
      self.assertEqual(sp.color, Color(1,0,1))
    
   def test_sphere_2(self):
      sp = Sphere(Point(4, 0, -6), 8.003, Color(1,1,0))
      self.assertEqual(sp.center.x, 4)
      self.assertEqual(sp.center.y, 0)
      self.assertEqual(sp.center.z, -6)
      self.assertAlmostEqual(sp.radius, 8.003)
      self.assertEqual(sp.color, Color(1,1,0))

   def test_equality_sphere_3(self):
      sp1 = Sphere(Point(1, 2, 3), 2.654, Color(1,0,0))
      sp2 = Sphere(Point(1, 2, 3), 2.654, Color(1,0,0))
      self.assertEqual(sp1, sp2)

   def test_equality_sphere_4(self):
      sp1 = Sphere(Point(9, 3, 3), 2.654, Color(1,1,0))
      sp2 = Sphere(Point(-19, 7, 9), 6.629, Color(0,0,0))
      self.assertNotEqual(sp1, sp2)

   def test_scale_vector_1(self):
      self.assertEqual(scale_vector(Vector(1, 2, 3), 3), Vector(3, 6, 9))
      
   def test_scale_vector_2(self):
      self.assertEqual(scale_vector(Vector(5, 2, 9), 0), Vector(0, 0, 0))

   def test_dot_vector_1(self):
      self.assertEqual(dot_vector(Vector(3,6,7), Vector(0,9,-1)), 47)

   def test_dot_vector_2(self):
      self.assertEqual(dot_vector(Vector(1,-3,0), Vector(14,2,9)), 8)

   def test_length_vector_1(self):
      self.assertAlmostEqual(length_vector(Vector(1, 2, 3)), 3.741657387)

   def test_length_vector_2(self):
      self.assertAlmostEqual(length_vector(Vector(-5, 12, 28)), 30.87069808)

   def test_normalize_vector_1(self):
      self.assertEqual(normalize_vector(Vector(1, 2, 3)), Vector(1 / 3.741657387, 2 / 3.741657387, 3 / 3.741657387))

   def test_normalize_vector_2(self):
      self.assertEqual(normalize_vector(Vector(-5, 12, 28)), Vector(-5 / 30.87069808, 12 / 30.87069808, 28 / 30.87069808))

   def test_difference_point_1(self):
      self.assertEqual(difference_point(Point(1,2,3), Point(0,-5,9)), Vector(1, 7, -6))

   def test_difference_point_2(self):
      self.assertEqual(difference_point(Point(0,8,-6), Point(1,3,4)), Vector(-1, 5, -10))

   def test_difference_vector_1(self):
      self.assertEqual(difference_vector(Vector(8,7,6), Vector(1,2,3)), Vector(7,5,3))

   def test_difference_vector_2(self):
      self.assertEqual(difference_vector(Vector(-2,5,3), Vector(0,7,2)), Vector(-2,-2,1))

   def test_translate_point_1(self):
      self.assertEqual(translate_point(Point(2,4,6), Vector(0,5,9)), Point(2,9,15))

   def test_translate_point_2(self):
      self.assertEqual(translate_point(Point(4,0,1), Vector(-1,2,1)), Point(3,2,2))

   def test_vector_from_to_1(self):
      self.assertEqual(vector_from_to(Point(0,-5,9), Point(1,2,3)), Vector(1, 7, -6))

   def test_vector_from_to_2(self):
      self.assertEqual(vector_from_to(Point(1,3,4), Point(0,8,-6)), Vector(-1, 5, -10))

   def test_sphere_intersection_point_1(self):
      s = Sphere(Point(-3,-4,0),1, Color(1,0,1))
      r = Ray(Point(1,1,0),Vector(6,6,0))
      self.assertEqual(sphere_intersection_point(r,s), None)

   def test_sphere_intersection_point_2(self):
      s = Sphere(Point(0,0,0),2, Color(1,1,0))
      r = Ray(Point(0,0,2),Vector(6,6,0))
      self.assertEqual(sphere_intersection_point(r,s), Point(0,0,2))

   def test_find_intersection_points_1(self):
      s0 = Sphere(Point(0,0,0),1, Color(1,1,0))
      s1 = Sphere(Point(0,4,0),1, Color(1,0,0))
      s2 = Sphere(Point(0,-10,0),4, Color(1,1,1))
      ray = Ray(Point(0,-10,4),Vector(0,15,-3))
      self.assertEqual (find_intersection_points([s0,s1,s2], ray), [(s2, Point(0,-10,4))])

   def test_find_intersection_points_2(self):
      s0 = Sphere(Point(0,0,5),3, Color(0,0,0))
      s1 = Sphere(Point(0,0,0),1, Color(0,1,0))
      s2 = Sphere(Point(0,0,-6),3, Color(1,0,0))
      ray = Ray(Point(0,3,5),Vector(0,-11,0))
      self.assertEqual (find_intersection_points([s0,s1,s2], ray), [(s0, Point(0,3,5))], [(s2, Point(0,3,-6))])

   def test_sphere_normal_at_point_1(self):
      s = Sphere(Point(1,2,3),4, Color(0,0,1))
      pt = Point(4,5,6)
      self.assertEqual(sphere_normal_at_point(s,pt), Vector(0.5773502691896257,0.5773502691896257,0.5773502691896257))

   def test_sphere_normal_at_point_2(self):
      s = Sphere(Point(8,2,6),3, Color(1,1,1))
      pt = Point(1,7,3)
      self.assertEqual(sphere_normal_at_point(s,pt), Vector(-0.7683498199278324,0.5488212999484517,-0.329292779969071))

   def test_cast_ray_1(self):
      s0 = Sphere(Point(0,0,0),1, Color(1,0,0))
      s1 = Sphere(Point(0,4,0),1, Color(1,1,1))
      s2 = Sphere(Point(0,-10,0),4, Color(0,0,0))
      ray = Ray(Point(0,-10,4),Vector(0,15,-3))
      self.assertTrue (cast_ray(ray, [s0,s1,s2]), [(s2, Point(0,-10,4))])

   def test_cast_ray_2(self):
      s0 = Sphere(Point(0,0,0),1, Color(0,1,1))
      s1 = Sphere(Point(0,4,0),1, Color(0,0,0))
      s2 = Sphere(Point(0,-10,0),4, Color(1,1,1))
      ray = Ray(Point(0,-10,4),Vector(0,15,-3))
      self.assertTrue (cast_ray(ray, [s0,s1,s2]), [(s2, Point(0,-10,4))])
   

if __name__ == "__main__":
     unittest.main()