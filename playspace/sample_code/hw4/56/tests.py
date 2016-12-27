import unittest
import math
import data
import vector_math
import collisions
import cast

class TestData(unittest.TestCase):
#Points
   def test_point_1(self):
      point1 = data.Point(3, 9, 5)
      self.assertEqual(point1.x, 3)
      self.assertEqual(point1.y, 9)
      self.assertEqual(point1.z, 5)

   def test_point_2(self):
      point2 = data.Point(5, 42, 51)
      self.assertEqual(point2.x, 5)
      self.assertEqual(point2.y, 42)
      self.assertEqual(point2.z, 51)

   def test_point_3(self):
      point3 = data.Point(67, 17, -2)
      self.assertEqual(point3.x, 67)
      self.assertEqual(point3.y, 17)
      self.assertEqual(point3.z, -2)

   def test_point_equality_1(self):
      point4 = data.Point(8, -5, .1)
      point5 = data.Point(8, -5, .1)
      point4 == point5 

   def test_point_equality_2(self):
      point6 = data.Point(2, 6, -3)
      point7 = data.Point(2, 6, -3)
      point6 = point7

   def test_point_equality_3(self):
      point8 = data.Point(8, 100, -10)
      point9 = data.Point(8, 100, -10)
      point8 = point9

#Vectors
   def test_vector_1(self):
      vector1 = data.Vector(9, 16, 25)
      self.assertEqual(vector1.x, 9)
      self.assertEqual(vector1.y, 16)
      self.assertEqual(vector1.z, 25)

   def test_vector_2(self):
      vector2 = data.Vector(5, 8, 13)
      self.assertEqual(vector2.x, 5)
      self.assertEqual(vector2.y, 8)
      self.assertEqual(vector2.z, 13)

   def test_vector_3(self):
      vector3 = data.Vector(7, 17, 13)
      self.assertEqual(vector3.x, 7)
      self.assertEqual(vector3.y, 17)
      self.assertEqual(vector3.z, 13)

   def test_vector_equality_1(self):
      vector4 = data.Vector(59, 3, -1)
      vector5 = data.Vector(59, 3, -1)
      vector4 = vector5

   def test_vector_equality_2(self):
      vector6 = data.Vector(-1, -9, 80)
      vector7 = data.Vector(-1, -9, 80)
      vector6 = vector7

   def test_vector_equality_3(self):
      vector8 = data.Vector(9, -5, 45)
      vector9 = data.Vector(9, -5, 45)
      vector8 = vector9

#Rays
   def test_ray_1(self):
      ray1 = data.Ray(data.Point(5, 3, 1), data.Vector(6, 4, 2))
      self.assertEqual(ray1.pt.x, 5)
      self.assertEqual(ray1.pt.y, 3)
      self.assertEqual(ray1.pt.z, 1)
      self.assertEqual(ray1.dir.x, 6)
      self.assertEqual(ray1.dir.y, 4)
      self.assertEqual(ray1.dir.z, 2)

   def test_ray_2(self):
      ray2 = data.Ray(data.Point(7, 19, 31), data.Vector(8, 42, 100))
      self.assertEqual(ray2.pt.x, 7)
      self.assertEqual(ray2.pt.y, 19)
      self.assertEqual(ray2.pt.z, 31)
      self.assertEqual(ray2.dir.x, 8)
      self.assertEqual(ray2.dir.y, 42)
      self.assertEqual(ray2.dir.z, 100)

   def test_ray_3(self):
      ray3 = data.Ray(data.Point(19, 4, 60), data.Vector(5, 78, 24))
      self.assertEqual(ray3.pt.x, 19)
      self.assertEqual(ray3.pt.y, 4)
      self.assertEqual(ray3.pt.z, 60)
      self.assertEqual(ray3.dir.x, 5)
      self.assertEqual(ray3.dir.y, 78)
      self.assertEqual(ray3.dir.z, 24)

   def test_ray_equality_1(self):
      ray4 = data.Ray(data.Point(5, 3, 2), data.Vector(5, 3, 2))
      ray5 = data.Ray(data.Point(5, 3, 2), data.Vector(5, 3, 2))
      ray4 = ray5

   def test_ray_equality_2(self):
      ray6 = data.Ray(data.Point(65, 43, 21), data.Vector(98, 76, 54))
      ray7 = data.Ray(data.Point(65, 43, 21), data.Vector(98, 76, 54))
      ray6 = ray7

   def test_ray_equality_3(self):
      ray8 = data.Ray(data.Point(54, 9, 6), data.Vector(63, 9, 7))
      ray9 = data.Ray(data.Point(54, 9, 6), data.Vector(63, 9, 7))
      ray8 = ray9

