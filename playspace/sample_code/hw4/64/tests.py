import unittest
from cast import *
from data import *
from collisions import *

class TestCases(unittest.TestCase):

   def test_cast_ray_1(self):
      s1 = Sphere(Point(0, 5, 0), 3, Color(0.5, 0.5, 0.5), Finish(0.5, 0.2, 0.05, 0.2))
      s2 = Sphere(Point(-10, -5, -2), 3, Color(0.3, .23, 1.0), Finish(0.1, 1.0, 0.5, 0.8))
      sphere_list = [s1, s2]
      r = Ray(Point(0, 0, 0), Vector(0, 1, 0))
      color = cast_ray(r, sphere_list, Color(0.5, 0.8, 0.0), Light(Point(0, -1, 1), Color(1.5, 1.5, 1.5)), Point(-1, 1, -1))
      self.assertEqual(color, Color(0.28254944, 0.35754944, 0.15754944))

   def test_cast_ray_2(self):
      s1 = Sphere(Point(34, 5, 6), 2, Color(.32, .4, 0.3), Finish(1.0, 0.0, 1.0, 0.5))
      s2 = Sphere(Point(0, 0, 0), 3, Color(.1, .9, .32), Finish(.9, .80, 0.0, 0.1))
      sphere_list = [s1, s2]
      r = Ray(Point(-7, -45, 8), Vector(0, -1, -1))
      color = cast_ray(r, sphere_list, Color(0.0, 1.0, 0.0), Light(Point(9, -3, 4), Color(1.5, 1.5, 1.5)), Point(1, -15, 15))
      self.assertEqual(color, Color(1.0, 1.0, 1.0))


   # Color fcns ************
   def test_combine_colors_1(self):
      colors= [Color(0.1, 0.3, 0.1), Color(0.5, 0.0, 0.0), Color(0.0, 0.2, 0.2)]
      self.assertEqual(combine_colors(colors), Color(0.6, 0.5, 0.3))

   def test_combine_colors_2(self):
      colors= []
      self.assertEqual(combine_colors(colors), Color(0.0, 0.0, 0.0))

   def test_scale_color_1(self):
      color = Color(0.1, 0.2, 0.3)
      vals = [2, 3]
      self.assertEqual(scale_color(color, vals), Color(.6, 1.2, 1.8))

   def test_scale_color_2(self):
      color = Color(0.1, 0.2, 0.3)
      vals = []
      self.assertEqual(scale_color(color, vals), Color(0.1, 0.2, 0.3))

   def test_mult_colors_1(self):
      c1 = Color(1.0, 1.0, 1.0)
      c2 = Color(0.0, 0.5, 0.2)
      self.assertEqual(mult_colors(c1, c2), Color(0.0, 0.5, 0.2))

   def test_mult_colors_2(self):
      c1 = Color(0.5, 0.0, 0.1)
      c2 = Color(.5, 0.5, 10.0)
      self.assertEqual(mult_colors(c1, c2), Color(.25, 0.0, 1.0))


   # Cast ray sub fcns
   def test_light_info_1(self):
      pass

   def test_find_closest_1(self):
      s1 = Sphere(Point(0, 5, 0), 3, Color(0.5, 0.5, 0.5), Finish(0.5, 0.2, 0.05, 0.2))
      s2 = Sphere(Point(-10, -5, -2), 3, Color(0.3, .23, 1.0), Finish(0.1, 1.0, 0.5, 0.8))
      sect_pts = [(s1, Point(0.0, 5.0, 1.0)), (s2, Point(100.0, -50.0, 6.0))]
      closest_sect \
         = find_closest_intersection_vals(sect_pts, Ray(Point(10.0, 10.0, 10.0), Vector(-1.0, -1.0, -1.0)))
      self.assertEqual(closest_sect, sect_pts[0])

   def test_find_closest_2(self):
      s1 = Sphere(Point(0, 5, 0), 3, Color(0.5, 0.5, 0.5), Finish(0.5, 0.2, 0.05, 0.2))
      s2 = Sphere(Point(-10, -5, -2), 3, Color(0.3, .23, 1.0), Finish(0.1, 1.0, 0.5, 0.8))
      sect_pts = [(s1, Point(0.0, 5.0, 1.0)), (s2, Point(100.0, -50.0, 6.0))]
      closest_sect \
         = find_closest_intersection_vals(sect_pts, Ray(Point(90.0, -40.0, 10.0), Vector(-1.0, -1.0, -1.0)))
      self.assertEqual(closest_sect, sect_pts[1])

   def test_distance_between_pts_1(self):
      dist = distance_between_points(Point(0, 0, 0), Point(3.0, -4.0, 0))
      self.assertEqual(dist, 5.0)

   def test_distance_between_pts_2(self):
      dist = distance_between_points(Point(3.0, -4.0, 0.0), Point(3.0, -4.0, 0.0))
      self.assertEqual(dist, 0.0)



# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
