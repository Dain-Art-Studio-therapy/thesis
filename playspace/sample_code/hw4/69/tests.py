from cast import *
import data
import unittest

sphere1 = data.Sphere(data.Point(0, 0, 0), 3, Color(1.0, 0, 0), Finish(0.2, 0.4, 0.5, 0.05))
sphere2 = data.Sphere(data.Point(5, 5, 5), 1, Color(0, 1.0, 0), Finish(0.2, 0.2, 0.5, 0.05))
sphere3 = data.Sphere(data.Point(0, 12, 0), 2, Color(0, 0, 1.0), Finish(0.1, 0.1, 0.5, 0.05))
sphere4 = data.Sphere(data.Point(6, 0, 0), 2, Color(0.47, 0, 0), Finish(0.8, 0.97, 0.5, 0.05))
sphere5 = data.Sphere(data.Point(12, 12, 12), 3, Color(0, 0.47, 0), Finish(0.4, 0.2, 0.5, 0.05))

raya = data.Ray(data.Point(-5, 0, 0), data.Vector(4, 0, 0))
rayb = data.Ray(data.Point(100, 0, 0), data.Vector(3, 0, 0))
rayc = data.Ray(data.Point(1, 1, 1), data.Vector(1, 1, 1))

rayd = Ray(Point(0, 0, -14), Vector(0, 0, 2))
other_list = [Sphere(Point(0, 0, 0), 2, Color(1.0, 0, 0), Finish(0.2, 0.2, 0.5, 0.05)), Sphere(Point(0, 0, -4), 
   1, Color(0, 1.0, 0), Finish(0.2, 0.2, 0.5, 0.05))]

sphere_list = [sphere1, sphere2, sphere3, sphere4, sphere5]

light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))

class TestData(unittest.TestCase):
   def test_cast_ray(self):
      #cast_ray(ray, sphere_list, amcolor, light, eyept)
      self.assertEqual(cast_ray(raya, sphere_list, Color(1.0, 1.0, 1.0), light, Point(0, 0, -14)), Color(0.53935, 0.0, 0.0))
      self.assertEqual(cast_ray(rayb, sphere_list, Color(1.0, 1.0, 1.0), light, Point(0, 0, -14)), Color(1.0, 1.0, 1.0))
      self.assertEqual(cast_ray(rayc, sphere_list, Color(1.0, 1.0, 1.0), light, Point(0, 0, -14)), Color(0.2, 0.0, 0.0))

   def test_closest_sphere(self):
      self.assertEqual(closest_sphere(find_intersection_points(
         sphere_list, raya), data.Point(-5,0,0)), sphere1)
      self.assertEqual(closest_sphere(find_intersection_points(
         other_list, rayd), data.Point(0, 0, -14)), Sphere(Point(0, 0, -4), 
      1, Color(0, 1.0, 0), Finish(0.2, 0.2, 0.5, 0.05)))

   def test_color_scale(self):
      self.assertEqual(color_scale(0.5), 127)
      self.assertEqual(color_scale(2.3), 255)
      self.assertEqual(color_scale(0), 0)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()