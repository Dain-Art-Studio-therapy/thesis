import unittest
from data import *
from vector_math import *
from collisions import *
from cast import *


class TestData(unittest.TestCase):
   def test_point_1(self):
      point1 = Point(3.063, 6.3, 4.2)
      self.assertAlmostEqual(point1.x, 3.063)
      self.assertAlmostEqual(point1.y, 6.3)
      self.assertAlmostEqual(point1.z, 4.2)


   def test_point_2(self):
      point2 = Point(14.1, 5.342, -6.1056)
      self.assertAlmostEqual(point2.x, 14.1)
      self.assertAlmostEqual(point2.y, 5.342)
      self.assertAlmostEqual(point2.z, -6.1056)


   def test_vector_1(self):
      vector1 = Vector(0.01, -5.15, -2.99)
      self.assertAlmostEqual(vector1.x, 0.01)
      self.assertAlmostEqual(vector1.y, -5.15)
      self.assertAlmostEqual(vector1.z, -2.99)


   def test_vector_2(self):
      vector2 = Vector(45.002, 10.86, 8.2)
      self.assertAlmostEqual(vector2.x, 45.002)
      self.assertAlmostEqual(vector2.y, 10.86)
      self.assertAlmostEqual(vector2.z, 8.2)


   def test_ray_1(self):
      ray1 = Ray(Point(-4.34, -2.123, 5.35), 
         Vector(30.12, 4.01, -6.7))
      self.assertAlmostEqual(ray1.pt.x, -4.34)
      self.assertAlmostEqual(ray1.pt.y, -2.123)
      self.assertAlmostEqual(ray1.pt.z, 5.35)
      self.assertAlmostEqual(ray1.dir.x, 30.12)
      self.assertAlmostEqual(ray1.dir.y, 4.01)
      self.assertAlmostEqual(ray1.dir.z, -6.7)


   def test_ray_2(self):
      ray2 = Ray(Point(15.6524, 3.65, 2.03), 
         Vector(12.11, 3.20, 4.53))
      self.assertAlmostEqual(ray2.pt.x, 15.6524)
      self.assertAlmostEqual(ray2.pt.y, 3.65)
      self.assertAlmostEqual(ray2.pt.z, 2.03)
      self.assertAlmostEqual(ray2.dir.x, 12.11)
      self.assertAlmostEqual(ray2.dir.y, 3.20)
      self.assertAlmostEqual(ray2.dir.z, 4.53)


   def test_sphere_1(self):
      sphere1 = Sphere(Point(35.2, -23.088, 21.0), 6.433, Color(0.42, 
         0.512, 0.99), Finish(0.97, 0.882, 0.545, 0.124))
      self.assertAlmostEqual(sphere1.center.x, 35.2)
      self.assertAlmostEqual(sphere1.center.y, -23.088)
      self.assertAlmostEqual(sphere1.center.z, 21.0)
      self.assertAlmostEqual(sphere1.radius, 6.433)
      self.assertAlmostEqual(sphere1.color.r, 0.42)
      self.assertAlmostEqual(sphere1.color.g, 0.512)
      self.assertAlmostEqual(sphere1.color.b, 0.99)
      self.assertAlmostEqual(sphere1.finish.ambient, 0.97)
      self.assertAlmostEqual(sphere1.finish.diffuse, 0.882)
      self.assertAlmostEqual(sphere1.finish.specular, 0.545)
      self.assertAlmostEqual(sphere1.finish.roughness, 0.124)


   def test_sphere_2(self):
      sphere2 = Sphere(Point(3.45, 10.16, 30.011), 3.777, Color(0.88, 
         0.22, 0.01), Finish(0.44, 0.012, 0.6623, 0.93))
      self.assertAlmostEqual(sphere2.center.x, 3.45)
      self.assertAlmostEqual(sphere2.center.y, 10.16)
      self.assertAlmostEqual(sphere2.center.z, 30.011)
      self.assertAlmostEqual(sphere2.radius, 3.777)
      self.assertAlmostEqual(sphere2.color.r, 0.88)
      self.assertAlmostEqual(sphere2.color.g, 0.22)
      self.assertAlmostEqual(sphere2.color.b, 0.01)
      self.assertAlmostEqual(sphere2.finish.ambient, 0.44)
      self.assertAlmostEqual(sphere2.finish.diffuse, 0.012)
      self.assertAlmostEqual(sphere2.finish.specular, 0.6623)
      self.assertAlmostEqual(sphere2.finish.roughness, 0.93)


   def test_color(self):
      c = Color(1.0, 0.33, 0.0)
      self.assertAlmostEqual(c.r, 1.0)
      self.assertAlmostEqual(c.g, 0.33)
      self.assertAlmostEqual(c.b, 0.0)


   def test_color_2(self):
      c = Color(0.66, 0.889, 0.99)
      self.assertAlmostEqual(c.r, 0.66)
      self.assertAlmostEqual(c.g, 0.889)
      self.assertAlmostEqual(c.b, 0.99)


   def test_finish(self):
      f = Finish(0.3234, 1.0, 0.54225, 0.0)
      self.assertAlmostEqual(f.ambient, 0.3234)
      self.assertAlmostEqual(f.diffuse, 1.0)
      self.assertAlmostEqual(f.specular, 0.54225)
      self.assertAlmostEqual(f.roughness, 0.0)


   def test_finish_2(self):
      f = Finish(0.699912, 0.7723, 0.534, 0.12)
      self.assertAlmostEqual(f.ambient, 0.699912)
      self.assertAlmostEqual(f.diffuse, 0.7723)
      self.assertAlmostEqual(f.specular, 0.534)
      self.assertAlmostEqual(f.roughness, 0.12)


   def test_light(self):
      l = Light(Point(-3.233, 0.9128, 43.2), Color(0.6434, 0.64, 1.0))
      self.assertAlmostEqual(l.pt.x, -3.233)
      self.assertAlmostEqual(l.pt.y, 0.9128)
      self.assertAlmostEqual(l.pt.z, 43.2)
      self.assertAlmostEqual(l.color.r, 0.6434)
      self.assertAlmostEqual(l.color.g, 0.64)
      self.assertAlmostEqual(l.color.b, 1.0)
      

   def test_light_2(self):
      l = Light(Point(9.84, -0.0012, 3.2), Color(0.0, 0.832, 0.66))
      self.assertAlmostEqual(l.pt.x, 9.84)
      self.assertAlmostEqual(l.pt.y, -0.0012)
      self.assertAlmostEqual(l.pt.z, 3.2)
      self.assertAlmostEqual(l.color.r, 0.0)
      self.assertAlmostEqual(l.color.g, 0.832)
      self.assertAlmostEqual(l.color.b, 0.66)


   def test_point_equal(self):
      pt = Point(-53.232, 1.22, -0.99)
      pt2 = Point(-53.232, 1.22, -0.99)
      self.assertEqual(pt, pt2)


   def test_point_equal_2(self):
      pt = Point(0.0001, 34.2, -0.017)
      pt2 = Point(0.0001, 34.2, -0.017)
      self.assertEqual(pt, pt2)


   def test_vector_equal(self):
      v = Vector(7.77, 23.3421, -4.53)
      v2 = Vector(7.77, 23.3421, -4.53)
      self.assertEqual(v, v2)


   def test_vector_equal_2(self):
      v = Vector(-66.34, -3.23001, 55.2)
      v2 = Vector(-66.34, -3.23001, 55.2)
      self.assertEqual(v, v2)


   def test_ray_equal(self):
      p = Point(34.233, -0.99, 12.3)
      v = Vector(15.012, 6.34, -33.2)
      r = Ray(p, v)
      p2 = Point(34.233, -0.99, 12.3)
      v2 = Vector(15.012, 6.34, -33.2)
      r2 = Ray(p2, v2)
      self.assertEqual(r, r2)


   def test_ray_equal_2(self):
      p = Point(0.3, -12.44, 2.7755)
      v = Vector(6.345, -20.1, 0.043)
      r = Ray(p, v)
      p2 = Point(0.3, -12.44, 2.7755)
      v2 = Vector(6.345, -20.1, 0.043)
      r2 = Ray(p2, v2)
      self.assertEqual(r, r2)


   def test_sphere_equal(self):
      c = Point(4.233, -6.1, 23.6)
      r = 8.65
      color1 = Color(0.301, 0.0, 0.81)
      f = Finish(0.001, 0.552, 0.6342, 0.0)
      s = Sphere(c, r, color1, f)

      c2 = Point(4.233, -6.1, 23.6)
      r2 = 8.65
      color2 = Color(0.301, 0.0, 0.81)
      f2 = Finish(0.001, 0.552, 0.6342, 0.0)
      s2 = Sphere(c2, r2, color2, f2)

      self.assertEqual(s, s2)


   def test_sphere_equal_2(self):
      c = Point(-9.834, -5.122, 1.1001)
      r = 77.3
      color1 = Color(0.623, 0.11, 1.0)
      f = Finish(0.48001, 0.992, 0.6124, 0.122)
      s = Sphere(c, r, color1, f)

      c2 = Point(-9.834, -5.122, 1.1001)
      r2 = 77.3
      color2 = Color(0.623, 0.11, 1.0)
      f2 = Finish(0.48001, 0.992, 0.6124, 0.122)
      s2 = Sphere(c2, r2, color2, f2)

      self.assertEqual(s, s2)


   def test_color_equal(self):
      c = Color(0.55, 1.0, 0.993)
      c2 = Color(0.55, 1.0, 0.993)
      self.assertEqual(c, c2)


   def test_color_equal_2(self):
      c = Color(0.6623, 0.44, 0.82)
      c2 = Color(0.6623, 0.44, 0.82)
      self.assertEqual(c, c2)


   def test_finish_equal(self):
      f = Finish(0.776, 0.2223, 0.455, 0.2366)
      f2 = Finish(0.776, 0.2223, 0.455, 0.2366)
      self.assertEqual(f, f2)


   def test_finish_equal_2(self):
      f = Finish(0.91288, 0.018, 0.122, 1.0)
      f2 = Finish(0.91288, 0.018, 0.122, 1.0)
      self.assertEqual(f, f2)


   def test_light_equal(self):
      l = Light(Point(0.38, 22.31, -4.4), Color(0.33, 0.6, 0.123))
      l2 = Light(Point(0.38, 22.31, -4.4), Color(0.33, 0.6, 0.123))
      self.assertEqual(l, l2)


   def test_light_equal_2(self):
      l = Light(Point(8.321, -10.23, 74.3), Color(0.988128, 0.323, 0.0))
      l2 = Light(Point(8.321, -10.23, 74.3), Color(0.988128, 0.323, 0.0))
      self.assertEqual(l, l2)


   def test_scale(self):
      v = Vector(-5.233, 15.2, 24.01)
      s = 4.52
      n = scale_vector(v, s)
      self.assertEqual(n, Vector(-23.65316, 68.704, 108.5252))


   def test_scale_2(self):
      v = Vector(111.23, -44.1, -0.991)
      s = -1.3201
      n = scale_vector(v, s)
      self.assertEqual(n, Vector(-146.834723, 58.21641, 1.3082191))


   def test_dot(self):
      v = Vector(-1.2433, 52.3, 96.3)
      v2 = Vector(-2.24, -14.09, 9.461)
      d = dot_vector(v, v2)
      self.assertAlmostEqual(d, 176.972292)


   def test_dot_2(self):
      v = Vector(7.6643, 6.1, -7.9)
      v2 = Vector(9.44, -52.74, 1.89)
      d = dot_vector(v, v2)
      self.assertAlmostEqual(d, -264.294008)


   def test_length(self):
      v = Vector(24.655, 96.4002, -5.12)
      l = length_vector(v)
      self.assertAlmostEqual(l, 99.6347429)


   def test_length_2(self):
      v = Vector(-3.887, 30.53, -12.491)
      l = length_vector(v)
      self.assertAlmostEqual(l, 33.2146767)


   def test_normalize(self):
      v = Vector(11.621, -6.3011, -243.12)
      n = normalize_vector(v)
      self.assertEqual(n, Vector(0.0477289, -0.02587943, -0.9985250))


   def test_normalize_2(self):
      v = Vector(-55.65, 2.8, 64.2222)
      n = normalize_vector(v)
      self.assertEqual(n, Vector(-0.6545132, 0.0329315, 0.7553330))


   def test_difference_pt(self):
      p = Point(7.334, -12.345, -0.0033)
      p2 = Point(13.23201, 5.6, -7.5)
      d = difference_point(p, p2)
      self.assertEqual(d, Vector(-5.89801, -17.945, 7.4967))


   def test_difference_pt_2(self):
      p = Point(-56.233, 18.4, 43.6)
      p2 = Point(0.06, -12.5, -55.2662)
      d = difference_point(p, p2)
      self.assertEqual(d, Vector(-56.293, 30.9, 98.8662))


   def test_difference_v(self):
      v = Vector(5.233, -7.321, 177.23)
      v2 = Vector(-62.3, 66.43, 123.5)
      d = difference_vector(v, v2)
      self.assertEqual(d, Vector(67.533, -73.751, 53.73))


   def test_difference_v_2(self):
      v = Vector(-61.209, 324.66, 1.153)
      v2 = Vector(83.38, -9.15, 9.51)
      d = difference_vector(v, v2)
      self.assertEqual(d, Vector(-144.589, 333.81, -8.357))


   def test_translate(self):
      p = Point(-3.776, 31.33, 29.4)
      v = Vector(65.63, -81.2, 3.62)
      t = translate_point(p, v)
      self.assertEqual(t, Point(61.854, -49.87, 33.02))


   def test_translate_2(self):
      p = Point(-124.74, 0.0012, 25.25)
      v = Vector(20.4, -21.3840, 4.11)
      t = translate_point(p, v)
      self.assertEqual(t, Point(-104.34, -21.3828, 29.36))


   def test_from_to(self):
      p = Point(9.22, -5.46, 124.37)
      p2 = Point(-3.4, 0.012, 37.7)
      v = vector_from_to(p, p2)
      self.assertEqual(v, Vector(-12.62, 5.472, -86.67))


   def test_from_to_2(self):
      p = Point(1.234, -885.23, 130.3554)
      p2 = Point(-6.34, -500.7, 100.004)
      v = vector_from_to(p, p2)
      self.assertEqual(v, Vector(-7.574, 384.53, -30.3514))

   
   #both t values positive
   def test_single_intersection(self):
      r = Ray(Point(-6.52, -2.25, 0.01), Vector(10.05, 12.23, 0.02))
      s = Sphere(Point(6.54, 3.224, -0.01), 10.51, Color(0.12, 0.0, 0.51), 
         Finish(0.7327, 0.332, 0.434, 0.677))
      i = sphere_intersection_point(r, s)
      self.assertEqual(i, Point(-3.7559165, 1.1136558, 0.0155007))


   #no intersection point
   def test_single_intersection_2(self):
      r = Ray(Point(19.45, -5.4, 0.51), Vector(3.233, 2.33, 3.4))
      s = Sphere(Point(-6.23, 3.123, -0.01), 11.2, Color(0.523, 0.01, 0.55),
         Finish(0.6615, 0.12, 0.656, 0.124))
      i = sphere_intersection_point(r, s)
      self.assertEqual(i, None)


   #both t values negative
   def test_single_intersection_3(self):
      r = Ray(Point(0.0, 2.5, 1.44), Vector(0.1, -7.0, -1.1))
      s = Sphere(Point(0.0, 5.0, 0.0), 2.0, Color(0.77, 0.710, 0.2), 
         Finish(0.9, 0.227, 0.7767, 0.12))
      i = sphere_intersection_point(r, s)
      self.assertEqual(i, None)


   #one negative, one positive; use non-negative
   def test_single_intersection_4(self):
      r = Ray(Point(1.5, 3.2, 1.5), Vector(-10.5, -12.7, 9.3))
      s = Sphere(Point(2.0, 4.0, 2.0), 5.0, Color(0.01, 0.0, 0.1), 
         Finish(0.11, 0.73, 0.8878, 0.23))
      i = sphere_intersection_point(r, s)
      self.assertEqual(i, Point(-0.9133425, 0.2810048, 3.6375319))


   #single root, positive
   def test_single_intersection_5(self):
      r = Ray(Point(0.0, 0.0, 3.0), Vector(-8.0, 0.0, 0.0))
      s = Sphere(Point(-8.0, 0.0, 0.0), 3.0, Color(0.63, 0.155, 0.4), 
         Finish(0.733, 0.012, 0.0, 0.122))
      i = sphere_intersection_point(r, s)
      self.assertEqual(i, Point(-8.0, 0.0, 3.0))


   #single root, negative
   def test_single_intersection_6(self):
      r = Ray(Point(2.5, 0.0, 0.0), Vector(0.0, 0.0, -5.0))
      s = Sphere(Point(0.0, 0.0, 5.0), 2.5, Color(0.9, 1.0, 0.4), 
         Finish(0.122, 0.335, 0.12994, 0.767))
      i = sphere_intersection_point(r, s)
      self.assertEqual(i, None)


   def test_all_intersections(self):
      s1 = Sphere(Point(0.0, -3.5, 0.0), 6.0, Color(0.52, 0.12, 0.6), 
         Finish(0.9, 0.382, 0.0, 1.0))
      s2 = Sphere(Point(1.25, 6.5, -4.3), 1.53, Color(0.41, 0.2, 0.1), 
         Finish(0.11, 0.7263, 0.656, 0.23))
      s3 = Sphere(Point(0.0, 0.0, 2.0), 15.0, Color(0.44, 0.3, 1.0), 
         Finish(0.43, 0.263, 0.9383, 0.482))
      spheres = [s1, s2, s3]
      r = Ray(Point(0.0, 0.0, 6.0), Vector(0.0, -7.5, 0.0))
      pts = find_intersection_points(spheres, r)
      self.assertEqual(pts, [(s1, Point(0.0, -3.5, 6.0)), 
         (s3, Point(0.0, -14.4568323, 6.0))])


   def test_all_intersections_2(self):
      s1 = Sphere(Point(6.54, 3.224, -0.01), 10.51, Color(1.0, 0.0, 0.0), 
         Finish(0.2, 0.112, 0.656, 0.1255))
      s2 = Sphere(Point(2.33, 4.51, 1.6), 5.01, Color(1.0, 0.44, 0.3), 
         Finish(0.3122, 0.4832, 0.595, 0.43))
      s3 = Sphere(Point(35.0, 15.23, -6.4), 2.23, Color(0.2, 0.1, 0.3), 
         Finish(0.77, 0.273, 0.2653, 0.3442))
      s4 = Sphere(Point(-10.23, -1.5, 1.2), 6.9, Color(0.55, 0.92, 0.0), 
         Finish(0.9, 0.223, 0.0, 0.12553))
      spheres = [s1, s2, s3, s4]
      r = Ray(Point(-6.52, -2.25, 0.01), Vector(10.05, 12.23, 0.02))
      pts = find_intersection_points(spheres, r)
      self.assertEqual(pts, [(s1, Point(-3.7559165, 1.1136558, 0.0155007)), 
         (s2, Point(-2.1857813, 3.0243776, 0.0186253)), (s4, 
         Point(-3.8896867, 0.9508688, 0.0152345))])


   def test_all_intersections_3(self):
      s1 = Sphere(Point(0.0, 7.12, 10.4), 1.01, Color(0.2, 0.11, 0.551), 
         Finish(0.12, 0.8231, 0.545, 0.125))
      s2 = Sphere(Point(-5.12, 9.012, 15.6), 5.3, Color(0.412, 0.4, 0.2), 
         Finish(0.7, 0.123, 0.567, 0.6542))
      spheres = [s1, s2]
      r = Ray(Point(5.01, -3.4, -5.12), Vector(0.1, 0.1, -6.7))
      pts = find_intersection_points(spheres, r)
      self.assertEqual(pts, [])


   def test_all_intersections_4(self):
      spheres = []
      r = Ray(Point(2.43, 12.32, -6.54), Vector(56.23, -0.12, -7.3))
      pts = find_intersection_points(spheres, r)
      self.assertEqual(pts, [])


   def test_normal(self):
      s = Sphere(Point(4.0, 0.0, 0.0), 3.0, Color(0.3, 0.133, 0.5), 
         Finish(0.166, 0.9128, 0.0, 1.0))
      p = Point(6.25, -1.5, 1.2990381)
      n = sphere_normal_at_point(s, p)
      self.assertEqual(n, Vector(0.75, -0.5, 0.4330127))


   def test_normal_2(self):
      s = Sphere(Point(-6.77, 12.33, -0.23), 15.4, Color(0.12, 0.4, 0.2), 
         Finish(0.2, 0.62, 0.3494, 0.2335))
      p = Point(-0.25, 12.01, 13.7180178)
      n = sphere_normal_at_point(s, p)
      self.assertEqual(n, Vector(0.4233766, -0.0207792, 0.9057154))

      
   def test_cast_ray(self):
      r = Ray(Point(0.0, 1.2, 4.12), Vector(-6.23, -4.32, -0.1))
      s1 = Sphere(Point(10.5, -7.34, -12.3), 0.2, Color(0.12, 0.5, 1.0), 
         Finish(0.4, 0.23, 0.125, 0.656))
      s2 = Sphere(Point(-5.66, 2.42, 3.501), 10.5, Color(0.12, 0.0, 0.5), 
         Finish(0.1, 0.2, 0.5423, 0.12))
      s3 = Sphere(Point(15.32, 5.1013, -10.66), 3.27, Color(0.32, 0.1, 0.3),
         Finish(0.93818, 0.1, 1.0, 0.11))
      s4 = Sphere(Point(-4.2301, 0.054, 4.04), 7.78, Color(0.1, 1.0, 0.32),
         Finish(0.388, 0.44, 0.545, 0.126))
      spheres = [s1, s2, s3, s4]
      c = Color(0.32, 0.0, 0.22)
      l = Light(Point(0.0, 0.0, 0.0), Color(0.33, 0.13, 0.4))
      pt = Point(0.5, 12.4, 0.5)

      test = cast_ray(r, spheres, c, l, pt)
      self.assertEqual(test, Color(0.0687911, 0.0222084, 0.0956486))
      

   def test_cast_ray_2(self):
      r = Ray(Point(-11.56, 15.634, -1.52), Vector(-0.23, 4.124, -0.88))
      s1 = Sphere(Point(5.342, 9.12, 9.9), 3.01, Color(0.998, 0.2, 0.5), 
         Finish(0.61, 0.102, 0.4, 0.12))
      s2 = Sphere(Point(7.33, -22.5015, -2.43), 5.23, Color(0.5, 0.2, 1.0),
         Finish(0.13112, 0.3, 0.0125, 0.002))
      s3 = Sphere(Point(-9.6609, -14.9, 5.67), 9.7, Color(0.12, 0.44, 0.0),
         Finish(0.53312, 0.2938, 0.129, 0.545))
      spheres = [s1, s2, s3]
      c = Color(0.66, 0.294, 0.1)
      l = Light(Point(0.532, 12.4, 5.3), Color(0.53, 0.172, 0.28))
      pt = Point(2.2, -4.12, 12.4)

      test = cast_ray(r, spheres, c, l, pt)
      self.assertEqual(test, Color(1.0, 1.0, 1.0))


   def test_cast_ray_3(self):
      r = Ray(Point(24.12, 54.2, 5.13), Vector(-6.2, 5.35, -10.99))
      spheres = []
      c = Color(0.623, 0.0, 1.0)
      l = Light(Point(0.5, 6.3, 6.2), Color(0.632, 0.12, 0.5))
      pt = Point(13.4, 0.23, 4.3)
      test = cast_ray(r, spheres, c, l, pt)
      self.assertEqual(test, Color(1.0, 1.0, 1.0))


   def test_p_e(self):
      n = Vector(0.0, 0.0, 2.2360680)
      i = Point(0.0, 2.0, 5.0)
      test = p_e(n, i)
      self.assertEqual(test, Point(0.0, 2.0, 5.0223607))


   def test_p_e_2(self):
      n = Vector(0.3333333, 0.6666667, -0.6666667)
      i = Point(5.0, 2.0, 3.0)
      test = p_e(n, i)
      self.assertEqual(test, Point(5.0033333, 2.0066667, 2.9933333))
      

   def test_l_dir(self):
      n = Vector(0.8084521, 0.5659165, -0.1616904)
      i = Point(-3.0, 0.0, 5.0)
      l = Light(Point(4.0, 2.0, 3.0), Color(0.434, 0.12, 0.53))
      test = l_dir(n, i, l)
      self.assertEqual(test, Vector(0.9272591, 0.2644870, -0.2650231))


   def test_l_dir_2(self):
      n = Vector(-0.2829276, -0.5800016, -0.7639045)
      i = Point(4.5, 6.2, 2.1)
      l = Light(Point(-1.2, 6.44, 5.3), Color(0.545, 0.776, 0.423))
      test = l_dir(n, i, l)
      self.assertEqual(test, Vector(-0.8707655, 0.03756850, 0.4902612))


   def test_visible(self):
      n = Vector(-4.12, 1.3, -6.623)
      l = Vector(0.534, 0.23, 1.434)
      test = is_visible(n, l)
      self.assertFalse(test)


   def test_visible_2(self):
      n = Vector(6.23, 1.4, 5.3)
      l = Vector(12.3, 0.54, 4.2)
      test = is_visible(n, l)
      self.assertTrue(test)


   def test_not_obscured(self):
      l_dir = Vector(0.0, 2.4494897, 0.0)
      p_e = Point(0.0, -2.3, 0.0)
      s1 = Sphere(Point(10.4, -5.32, -19.2), 0.32, Color(0.23, 0.43, 0.1),
         Finish(0.533, 0.43, 0.45, 0.02))
      s2 = Sphere(Point(0.0, 10.2, 0.0), 0.9, Color(0.54, 0.33, 0.53), 
         Finish(0.32, 0.1112, 0.5495, 0.54824))
      spheres = [s1, s2]
      test = not_obscured(l_dir, p_e, spheres)
      self.assertFalse(test)

      
   def test_not_obscured_2(self):
      l_dir = Vector(0.0, -1.0, -1.0)
      p_e = Point(0.0, 0.0, 0.0)
      s1 = Sphere(Point(23.52, 12.3, 5.23), 0.12, Color(0.634, 0.12, 0.32),
         Finish(0.12, 0.688, 0.45, 0.243))
      s2 = Sphere(Point(6.45, 10.233, 33.52), 0.9, Color(0.233, 0.912, 0.0),
         Finish(0.66, 0.12, 1.0, 0.0))
      spheres = [s1, s2]
      test = not_obscured(l_dir, p_e, spheres)
      self.assertTrue(test)

      
   def test_diffuse(self):
      light = Light(Point(0.0, 0.0, -5.0), Color(0.634, 0.12, 0.434))
      n = Vector(0.0, 1.0, 0.0)
      l = Vector(0.0, 0.001999996, -0.999998)
      p = Point(0.0, 0.01, -5.0)
      s = Sphere(Point(0.0, 0.0, 5.0), 5.0, Color(0.44, 0.224, 0.539),
         Finish(0.3212, 0.773, 0.23, 0.124))
      s1 = Sphere(Point(23.52, 12.3, 5.23), 0.12, Color(0.634, 0.12, 0.32),
         Finish(0.12, 0.688, 0.34, 0.1254))
      s2 = Sphere(Point(6.45, 10.233, 33.52), 0.9, Color(0.233, 0.912, 0.0),
         Finish(0.66, 0.12, 0.3443, 0.152))
      spheres = [s, s1, s2]
      closest = s

      test = diffuse(n, l, p, closest, spheres, light)
      self.assertEqual(test, Color(0.0004313, 0.0000416, 0.0003616))
      
            
   def test_diffuse_2(self):
      light = Light(Point(-12.43, -5.33, 0.12), Color(0.634, 0.12, 0.11))
      n = Vector(1.0, 0.0, 0.0)
      l = Vector(-0.9381688, -0.3106676, 0.1527252)
      p = Point(7.35, 1.22, -3.1)
      s = Sphere(Point(4.34, 1.22, -3.1), 3.0, Color(0.123, 0.66, 0.3),
         Finish(0.43, 0.12, 0.4342, 0.235))
      s1 = Sphere(Point(0.534, -12.44, 0.64), 12.4, Color(0.765, 0.9128, 1.0),
         Finish(0.64, 0.553, 0.434, 0.58823))
      s2 = Sphere(Point(12.34, 0.634, -42.3), 6.23, Color(0.534, 0.122, 0.0),
         Finish(0.019, 0.99, 0.23847, 0.124))
      spheres = [s, s1, s2]
      closest = s

      test = diffuse(n, l, p, closest, spheres, l)
      self.assertEqual(test, Color(0.0, 0.0, 0.0))

            
   def test_spec_intensity(self):
      n = Vector(1.344, 10.55, -5.44)
      l = Vector(9.434, -2.3, 14.3)
      p = Point(0.4, 1.4, 0.43)
      point = Point(0.434, 0.66, 0.392)

      test = spec_intensity(n, l, p, point)
      self.assertAlmostEqual(test, 1818.58427329)

      
   def test_spec_intensity_2(self):
      n = Vector(1.5, 0.44, 0.14)
      l = Vector(0.12, 0.0, 0.23)
      p = Point(0.124, 0.0, 1.0)
      point = Point(1.55, 3.3, 1.5)

      test = spec_intensity(n, l, p, point)
      self.assertAlmostEqual(test, 0.3492488)

      
   def test_specular(self):
      si = 0.545256
      closest = Sphere(Point(0.123, 0.346, -6.45), 6.662, Color(0.15, 0.5, 
         0.0), Finish(0.545, 0.166, 0.66, 1.0))
      light = Light(Point(0.5, 0.12, 1.2), Color(0.656, 0.2, 0.5))      

      test = specular(si, closest, light)
      self.assertEqual(test, Color(0.23607404, 0.07197379, 0.1799345))

      
   def test_specular_2(self):
      si = 0.1255
      closest = Sphere(Point(0.75, 34.45, 22.4), 1.30, Color(0.26, 0.77, 0.2),
         Finish(0.66, 0.93, 0.5, 0.5))
      light = Light(Point(0.25, -1.4, 0.6), Color(0.838, 0.28, 1.0))

      test = specular(si, closest, light)
      self.assertEqual(test, Color(0.0065994, 0.0022050, 0.0078751))
      

   def test_closest_sphere(self):
      r = Ray(Point(0.323, 0.112, 0.5442), Vector(0.0, -1.22, 0.323))
      s1 = Sphere(Point(0.434, 0.124, 0.343), 9.032, Color(0.434, 0.14, 0.32),
         Finish(0.434, 0.252, 0.25, 0.0))
      p1 = Point(9.466, 0.124, 0.343)
      s2 = Sphere(Point(10.44, 10.4, -34.12), 1.003, Color(0.938, 1.0, 0.434),
         Finish(0.3235, 0.124, 0.34, 0.0))
      p2 = Point(10.44, 11.4003, -34.12)
      s3 = Sphere(Point(103.44, 12.44, 4.45), 0.33, Color(0.44, 1.0, 1.0),
         Finish(0.545, 0.235, 0.443, 0.12))
      p3 = Point(103.44, 12.77, 4.45)

      intersections = [(s1, p1), (s2, p2), (s3, p3)]
      test = closest_sphere(r, intersections)
      self.assertEqual(test[0], s1)
      self.assertEqual(test[1], p1)

      
   def test_closest_sphere_2(self):
      r = Ray(Point(10.534, -12.34, 22.4), Vector(0.0, 2.0, 1.2))
      s1 = Sphere(Point(0.34, 0.2, -10.24), 6.34, Color(0.55, 0.12, 0.554),
         Finish(0.30012, 0.993, 0.12, 0.545))
      p1 = Point(0.34, 6.54, -10.24)
      s2 = Sphere(Point(10.23, -20.4, 18.2), 10.3, Color(0.33, 0.455, 0.23),
         Finish(0.43466, 0.00023, 1.0, 0.0))
      p2 = Point(10.23, -20.4, 7.9)

      intersections = [(s1, p1), (s2, p2)]
      test = closest_sphere(r, intersections)
      self.assertEqual(test[0], s2)
      self.assertEqual(test[1], p2)      
      

   def test_scale_color(self):
      c = Color(0.323, 0.12, 0.4)
      scale = 0.0
      new_color = scale_color(c, scale)
      self.assertEqual(new_color, Color(0.0, 0.0, 0.0))


   def test_scale_color_2(self):
      c = Color(0.6233, 1.0, 0.655)
      scale = 0.42
      new_color = scale_color(c, scale)
      self.assertEqual(new_color, Color(0.261786, 0.42, 0.2751))


   def test_mult_color(self):
      c = Color(0.5, 0.0, 1.0)
      c2 = Color(0.53, 1.0, 4.233)
      new_color = mult_color(c, c2)
      self.assertEqual(new_color, Color(0.265, 0.0, 4.233))


   def test_mult_color_2(self):
      c = Color(0.1242, 0.644, 1.0)
      c2 = Color(0.62, 0.99, 4.2)
      new_color = mult_color(c, c2)
      self.assertEqual(new_color, Color(0.077004, 0.63756, 4.2))


   def test_add_color(self):
      c = Color(0.4232, 0.12, 0.43)
      c2 = Color(0.11, 0.0, 0.42)
      new_color = add_color(c, c2)
      self.assertEqual(new_color, Color(0.5332, 0.12, 0.85))


   def test_add_color_2(self):
      c = Color(0.123, 1.0, 0.9912)
      c2 = Color(0.747, 0.0, 0.012)
      new_color = add_color(c, c2)
      self.assertEqual(new_color, Color(0.87, 1.0, 1.0032))


   def test_external_color(self):
      c = Color(0.0, 0.0, 0.0)
      new_color = external_color(c)
      self.assertEqual(new_color, Color(0, 0, 0))


   def test_external_color_2(self):
      c = Color(1.0, 1.0, 1.0)
      new_color = external_color(c)
      self.assertEqual(new_color, Color(255, 255, 255))


   def test_external_color_3(self):
      c = Color(0.5, 0.765, 0.211)
      new_color = external_color(c)
      self.assertEqual(new_color, Color(127, 195, 53))


if __name__ == "__main__":
   unittest.main()
