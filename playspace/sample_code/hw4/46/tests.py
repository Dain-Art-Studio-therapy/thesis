import unittest
from data import *
from cast import *
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class TestCases(unittest.TestCase):

   def test_dist1(self):
      d = dist(Point(0.0, 0.0, 0.0), Point(3.0, 4.0, 0.0))
      self.assertEqual(d, 5.0)
   def test_dist2(self):
      d = dist(Point(0.0, 0.0, 0.0), Point(10.0, 2.0, 6.0))
      self.assertEqual(d, math.sqrt(140.0))

   def test_deffuse_check1(self):
      sphere = Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0),
                      Finish(0.4, 0.4, 0.5, 0.05))
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      N = Vector( 0.0, -1.0, 0.0)
      Ldir = Vector(1.0, -.5, 6.3)
      result = Color(0.3, 0.0, 0.0)
      self.assertEqual(diffuse_check(sphere, light, N, Ldir), result)
   def test_deffuse_check2(self):
      sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0, Color(1.0, 1.0, 1.0),
                      Finish(0.1, 0.2, 0.3, 0.4))
      N = Vector(0.57735, 0.57735, .57735)
      Ldir = Vector(1.0, 2.0, 3.0)
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      result = Color(1.03923, 1.03923, 1.03923)
      self.assertEqual(diffuse_check(sphere, light, N, Ldir), result)

   def test_light_check1(self):
      sphere_list = []
      pe = Point(0.0, 0.0, 0.0)
      Ldir = Vector(1.0, -.5, 6.3)
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      self.assertFalse(light_check(sphere_list, pe, Ldir, light))
   def test_light_check2(self):
      sphere_list = [Sphere(Point(-50.0, -50.0, -50.0), 1.0,
                     Color(1.0, 0.0, 0.0), Finish(0.4, 0.4, 0.5, 0.05)), 
                     Sphere(Point(1.0, 0.0, 0.0), 1.0,
                            Color(1.0, 0.0, 0.0), Finish(0.4, 0.4, 0.5, 0.05))]
      pe = Point(0.0, 0.0, 0.0)
      Ldir = Vector(-100.0, -100.0, -100.0)
      light = Light(Point(-100.0, -100.0, -100.0), Color(1.5, 1.5, 1.5))
      self.assertTrue(light_check(sphere_list, pe, Ldir, light))

   def test_diffuse1(self):
      sphere_list = []
      sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0, Color(1.0, 1.0, 1.0),
                      Finish(0.4, 0.4, 0.5, 0.05))
      intersect = Point(1.0, 0.0, 0.0)
      light = Light(Point(-100.0, -100.0, -100.0), Color(1.5, 1.5, 1.5))
      Ldir = Vector(-1.0, -1.0, -1.0)
      pe = Point(1.0, 2.0, 3.0)
      N = Vector( 0.0, -1.0, 0.0)
      result = Color(0.6, 0.6, 0.6)
      self.assertEqual(diffuse(sphere_list, sphere, intersect, light, pe, N,
                       Ldir), result)
   def test_diffuse2(self):
      sphere_list = [Sphere(Point (1.0, 1.0, 0.0), 2.0, Color(0.0, 0.0, 1.0), 
                     Finish(0.2, 0.4, 0.5, 0.05)), Sphere(Point(0.5, 1.5,     
                     -3.0), 0.5, Color(1.0, 0.0, 0.0), Finish(0.4, 0.4, 0.5, 
                     0.05))]
      sphere = Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0),
                      Finish(0.4, 0.4, 0.5, 0.05))
      intersect = Point(0.0, 1.0, -2.5)
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      N = Vector( 0.0, -1.0, 0.0)
      Ldir = Vector(1.0, -.5, 6.3)
      pe = Point(1.0, 2.0, 3.0)
      result = Color(0.3, 0.0, 0.0)
      self.assertEqual(diffuse(sphere_list, sphere, intersect, light, pe, N,
                       Ldir), result)

   def test_specular_intensity1(self):
      sphere = Sphere(Point(0.0, 0.0, 0.0), 1.0, Color(1.0, 1.0, 1.0),
                      Finish(0.4, 0.4, 0.5, 0.05))
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
      eye_pt = Point(0.0, 0.0, -1.0)
      pe = Point(-1.0, -2.0, 3.0)
      N = Vector( 0.0, 1.0, 0.0)
      Ldir = Vector(-1.0, -0.5, -6.3)
      result = Color(0.0, 0.0, 0.0)
      self.assertEqual(specular_intensity(sphere, light, eye_pt, pe, N, Ldir), 
                       result)

   def test_cast_ray1(self):
      ray1 = Ray(Point(-10.1, -15.2, -62.9), Vector(-12.0, -13.6, -22.4))
      sphere_list1 = [Sphere(Point(100.0, 101.1, 102.2), 1.2, Color(0.0, 0.0, 
                     1.0), Finish(.1, .2, .3, .4))]
      color = Color(.1, .5, .2)
      eyept = Point(0.0, 0.0, -14.0)
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.1, 1.2, 1.3))
      result1 = Color(1.0, 1.0, 1.0)
      self.assertEqual(cast_ray(ray1, sphere_list1, color, light, eyept),
                       result1)
   def test_2(self):
      ray2 = Ray(Point(0.0, 0.0, -14.0), Vector(1.0, 1.0, 14.0))
      sphere_list2 = [Sphere(Point(-105.6, -126.2, -120.0), 1.0, 
                      Color(0.0,0.0,0.0), Finish(0.2, 0.4, 0.5, 0.05)), 
                      Sphere(Point(1.0, 0.0, 0.0), 1.0, Color(1.0, 0.0, 0.0), 
                      Finish(0.4, 0.4, 0.5, 0.05))]
      light = Light(Point(-100.0, 100.0, -100.0), Color(1.1, 1.2, 1.3))
      color = Color(.5, .8, .1)
      eyept = Point(1.0, 1.0, -12.0)
      result2 = Color(0.48755498, 0.0, 0.0)
      self.assertEqual(cast_ray(ray2, sphere_list2, color, light, eyept), result2)


if __name__ == '__main__':
   unittest.main()