#Spheres
   def test_sphere_1(self):
      sphere1 = data.Sphere(data.Point(31, -3, 25), 6, data.Color(0.0, 0.0, 0.0), 1.0)
      self.assertEqual(sphere1.center.x, 31)
      self.assertEqual(sphere1.center.y, -3)
      self.assertEqual(sphere1.center.z, 25)
      self.assertEqual(sphere1.radius, 6)
      self.assertEqual(sphere1.color.r, 0.0)
      self.assertEqual(sphere1.color.g, 0.0)
      self.assertEqual(sphere1.color.b, 0.0)
      self.assertEqual(sphere1.finish, 1.0)

   def test_sphere_2(self):
      sphere2 = data.Sphere(data.Point(24, 78, -14), 13, data.Color(1.0, 0.0, 0.0), .5)
      self.assertEqual(sphere2.center.x, 24)
      self.assertEqual(sphere2.center.y, 78)
      self.assertEqual(sphere2.center.z, -14)
      self.assertEqual(sphere2.radius, 13)
      self.assertEqual(sphere2.color.r, 1.0)
      self.assertEqual(sphere2.color.g, 0.0)
      self.assertEqual(sphere2.color.b, 0.0)
      self.assertEqual(sphere2.finish, .5)

   def test_sphere_3(self):
      sphere3 = data.Sphere(data.Point(14, 8, -9), 12, data.Color(1.0, 1.0, 1.0), .1)
      self.assertEqual(sphere3.center.x, 14)
      self.assertEqual(sphere3.center.y, 8)
      self.assertEqual(sphere3.center.z, -9)
      self.assertEqual(sphere3.radius, 12)
      self.assertEqual(sphere3.color.r, 1.0)
      self.assertEqual(sphere3.color.g, 1.0)
      self.assertEqual(sphere3.color.b, 1.0)
      self.assertEqual(sphere3.finish, .1)

   def test_sphere_equality_1(self):
      sphere4 = data.Sphere(data.Point(15, 3, -5), 5, data.Color(0.0, 0.0, 0.0), 1.0)
      sphere5 = data.Sphere(data.Point(15, 3, -5), 5, data.Color(0.0, 0.0, 0.0), 1.0)
      sphere4 = sphere5

   def test_sphere_equality_2(self):
      sphere6 = data.Sphere(data.Point(1, -3, .03), 9, data.Color(0.0, 0.0, 1.0), .5)
      sphere7 = data.Sphere(data.Point(1, -3, .03), 9, data.Color(0.0, 0.0, 1.0), .5)
      sphere6 = sphere7

   def test_sphere_equality_3(self):
      sphere8 = data.Sphere(data.Point(5, -2.5, 98), 78, data.Color(1.0, 1.0, 1.0), .01)
      sphere9 = data.Sphere(data.Point(5, -2.5, 98), 78, data.Color(1.0, 1.0, 1.0), .01)
      sphere8 = sphere9

class TestVectorMath(unittest.TestCase):
#Scale Vector
   def test_scale_vector_1(self):
      vector1 = data.Vector(3, 8, 21)
      scalar1 = 2
      answer1 = data.Vector(6, 16, 42)
      self.assertEqual(vector_math.scale_vector(vector1, scalar1), answer1)

   def test_scale_vector_2(self):
      vector2 = data.Vector(2, -2, 44)
      scalar2 = .5
      answer2 = data.Vector(1, -1, 22)
      self.assertEqual(vector_math.scale_vector(vector2, scalar2), answer2)

   def test_scale_vector_3(self):
      vector3 = data.Vector(33, 11, 44)
      scalar3 = 3
      answer3 = data.Vector(99, 33, 132)
      self.assertEqual(vector_math.scale_vector(vector3, scalar3), answer3)

#Dot Vector
   def test_dot_vector_1(self):
      vector4 = data.Vector(-3, 4, 5)
      vector5 = data.Vector(5, -2, 7)
      self.assertEqual(vector_math.dot_vector(vector4, vector5), 12)

   def test_dot_vector_2(self):
      vector6 = data.Vector(100, 20, .1)
      vector7 = data.Vector(.1, .2, 300)
      self.assertEqual(vector_math.dot_vector(vector6, vector7), 44)

   def test_dot_vector_3(self):
      vector8 = data.Vector(20, 3, 56)
      vector9 = data.Vector(.5, 2, .5)
      self.assertEqual(vector_math.dot_vector(vector8, vector9), 44) 

