import unittest
from cast import *


class TestData(unittest.TestCase):
   def test_cast_ray_1(self):
      ray = Ray(Point(0, 0, 0), Vector(10, 0, 0))
      sphere_1 = Sphere(Point(1.0, 1.0, 0.0), 2.0, Color(0.0, 0.0, 1.0), Finish(0.2, 0.4, 0.5, 0.05))
      sphere_2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0), Finish(0.4, 0.4, 0.5, 0.05))
      sphere_list = [sphere_1, sphere_2]
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      color = cast_ray(ray, sphere_list, Color(1, 1, 1), light)
      self.assertTrue(color == Color(0.0, 0.0, 0.2))

   def test_cast_ray_2(self):
      ray = Ray(Point(0, 0, -5), Vector(0, 0, 1))
      sphere_1 = Sphere(Point(1.0, 1.0, 0.0), 2.0, Color(0.0, 0.0, 1.0), Finish(0.2, 0.4, 0.5, 0.05))
      sphere_2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0), Finish(0.4, 0.4, 0.5, 0.05))
      sphere_list = [sphere_1, sphere_2]
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      color = cast_ray(ray, sphere_list, Color(1, 1, 1), light)
      self.assertTrue(color == Color(0.0, 0.0, 0.442594))

   def test_color_1(self):
      ray = Ray(Point(0, 0, 0), Vector(10, 0, 0))
      sphere_1 = Sphere(Point(1.0, 1.0, 0.0), 2.0, Color(0.0, 0.0, 1.0), Finish(0.2, 0.4, 0.5, 0.05))
      sphere_2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0), Finish(0.4, 0.4, 0.5, 0.05))
      sphere_list = [sphere_1, sphere_2]
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      point_tuple = find_closest_sphere(sphere_list, ray)
      color = get_color_diffusion_and_intensity(point_tuple[0], point_tuple[1], light, sphere_list, ray.pt)
      self.assertTrue(color == Color(0.0, 0.0, 0.0))

   def test_color_2(self):
      ray = Ray(Point(0, 0, -5), Vector(0, 0, 1))
      sphere_1 = Sphere(Point(1.0, 1.0, 0.0), 2.0, Color(0.0, 0.0, 1.0), Finish(0.2, 0.4, 0.5, 0.05))
      sphere_2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0), Finish(0.4, 0.4, 0.5, 0.05))
      sphere_list = [sphere_1, sphere_2]
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      point_tuple = find_closest_sphere(sphere_list, ray)
      color = get_color_diffusion_and_intensity(point_tuple[0], point_tuple[1], light, sphere_list, ray.pt)
      self.assertTrue(color == Color(0.0, 0.0, 0.242594))

   def test_add_two_colors(self):
      self.assertEqual(add_colors(Color(0, 1, 1), Color(1, 0, 0)), Color(1, 1, 1))

   def test_add_two_colors_two(self):
      self.assertEqual(add_colors(Color(0.5, 0.5, 1), Color(0, 0.5, 0)), Color(0.5, 1, 1))



if __name__ == '__main__':
   unittest.main()