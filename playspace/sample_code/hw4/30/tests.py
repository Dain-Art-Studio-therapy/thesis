import unittest
import cast
import data
import collisions

class TestCases(unittest.TestCase):

   def test_1(self):    #  does not hit any sphere
      r1 = data.Ray(data.Point(5, 1, -1), data.Vector(0, 0, 8))

      s1 = data.Sphere(data.Point(5, 1, -25), 1, data.Color(0, 1.0, 1.0), data.Finish(0.5, 0.4, 0.3, 0.02))
      s2 = data.Sphere(data.Point(-2, -24, -5), 11, data.Color(0, 1.0, 0), data.Finish(0.7, 0.5, 0.6, 0.01))
  
      l1 = [s1, s2]
      amb = data.Color(0.4, 0.3, 0.5)

      light = data.Light(data.Point(-3.0, 2.0, 0.0), data.Color(1.0, 1.0, 1.0))
  
      e = data.Point(5, 2, -5)

      self.assertEqual(cast.cast_ray(r1, l1, amb, light, e), data.Color(1.0, 1.0, 1.0))

   def test_2(self):    # hits sphere
      r1 = data.Ray(data.Point(0, 0, 0), data.Vector(1, 0, 0))

      s1 = data.Sphere(data.Point(-5, 0, 0), 1, data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.1, 0.5, 0.01))
      s2 = data.Sphere(data.Point(50, 0, 0), 1, data.Color(0.0, 1.0, 0.0), data.Finish(0.2, 0.2, 0.4, 0.02))
      s3 = data.Sphere(data.Point(-5, -5, -5), 1, data.Color(0.0, 0.0, 0.0), data.Finish(0.3, 0.3, 0.3, 0.03))
      s4 = data.Sphere(data.Point(5, 1, 1), 4, data.Color(0.0, 0.0, 1.0), data.Finish(0.4, 0.4, 0.4, 0.02))

      l1 = [s1, s2, s3, s4]
      amb = data.Color(0.3, 0.6, 0.9)

      light = data.Light(data.Point(-100.0, 50.0, 0.0), data.Color(1.0, 1.0, 1.0))

      e = data.Point(0.0, -5.0, 0.0)

      self.assertEqual(cast.cast_ray(r1, l1, amb, light, e), data.Color(0.001594,  0.001594, 0.652796))

      # i will test all my helper functions (calcs, add_amb, add_diff, add_spec) using this list of spheres

      l = collisions.find_intersection_points(l1, r1)      

      calc = cast.calcs(r1, l1, l, light)

      first_sphere = calc[0]
      n = calc[1] 
      p_e = calc[2] 
      l_dir = calc[3] 
      l_dir_norm = calc[4] 
      dot = calc[5] 
 
      self.assertEqual(first_sphere, s4)
      self.assertEqual(n, data.Vector(-0.93541434, -0.25, -0.25))
      self.assertEqual(p_e, data.Point(1.2489884, -0.0025, -0.0025))
      self.assertEqual(l_dir, data.Vector(-101.248988, 50.0025, 0.0025))
      self.assertEqual(l_dir_norm, data.Vector(-0.896619, 0.4428016, .00002213))
      self.assertAlmostEqual(dot, .72800487) 
 
      a = cast.add_amb(s4, amb)

      self.assertAlmostEqual(a[0], 0.0)
      self.assertAlmostEqual(a[1], 0.0)
      self.assertAlmostEqual(a[2], 0.36) 

      d = cast.add_diff(dot, light, first_sphere, p_e, l_dir, l1)
 
      self.assertAlmostEqual(d[0], 0.0)
      self.assertAlmostEqual(d[1], 0.0)
      self.assertAlmostEqual(d[2], 0.2912019)

      s = cast.add_spec(l_dir_norm, dot, n, e, p_e, first_sphere, light)

      self.assertAlmostEqual(s[0], 0.00159415)
      self.assertAlmostEqual(s[1], 0.00159415)
      self.assertAlmostEqual(s[2], 0.00159415)

   def test_3(self):
      pt1 = data.Point(0, 0, 0)
      pt2 = data.Point(0, 3, 4)
      self.assertEqual(cast.distance(pt1, pt2), 5)

   def test_4(self):
      pt1 = data.Point(4, 3, 2)
      pt2 = data.Point(8, -2, 9)
      self.assertAlmostEqual(cast.distance(pt1, pt2), 9.486832981)

   def test_5(self):
      self.assertEqual(cast.format_change(data.Color(0.4, 0.3, 0.2)), data.Color(102, 76, 51))

   def test_6(self):
      self.assertEqual(cast.format_change(data.Color(1.4, 0.7, 0.4)), data.Color(255, 178, 102))

   def test_7(self):
      self.assertEqual(cast.mindex([1, 4, 5, 34, 6, 34, 25, -4]), 7)

   def test_8(self):
      self.assertEqual(cast.mindex([0, 4, 36, 43.3, 25, -2, -25, 5]), 6)

if __name__ == '__main__':
   unittest.main()