#Length Vector
   def test_length_vector_1(self):
      vector10 = data.Vector(2, 1, 2)
      self.assertEqual(vector_math.length_vector(vector10), 3)

   def test_length_vector_2(self):
      vector11 = data.Vector(4, math.sqrt(7), math.sqrt(2))
      self.assertEqual(vector_math.length_vector(vector11), 5)

   def test_length_vector_3(self):
      vector12 = data.Vector(math.sqrt(6), 5, 15)
      self.assertEqual(vector_math.length_vector(vector12), 16)

#Normalize Vector
   def test_normalize_vector_1(self):
      vector13 = data.Vector(2.0, 1.0, 2.0)
      answer4 = data.Vector(2.0/3.0, 1.0/3.0, 2.0/3.0)
      self.assertEqual(vector_math.normalize_vector(vector13), answer4)

   def test_normalize_vector_2(self):
      vector14 = data.Vector(4.0, 2.0, 4.0)
      answer5 = data.Vector(4.0/6.0, 2.0/6.0, 4.0/6.0)
      self.assertEqual(vector_math.normalize_vector(vector14), answer5)

   def test_normalize_vector_3(self):
      vector15 = data.Vector(6.0, 3.0, 6.0)
      answer6 = data.Vector(6.0/9.0, 3.0/9.0, 6.0/9.0)
      self.assertEqual(vector_math.normalize_vector(vector15), answer6)

#Difference Point
   def test_difference_point_1(self):
      point10 = data.Point(3, 6, 9)
      point11 = data.Point(9, 112, 179)
      answer7 = data.Point(-6, -106, -170)
      self.assertEqual(vector_math.difference_point(point10, point11), answer7)

   def test_difference_point_2(self):
      point12 = data.Point(106, 532, 80)
      point13 = data.Point(54, 425, 12)
      answer8 = data.Point(52, 107, 68)
      self.assertEqual(vector_math.difference_point(point12, point13), answer8)

   def test_difference_point_3(self):
      point14 = data.Point(53, 21, 8)
      point15 = data.Point(29, -5, 6)
      answer9 = data.Point(24, 26, 2)
      self.assertEqual(vector_math.difference_point(point14, point15), answer9)

#Difference Vector
   def test_difference_vector_1(self):
      vector16 = data.Vector(9, 12, 54)
      vector17 = data.Vector(5, 18, 52)
      answer10 = data.Vector(4, -6, 2)
      self.assertEqual(vector_math.difference_vector(vector16, vector17), answer10)

   def test_difference_vector_2(self):
      vector18 = data.Vector(98, 54, 21)
      vector19 = data.Vector(87, 65, 32)
      answer11 = data.Vector(11, -11, -11)
      self.assertEqual(vector_math.difference_vector(vector18, vector19), answer11)

   def test_difference_vector_3(self):
      vector20 = data.Vector(51, 21, 61)
      vector21 = data.Vector(32, 41, 2)
      answer12 = data.Vector(19, -20, 59)
      self.assertEqual(vector_math.difference_vector(vector20, vector21), answer12)

#Translate Point
   def test_translate_point_1(self):
      point16 = data.Point(2, 5, 12)
      vector22 = data.Vector(6, 8, 1)
      answer13 = data.Point(8, 13, 13)
      self.assertEqual(vector_math.translate_point(point16, vector22), answer13)

   def test_translate_point_2(self):
      point17 = data.Point(5, -3, 18)
      vector23 = data.Vector(-20, 25, -3)
      answer14 = data.Point(-15, 22, 15)
      self.assertEqual(vector_math.translate_point(point17, vector23), answer14)

   def test_translate_point_3(self):
      point18 = data.Point(6, 54, -12)
      vector24 = data.Vector(25, -41, 2)
      answer15 = data.Point(31, 13, -10)
      self.assertEqual(vector_math.translate_point(point18, vector24), answer15)

#Vector From To
   def test_vector_from_to_1(self):
      point19 = data.Point(5, 16, 12)
      point20 = data.Point(9, 5, 6)
      answer16 = data.Vector(4, -11, -6)
      self.assertEqual(vector_math.vector_from_to(point19, point20), answer16)

   def test_vector_from_to_2(self):
      point21 = data.Point(6, 51, 78)
      point22 = data.Point(-10, 25, 12)
      answer17 = data.Vector(-16, -26, -66)
      self.assertEqual(vector_math.vector_from_to(point21, point22), answer17)

   def test_vector_from_to_3(self):
      point23 = data.Point(45, 92, 13)
      point24 = data.Point(42, -8, 16)
      answer18 = data.Vector(-3, -100, 3)
      self.assertEqual(vector_math.vector_from_to(point23, point24), answer18)

