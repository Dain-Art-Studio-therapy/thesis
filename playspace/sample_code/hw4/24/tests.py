import unittest
import data
import vector_math
import math
import collisions
import cast

class TestData(unittest.TestCase):
   def test_point(self):
      point1 = data.Point(1, 2, 3)
      self.assertAlmostEqual(point1.x, 1)
      self.assertAlmostEqual(point1.y, 2)
      self.assertAlmostEqual(point1.z, 3)
      self.assertEqual(point1, data.Point(1, 2, 3))
   def test_point_2(self):
      point2 = data.Point(0, -5, 20.0)
      self.assertAlmostEqual(point2.x, 0)
      self.assertAlmostEqual(point2.y, -5)
      self.assertAlmostEqual(point2.z, 20)
      self.assertEqual(point2, data.Point(0, -5, 20))
   def test_vector(self):
      vector = data.Vector(1, 2, 3)
      self.assertAlmostEqual(vector.x, 1)
      self.assertAlmostEqual(vector.y, 2)
      self.assertAlmostEqual(vector.z, 3)
      self.assertEqual(vector, data.Vector(1, 2, 3))
   def test_vector_2(self):
      vector2 = data.Vector(0, -5, 20.0)
      self.assertAlmostEqual(vector2.x, 0)
      self.assertAlmostEqual(vector2.y, -5)
      self.assertAlmostEqual(vector2.z, 20)
      self.assertEqual(vector2, data.Vector(0, -5, 20))
   def test_ray(self):
      point = data.Point(1, 2, 3)
      vector = data.Vector(4, 5, 6)
      ray = data.Ray(point, vector)
      self.assertAlmostEqual(ray.pt.x, 1)
      self.assertAlmostEqual(ray.pt.y, 2)
      self.assertAlmostEqual(ray.pt.z, 3)
      self.assertAlmostEqual(ray.dir.x, 4)
      self.assertAlmostEqual(ray.dir.y, 5)
      self.assertAlmostEqual(ray.dir.z, 6)
      self.assertEqual(ray.pt, point)
      self.assertEqual(ray.dir, vector)
      self.assertEqual(ray.pt, data.Point(1, 2, 3))
      self.assertEqual(ray.dir, data.Vector(4, 5, 6))
      self.assertEqual(ray, data.Ray(data.Point(1, 2, 3), data.Vector(4, 5, 6)))
   def test_ray_2(self):
      point2 = data.Point(0, -1, -2.0)
      vector2 = data.Vector(1, 2, 3.0)
      ray2 = data.Ray(point2, vector2)
      self.assertAlmostEqual(ray2.pt.x, 0)
      self.assertAlmostEqual(ray2.pt.y, -1)
      self.assertAlmostEqual(ray2.pt.z, -2)
      self.assertAlmostEqual(ray2.dir.x, 1)
      self.assertAlmostEqual(ray2.dir.y, 2)
      self.assertAlmostEqual(ray2.dir.z, 3)
      self.assertEqual(ray2.pt, point2)
      self.assertEqual(ray2.dir, vector2)
      self.assertEqual(ray2.pt, data.Point(0, -1, -2))
      self.assertEqual(ray2.dir, data.Vector(1, 2, 3))
      self.assertEqual(ray2, data.Ray(data.Point(0, -1, -2), data.Vector(1, 2, 3)))
   def test_sphere(self):
      point = data.Point(1, 2, 3)
      color = data.Color(0, 0, 0)
      finish = data.Finish(0.2, 1, 0, 0)
      sphere = data.Sphere(point, 1.0, color, finish)
      self.assertAlmostEqual(sphere.center.x, 1)
      self.assertAlmostEqual(sphere.center.y, 2)
      self.assertAlmostEqual(sphere.center.z, 3)
      self.assertEqual(sphere.center, point)
      self.assertAlmostEqual(sphere.radius, 1.0)
      self.assertEqual(sphere.center, data.Point(1, 2, 3))
      self.assertEqual(sphere, data.Sphere(data.Point(1, 2, 3), 1, data.Color(0, 0, 0), data.Finish(.2, 1, 0, 0)))
   def test_sphere_2(self):
      point2 = data.Point(0, -1, -2.0)
      color2 = data.Color(0, 1, 0)
      finish2 = data.Finish(0.2, 1, 0, 0)
      sphere2 = data.Sphere(point2, 2.5, color2, finish2)
      self.assertAlmostEqual(sphere2.center.x, 0)
      self.assertAlmostEqual(sphere2.center.y, -1)
      self.assertAlmostEqual(sphere2.center.z, -2.0)
      self.assertEqual(sphere2.center, point2)
      self.assertAlmostEqual(sphere2.radius, 2.5)
      self.assertEqual(point2, data.Point(0, -1, -2))
      self.assertEqual(sphere2, data.Sphere(data.Point(0, -1, -2), 2.5, data.Color(0, 1, 0), data.Finish(0.2, 1, 0, 0)))
   def test_color_1(self):
      color1 = data.Color(255, 250, 100)
      self.assertAlmostEqual(color1.r, 255)
      self.assertAlmostEqual(color1.g, 250)
      self.assertAlmostEqual(color1.b, 100)
      self.assertEqual(color1, data.Color(255, 250, 100))
   def test_color_2(self):
      color = data.Color(25,77,120)
      self.assertAlmostEqual(color.r, 25)
      self.assertAlmostEqual(color.g, 77)
      self.assertAlmostEqual(color.b, 120)
      self.assertEqual(color, data.Color(25, 77, 120))
   def test_finish_1(self):
      finish = data.Finish(.2, 1, 0, 0)
      self.assertAlmostEqual(finish.ambient, .2)
      self.assertAlmostEqual(finish.diffuse, 1)
      self.assertAlmostEqual(finish.specular, 0)
      self.assertAlmostEqual(finish.roughness, 0)
   def test_finish_2(self):
      finish = data.Finish(.33, .75, 0, 0)
      self.assertAlmostEqual(finish.ambient, .33)
      self.assertAlmostEqual(finish.diffuse, .75)
      self.assertAlmostEqual(finish.specular, 0)
      self.assertAlmostEqual(finish.roughness, 0)
   def test_light_1(self):
      light = data.Light(data.Point(0, 0, 0), data.Color(1, 1, 1))
      self.assertEqual(light.pt, data.Point(0, 0, 0))
      self.assertEqual(light.color, data.Color(1, 1, 1))
   def test_light_2(self):
      light = data.Light(data.Point(1,5,2), data.Color(.5, .25, .75))
      self.assertEqual(light.pt, data.Point(1, 5, 2))
      self.assertEqual(light.color, data.Color(.5, .25, .75))


