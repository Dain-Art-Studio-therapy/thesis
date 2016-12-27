#tests

import unittest
import cast
import data

class TestChar(unittest.TestCase):
  def test_sphere_normal(self):
    p = data.Point(2,0,0)
    s = data.Sphere(data.Point(3, 0, 0), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    self.assertEqual(cast.sphere_normal(p, s), data.Vector(-1, 0, 0))
  def test_sphere_normal_again(self):
    p = data.Point(2,3,5)
    s = data.Sphere(data.Point(3, 1, 2), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    self.assertEqual(cast.sphere_normal(p, s),
          data.Vector(-0.267261241912, 0.534522483825, 0.801783725737))

  def test_distance_between_points(self):
    p1 = data.Point(2, 0, 0)
    p2 = data.Point(1, 0, 0)
    self.assertEqual(cast.distance_between_points(p1, p2), 1)
  def test_distance_between_points_again(self):
    p1 = data.Point(1, 3, 5)
    p2 = data.Point(4, 2, 7)
    self.assertAlmostEqual(cast.distance_between_points(p1, p2),
              3.7416573867739413)

  def test_closest_point_index(self):
    plist = [data.Point(2, 0, 0), data.Point(1, 0, 0), data.Point(2,3,5)]
    eye = data.Point(0,0,0)
    self.assertEqual(cast.closest_point_index(plist, eye), 1)
  def test_closest_point_index_again(self):
    plist = [data.Point(1, 2, 3), data.Point(3, 3, 3)]
    eye = data.Point(0,0,0)
    self.assertEqual(cast.closest_point_index(plist, eye), 0)

  def test_vector_to_pz(self):
    p = data.Point(2,0,0)
    s = data.Sphere(data.Point(3, 0, 0), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    self.assertEqual(cast.vector_to_pz(p, s), data.Vector(-.01, 0, 0))
  def test_vector_to_pz_again(self):
    p = data.Point(2,6,3)
    s = data.Sphere(data.Point(2, 5, 3), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    self.assertEqual(cast.vector_to_pz(p, s), data.Vector(0, 0.01, 0))

  def test_find_pz(self):
    p = data.Point(2,0,0)
    s = data.Sphere(data.Point(3, 0, 0), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    self.assertEqual(cast.find_pz(p,s), data.Point(1.99, 0, 0))
  def test_find_pz_again(self):
    p = data.Point(2,4,3)
    s = data.Sphere(data.Point(2, 4, 5), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    self.assertEqual(cast.find_pz(p,s), data.Point(2, 4, 2.99))

  def test_vector_pz_to_light(self):
    p = data.Point(2,0,0)
    s = data.Sphere(data.Point(3, 0, 0), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    l = data.Point(0, 10, 10)
    v = data.Vector(-0.139341495806, 0.700208521637, 0.700208521637)
    self.assertEqual(cast.vector_pz_to_light(p, s, l), v)
  def test_vector_pz_to_light_again(self):
    p = data.Point(0,5,0)
    s = data.Sphere(data.Point(0, 4, 0), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    l = data.Point(10, 10, 10)
    v = data.Vector(0.666814715969, 0.332740543268, 0.666814715969)
    self.assertEqual(cast.vector_pz_to_light(p, s, l), v)

  def test_dot_product_pz(self):
    p = data.Point(2,0,0)
    s = data.Sphere(data.Point(3, 0, 0), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    l = data.Point(0, 10, 10)
    self.assertAlmostEqual(cast.dot_product_pz(p,s,l), 0.139341495806)
  def test_dot_product_pz_again(self):
    p = data.Point(0,5,0)
    s = data.Sphere(data.Point(0, 4, 0), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    l = data.Point(10, 10, 10)
    self.assertAlmostEqual(cast.dot_product_pz(p, s, l), 0.332740543268)

  def test_sphere_obscure(self):
    p = data.Point(0,5,0)
    s = data.Sphere(data.Point(0, 4, 0), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    l = data.Point(10, 10, 10)
    s1 = data.Sphere(data.Point(1, 4, 3), 2, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    self.assertTrue(cast.sphere_obscure(p,s,l,[s,s1]))
  def test_sphere_obscure_again(self):
    p = data.Point(0,5,0)
    s = data.Sphere(data.Point(0, 4, 0), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    l = data.Point(10, 10, 10)
    s1 = data.Sphere(data.Point(7, 7, 7), 3, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    self.assertFalse(cast.sphere_obscure(p,s,l,[s,s1]))

  def test_reflection_vector(self):
    p = data.Point(0,5,0)
    s = data.Sphere(data.Point(0, 4, 0), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    l = data.Point(10, 10, 10)
    self.assertEqual(cast.reflection_vector(p, s, l), 
           data.Vector(0.666814715969, -0.332740543268, 0.666814715969))
  def test_reflection_vector_again(self):
    p = data.Point(2,0,0)
    s = data.Sphere(data.Point(3, 0, 0), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    l = data.Point(0, 10, 10)
    self.assertEqual(cast.reflection_vector(p, s, l),
           data.Vector(0.139341495806, 0.700208521637, 0.700208521637))

  def test_specular_intensity(self):
    p = data.Point(0,5,0)
    s = data.Sphere(data.Point(0, 4, 0), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    l = data.Point(10, 10, 10)
    e = data.Point(0,0,0)
    self.assertAlmostEqual(cast.specular_intensity(p,s,l,e), -0.332740543268)
  def test_specular_intensity_again(self):
    p = data.Point(7,4,2)
    s = data.Sphere(data.Point(8, 4, 2), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    l = data.Point(0, 10, 1)
    e = data.Point(0,0,0)
    self.assertAlmostEqual(cast.specular_intensity(p,s,l,e), 0.921527596249)

  def test_spec_int_color(self):
    l = 1.5
    s = 0.5
    sr = .05
    si = -.12312
    self.assertAlmostEqual(cast.spec_int_color(l,s,sr,si), 0.0)
  def test_spec_int_color_again(self):
    l = 1.5
    s = 0.6
    sr = .05
    si = 0.818302
    self.assertAlmostEqual(cast.spec_int_color(l,s,sr,si), 0.01631228355142)

  def test_cast_ray(self):
    ray = data.Ray(data.Point(0,0,0), data.Vector(1,0,0))
    s1 = data.Sphere(data.Point(0, 4, 0), 1, data.Color(0.0, 0.0, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    s2 = data.Sphere(data.Point(5, 1, 1), 2, data.Color(1.0, 0.0, 0.0),
                    data.Finish(0.4, 0.4, .5, .05))
    ambient = data.Color(1.0, 1.0, 1.0)
    light = data.Light(data.Point(-100.0, 100.0, -100.0),
              data.Color(1.5, 1.5, 1.5))
    eye = data.Point(0.0, 0.0, -14.0)

    sphere_list = [s1, s2]
    self.assertEqual(cast.cast_ray(ray, sphere_list, ambient, light, eye),
                    data.Color(0.650672150965, 0.0, 0.0))
  def test_cast_ray_again(self):
    ray = data.Ray(data.Point(0,0,0), data.Vector(1,1,1))
    s1 = data.Sphere(data.Point(4, 4, 1), 2, data.Color(0.5, 0.5, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    s2 = data.Sphere(data.Point(5, 1, 1), 2, data.Color(1.0, 0.0, 0.0),
                    data.Finish(0.4, 0.4, .5, .05))
    ambient = data.Color(0.3, 0.4, 0.4)
    light = data.Light(data.Point(-10.0, 200.0, -10.0),
              data.Color(1.5, 1.5, 1.5))
    eye = data.Point(1.0, 1.0, -5.0)
    sphere_list = [s1, s2]
    self.assertEqual(cast.cast_ray(ray, sphere_list, ambient, light, eye),
              data.Color(1.0, 1.0, 1.0))
  def test_cast_ray_again2(self):
    ray = data.Ray(data.Point(0,0,0), data.Vector(2,2,1))
    s1 = data.Sphere(data.Point(4, 4, 1), 2, data.Color(0.5, 0.5, 1.0),
                    data.Finish(0.2, 0.4, .5, .05))
    s2 = data.Sphere(data.Point(5, 1, 1), 2, data.Color(1.0, 0.0, 0.0),
                    data.Finish(0.4, 0.4, .5, .05))
    ambient = data.Color(0.3, 0.4, 0.4)
    light = data.Light(data.Point(-10.0, 200.0, -10.0),
              data.Color(1.5, 1.5, 1.5))
    eye = data.Point(1.0, 1.0, -5.0)
    sphere_list = [s1, s2]
    self.assertEqual(cast.cast_ray(ray, sphere_list, ambient, light, eye),
              data.Color(0.03, 0.04, 0.08))




















if __name__ == '__main__':
   unittest.main()
