import unittest
import cast
from data import *

class TestCase(unittest.TestCase):
   def test_cast_rays_1(self):
      s1 = Sphere(Point(0,0,0), 3, Color(1.0,0.0,0.0),Finish(.1,.1, 1, 1))
      s2 = Sphere(Point(2,0,0), 1, Color(0.0,1.0,0.0),Finish(.1,.1, 1, 1))
      sphere_list = [s1, s2]
      ray = Ray(Point(-4,0,0), Vector(8,0,0))
      color = Color(0,0,0)
      point = Point(0,0,0)
      light = Light(point, color)
      self.assertEqual(cast.cast_ray(ray,sphere_list, color, light, point), Color(1.0,0.0,0.0))
      pass

   def test_cast_rays_2(self):
      s1 = Sphere(Point(6,6,6), 1, Color(1,0,1),Finish(.1,.1, 1, 1))
      s2 = Sphere(Point(9,9,9), 2, Color(1,1,0),Finish(.1,.1, 1, 1))
      sphere_list = [s1, s2]
      ray = Ray(Point(0,0,0), Vector(8,0,0))
      self.assertEqual(cast.cast_ray(ray,sphere_list), Color(1,1,1))
      pass

   def test_cast_ray_3(self):
      s1 = Sphere(Point(5,5,0), 4, Color(0,0,1),Finish(1,1,1,1))
      s2 = Sphere(Point(7,4,0), 2, Color(0,1,0),Finish(1,1,1,1))
      sphere_list = [s1, s2]
      ray = Ray(Point(0,0,0), Vector(10,10,0))
      self.assertEqual(cast.cast_ray(ray,sphere_list), Color(0,0,1))
      pass

   def test_nearest_point(self):
      s1 = Sphere(Point(5,5,0), 4, Color(0,0,1),Finish(1,1,1,1))
      s2 = Sphere(Point(7,4,0), 2, Color(0,1,0),Finish(1,1,1,1))
      sphere_list = [(s1, Point(5,5,0)), (s2, Point(7,4,0))]
      self.assertEqual(cast.nearest_point(sphere_list, Point(0,0,0)), 0)
      pass      

   def test_color_add(self):
      c1 = Color(1, 0, 0)
      c2 = Color(0, 1, 1)
      c3 = Color(1, 1, 1)
      self.assertEqual(cast.color_add(c1, c2), c3)
      pass

   def test_color_diffuse(self):
      dp = 3
      light = Light(Point(0, 0, 0), Color(.1, .1, .2))
      sphere = Sphere(Point(0, 0, 0),1, Color(1, 0, 1), Finish(.1, .5, .5, .01))
      self.assertEqual(cast.color_diffuse(dp, light, sphere), Color(.15, 0, .3))
      pass

   def test_light_visible(self):
      N = Vector(1, 2, 3)
      L = Vector(4, 5, 6)
      sphere = Sphere(Point(0,0,0),1,Color(1, .5, .2), Finish(.1, .1,.1, .1))
      pt = Point(1, 1, 1)
      P = Point(2, 1, 1)   
      List = [sphere, pt]
      self.assertEqual(cast.light_visible(N, L, List, pt, P), 32)
      pass

   def test_nearest_point(self):
      s1 = Sphere(Point(1, 1, 1), 2, Color(1, 1, 0), Finish(.2, .5, .1, .1))
      s2 = Sphere(Point(0, 0, 0), 1, Color(0, 0, 1), Finish(.4, .4, .1, .1))
      p1 = Point(0,0,0)
      p2 = Point(2,2,2)
      point = Point(4, 4, 4)
      List = [(s1, p1), (s2, p2)]
      self.assertEqual(cast.nearest_point(List, point), 1)
      pass
   
   def test_final_color(self):
      s_c = 2
      light = Light(Point(0,0,0), Color(1, 2, 3))
      sphere = Sphere(Point(0,0,0),1, Color(1, 2, 3), Finish(.1,.2,.3,.01))
      color = Color(1, 1, 1)
      pass

   def test_cap_color(self):
      color = Color(145, 257, 300)
      self.assertEqual(cast.cap_color(color), Color(145, 255, 255))
      pass

   def test_cap_color_2(self):
      self.assertEqual(cast.cap_color(Color(400, 1, 500)), Color(255, 1, 255))
      pass

   def test_color_add(self):
      c1 = Color(1, 3, 2)
      c2 = Color(4, 5, 6)
      c3 = Color(5, 8, 8)
      self.assertEqual(cast.color_add(c1, c2), c3)
      pass

   def test_final_color(s_c, light, sphere):
      s_c = 2
      light = Light(Point(0, 0, 0), Color(1, 1, 1))
      sphere = Sphere(Point(0,0,0,),1,Color(1,1,1), Finish(1,1,1,1))
      color = Color(2, 2, 2)
      self.assertEqual(cast.final_color(s_c, light, sphere), color)
      pass

   def test_scale_color(self):
      color = Color(1, .5, .2)
      self.assertEqual(cast.scale_color(color), Color(255, 127.5, 51))
      pass

if __name__ == '__main__':
   unittest.main()