class TestVectorMath(unittest.TestCase):
   def test_scale_vector_1(self):
      self.assertEqual(vector_math.scale_vector(data.Vector(1, 2, 3), 1.5), data.Vector(1.5, 3, 4.5))
   def test_scale_vector_2(self):
      self.assertEqual(vector_math.scale_vector(data.Vector(5, 10, 15), .2),
         data.Vector(1, 2, 3))
   def test_dot_vector_1(self):
      v1 = data.Vector(1, 2, 3)
      v2 = data.Vector(2, 3, 4)
      self.assertAlmostEqual(vector_math.dot_vector(v1, v2), 20)
   def test_dot_vector_2(self):
      v1 = data.Vector(0, -5, 2)
      v2 = data.Vector(2, 2, 5)
      self.assertAlmostEqual(vector_math.dot_vector(v1, v2), 0)
   def test_length_vector_1(self):
      vec = data.Vector(1, 3, 5)
      self.assertAlmostEqual(vector_math.length_vector(vec), math.sqrt(35))
   def test_length_vector_2(self):
      vec = data.Vector(2, 3, 4)
      self.assertAlmostEqual(vector_math.length_vector(vec), math.sqrt(29))
   def test_normalize_vector_1(self):
      vec = data.Vector(9, 15456, 22)
      newvec = vector_math.normalize_vector(vec)
      self.assertAlmostEqual(vector_math.length_vector(newvec), 1)
   def test_normalize_vector_2(self):
      vec = data.Vector(1, 2, 2)
      newvec = vector_math.normalize_vector(vec)
      self.assertAlmostEqual(vector_math.length_vector(newvec), 1)
      self.assertEqual(newvec, data.Vector(1. / 3, 2. / 3, 2. / 3))
   def test_difference_point_1(self):
      point1 = data.Point(1, 2, 3)
      point2 = data.Point(0, 0, 0)
      vec = vector_math.difference_point(point1, point2)
      self.assertEqual(vec, data.Vector(1, 2, 3))
   def test_difference_point_2(self):
      point1 = data.Point(3, 1, 9)
      point2 = data.Point(1, 5, -4)
      vec = vector_math.difference_point(point1, point2)
      self.assertEqual(vec, data.Vector(2, -4, 13))
   def test_difference_vector_1(self):
      vector1 = data.Vector(2, 5, 2)
      vector2 = data.Vector(0, 4, 0.1)
      newvec = vector_math.difference_vector(vector1, vector2)
      self.assertEqual(newvec, data.Vector(2, 1, 1.9))
   def test_defference_vector_2(self):
      vector1 = data.Vector(-1, -4, 2)
      vector2 = data.Vector(3, -6, 2)
      newvec = vector_math.difference_vector(vector1, vector2)
      self.assertEqual(newvec, data.Vector(-4, 2, 0))
   def test_translate_point_1(self):
      point = data.Point(1, 2, 3)
      vector = data.Vector(1, 2, 3)
      newpoint = vector_math.translate_point(point, vector)
      self.assertEqual(newpoint, data.Point(2, 4, 6))
   def test_translate_point_2(self):
      point = data.Point(3, -2, 6)
      vector = data.Vector(-2.5, 3.3, -2)
      newpoint = vector_math.translate_point(point, vector)
      self.assertEqual(newpoint, data.Point(0.5, 1.3, 4))
   def test_vector_from_to_1(self):
      from_p = data.Point(1, 0, -1)
      to_p = data.Point(2, 2, 2)
      vec = vector_math.vector_from_to(from_p, to_p)
      self.assertEqual(vec, data.Vector(1, 2, 3))
   def test_vector_from_to_2(self):
      from_p = data.Point(3, 6, 1)
      to_p = data.Vector(-1, 2, 5)
      vec = vector_math.vector_from_to(from_p, to_p)
      self.assertEqual(vec, data.Vector(-4, -4, 4))
   def test_distance_1(self):
      p1 = data.Point(0, 0, 0)
      p2 = data.Point(1, 2, 2)
      self.assertAlmostEqual(vector_math.distance(p1, p2), 3)


