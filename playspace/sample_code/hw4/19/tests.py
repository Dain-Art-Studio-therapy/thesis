import unittest
from cast import *

class TestCast(unittest.TestCase):
 
   def test_Castray(self):
      color1 = cast_ray(Ray(Point(-10,0,0), Vector(3,0,0)),
      [Sphere(Point(6,0,0), 5, Color(.5,1,.7), Finish(0.1, 0.2, 0.4, 0.04)), Sphere(Point(-3,0,0), 1, Color(0.1,0.5,0.4), Finish(0.5, 0.5, 0.2, 0.02))], 
      Color(1.0,1.0,1.0), Light(Point(10,5,3), Color(1.2,1.2,1.2)), Point(-10,0,0))
      self.assertTrue(color1== Color(0.05,0.25,0.2))
   def test_castray_again(self):
      color1 = cast_ray(Ray(Point(-10,0,0), Vector(3,0,0)),
      [Sphere(Point(8,0,0), 5, Color(.7,0.3,.7), Finish(0.1, 0.2, 0.4, 0.07)), Sphere(Point(-3,0,0), 1, Color(1,0.8,0.3), Finish(0.5, 0.5, 0.2, 0.02))], 
      Color(1.0,1.0,1.0), Light(Point(11,5,3), Color(1.5,1,1.0)), Point(-10,0,0))
      self.assertTrue(color1== Color(0.5,0.4,0.15))

   def test_sphere_normal_at_point(self):
      test= sphere_normal_at_point(Sphere(Point(0,0,0), 1, Color(1,1,1),Finish(0.5,0.5,0.5,0.05)), Point(2,0,0))
      self.assertTrue(test==Vector(1,0,0))

   def  test_fake_point_translate(self):
      test= fake_point_translate(Sphere(Point(0,0,0), 1, Color(1,1,1),Finish(0.5,0.5,0.5,0.05)), Point(2,0,0))
      self.assertTrue(test==Point(2.01, 0.0, 0.0))
      #print test.x, test.y, test.z

   def test_light_normal(self):
      test= light_normal(Point(2, 0.0, 0.0), Light(Point(7,0,0), Color(1.5,1.5,1.5)))
      self.assertTrue(test== Point(1,0,0))
      
   def test_light_diffuse(self):
      test= light_diffuse(Sphere(Point(0,0,0), 1, Color(1,1,1),Finish(0.5,0.5,0.5,0.05)), Point(2,0,0), Light(Point(7,0,0), Color(1.5,1.5,1.5)))
      self.assertTrue(test==1)

   def test_specular_value(self):
      test= specular_value(Point(9,0,0), Point(1,0,0), Sphere(Point(0,0,0), 1, Color(1,1,1),Finish(0.5,0.5,0.5,0.05)), Light(Point(7,0,0), Color(1.5,1.5,1.5)), 0.7)
      self.assertAlmostEqual(test, 0.4)
   
   def test_specular_shade(self):
      test=specular_shade(0.1, Sphere(Point(0,0,0), 1, Color(1,1,1),Finish(0.5,0.5,0.5,0.05)), Light(Point(7,0,0), Color(1.5,1.5,1.5)))
      self.assertTrue(test==Color(0,0,0))

   def test_sphere_ambient_finish(self):
      test= sphere_ambient_finish(Sphere(Point(6,6,6), 3, Color(1,1,1), Finish(0.7,0.7,0.5,0.05)), Color(1,1,1))
      self.assertTrue(test==Color(0.7, 0.7, 0.7))

   def test_sphere_lightpoint(self):
      test= sphere_lightpoint(Sphere(Point(0,0,0), 1, Color(1,1,1),Finish(0.5,0.5,0.5,0.05)), Light(Point(7,0,0), Color(1.5,1.5,1.5)), 0.7)
      self.assertTrue(Color(0.525, 0.525, 0.525))

   def test_add_shades(self):
      test= add_shades(Color(0.1,0.1,0.1), Color(0.2,0.2,0.2), Color(0.3,0.3,0.3))
      self.assertTrue(test== Color(0.6,0.6,0.6))

   def test_convert_color(self):
      test= convert_color(Color(0.1,0.1,0.1))
      self.assertTrue(test==Color(25,25,25))
      
   def test_spherecolor(self):
      sphere1 = Sphere(Point(6,6,6), 3, Color(1,1,1), Finish(0.7,0.7,0.5,0.05))
      self.assertTrue(sphere1.color == Color(1,1,1))

  


if __name__=='__main__':
 unittest.main()
