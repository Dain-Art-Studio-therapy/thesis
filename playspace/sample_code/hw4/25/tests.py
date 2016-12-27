import collisions
import unittest
import data
import cast
class TestData(unittest.TestCase):
   def test_ambient_color_1(self):
      color= data.Color(1.0, 1.0, 1.0)
      center=data.Point(1.0, 1.0, 0.0)
      radius= 2.0
      finish= data.Finish(0.2, 0.4, 0.5, 0.05)
      sphere_color= data.Color(0.0, 0.0, 1.0)
      sphere= data.Sphere(center, radius, sphere_color, finish)
      final_color= data.Color(0.0, 0.0, 0.2)
      final_color2= cast.ambient_color(color, sphere)
      self.assertEqual(final_color, final_color2)
   def test_ambient_color_2(self):
      color= data.Color(1.0, 1.0, 1.0)
      center= data.Point(0.5, 1.5, -3.0)
      radius= 0.5
      finish= data.Finish(0.4, 0.4, 0.5, 0.05)
      sphere_color= data.Color(1.0, 0.0, 0.0)
      sphere= data.Sphere(center, radius, sphere_color, finish)
      final_color= data.Color(0.4, 0.0, 0.0)
      final_color2= cast.ambient_color(color, sphere)
      self.assertEqual(final_color, final_color2)
   def test_light_color_diffused_1(self):
      light= data.Light(data.Point(-100.0, 100.0, -100.0),data.Color(1.5, 1.5, 1.5))
      center= data.Point(1.0, 1.0, 0.0)
      radius= 2.0
      visible_value= 1.0
      finish= data.Finish(0.2, 0.4, 0.5, 0.05)
      sphere_color= data.Color(0.0, 0.0, 1.0)
      sphere= data.Sphere(center, radius, sphere_color, finish)
      final_color= data.Color(0.0, 0.0, 0.6)
      final_color2= cast.light_color_diffused(light, sphere, visible_value)
      self.assertEqual(final_color, final_color2)
   def test_light_color_diffused_2(self):
      light= data.Light(data.Point(-100.0, 100.0, -100.0),data.Color(1.5, 1.5, 1.5))
      center= data.Point(0.5, 1.5, -3.0)
      radius= 0.5
      visible_value= 1.0
      finish= data.Finish(0.4, 0.4, 0.5, 0.05)
      sphere_color= data.Color(1.0, 0.0, 0.0)
      sphere= data.Sphere(center, radius, sphere_color, finish)
      final_color= data.Color(0.6, 0.0, 0.0)
      final_color2= cast.light_color_diffused(light, sphere, visible_value)
      self.assertEqual(final_color, final_color2)
   def test_ambient_light_color_diffused_1(self):
      ambcolor= data.Color(0.0, 0.0, 0.2)
      lcolor= data.Color(0.0, 0.0, 0.6)
      final_color= data.Color(0.0, 0.0, 0.8)
      final_color2= cast.ambient_light_color_diffused(ambcolor, lcolor)
      self.assertEqual(final_color, final_color2)
   def test_ambient_light_color_diffused_2(self):
      ambcolor= data.Color(0.4, 0.0, 0.0)
      lcolor= data.Color(0.6, 0.0, 0.0)
      final_color= data.Color(1.0, 0.0, 0.0)
      final_color2= cast.ambient_light_color_diffused(ambcolor, lcolor)
      self.assertEqual(final_color, final_color2)
   def test_specular_light_roughness_1(self):
      light= data.Light(data.Point(-100.0, 100.0, -100.0),data.Color(1.5, 1.5, 1.5))
      center= data.Point(1.0, 1.0, 0.0)
      radius= 2.0
      specular_intensity= 1.0
      finish= data.Finish(0.2, 0.4, 0.5, 0.05)
      sphere_color= data.Color(0.0, 0.0, 1.0)
      sphere= data.Sphere(center, radius, sphere_color, finish)
      final_color= data.Color(0.75, 0.75, 0.75)
      final_color2= cast.specular_light_roughness(light, sphere, specular_intensity)
      self.assertEqual(final_color, final_color2)

   def test_specular_light_roughness_2(self):
      light= data.Light(data.Point(-100.0, 100.0, -100.0),data.Color(1.5, 1.5, 1.5))
      center= data.Point(0.5, 1.5, -3.0)
      radius= 0.5
      specular_intensity= 1.0
      finish= data.Finish(0.4, 0.4, 0.5, 0.05)
      sphere_color= data.Color(1.0, 0.0, 0.0)
      sphere= data.Sphere(center, radius, sphere_color, finish)
      final_color= data.Color(0.75, 0.75, 0.75)
      final_color2= cast.specular_light_roughness(light, sphere, specular_intensity)
      self.assertEqual(final_color, final_color2)

   def test_specular_ambient_diffuse_1(self):
      ambdiff= data.Color(0.0, 0.0, 0.8)
      specrough= data.Color(0.75, 0.75, 0.75)
      final_color= data.Color(0.75, 0.75, 1.55)
      final_color2= cast.specular_ambient_diffuse(ambdiff, specrough)
   def test_specular_ambient_diffuse_2(self):
      ambdiff= data.Color(1.0, 0.0, 0.0)
      specrough= data.Color(0.75, 0.75, 0.75)
      final_color= data.Color(1.75, 0.75, 0.75)
      final_color2= cast.specular_ambient_diffuse(ambdiff, specrough)
   def test_move_point_1(self):
      pass
   def test_move_point_2(self):
      pass
"""
   def test_cast_ray_1(self):
      sphere1= data.Sphere(data.Point(5, 5, 5), 10, 
      sphere2= data.Sphere(data.Point
      sphere3= data.Sphere(data.Point
      ray= data.Ray(data.Point
      sphere_list= [sphere1, sphere2, sphere3]
   def test_cast_ray_2(self):
      f= data.Finish(0.0, 0.0, 0.0, 0.0)
      sphere1= data.Sphere(data.Point(-15, -10, -24), 2, data.Color(0.0, 0.0, 1.0), f)
      sphere2= data.Sphere(data.Point(-50, -22, -90), 5, data.Color(0.0, 0.0, 1.0), f)
      sphere3= data.Sphere(data.Point(-44, -17, -100), 4, data.Color(0.0, 0.0, 1.0), f)
      ray= data.Ray(data.Point(1, 1, 1), data.Vector(1, 2, 3))
      sphere_list= [sphere1, sphere2, sphere3]
      color= data.Color(1.0, 1.0, 1.0)
      color_2= data.Color(0.0, 0.0, 0.0)
      self.assertEqual(color ,cast.cast_ray(ray, sphere_list, color_2))
"""
if __name__== "__main__":
   unittest.main()