class TestCollisions(unittest.TestCase):
   def test_intersection_point_1(self):
      sphere = data.Sphere(data.Point(0, 0, 0), 1, data.Color(0, 0, 0), data.Finish(.2, 1, 0, 0))
      ray = data.Ray(data.Point(2, 0, 0), data.Vector(-1, 0, 0))
      int_point = collisions.sphere_intersection_point(ray, sphere)
      self.assertEqual(int_point, data.Point(1, 0, 0))
   def test_intersection_point_2(self):
      sphere = data.Sphere(data.Point(0, 3, 0), 2, data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      ray = data.Ray(data.Point(0, 0, 0), data.Vector(0, 1, 0))
      int_point = collisions.sphere_intersection_point(ray, sphere)
      self.assertEqual(int_point, data.Point(0, 1, 0))
   def test_intersection_point_3(self):
      sphere = data.Sphere(data.Point(1, 1, 1), math.sqrt(3), data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      ray = data.Ray(data.Point(-1, -1, -1), data.Vector(1, 1, 1))
      int_point = collisions.sphere_intersection_point(ray, sphere)
      self.assertEqual(int_point, data.Point(0, 0, 0))
   def test_intersection_point_4(self):
      sphere = data.Sphere(data.Point(0, 0, 0), 1, data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      ray = data.Ray(data.Point(0, 0, 0), data.Vector(1, 0, 0))
      int_point = collisions.sphere_intersection_point(ray, sphere)
      self.assertEqual(int_point, data.Point(1, 0, 0))
   def test_intersection_points_1(self):
      s1 = data.Sphere(data.Point(1, 0, 1), 1, data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      s2 = data.Sphere(data.Point(1, 0, 3), 1, data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      s3 = data.Sphere(data.Point(-1, 0, 5), 1, data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      ray = data.Ray(data.Point(0, 0, 0), data.Vector(0, 0, 1))
      s_list = [s1, s2, s3]
      result_list = [(s1, data.Point(0, 0, 1)), (s2, data.Point(0, 0, 3)), (s3, data.Point(0, 0, 5))]
      self.assertEqual(collisions.find_intersection_points(s_list, ray), result_list)
   def test_intersection_points_2(self):
      s1 = data.Sphere(data.Point(2, 0 ,2), 2, data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      s2 = data.Sphere(data.Point(0, 2, 4), 2, data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      s3 = data.Sphere(data.Point(2, 2, 0), 2, data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      ray = data.Ray(data.Point(0, 0, -6), data.Vector(0, 0, 1))
      s_list = [s1, s2, s3]
      result_list = [(s1, data.Point(0, 0, 2)), (s2, data.Point(0, 0, 4))]
      self.assertEqual(collisions.find_intersection_points(s_list, ray), result_list)
   def test_intersection_points_3(self):
      s1 = data.Sphere(data.Point(2, 2, 2), math.sqrt(3), data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      s2 = data.Sphere(data.Point(-2, -2, 3), 1, data.Color(0, 1, 0), data.Finish(0.2, 1, 0, 0))
      s3 = data.Sphere(data.Point(0, 3, 0), 3 * math.sqrt(2), data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      ray = data.Ray(data.Point(0, 0, 0), data.Vector(1, 1, 1))
      s_list = [s1, s2, s3]
      result_list = [(s1, data.Point(1, 1, 1)), (s3, data.Point(3, 3, 3))]
      self.assertEqual(collisions.find_intersection_points(s_list, ray), result_list)
   def test_normal_point_1(self):
      sphere = data.Sphere(data.Point(0, 0, 0), 5, data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      point_x = data.Point(5, 0, 0)
      point_y = data.Point(0, 5, 0)
      point_z = data.Point(0, 0, 5)
      vec_x = data.Vector(1, 0, 0)
      vec_y = data.Vector(0, 1, 0)
      vec_z = data.Vector(0, 0, 1)
      self.assertEqual(collisions.sphere_normal_at_point(sphere, point_x), vec_x)
      self.assertEqual(collisions.sphere_normal_at_point(sphere, point_y), vec_y)
      self.assertEqual(collisions.sphere_normal_at_point(sphere, point_z), vec_z)
   def test_normal_point_2(self):
      sphere = data.Sphere(data.Point(1, 1, 1), math.sqrt(3), data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      point = data.Point(2, 2, 2)
      vec = data.Vector(1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3))
      self.assertEqual(collisions.sphere_normal_at_point(sphere, point), vec)
   def test_normal_point_3(self):
      sphere = data.Sphere(data.Point(1, -2, 2), 3, data.Color(0, 1, 0), data.Finish(.2, 1, 0, 0))
      point = data.Point(0, 0, 0)
      l = 3.0
      vec = data.Vector(-1 / l, 2 / l, -2 / l)
      self.assertEqual(collisions.sphere_normal_at_point(sphere, point), vec)
      self.assertAlmostEqual(vector_math.length_vector(vec), 1)


class TestCast(unittest.TestCase):
   
   def test_cast_ray_1(self):
      sphere_list = [data.Sphere(data.Point(0, 0, 0), 1, data.Color(0, 0, 0), data.Finish(.2, 1, 0, 0))]
      ray = data.Ray(data.Point(0, 0, -15), data.Vector(0, 0, 1))
      light = data.Light(data.Point(0, 0, 3), data.Color(1, 1, 1))
      ambient_color = data.Color(1, 1, 1)
      eye_point = data.Point(0, 0, -14)
      calc_color = cast.cast_ray(ray, sphere_list, ambient_color, light, eye_point)
      exp_color = data.Color(0, 0, 0)
      self.assertEqual(calc_color, exp_color)
   def test_cast_ray_2(self):
      sphere_list = [data.Sphere(data.Point(0, 0, 0), 1, data.Color(0, 0, 0), data.Finish(.2, 1, 0, 0))]
      ray = data.Ray(data.Point(0, 0, -10), data.Vector(1, 0, 1))
      light = data.Light(data.Point(0, 0, 5), data.Color(1, 1, 1))
      ambient_color = data.Color(1, 1, 1)
      eye_point = data.Point(0, 0, -10)
      calc_color = cast.cast_ray(ray, sphere_list, ambient_color, light, eye_point)
      exp_color = data.Color(1, 1, 1)
      self.assertEqual(calc_color, exp_color)
    def test_closest_sphere_1(self):
      sphere1 = data.Sphere(data.Point(0, 1, 0), 1, data.Color(1, 0, 0), data.Finish(.4, .4, .5, .05))
      point1 = data.Point(0, 0, 0)
      sphere2 = data.Sphere(data.Point(1, 1, 0), 1, data.Color(0, 1, 0), data.Finish(.4, .4, .5, .05))
      point2 = data.Point(0, 1, 0)
      pair1 = (sphere1, point1)
      pair2 = (sphere2, point2)
      pairlist = [pair1, pair2]
      closest = cast.find_closest_sphere(data.Point(0, 0, -14), pairlist)
      self.assertEqual(

      



if __name__ == "__main__":
   unittest.main()
