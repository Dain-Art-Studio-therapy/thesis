#For tests!
import unittest
import data
import vector_math
import collisions
import cast

class TestsHw1(unittest.TestCase):
   def test_point(self):
      a = data.Point(2, 3, 4)
      self.assertEqual(a.x, 2)
      self.assertEqual(a.y, 3)
      self.assertEqual(a.z, 4)

   def test_point_equality(self):
      self.assertEqual(data.Point(15, 4, 12) == data.Point(12, 4, 15), False)

   def test_point_again(self):
      b = data.Point(1, 5, 7)
      self.assertEqual(b.x, 1)
      self.assertEqual(b.y, 5)
      self.assertEqual(b.z, 7)

   def test_point_equality_2(self):
      self.assertEqual(data.Point(5, 7, 9) != data.Point(15, 14, 7), True)

   def test_vector(self):
      c = data.Vector(2.0, 1.0, 0.0)
      self.assertEqual(c.x, 2.0)
      self.assertEqual(c.y, 1.0)
      self.assertEqual(c.z, 0.0)

   def test_vector_equality(self):
      self.assertEqual(data.Vector(3.0, 4.0, 1.2) == data.Vector(3.0, 4.0, 1.2),
         True)

   def test_vector_again(self):
      d = data.Vector(1.0, 0.0, 5.0)
      self.assertEqual(d.x, 1.0)
      self.assertEqual(d.y, 0.0)
      self.assertEqual(d.z, 5.0)

   def test_vector_equality_2(self):
      self.assertEqual(data.Vector(0.0, 3.5, 6.1) == data.Vector(4.2, 3.5, 6.9),
         False)

   def test_ray(self):
      e = data.Ray(data.Point(1, 5, 7), data.Vector(2.0, 3.0, 4.0))
      self.assertEqual(e.pt.x, 1)
      self.assertEqual(e.pt.y, 5)
      self.assertEqual(e.pt.z, 7)
      self.assertAlmostEqual(e.dir.x, 2.0)
      self.assertAlmostEqual(e.dir.y, 3.0)
      self.assertAlmostEqual(e.dir.z, 4.0)

   def test_ray_equality(self):
      ray = data.Ray(data.Point(2, 8, 6), data.Vector(3.0, 5.4, 6.7))
      ray2 = data.Ray(data.Point(5, 7, 4), data.Vector(3.0, 5.4, 6.7))
      self.assertEqual(ray == ray2, False)

   def test_ray_again(self):
      f = data.Ray(data.Point(2, 4, 6), data.Vector(1.0, 0.0, 2.0))
      self.assertEqual(f.pt.x, 2)
      self.assertEqual(f.pt.y, 4)
      self.assertEqual(f.pt.z, 6)
      self.assertAlmostEqual(f.dir.x, 1.0)
      self.assertAlmostEqual(f.dir.y, 0.0)
      self.assertAlmostEqual(f.dir.z, 2.0)

   def test_ray_equality_2(self):
      ray3 = data.Ray(data.Point(5, 7, 1), data.Vector(5.6, 8.9, 3.1))
      ray4 = data.Ray(data.Point(5, 7, 1), data.Vector(5.6, 8.9, 3.1))
      self.assertEqual(ray3 == ray4, True)

   def test_sphere(self):
      g = data.Sphere(data.Point(1, 2, 3), 2.0, data.Color(0.5, 1.0, 0.0),
         data.Finish(0.3, 0.64, 0.4, 0.2))
      self.assertEqual(g.center.x, 1)
      self.assertEqual(g.center.y, 2)
      self.assertEqual(g.center.z, 3)
      self.assertAlmostEqual(g.radius, 2.0)
      self.assertEqual(g.color, data.Color(0.5, 1.0, 0.0))
      self.assertEqual(g.finish, data.Finish(0.3, 0.64, 0.4, 0.2))

   def test_sphere_equality(self):
      self.assertEqual(data.Sphere(data.Point(5, 4, 8), 5.3,
         data.Color(0.0, 0.0, 1.0), data.Finish(0.6, 0.55, 0.1, 0.3)) ==
         data.Sphere(data.Point(4, 1, 22), 8.7, data.Color(0.0, 0.0, 1.0),
         data.Finish(0.6, 0.55, 0.1, 0.3)), False)

   def test_sphere_again(self):
      h = data.Sphere(data.Point(2, 4, 6), 8.0, data.Color(0.0, 1.0, 0.0),
         data.Finish(0.2, 0.3, 0.1, 0.2))
      self.assertEqual(h.center.x, 2)
      self.assertEqual(h.center.y, 4)
      self.assertEqual(h.center.z, 6)
      self.assertAlmostEqual(h.radius, 8.0)
      self.assertEqual(h.color, data.Color(0.0, 1.0, 0.0))
      self.assertEqual(h.finish, data.Finish(0.2, 0.3, 0.1, 0.2))

   def test_sphere_equality_2(self):
      self.assertEqual(data.Sphere(data.Point(4, 3, 6), 4.0,
         data.Color(0.0, 0.5, 0.5), data.Finish(0.5, 0.4, 0.18, 0.65)) ==
         data.Sphere(data.Point(4, 3, 6), 4.0, data.Color(0.0, 0.5, 0.5),
         data.Finish(0.5, 0.4, 0.18, 0.65)), True)

   def test_finish(self):
      fin = data.Finish(0.5, 0.1, 0.4, 0.1)
      self.assertEqual(fin == data.Finish(0.5, 0.1, 0.4, 0.1), True)

   def test_finish_2(self):
      fin = data.Finish(0.1, 0.2, 0.8, 0.4)
      self.assertEqual(fin == data.Finish(0.1, 0.2, 0.8, 0.4), True)

   def test_scale_vector(self):
      vector = data.Vector(2.0, 4.1, 3.5)
      scalar = 2
      self.assertAlmostEqual(vector_math.scale_vector(vector, scalar).x, 4.0)
      self.assertAlmostEqual(vector_math.scale_vector(vector, scalar).y, 8.2)
      self.assertAlmostEqual(vector_math.scale_vector(vector, scalar).z, 7.0)

   def test_scale_vector_2(self):
      vector = data.Vector(1.0, 4.0, 8.0)
      scalar = 4
      self.assertAlmostEqual(vector_math.scale_vector(vector, scalar).x, 4.0)
      self.assertAlmostEqual(vector_math.scale_vector(vector, scalar).y, 16.0)
      self.assertAlmostEqual(vector_math.scale_vector(vector, scalar).z, 32.0)

   def test_dot_vector(self):
      vector = data.Vector(1.0, 5.0, 7.0)
      vector2 = data.Vector(3.0, 4.0, 6.0)
      self.assertAlmostEqual(vector_math.dot_vector(vector, vector2),
         (3.0 + 20.0 + 42.0))

   def test_dot_vector_2(self):
      vector = data.Vector(4.0, 1.0, 2.0)
      vector2 = data.Vector(5.0, 2.0, 3.0)
      self.assertAlmostEqual(vector_math.dot_vector(vector, vector2),
         (20.0 + 2.0 + 6.0))

   def test_length_vector(self):
      self.assertAlmostEqual(vector_math.length_vector(data.Vector(3.0, 4.0,
         0.0)), 5.0)

   def test_length_vector_2(self):
      self.assertAlmostEqual(vector_math.length_vector(data.Vector(5.0, 12.0,
         0.0)), 13.0)

   def test_normalize_vector(self):
      self.assertAlmostEqual(vector_math.normalize_vector(data.Vector(3.0, 4.0,
         5.0)).x, 3.0/7.071067811865476)
      self.assertAlmostEqual(vector_math.normalize_vector(data.Vector(3.0, 4.0,
         5.0)).y, 4.0/7.071067811865476)
      self.assertAlmostEqual(vector_math.normalize_vector(data.Vector(3.0, 4.0,
         5.0)).z, 5.0/7.071067811865476)

   def test_normalize_vector_2(self):
      vector = data.Vector(5.0, 12.0, 13.0)
      self.assertAlmostEqual(vector_math.normalize_vector(vector).x,
         5.0/18.38477631085023)
      self.assertAlmostEqual(vector_math.normalize_vector(vector).y,
         12.0/18.38477631085023)
      self.assertAlmostEqual(vector_math.normalize_vector(vector).z,
         13.0/18.38477631085023)

   def test_difference_point(self):
      self.assertAlmostEqual(vector_math.difference_point(data.Point(5, 4, 7),
         data.Point(2, 3, 8)).x, 3)
      self.assertAlmostEqual(vector_math.difference_point(data.Point(5, 4, 7),
         data.Point(2, 3, 8)).y, 1)
      self.assertAlmostEqual(vector_math.difference_point(data.Point(5, 4, 7),
         data.Point(2, 3, 8)).z, -1)

   def test_difference_point_2(self):
      point1 = data.Point(4, 9, 8)
      point2 = data.Point(4, 6, 7)
      self.assertAlmostEqual(vector_math.difference_point(point1, point2).x, 0)
      self.assertAlmostEqual(vector_math.difference_point(point1, point2).y, 3)
      self.assertAlmostEqual(vector_math.difference_point(point1, point2).z, 1)

   def test_difference_vector(self):
      vector1 = data.Vector(5.0, 2.3, 9.1)
      vector2 = data.Vector(4.5, 1.1, 2.0)
      self.assertAlmostEqual(vector_math.difference_vector(vector1,
         vector2).x, 0.5)
      self.assertAlmostEqual(vector_math.difference_vector(vector1,
         vector2).y, 1.2)
      self.assertAlmostEqual(vector_math.difference_vector(vector1,
         vector2).z, 7.1)

   def test_difference_vector_2(self):
      vector1 = data.Vector(7.5, 8.0, 1.4)
      vector2 = data.Vector(8.0, 5.6, 2.4)
      self.assertAlmostEqual(vector_math.difference_vector(vector1,
         vector2).x, -0.5)
      self.assertAlmostEqual(vector_math.difference_vector(vector1,
         vector2).y, 2.4)
      self.assertAlmostEqual(vector_math.difference_vector(vector1,
         vector2).z, -1.0)

   def test_translate_point(self):
      point = data.Point(1, 5, 7)
      vector = data.Vector(6, 7, 1)
      self.assertAlmostEqual(vector_math.translate_point(point, vector).x, 7)
      self.assertAlmostEqual(vector_math.translate_point(point, vector).y, 12)
      self.assertAlmostEqual(vector_math.translate_point(point, vector).z, 8)

   def test_translate_point_2(self):
      point = data.Point(2, 8, 1)
      vector = data.Vector(3, 6, 4)
      self.assertAlmostEqual(vector_math.translate_point(point, vector).x, 5)
      self.assertAlmostEqual(vector_math.translate_point(point, vector).y, 14)
      self.assertAlmostEqual(vector_math.translate_point(point, vector).z, 5)

   def test_vector_from_to(self):
      point1 = data.Point(5, 8, 4)
      point2 = data.Point(2, 4, 7)
      self.assertAlmostEqual(vector_math.vector_from_to(point1, point2).x, -3)
      self.assertAlmostEqual(vector_math.vector_from_to(point1, point2).y, -4)
      self.assertAlmostEqual(vector_math.vector_from_to(point1, point2).z, 3)

   def test_vector_from_to_2(self):
      point1 = data.Point(5, 2, 3)
      point2 = data.Point(-6, -2, 8)
      self.assertAlmostEqual(vector_math.vector_from_to(point1, point2).x, -11)
      self.assertAlmostEqual(vector_math.vector_from_to(point1, point2).y, -4)
      self.assertAlmostEqual(vector_math.vector_from_to(point1, point2).z, 5)

   def test_sphere_intersection_point(self):
      ray = data.Ray(data.Point(1, 2, 0), data.Vector(3, 4, 1))
      sphere = data.Sphere(data.Point(10, 5, 0), 2, data.Color(1.0, 0.0, 0.5),
         data.Finish(0.3, 0.2, 0.5, 0.9))
      self.assertAlmostEqual(collisions.sphere_intersection_point(ray,
         sphere) == None, True)

   def test_sphere_intersection_point_2(self):
      ray = data.Ray(data.Point(5, 5, 0), data.Vector(1, 1, 0))
      sphere = data.Sphere(data.Point(10, 10, 0), 5, data.Color(0.0, 0.5, 0.0),
         data.Finish(0.4, 0.2, 0.3, 0.7))
      self.assertAlmostEqual(collisions.sphere_intersection_point(ray,
         sphere).x, 6.46446609)
      self.assertAlmostEqual(collisions.sphere_intersection_point(ray,
         sphere).y, 6.46446609)
      self.assertAlmostEqual(collisions.sphere_intersection_point(ray,
         sphere).z, 0)

   def test_find_intersection_points(self):
      spheres = [data.Sphere(data.Point(10, 10, 0), 5, 
         data.Color(0.25, 0.0, 0.0), data.Finish(1.0, 0.1, 0.6, 0.5)),
         data.Sphere(data.Point(20, 10, 0), 1, data.Color(0.0, 1.0, 0.25),
         data.Finish(0.2, 0.5, 0.4, 0.3)), data.Sphere(data.Point(15, 20, 0), 1,
         data.Color(0.25, 0.5, 0.0), data.Finish(0.25, 0.1, 0.2, 0.1))]
      ray = data.Ray(data.Point(5, 15, 0), data.Vector(1, 0, 0))
      self.assertAlmostEqual(collisions.find_intersection_points(spheres,
         ray)[0] == (data.Sphere(data.Point(10, 10, 0), 5, data.Color(0.25, 0.0,         0.0), data.Finish(1.0, 0.1, 0.6, 0.5)), data.Point(10.0, 15.0, 0.0)),
         True)

   def test_find_intersection_points_2(self):
      spheres = [data.Sphere(data.Point(5, 5, 0), 1, data.Color(0.5, 1.0, 0.1), 
         data.Finish(0.2, 0.5, 0.1, 0.2)), data.Sphere(data.Point(0, 0, 0), 2,
         data.Color(0.25, 0.1, 0.0), data.Finish(0.4, 0.1, 0.3, 0.4)),
         data.Sphere(data.Point(10, 10, 0), 5, data.Color(0.0, 0.25, 0.1),
         data.Finish(0.1, 0.2, 0.5, 0.6))]
      ray = data.Ray(data.Point(20, 20, 0), data.Vector(-5, -5, 0))
      l = [(data.Sphere(data.Point(5, 5, 0), 1, data.Color(0.5, 1.0, 0.1),
         data.Finish(0.2, 0.5, 0.1, 0.2)), data.Point(5.70710678119,
         5.70710678119, 0)), (data.Sphere(data.Point(0, 0, 0), 2,
         data.Color(0.25, 0.1, 0.0), data.Finish(0.4, 0.1, 0.3, 0.4)),
         data.Point(1.41421356237, 1.41421356237, 0)), (data.Sphere(
         data.Point(10, 10, 0), 5, data.Color(0.0, 0.25, 0.1), data.Finish(0.1, 
         0.2, 0.5, 0.6)), data.Point(13.5355339059, 13.5355339059, 0))]
      self.assertAlmostEqual(collisions.find_intersection_points(spheres,
         ray)[0] == l[0], True)
      self.assertAlmostEqual(collisions.find_intersection_points(spheres,
         ray)[1] == l[1], True)
      self.assertAlmostEqual(collisions.find_intersection_points(spheres,
         ray)[2] == l[2], True)

   def test_sphere_normal_at_point(self):
      sphere = data.Sphere(data.Point(10, 10, 0), 5,\
         data.Color(0.2, 0.0, 1.0), data.Finish(0.5, 0.1, 0.3, 0.6))
      point = data.Point(15, 10, 0)
      self.assertAlmostEqual(collisions.sphere_normal_at_point(sphere,
         point) == data.Vector(1, 0, 0), True)

   def test_sphere_normal_at_point_2(self):
      sphere = data.Sphere(data.Point(20, 10, 0), 10,\
         data.Color(0.0, 0.0, 0.2), data.Finish(1.0, 0.1, 0.2, 0.5))
      point = data.Point(20, 0, 0)
      self.assertAlmostEqual(collisions.sphere_normal_at_point(sphere,
         point) == data.Vector(0, -1, 0), True)

   def test_cast_ray(self):
      ray = data.Ray(data.Point(0.0, 5.0, 5.0), data.Vector(0.0, 0.0, 1.0))
      sphere1 = data.Sphere(data.Point(0.0, 5.0, 20.0), 5.0,\
         data.Color(0.25, 0.2, 0.0), data.Finish(0.1, 0.5, 0.4, 0.2))
      sphere2 = data.Sphere(data.Point(30.0, 1.0, -30.0), 2.0,\
         data.Color(1.0, 0.5, 0.25), data.Finish(0.2, 0.1, 0.5, 0.6))
      sphere_list = [sphere1, sphere2]
      a_color = data.Color(1.0, 0.5, 0.2)
      light = data.Light(data.Point(0.0, 0.0, 0.0), data.Color(1.0, 1.0, 1.0))
      eye_point = data.Point(4, 10, -30)

      self.assertEqual(cast.cast_ray(ray, sphere_list, a_color, light, \
         eye_point), data.Color(0.494159, 0.455443, 0.350581))

   def test_cast_ray_2(self):
      ray = data.Ray(data.Point(2.0, 2.0, 0.0), data.Vector(0.0, 5.0, 0.0))
      sphere1 = data.Sphere(data.Point(2.0, 9.0, 0.0), 3.0,
         data.Color(0.1, 0.2, 0.0), data.Finish(0.1, 0.2, 0.8, 0.3))
      sphere2 = data.Sphere(data.Point(2.0, 4.0, 0.0), 1.0,
         data.Color(0.5, 0.25, 0.1), data.Finish(0.5, 0.1, 0.1, 0.7))
      sphere_list = [sphere1, sphere2]
      a_color = data.Color(0.2, 0.5, 1.0)
      light = data.Light(data.Point(2.5, 0.3, 4.0), data.Color(0.2, 0.4, 0.66))
      eye_point = data.Point(2, 14, 13)

      self.assertEqual(cast.cast_ray(ray, sphere_list, a_color, light, \
         eye_point), data.Color(0.055551, 0.068051, 0.053663))



if __name__ == '__main__':
   unittest.main()