class TestCollisions (unittest.TestCase):
#Sphere Intersection Point
   def test_sphere_intersection_point_1(self):
      sphere1 = data.Sphere(data.Point(0, 0, 0), 10, data.Color(0.0, 0.0, 0.0), 1.0)
      ray1 = data.Ray(data.Point(-20, 0, 0), data.Vector(1, 0, 0))
      point1 = collisions.sphere_intersection_point(ray1, sphere1)
      answer1 = data.Point(-10, 0, 0)
      self.assertEqual(point1, answer1)

   def test_sphere_intersection_point_2(self):
      sphere2 = data.Sphere(data.Point(-1000, -100, -10), 1, data.Color(0.0, 0.0, 1.0), .5)
      ray2 = data.Ray(data.Point(900, 3, 15), data.Vector(1, 1, 1))
      point2 = collisions.sphere_intersection_point(ray2, sphere2)
      self.assertEqual(point2, None)

   def test_sphere_intersection_point_3(self):
      sphere3 = data.Sphere(data.Point(3, 6, 9), 21, data.Color(1.0, 1.0, 1.0), .5)
      ray3 = data.Ray(data.Point(3, 6, 9), data.Vector(0, 0, 12))
      point3 = collisions.sphere_intersection_point(ray3, sphere3)
      answer3 = data.Point(3, 6, 30)
      self.assertTrue(point3 == answer3)

#Find Intersection Points
   def test_find_intersection_points_1(self):
      sphere1 = data.Sphere(data.Point(-5, 0, 0), 1, data.Color(1.0, 0.0, 0.0), .5)
      sphere2 = data.Sphere(data.Point(0, 0, 0), 2, data.Color(0.0, 1.0, 0.0), .15)
      sphere3 = data.Sphere(data.Point(5, 0, 0), 2, data.Color(0.0, 0.0, 1.0), .01)
      ray = data.Ray(data.Point(-100, 0, 0), data.Vector(150, 0, 0))
      sphereList = [sphere1, sphere2, sphere3]
      intersectionList = collisions.find_intersection_points(sphereList, ray)
      point1 = data.Point(-6, 0, 0)
      point2 = data.Point(-2, 0, 0)
      point3 = data.Point(3, 0, 0)
      intersection1 = (sphere1, point1)
      intersection2 = (sphere2, point2)
      intersection3 = (sphere3, point3)
      answerList = [intersection1, intersection2, intersection3]
      self.assertEqual(intersectionList, answerList)

   def test_find_intersection_points_2(self):
      sphere1 = data.Sphere(data.Point(0, 11, 0), 10, data.Color(0.0, 0.0, 0.0), .25)
      sphere2 = data.Sphere(data.Point(-100, -100, -100), 1, data.Color(1.0, 1.0, 1.0), .5)
      ray = data.Ray(data.Point(0, 0, 0), data.Vector(0, 100, 0))
      sphereList = [sphere1, sphere2]
      intersectionList = collisions.find_intersection_points(sphereList, ray)
      intersection1 = (sphere1, data.Point(0, 1, 0))
      answerList = [intersection1]
      self.assertEqual(intersectionList, answerList)

   def test_find_intersection_points_3(self):
      sphere1 = data.Sphere(data.Point(0, 0, -100), 3, data.Color(1.0, 1.0, 0.0), .6)
      sphere2 = data.Sphere(data.Point(100, 0, -100), 10, data.Color(0.0, 1.0, 1.0), .7)
      sphere3 = data.Sphere(data.Point(-100, 0, -100), 2, data.Color(1.0, 0.0, 1.0), .8)
      ray = data.Ray(data.Point(0, 0, -100), data.Vector(1, 0, 0))
      sphereList = [sphere1, sphere2, sphere3]
      intersectionList = collisions.find_intersection_points(sphereList, ray)
      intersection1 = (sphere1, data.Point(3, 0, -100))
      intersection2 = (sphere2, data.Point(90, 0, -100))
      answerList = [intersection1, intersection2]
      self.assertEqual(intersectionList, answerList)

