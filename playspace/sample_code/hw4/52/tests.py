import unittest
import cast
from data import *
import collisions

class TestCollisions(unittest.TestCase):
   def test_cast_ray(self):
      ray=Ray(Point(0,0,0),Vector(1,0,0))
      s1=Sphere(Point(7,0,0),5,Color(.25,.25,.25),Finish(1,1,1,1))
      s2=Sphere(Point(1,1,0),5,Color(.5,.5,.5),Finish(4,4,4,4))
      sphere_list=[s1,s2]
      light=Light(Point(-100,0,0),Color(1,1,1))
      point=Point(200,0,0)
      self.assertEqual(cast.cast_ray(ray,sphere_list,Color(1,.5,.25),light,point),Color(.25,.125,.0625))
   def test_cast_ray2(self):
      ray=Ray(Point(0,0,0),Vector(1,1,1))
      s1=Sphere(Point(-100,-8,-5),2,Color(.2,.22,.2),Finish(.2,.2,.2,.2))
      s2=Sphere(Point(5,5,5),3,Color(.45,.5,.3),Finish(.1,.2,.3,.4))
      sphere_list=[s1,s2]
      light=Light(Point(0,0,0),Color(.2,.2,.2))
      point=Point(0,-2,0)
      self.assertEqual(cast.cast_ray(ray,sphere_list,Color(.2,.1,1),light,point),Color(.082944,.080944,.097944))
   def test_diffuse_light(self):
      intersection=(Sphere(Point(0,0,0),1,Color(.1,.1,.1),Finish(2,1,1,1)),Point(0,0,1))
      light=Light(Point(0,0,5),Color(.5,.5,.5))
      self.assertEqual(cast.diffuse_light(intersection,light),Color(.05,.05,.05))
   def test_specular_color(self):
      light=Light(Point(-100,100,-100),Color(1.5,1.5,1.5))
      sphere=Sphere(Point(1,1,0),2,Color(0,0,1),Finish(.2,.4,.5,.05))
      intensity=1
      self.assertEqual(cast.specular_color(light,sphere,intensity).r,.75)
   def test_specular_color_again(self):
      light=Light(Point(1,1,1),Color(.5,.5,.5))
      sphere=Sphere(Point(0,0,0),2,Color(.2,.2,.2),Finish(.3,.4,.5,.6))
      intensity=.5
      self.assertEqual(cast.specular_color(light,sphere,intensity),Color(.125,.125,.125))
   def test_specular_intensity(self):
      intersection=(Sphere(Point(0,0,0),1,Color(.2,.2,.2),Finish(1,1,1,1)),Point(1,0,0))
      light=Light(Point(5,0,0),Color(1,1,1))
      point=Point(1,1,1)
      self.assertAlmostEqual(cast.specular_intensity(intersection,light,point),-.007070891)
   def test_add_colors(self):
      c1=Color(2,4,7)
      c2=Color(1,2,3)
      self.assertEqual(collisions.add_colors(c1,c2),Color(3,6,10))

if __name__=='__main__':
   unittest.main()
