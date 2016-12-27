import unittest
from data import *
from cast import *

class TestData(unittest.TestCase):

  def test_cast_ray_1(self):

    ray = Ray(Point(0, 0, 0), Vector(0, 8, 0))

    color1 = Color(0.5, 0.4, 0.2)
    sphere1 = Sphere(Point(5, 4, 4), 2, color1, Finish(0.4))
    color2 = Color(0.1, 0.1, 0.9)
    sphere2 = Sphere(Point(2, -4, 0), 1, color2, Finish(0.4))
    color3 = Color(0.7, 0.8, 0.2)
    sphere3 = Sphere(Point(0, 9, 0), 2, color3, Finish(0.4))

    ambient_light = Color(0.3, 0.3, 0.3)

    sphere_list = [sphere1, sphere2, sphere3]
    
    expected_color = Color(0.084, 0.096, 0.024)
    self.assertEqual(cast_ray(ray, sphere_list, ambient_light), expected_color)


  def test_cast_ray_2(self):

    ray = Ray(Point(4, 0, 2), Vector(10, 0, 0))

    color1 = Color(0.5, 0.4, 0.3)
    finish1 = Finish(0.2)
    sphere1 = Sphere(Point(5, 4, 4), 2, color1, finish1)
    color2 = Color(0.1, 0.1, 0.9)
    finish2 = Finish(0.2)
    sphere2 = Sphere(Point(2, -4, 0), 1, color2, finish2)
    color3 = Color(0.7, 0.8, 0.2)
    finish3 = Finish(.1)
    sphere3 = Sphere(Point(0, 9, 0), 2, color3, finish3)

    ambient_light = Color(0.5, 0.5, 0.5)

    sphere_list = [sphere1, sphere2, sphere3]

    expected_color = Color(1.0, 1.0, 1.0)
    self.assertEqual(cast_ray(ray, sphere_list, ambient_light), expected_color)

  
  def test_convert_to_RGB_1(self):
    color = Color(1.0, 1.0, 1.0)
    expected = Color(255, 255, 255)
    rgb = convert_to_RGB(color)

    self.assertEqual(rgb, expected)
  
  def test_convert_to_RGB_2(self):
    color = Color(0.0, 0.0, 0.0)
    expected = Color(0, 0, 0)
    rgb = convert_to_RGB(color)

    self.assertEqual(rgb, expected)

  def test_convert_to_RGB_3(self):
    color = Color(0.5, 0.2, 0.3)
    expected = Color(127, 51, 76)
    rgb = convert_to_RGB(color)

    self.assertEqual(rgb, expected)


  def test_nearest_intersection_1(self):

    color1 = Color(0.0, 0.0, 1.0)
    finish1 = Finish(0.1)
    sphere1 = Sphere(Point(1.0, 1.0, 0.0), 2, color1, finish1)
    color2 = Color(1.0, 0.0, 0.0)
    finish2 = Finish(0.1)
    sphere2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, color2, finish2)
    eye_point = Point(0.0, 0.0, -14.0)
    ray = Ray(eye_point, difference_point(Point(0.5, 1.5, 0), eye_point))

    ambient_light = Color(0.5, 0.5, 0.5)

    sphere_list = [sphere1, sphere2]
    intersection_points = find_intersection_points(sphere_list, ray)


    expected = Sphere(Point(0.5, 1.5, -3.0), 0.5, color2, finish2)
    result = nearest_intersection(intersection_points, ray)
    #print result

    self.assertEqual(result[0], expected)


  def test_nearest_intersection_2(self):

    color1 = Color(0.0, 0.0, 1.0)
    finish1 = Finish(0.5)
    sphere1 = Sphere(Point(1.0, 1.0, 0.0), 2, color1, finish1)
    color2 = Color(1.0, 0.0, 0.0)
    finish2 = Finish(0.5)
    sphere2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, color2, finish2)
    sphere3 = Sphere(Point(0.5, 1.5, -5.0), 4, color1, finish1)
    eye_point = Point(0.0, 0.0, -14.0)
    ray = Ray(eye_point, difference_point(Point(0.5, 1.5, 0), eye_point))

    ambient_light = Color(0.1, 0.1, 0.1)

    sphere_list = [sphere1, sphere2, sphere3]
    intersection_points = find_intersection_points(sphere_list, ray)


    expected = Sphere(Point(0.5, 1.5, -5.0), 4, color1, finish1)
    result = nearest_intersection(intersection_points, ray)
    #print result

    self.assertEqual(result[0], expected)
    

if __name__ == '__main__':
  unittest.main()