#Sphere Normal At Point
   def test_sphere_normal_at_point_1(self):
      sphere1 = data.Sphere(data.Point(0, 0, 0), 10, data.Color(0.0, 0.0, 0.0), 1.0)
      point1 = data.Point(10, 10, 10)
      vector1 = collisions.sphere_normal_at_point(sphere1, point1)
      answer1 = data.Vector(1.0 / math.sqrt(3), 1.0 / math.sqrt(3), 1.0 / math.sqrt(3))
      self.assertTrue(vector1 == answer1)

   def test_sphere_normal_at_point_2(self):
      sphere2 = data.Sphere(data.Point(0, 0, 0), 50, data.Color(1.0, 1.0, 1.0), .1)
      point2 = data.Point(0, 50, 0)
      vector2 = collisions.sphere_normal_at_point(sphere2, point2)
      answer2 = data.Vector(0, 1, 0)
      self.assertTrue(vector2 == answer2)

   def test_sphere_normal_at_point_3(self):
      sphere3 = data.Sphere(data.Point(3, 4, 0), 5, data.Color(0.0, 0.0, 0.0), .3)
      point3 = data.Point(3,-1, 5)
      vector3 = collisions.sphere_normal_at_point(sphere3, point3)
      answer3 = data.Vector(0, -1 / math.sqrt(2), 1 / math.sqrt(2))
      self.assertTrue(vector3 == answer3)

class TestCast (unittest.TestCase):
#Cast Ray
   def test_cast_ray_1(self):
      ray1 = data.Ray(data.Point(0, 0, 0), data.Vector(1, 0, 0))
      sphere_list_1 = [data.Sphere(data.Point(5, 0, 0) , 2, data.Color(0.0, 1.0, 0), data.Finish(.5, .5)), data.Sphere(data.Point(-5, 0, 0), 2, data.Color(1.0, 0.0, 0.0), data.Finish(.5, .5)), data.Sphere(data.Point(3, 3, 3), 1, data.Color(0.0, 0.0, 1.0), data.Finish(.5, .5))]
      light1 = data.Light(data.Point(0, 0, 0), data.Color(1.0, 1.0, 1.0))
      cast_ray_1 = cast.cast_ray(ray1, sphere_list_1, light1)
      self.assertTrue(cast_ray_1 == data.Color(0.0, .5, 0.0))

   def test_cast_ray_2(self):
      ray2 = data.Ray(data.Point(0, 100, 0), data.Vector(0, 100, 0))
      sphere_list_2 = [data.Sphere(data.Point(-100, 0, 0), 10, data.Color(0.9, 0.0, 0.0), data.Finish(.1, .5)), data.Sphere(data.Point(900, 0, 0), 5, data.Color(1.0, 1.0, 1.0), data.Finish(.1, .5))]
      light2 = data.Light(data.Point(0, 0, 0), data.Color(0.0, 0.0, 1.0))
      cast_ray_2 = cast.cast_ray(ray2, sphere_list_2, light2)
      self.assertTrue(cast_ray_2 == data.Color(1.0, 1.0, 1.0))

   def test_cast_ray_3(self):
      ray3 = data.Ray(data.Point(1, 1, 1), data.Vector(1, 1, 1))
      sphere_list_3 = [data.Sphere(data.Point(3, 3, 3), 1, data.Color(1.0, 1.0, 1.0), data.Finish(1.0, .5)), data.Sphere(data.Point(900, 900, 900), 100, data.Color(0.0, 1.0, 0.0), data.Finish(1.0, .5)), data.Sphere(data.Point(10, 10, 10), 5, data.Color(0.0, 0.0, 1.0), data.Finish(1.0, .5))]
      light3 = data.Light(data.Point(0, 0, 0), data.Color(0.0, 1.0, 1.0))
      cast_ray_3 = cast.cast_ray(ray3, sphere_list_3, light3)
      self.assertTrue(cast_ray_3 == data.Color(0.0, 1.0, 1.0))

#Color Conversion
   def test_color_conversion_1(self):
      color1 = data.Color(1.0, 1.0, 1.0)
      answer = cast.color_conversion(color1)
      new_color_1 = data.Color(255.0, 255.0, 255.0)
      self.assertTrue(answer  == new_color_1)

   def test_color_conversions_2(self):
      color2 = data.Color(0.0, 0.0, 1.0)
      answer = cast.color_conversion(color2)
      new_color_2 = data.Color(0.0, 0.0, 255.0)
      self.assertTrue(answer  == new_color_2)

   def test_color_conversions_3(self):
      color3 = data.Color(0.0, 0.0, 0.0)
      answer = cast.color_conversion(color3)
      new_color_3 = data.Color(0.0, 0.0, 0.0)
      self.assertTrue(answer == new_color_3)
if __name__ == "__main__":
   unittest.main()

