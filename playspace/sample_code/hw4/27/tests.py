import unittest
from vector_math import *
import utility
from data import *
from collisions import *
from cast import cast_ray

class TestData(unittest.TestCase):
        def test_Point1(self):
                Point1 = Point(0, 0, 0)
                self.assertEqual(Point1.x, 0)
                self.assertEqual(Point1.y, 0)
                self.assertEqual(Point1.z, 0)

        def test_equality1(self):
                pt1 = Point(1, 1, 1)
                pt2 = Point(1, 1, 1)
                self.assertEqual(pt1, pt2)

        def test_Point2(self):
                Point2 = Point(1, 1, 1)
                self.assertEqual(Point2.x, 1)
                self.assertEqual(Point2.y, 1)
                self.assertEqual(Point2.z, 1)

        def test_equality2(self):
                pt1 = Point(1, 1, 2)
                pt2 = Point(1, 1, 2)
                self.assertEqual(pt1, pt2)

        def test_Vector1(self):
                Vector1 = Vector(1, 0, 0)
                self.assertEqual(Vector1.x, 1)
                self.assertEqual(Vector1.y, 0)
                self.assertEqual(Vector1.z, 0)

        def test_equality3(self):
                vct1 = Vector(1, 1, 1)
                vct2 = Vector(1, 1, 1)
                self.assertEqual(vct1, vct2)

        def test_Vector2(self):
                Vector2 = Vector(0, 1, 0)
                self.assertEqual(Vector2.x, 0)
                self.assertEqual(Vector2.y, 1)
                self.assertEqual(Vector2.z, 0)

        def test_equality4(self):
                vct1 = Vector(1, 1, 2)
                vct2 = Vector(1, 1, 2)
                self.assertEqual(vct1, vct2)

	def test_Ray1(self):
                Ray1 = Ray(Point(0, 0, 0), Vector(1, 0, 0))
                self.assertEqual(Ray1.pt.x, 0)
                self.assertEqual(Ray1.pt.y, 0)
                self.assertEqual(Ray1.pt.z, 0)
                self.assertEqual(Ray1.dir.x, 1)
                self.assertEqual(Ray1.dir.y, 0)
                self.assertEqual(Ray1.dir.z, 0)

        def test_equality5(self):
                ray1 = Ray(Point(1, 1, 2), Vector(0, 0, 0))
                ray2 =Ray(Point(1, 1, 2), Vector(0, 0, 0))
                self.assertEqual(ray1.pt, ray2.pt)
                self.assertEqual(ray1.dir, ray2.dir)

        def test_Ray2(self):
                Ray2 = Ray(Point(1, 1, 1), Vector(0, 1, 0))
                self.assertEqual(Ray2.pt.x, 1)
                self.assertEqual(Ray2.pt.y, 1)
                self.assertEqual(Ray2.pt.z, 1)
                self.assertEqual(Ray2.dir.x, 0)
                self.assertEqual(Ray2.dir.y, 1)
                self.assertEqual(Ray2.dir.z, 0)

        def test_equality6(self):
                ray1 = Ray(Point(1, 1, 3), Vector(0, 0, 1))
                ray2 = Ray(Point(1, 1, 3), Vector(0, 0, 1))
                self.assertEqual(ray1.pt, ray2.pt)
                self.assertEqual(ray1.dir, ray2.dir)

	def test_Sphere1(self):
                Sphere1 = Sphere(Point(0, 0, 0), (1), Color(1.0, 0, 0))
                self.assertEqual(Sphere1.center.x, 0)
                self.assertEqual(Sphere1.center.y, 0)
                self.assertEqual(Sphere1.center.z, 0)
                self.assertAlmostEqual(Sphere1.radius, 1)
		self.assertEqual(Sphere1.color.r, 1.0)
                self.assertEqual(Sphere1.color.g, 0)
                self.assertEqual(Sphere1.color.b, 0)

        def test_equality7(self):
                sphere1 = Sphere(Point(0, 0, 0), 7, Color(0,0,0))
                sphere2 = Sphere(Point(0, 0, 0), 7, Color(0,0,0))
                self.assertEqual(sphere1.center, sphere2.center)
                self.assertEqual(sphere1.radius, sphere2.radius)
		self.assertEqual(sphere1.color, sphere2.color)

        def test_Sphere2(self):
                Sphere2 = Sphere(Point(1, 1, 1), 4, Color(0, 1.0, 0))
                self.assertEqual(Sphere2.center.x, 1)
                self.assertEqual(Sphere2.center.y, 1)
                self.assertEqual(Sphere2.center.z, 1)
                self.assertAlmostEqual(Sphere2.radius, 4)
		self.assertEqual(Sphere2.color.r, 0)
                self.assertEqual(Sphere2.color.g, 1.0)
                self.assertEqual(Sphere2.color.b, 0)


        def test_equality8(self):
                sphere1 = Sphere(Point(0, 1, 0), 8, Color(1.0, 1.0, 1.0))
                sphere2 = Sphere(Point(0, 1, 0), 8, Color(1.0, 1.0, 1.0))
                self.assertEqual(sphere1.center, sphere2.center)
                self.assertEqual(sphere1.radius, sphere2.radius)
		self.assertEqual(sphere1.color, sphere2.color)


	def test_Color1(self):
                Color1 = Color(0.0, 0.0, 0.0)
                self.assertEqual(Color1.r, 0.0)
                self.assertEqual(Color1.g, 0.0)
                self.assertEqual(Color1.b, 0.0)

        def test_equality9(self):
                cl1 = Color(1.0, 1.0, 1.0)
                cl2 = Color(1.0, 1.0, 1.0)
                self.assertEqual(cl1, cl2)

        def test_Color2(self):
                Color2 = Color(1.0, 1.0, 1.0)
                self.assertEqual(Color2.r, 1.0)
                self.assertEqual(Color2.g, 1.0)
                self.assertEqual(Color2.b, 1.0)

        def test_equality10(self):
                pt1 = Color(1.0, 1.0, 1.0)
                pt2 = Color(1.0, 1.0, 1.0)
                self.assertEqual(pt1, pt2)

	def test_scale_vector1(self):
                scale_vector1 = scale_vector(Vector(0, 0, 1), 1)
                self.assertEqual(scale_vector1.x, 0)
                self.assertEqual(scale_vector1.y, 0)
                self.assertEqual(scale_vector1.z, 1)

        def test_scale_vector2(self):
                scale_vector2 = scale_vector(Vector(1, 1, 1), 7)
                self.assertEqual(scale_vector2.x, 7)
                self.assertEqual(scale_vector2.y, 7)
                self.assertEqual(scale_vector2.z, 7)

        def test_dot_vector1(self):
                dot_vector1 = dot_vector(Vector(2, 2, 2), Vector(3, 3, 3))
                self.assertEqual(dot_vector1, 18)

        def test_dot_vector2(self):
                dot_vector2 = dot_vector(Vector(3, 2, 2), Vector(2, 3, 3))
                self.assertEqual(dot_vector2, 18)

        def test_length_vector1(self):
                length_vector1 = length_vector(Vector(1, 4, 3))
                self.assertEqual(length_vector1, 5.0990195135927845)

        def test_length_vector2(self):
                length_vector2 = length_vector(Vector(1, 1, 1))
                self.assertEqual(length_vector2, 1.7320508075688772)

	def test_normalize_vector1(self):
                normalize_vector1 = normalize_vector(Vector(1, 1, 1))
                self.assertEqual(normalize_vector1.x, 0.57735026918962584)
                self.assertEqual(normalize_vector1.y, 0.57735026918962584)
                self.assertEqual(normalize_vector1.z, 0.57735026918962584)

        def test_normalize_vector2(self):
                normalize_vector2 = normalize_vector(Vector(3, 4, 7))
                self.assertEqual(normalize_vector2.x, 0.34874291623145787)
                self.assertEqual(normalize_vector2.y, 0.46499055497527714)
                self.assertEqual(normalize_vector2.z, 0.813733471206735)


        def test_Difference_Point1(self):
                difference_point1 = difference_point(Point(4, 4, 4), Point(0, 0, 0))
                self.assertEqual(difference_point1.x, 4)
                self.assertEqual(difference_point1.y, 4)
                self.assertEqual(difference_point1.z, 4)

        def test_Difference_Point2(self):
                difference_point2 = difference_point(Point(2, 2, 2), Point(0, 0, 0))
                self.assertEqual(difference_point2.x, 2)
                self.assertEqual(difference_point2.y, 2)
                self.assertEqual(difference_point2.z, 2)

	def test_Difference_Vector1(self):
                difference_vector1 = difference_vector(Vector(4, 4, 4), Vector(0, 0, 0))
                self.assertEqual(difference_vector1.x, 4)
                self.assertEqual(difference_vector1.y, 4)
                self.assertEqual(difference_vector1.z, 4)

        def test_Difference_Vector2(self):
                difference_vector2 = difference_vector(Vector(2, 2, 2), Vector(0, 0, 0))
                self.assertEqual(difference_vector2.x, 2)
                self.assertEqual(difference_vector2.y, 2)
                self.assertEqual(difference_vector2.z, 2)

        def test_Translate_Point1(self):
                translate_point1 = translate_point(Point(0, 0, 0), Vector(1, 1, 1))
                self.assertEqual(translate_point1.x, 1)
                self.assertEqual(translate_point1.y, 1)
                self.assertEqual(translate_point1.z, 1)

        def test_Translate_Point2(self):
                translate_point2 = translate_point(Point(0, 0, 0), Vector(2, 2, 2))
                self.assertEqual(translate_point2.x, 2)
                self.assertEqual(translate_point2.y, 2)
                self.assertEqual(translate_point2.z, 2)

        def test_Vector_From_To1(self):
                vector_from_to1 = vector_from_to(Point(1, 0, 0), Point(2, 0, 0))
                self.assertEqual(vector_from_to1.x, 1)
                self.assertEqual(vector_from_to1.y, 0)
                self.assertEqual(vector_from_to1.z, 0)

        def test_Vector_From_To_2(self):
                vector_from_to2 = vector_from_to(Point(0, 0,0), Point(2, 0, 0))
                self.assertEqual(vector_from_to2.x, 2)
                self.assertEqual(vector_from_to2.y, 0)
                self.assertEqual(vector_from_to2.z, 0)


	def test_scale_color1(self):
                scale_color1 = scale_color(Color(0.0, 0.0, 1.0), 255)
                self.assertEqual(scale_color1.r, 0.0)
                self.assertEqual(scale_color1.g, 0.0)
                self.assertEqual(scale_color1.b, 255.0)

        def test_scale_color2(self):
                scale_color2 = scale_color(Color(1.0, 1.0, 1.0), 255)
                self.assertEqual(scale_color2.r, 255.0)
                self.assertEqual(scale_color2.g, 255.0)
                self.assertEqual(scale_color2.b, 255.0)


        def test_sphere_intersection_point(self):
                ray1 = Ray(Point(0, 0, 0), Vector(10, 0, 0))
                sphere1 = Sphere(Point(5, 0, 0), 3, Color(0, 0, 0))
                self.assertEqual(sphere_intersection_point(ray1, sphere1), Point(2, 0, 0))

        def test_sphere_intersection_point2(self):
                ray1 = Ray(Point(0, 0, 0), Vector(8, 0, 0))
                sphere1 = Sphere(Point(4, 0, 0), 1, Color(1.0, 1.0, 1.0))
                self.assertEqual(sphere_intersection_point(ray1, sphere1), Point(3, 0, 0))

        def test_find_intersection_points(self):
                list1 = [Sphere(Point(3, 0, 0), 1, Color(1.0, 1.0, 1.0)), Sphere(Point(289, 200, 2001), 1, Color(0, 0, 0)), Sphere(Point(7, 0, 0), 4, Color(1.0, 0, 1.0))]
                ray1 = Ray(Point(0, 0, 0), Vector(10, 0, 0))
                list2 = [(Sphere(Point(3, 0, 0), 1, Color(1.0, 1.0, 1.0)), Point(2, 0, 0)), (Sphere(Point(7, 0, 0), 4, Color(1.0, 0, 1.0)), Point(3, 0, 0))]
                self.assertEqual(find_intersection_points(list1, ray1), list2)

	def test_find_intersection_points1(self):
                list1 = [Sphere(Point(2, 0, 0), 1, Color(1.0, 0, 0)), Sphere(Point(289, 200, 2001), 1, Color(0, 0, 0)), Sphere(Point(4, 0, 0), 1, Color(1.0, 1.0, 1.0))]
                ray1 = Ray(Point(0, 0, 0), Vector(14, 0, 0))
                list2 = [(Sphere(Point(2, 0, 0), 1, Color(1.0, 0, 0)), Point(1, 0, 0)), (Sphere(Point(4, 0, 0), 1, Color(1.0, 1.0, 1.0)), Point(3, 0, 0))]
                self.assertEqual(find_intersection_points(list1, ray1),  list2)


        def test_sphere_normal_at_point(self):
                sphere1 = Sphere(Point(0, 0, 0), 3, Color(0, 0, 0))
                point2 = Point(3, 0, 0)
                self.assertEqual(sphere_normal_at_point(sphere1, point2), Vector(1, 0, 0))


        def test_sphere_normal_at_point2(self):
                sphere1 = Sphere(Point(0, 0, 0), 5, Color(0, 0, 1.0))
                point2 = Point(0, 5, 0)
                self.assertEqual(sphere_normal_at_point(sphere1, point2), Vector(0, 1, 0))


        def test_cast_ray1(self):
                list1 = [Sphere(Point(3, 0, 0), 1, Color(1.0, 1.0, 1.0)), Sphere(Point(289, 200, 2001), 1, Color(0, 1.0, 0))]
                ray1 = Ray(Point(0, 0, 0), Vector(14, 0, 0))
                self.assertEqual(cast_ray(list1, ray1), True)

        def test_cast_ray2(self):
                list1 = [Sphere(Point(3, 0, 0), 1, Color(0, 0, 0)), Sphere(Point(7, 0, 0), 1, Color(0, 0, 0))]
                ray1 = Ray(Point(0, 0, 0), Vector(0, 1, 0))
                self.assertEqual(cast_ray(list1, ray1), False)

if __name__ == "__main__":
     unittest.main()

