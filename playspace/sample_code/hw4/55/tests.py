#Assignment 4 PART 4 Tests
import data
import vector_math
from utility import *
import unittest
import collisions
import cast
import math


class DataTests(unittest.TestCase):


   def test_cast_ray1(self):
      ray1 = data.Ray(data.Point(0.0,0.0,0.0), data.Vector(1000.0,0.0,0.0))
      empty_list = []
      white = data.Color(1.0,1.0,1.0)
      Light = data.Light(data.Point(0.0,10.0,0.0), white)
      Point = data.Point(1.0,1.0,1.0)
      self.assertEqual(cast.cast_ray(ray1, empty_list, white, Light, Point),
                                                                     white)

   def test_cast_ray2(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      s0 = data.Sphere(data.Point(0,0,0), 6, white, finish)
      s1 = data.Sphere(data.Point(200.0,0.0,0.0), 1, white, finish)
      s2 = data.Sphere(data.Point(300.0,0.0,0.0), 23, white,finish)
      intersect_pt = data.Point(6,0,0)
      Light = data.Light(data.Point(10.01,0.0,0.0), white)
      Point = data.Point(9.01,0.0,0.0)
      sphere_list = [s0, s1, s2]
      ray = data.Ray(data.Point(9.01,0.0,0.0), data.Vector(-3.01,0.0,0.0))
      final_color = white
      self.assertEqual(cast.cast_ray(ray, sphere_list, white, Light, Point),
                                     white)


   def test_find_distance1(self):
      ray1 = data.Ray(data.Point(0.0,0.0,0.0), data.Vector(20.0,0.0,0.0))
      intersect_pt = data.Point(8.0,0.0,0.0)
      self.assertEqual(cast.find_distance(ray1, intersect_pt), 8.0)

   def test_find_distance2(self):
      ray1 = data.Ray(data.Point(0.0,0.0,0.0), data.Vector(0.0,20.0,0.0))
      intersect_pt = data.Point(0.0,10.0,0.0)
      self.assertEqual(cast.find_distance(ray1, intersect_pt), 10.0)

   def test_find_N1(self):
      white = data.Color(1.0,1.0,1.0)
      red = data.Color(1.0,0.0,0.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere4 = data.Sphere(data.Point(0,0,0), 6, red, finish)
      point1 = data.Point(6,0,0)
      self.assertEqual(cast.find_N(sphere4, point1), data.Vector(1,0,0))
   
   def test_find_N2(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere5 = data.Sphere(data.Point(1,1,1), 5, white, finish)
      point2 = data.Point(1,1,6)
      self.assertEqual(cast.find_N(sphere5, point2), data.Vector(0,0,1))

   def test_find_px1(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(0,0,0), 6, white, finish)
      intersect_pt = data.Point(6,0,0)
      self.assertEqual(cast.find_px(sphere, intersect_pt),
                       data.Point(6.01,0.0,0.0))

   def test_find_px2(self):
      white = data.Color(1.0,1.0,1.0)
      red = data.Color(1.0,0.0,0.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(1,1,1), 5, red, finish)
      intersect_pt = data.Point(1,1,6)
      self.assertEqual(cast.find_px(sphere, intersect_pt),
                       data.Point(1.0,1.0,6.01))

   def test_find_Ldir1(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(0,0,0), 6, white, finish)
      intersect_pt = data.Point(6,0,0)
      Light = data.Light(data.Point(10.01,0.0,0.0), white)
      self.assertEqual(cast.find_Ldir(sphere, intersect_pt, Light),
                       data.Vector(1.0,0.0,0.0))            

   def test_find_Ldir2(self):
      white = data.Color(1.0,1.0,1.0)
      red = data.Color(1.0,0.0,0.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(1,1,1), 5, red, finish)
      intersect_pt = data.Point(1,1,6)
      Light = data.Light(data.Point(1.0,1.0,10.01), white)
      self.assertEqual(cast.find_Ldir(sphere, intersect_pt, Light),
                       data.Vector(0.0,0.0,1.0))

   def test_LdotN1(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(0,0,0), 6, white, finish)
      intersect_pt = data.Point(6,0,0)
      Light = data.Light(data.Point(10.01,0.0,0.0), white)
      self.assertEqual(cast.find_LdotN(sphere, intersect_pt, Light), 1.0)

   def test_LdotN2(self):
      white = data.Color(1.0,1.0,1.0)
      red = data.Color(1.0,0.0,0.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(1,1,1), 5, red, finish)
      intersect_pt = data.Point(1,1,6)
      Light = data.Light(data.Point(1.0,1.0,10.01), white)
      self.assertEqual(cast.find_LdotN(sphere, intersect_pt, Light), 1.0)

   def test_light_contribution1(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(0,0,0), 6, white, finish)
      intersect_pt = data.Point(6,0,0)
      Light = data.Light(data.Point(10.01,0.0,0.0), white)
      result = [0.5,0.5,0.5]
      self.assertEqual(cast.light_contribution(sphere, intersect_pt, Light),
                       result)

   def test_light_contribution2(self):      
      white = data.Color(1.0,1.0,1.0)
      red = data.Color(1.0,0.0,0.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(1,1,1), 5, red, finish)
      intersect_pt = data.Point(1,1,6)
      Light = data.Light(data.Point(1.0,1.0,10.01), white)
      result = [0.5,0.0,0.0]
      self.assertEqual(cast.light_contribution(sphere, intersect_pt, Light),
                       result)

   def test_is_light_obscured1(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(0,0,0), 6, white, finish)
      intersect_pt = data.Point(6,0,0)
      Light = data.Light(data.Point(10.01,0.0,0.0), white)
      s0 = data.Sphere(data.Point(123.0,3243.0,213.0), 1.0, white, finish)
      s1 = data.Sphere(data.Point(8.0,0.0,0.0), 1.0, white, finish)
      sphere_list = [s0, s1]
      self.assertEqual(cast.is_light_obscured
                      (sphere, intersect_pt, Light, sphere_list), True)

   def test_is_light_obscured2(self):
      white = data.Color(1.0,1.0,1.0)
      red = data.Color(1.0,0.0,0.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(1,1,1), 5, red, finish)
      intersect_pt = data.Point(1,1,6)
      Light = data.Light(data.Point(1.0,1.0,10.01), white)
      empty_list = []
      self.assertEqual(cast.is_light_obscured
                      (sphere, intersect_pt, Light, empty_list), False)

   def test_light_visible1(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(0,0,0), 6, white, finish)
      intersect_pt = data.Point(-6.0,0.0,0.0)
      Light = data.Light(data.Point(10.01,0.0,0.0), white)
      sphere_list = []
      result = [0.0,0.0,0.0]
      self.assertEqual(cast.light_visible
                      (sphere, intersect_pt, Light, sphere_list), result)

   def test_light_visible2(self):
      white = data.Color(1.0,1.0,1.0)
      red = data.Color(1.0,0.0,0.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(1,1,1), 5, red, finish)
      intersect_pt = data.Point(1,1,6)
      Light = data.Light(data.Point(1.0,1.0,10.01), white)
      sphere_list = []
      result = [0.5,0.0,0.0]
      self.assertEqual(cast.light_visible
                      (sphere, intersect_pt, Light, sphere_list), result)

   def test_reflection_vector1(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(0,0,0), 6, white, finish)
      intersect_pt = data.Point(6,0,0)
      Light = data.Light(data.Point(10.01,0.0,0.0), white)
      reflection_vector = data.Vector(-1.0,0.0,0.0)
      self.assertEqual(cast.find_reflection_vector
                      (sphere, intersect_pt, Light), reflection_vector)

   def test_reflection_vector2(self):
      white = data.Color(1.0,1.0,1.0)
      red = data.Color(1.0,0.0,0.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(1,1,1), 5, red, finish)
      intersect_pt = data.Point(1,1,6)
      Light = data.Light(data.Point(1.0,1.0,10.01), white)
      reflection_vector = data.Vector(0.0,0.0,-1.0)
      self.assertEqual(cast.find_reflection_vector
                      (sphere, intersect_pt, Light), reflection_vector)

   def test_find_Vdir1(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(0,0,0), 6, white, finish)
      intersect_pt = data.Point(6,0,0)
      Point = data.Point(9.01,0.0,0.0)
      result = data.Vector(-1.0,0.0,0.0)
      self.assertEqual(cast.find_Vdir(sphere, intersect_pt, Point), result)

   def test_find_Vdir2(self):
      white = data.Color(1.0,1.0,1.0)
      red = data.Color(1.0,0.0,0.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(1,1,1), 5, red, finish)
      intersect_pt = data.Point(1,1,6)
      Point = data.Point(1,1,2.01)
      result = data.Vector(0.0,0.0,1.0)
      self.assertEqual(cast.find_Vdir(sphere, intersect_pt, Point), result)

   def test_find_specular_intensity1(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(0,0,0), 6, white, finish)
      intersect_pt = data.Point(6,0,0)
      Light = data.Light(data.Point(10.01,0.0,0.0), white)
      Point = data.Point(9.01,0.0,0.0)
      self.assertEqual(cast.find_specular_intensity
                      (sphere, intersect_pt, Light, Point), 1.0)

   def test_find_specular_intensity2(self):
      white = data.Color(1.0,1.0,1.0)
      red = data.Color(1.0,0.0,0.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(1,1,1), 5, red, finish)
      intersect_pt = data.Point(1,1,6)
      Point = data.Point(1,1,2.01)
      Light = data.Light(data.Point(1.0,1.0,10.01), white)
      self.assertEqual(cast.find_specular_intensity
                      (sphere, intersect_pt, Light, Point), -1.0)

   def test_find_specular_value1(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(0,0,0), 6, white, finish)
      intersect_pt = data.Point(6,0,0)
      Light = data.Light(data.Point(10.01,0.0,0.0), white)
      Point = data.Point(9.01,0.0,0.0)
      result_list = [0.5,0.5,0.5]
      self.assertEqual(cast.find_specular_value
                      (sphere, intersect_pt, Light, Point), result_list)

   def test_find_specular_value2(self):
      white = data.Color(1.0,1.0,1.0)
      red = data.Color(1.0,0.0,0.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(1,1,1), 5, red, finish)
      intersect_pt = data.Point(1,1,6)
      Point = data.Point(1,1,2.01)
      Light = data.Light(data.Point(1.0,1.0,10.01), white)
      result_list = [0.5,0.5,0.5]
      self.assertEqual(cast.find_specular_value
                      (sphere, intersect_pt, Light, Point), result_list)

   def test_is_sphere_contribution1(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(0,0,0), 6, white, finish)
      intersect_pt = data.Point(6,0,0)
      Light = data.Light(data.Point(10.01,0.0,0.0), white)
      Point = data.Point(9.01,0.0,0.0)
      result_list = [0.5,0.5,0.5]
      self.assertEqual(cast.is_specular_contribution
                      (sphere, intersect_pt, Light, Point), result_list)

   def test_is_sphere_contribution2(self):
      white = data.Color(1.0,1.0,1.0)
      red = data.Color(1.0,0.0,0.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      sphere = data.Sphere(data.Point(1,1,1), 5, red, finish)
      intersect_pt = data.Point(1,1,6)
      Point = data.Point(1,1,2.01)
      Light = data.Light(data.Point(1.0,1.0,10.01), white)
      result_list = [0.0,0.0,0.0]
      self.assertEqual(cast.is_specular_contribution
                      (sphere, intersect_pt, Light, Point), result_list)   

   def test_cast_ray1(self):
      white = data.Color(1.0,1.0,1.0)
      finish = data.Finish(0.5,0.5,0.5,0.05)
      s0 = data.Sphere(data.Point(0,0,0), 6, white, finish)
      s1 = data.Sphere(data.Point(200.0,0.0,0.0), 1, white, finish)
      s2 = data.Sphere(data.Point(300.0,0.0,0.0), 23, white,finish)
      intersect_pt = data.Point(6,0,0)
      Light = data.Light(data.Point(10.01,0.0,0.0), white)
      Point = data.Point(9.01,0.0,0.0)
      sphere_list = [s0, s1, s2]
      ray = data.Ray(data.Point(9.01,0.0,0.0), data.Vector(-3.01,0.0,0.0))
      final_color = white
      self.assertEqual(cast.cast_ray
                      (ray, sphere_list, white, Light, Point), white)








if __name__ == '__main__':
   unittest.main()
