from data import *
from collisions import *
from utility import *
from vector_math import *
from math import *
from cast import *
import unittest

class TestCast(unittest.TestCase):
   def test_cast_ray_1(self):
      self.assertEqual(cast_ray(Ray(Point(0,0,0), Vector(1,2,3)),[Sphere(Point(8,8,8),3,Color(0,1,0),
Finish(0.2,0.4,0.5,0.05))], Color(255,255,255),
Light(Point(-100,100,-100),Color(255,255,255)), Point(0,-14,0)), Color(1.0,1.0,1.0))
   def test_cast_ray_2(self):
      self.assertEqual(cast_ray(Ray(Point(1,1,1), Vector(4,4,4)),[Sphere(Point(3,3,3),2,Color(0,0,1),
Finish(0.4,0.4,0.5,0.05))],Color(255,255,255), Light(Point(-100,100,-100),
Color(255,255,255)),Point(0,-14,0)) , Color(20.47079184954702,20.47079184954702,158.12316794101696))
   def test_dist_form_1(self):
      self.assertEqual(distform(Point(0,0,0),Point(1,1,1)), 1.7320508075688772)
   def test_dist_form_2(self):
      self.assertEqual(distform(Point(1,1,1), Point(3,4,5)), 5.385164807134504)
   def test_convert_color_1(self):
      self.assertEqual(convert_color(Color(0.0,1.0,0.0)), (0.0,255.0,0.0))
   def test_convert_color_2(self):
      self.assertEqual(convert_color(Color(1.0,0.0,0.0)), (255.0,0.0,0.0))
   def test_ambient_coloring_1(self):
      self.assertEqual(ambient_coloring(Sphere(Point(8,8,8),3,Color(0,1,0),Finish(0.2,0.4,0.5,0.05)),
 Color(255,255,255)),Color(0.0,51.0,0.0))
   def test_ambient_coloring_2(self):
      self.assertEqual(ambient_coloring(Sphere(Point(3,3,3),2,Color(0,0,1),Finish(0.4,0.4,0.5,0.05)),
 Color(255,255,255)), Color(0.0,0.0,102.0))
   def test_diffuse_component_1(self):
      self.assertEqual(diffuse_component(Point(24,24,24), Light(Point(45,45,45),Color(200,200,200)),
 Sphere(Point(8,8,8),3,Color(0,1,0),Finish(0.2,0.4,0.5,0.05)),
 [Sphere(Point(3,3,3),2,Color(0,0,1),Finish(0.4,0.4,0.5,0.05))]), Color(0,80,0))
   def test_diffuse_component_2(self):
      self.assertEqual(diffuse_component(Point(9,9,9), Light(Point(100,100,100),Color(244,244,244)),
 Sphere(Point(10,10,10),4,Color(1,0,0),Finish(0.4,0.5,0.2,0.2)),
 [Sphere(Point(4,4,4),4,Color(2,2,1),Finish(.1,.1,.1,.1))]),Color(0,0,0))
   def test_specular_component_1(self):
      self.assertEqual(specular_component(Point(24,24,24), Light(Point(45,45,45),Color(200,200,200)),
 Sphere(Point(8,8,8),3,Color(0,1,0),Finish(0.2,0.4,0.5,0.05)),
 [Sphere(Point(3,3,3),2,Color(0,0,1),Finish(0.4,0.4,0.5,0.05))], Point(0,14,0)),Color(0,0,0))
   def test_specular_component_2(self):
      self.assertEqual(specular_component(Point(9,9,9), Light(Point(100,100,100),Color(244,244,244)),
 Sphere(Point(10,10,10),4,Color(1,0,0),Finish(0.4,0.5,0.2,0.2)),
 [Sphere(Point(4,4,4),4,Color(2,2,1),Finish(.1,.1,.1,.1))], Point(0,14,0)),Color(0,0,0))
if __name__ == "__main__":
     unittest.main()
