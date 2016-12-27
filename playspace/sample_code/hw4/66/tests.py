import unittest
import utility
import data
import vector_math
import collisions
import cast

class TestData(unittest.TestCase):
   '''
   def test_point_1(self):
        point1 = data.Point(7, 3, -2.0)
        self.assertEqual(point1.x, 7)
        self.assertEqual(point1.y, 3)
        self.assertAlmostEqual(point1.z, -2.0)
   def test_vector_1(self):
        vector1 = data.Vector(-2.333, 8889, 10)
        self.assertAlmostEqual(vector1.x, -2.333)
        self.assertEqual(vector1.y, 8889)
        self.assertEqual(vector1.z, 10)
   def test_ray_1(self):
        ray1 = data.Ray(data.Point(61852, -3.2, 0), data.Vector(2.2, 3.0, 8))
        self.assertEqual(ray1.pt.x, 61852)
        self.assertAlmostEqual(ray1.pt.y, -3.2)
        self.assertEqual(ray1.pt.z, 0)
        self.assertAlmostEqual(ray1.dir.x, 2.2)
        self.assertAlmostEqual(ray1.dir.y, 3.0)
        self.assertEqual(ray1.dir.z, 8)
   def test_sphere_1(self):
        sphere1 = data.Sphere(data.Point(35, 0, -5), 3.7, data.Color(0,0,0), data.Finish(0))
        self.assertEqual(sphere1.center.x, 35)
        self.assertEqual(sphere1.center.y, 0)
        self.assertEqual(sphere1.center.z, -5)
        self.assertAlmostEqual(sphere1.radius, 3.7)
   def test_point_2(self):
        point2 = data.Point(2, 2.3, 7.89)
        self.assertEqual(point2.x, 2)
        self.assertAlmostEqual(point2.y, 2.3)
        self.assertAlmostEqual(point2.z, 7.89)
   def test_vector_2(self):
        vector2 = data.Vector(999, 3.2, -2)
        self.assertEqual(vector2.x, 999)
        self.assertAlmostEqual(vector2.y, 3.2)
        self.assertEqual(vector2.z, -2)
   def test_ray_2(self):
        ray2 = data.Ray(data.Point(3.22, -2.0, 3.6), data.Vector(6, 10, 369))
        self.assertAlmostEqual(ray2.pt.x, 3.22)
        self.assertAlmostEqual(ray2.pt.y, -2.0)
        self.assertAlmostEqual(ray2.pt.z, 3.6)
        self.assertEqual(ray2.dir.x, 6)
        self.assertEqual(ray2.dir.y, 10)
        self.assertEqual(ray2.dir.z, 369)
   def test_sphere_2(self):
        sphere2 = data.Sphere(data.Point(99, -0.2, -100), 0, data.Color(1,0,0), data.Finish(0))
        self.assertEqual(sphere2.center.x, 99)
        self.assertAlmostEqual(sphere2.center.y, -0.2)
        self.assertEqual(sphere2.center.z, -100)
        self.assertEqual(sphere2.radius, 0)
   def test_point_eq1(self):
        self.assertEqual(data.Point(3.000001, 6.000001, 4.999999), data.Point(2.999999, 5.999999, 5.000001))
   def test_point_eq2(self):
        self.assertEqual(data.Point(-2.499999, -0.999999, 13.000001), data.Point(-2.500001, -1.000001, 12.999999))
   def test_vector_eq1(self):
        self.assertEqual(data.Vector(3.000001, 6.000001, 4.999999), data.Vector(2.999999, 5.999999, 5.000001))
   def test_vector_eq2(self):
        self.assertEqual(data.Vector(-2.499999, -0.999999, 13.000001), data.Vector(-2.500001, -1.000001, 12.999999))
   def test_ray_eq1(self):
        self.assertEqual(data.Ray(data.Point(3.000001, 6.000001, 4.999999), 5.000001), data.Ray(data.Point(2.999999, 5.999999, 5.000001), 4.999999))
   def test_ray_eq2(self):
        self.assertEqual(data.Ray(data.Point(-2.499999, -0.999999, 13.000001), -2.999999), data.Ray(data.Point(-2.500001, -1.000001, 12.999999), -3.000001))
   def test_sphere_eq1(self):
        self.assertEqual(data.Sphere(data.Point(3.000001, 6.000001, 4.999999), 5.000001, data.Color(0,0,0)), data.Sphere(data.Point(2.999999, 5.999999, 5.000001), 4.999999, data.Color(0,0,0)))
   def test_sphere_eq2(self):
        self.assertEqual(data.Sphere(data.Point(-2.499999, -0.999999, 13.000001), -2.999999, data.Color(1,0,0)), data.Sphere(data.Point(-2.500001, -1.000001, 12.999999), -3.000001, data.Color(1,0,0)))
   def test_vector_scale1(self):
        self.assertEqual(vector_math.scale_vector(data.Vector(0, 2, -3), 4), data.Vector(0, 8, -12))
   def test_vector_scale2(self):
        self.assertEqual(vector_math.scale_vector(data.Vector(-1, 4, 2.1), 10), data.Vector(-10, 40, 21))
   def test_dot_vector1(self):
        self.assertEqual(vector_math.dot_vector(data.Vector(1, 2, 3), data.Vector(4, 5, 6)), 32)
   def test_dot_vector2(self):
        self.assertEqual(vector_math.dot_vector(data.Vector(4, 3, 1), data.Vector(7, 2, 0)), 34)
   def test_length_vector1(self):
        self.assertEqual(vector_math.length_vector(data.Vector(4, 2, 4)), 6)
   def test_length_vector2(self):
        self.assertEqual(vector_math.length_vector(data.Vector(6, 3, 2)), 7)
   def test_normalize_vector1(self):
        self.assertEqual(vector_math.normalize_vector(data.Vector(4, 2, 4)), data.Vector(0.6666666, 0.3333333, 0.6666666))
   def test_normalize_vector2(self):
        self.assertEqual(vector_math.normalize_vector(data.Vector(6, 3, 2)), data.Vector(0.8571428, 0.4285714, 0.2857142))
   def test_point_diff1(self):
        self.assertEqual(vector_math.difference_point(data.Point(4, 5, 6), data.Point(1, 2, 3)), data.Vector(3, 3, 3))
   def test_point_diff2(self):
        self.assertEqual(vector_math.difference_point(data.Point(7, 2, 1), data.Point(4, 6, 9)), data.Vector(3, -4, -8))
   def test_vect_diff1(self):
        self.assertEqual(vector_math.difference_vector(data.Vector(4, 5, 6), data.Vector(1, 2, 3)), data.Vector(3, 3, 3))
   def test_vect_diff2(self):
        self.assertEqual(vector_math.difference_vector(data.Vector(7, 2, 1), data.Vector(4, 6, 9)), data.Vector(3, -4, -8))
   def test_trans_point1(self):
        self.assertEqual(vector_math.translate_point(data.Point(4, 5, 6), data.Vector(1, 2, 3)), data.Point(5, 7, 9))
   def test_trans_point2(self):
        self.assertEqual(vector_math.translate_point(data.Point(7, 2, 1), data.Vector(4, 6, 9)), data.Point(11, 8, 10))
   def test_vector_from_to1(self):
         self.assertEqual(vector_math.vector_from_to(data.Point(1, 2, 3), data.Point(4, 5, 6)), data.Vector(3, 3, 3))
   def test_vector_from_to2(self):
         self.assertEqual(vector_math.vector_from_to(data.Point(4, 6, 9), data.Point(7, 2, 1)), data.Vector(3, -4, -8))
   def test_sphere_intersection_point1(self):
         self.assertEqual(collisions.sphere_intersection_point(data.Ray(data.Point(3,0,0), data.Vector(1,0,0)), data.Sphere(data.Point(10,0,0), 2, data.Color(0,0,0), data.Finish(0))), data.Point(8,0,0))
   def test_sphere_intersection_point2(self):                                                                                                                                      
         self.assertEqual(collisions.sphere_intersection_point(data.Ray(data.Point(4,3,2), data.Vector(1,4,3)), data.Sphere(data.Point(16,12,8), 8, data.Color(1,0,0), data.Finish(0))), None)
   def test_find_intersection_points1(self):
         self.assertEqual(collisions.find_intersection_points([data.Sphere(data.Point(0,0,0), 1, data.Color(0,0,0), data.Finish(0)), data.Sphere(data.Point(4,0,0), 1, data.Color(0,0,0), data.Finish(0))], data.Ray(data.Point(5,0,0), data.Vector(1,0,0))), [(data.Sphere(data.Point(4,0,0),1, data.Color(0,0,0), data.Finish(0)), data.Point(5,0,0))])
   def test_find_intersection_points2(self):
         self.assertEqual(collisions.find_intersection_points([data.Sphere(data.Point(3.0,2.0,5.0), 4.0, data.Color(0,0,0), data.Finish(0)), data.Sphere(data.Point(8.0,2.0,1.0), 3.0, data.Color(0,0,0), data.Finish(0))], data.Ray(data.Point(3.0,1.0,1.0), data.Vector(4.0,1.0,2.0))), [(data.Sphere(data.Point(3,2,5), 4, data.Color(0,0,0), data.Finish(0)), data.Point(3.238863,1.059715,1.119431)), (data.Sphere(data.Point(8,2,1), 3, data.Color(0,0,0), data.Finish(0)), data.Point(5.254256,1.563564,2.127128))])
   def test_sphere_normal_at_point1(self):
         self.assertEqual(collisions.sphere_normal_at_point(data.Sphere(data.Point(10,0,0), 2, data.Color(0,0,0), data.Finish(0)), data.Point(8,0,0)), data.Point(-1,0,0))
   def test_sphere_normal_at_point2(self):
         self.assertEqual(collisions.sphere_normal_at_point(data.Sphere(data.Point(5,4,-1), 7, data.Color(0,0,0), data.Finish(0)), data.Point(6.5119768,9.0239536,3.6339826)), data.Point(0.2159967,0.7177078,0.6619976))
   def test_cast_ray1(self):
         self.assertEqual(cast.cast_ray(data.Ray(data.Point(5,0,0), data.Vector(1,0,0)), [data.Sphere(data.Point(3.0,2.0,5.0), 4.0, data.Color(0,0,0), data.Finish(0,0)), data.Sphere(data.Point(8.0,2.0,1.0), 3.0, data.Color(0,0,0), data.Finish(0,0))], 0, 0), data.Color(0,0,0))
   def test_cast_ray2(self):
         self.assertEqual(cast.cast_ray(data.Ray(data.Point(5,0,0), data.Vector(1,0,0)), [data.Sphere(data.Point(0,0,0), 1, data.Color(0,0,0), data.Finish(0,0)), data.Sphere(data.Point(4,0,0), 1, data.Color(0,0,0), data.Finish(0,0))], 0, 0), data.Color(0,0,0))
'''

if __name__ == "__main__":
     unittest.main()

