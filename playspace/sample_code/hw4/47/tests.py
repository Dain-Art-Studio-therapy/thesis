import unittest
from data import *
from vector_math import *
from collisions import *
from cast import *

class TestData(unittest.TestCase):

    def test_finish_init_1(self):
        f = Finish(0.0, 0.0, 0.0, 0.0)
        self.assertAlmostEqual(f.ambient, 0.0)
        self.assertAlmostEqual(f.diffuse, 0.0)
        self.assertAlmostEqual(f.specular, 0.0)
        self.assertAlmostEqual(f.roughness, 0.0)

    def test_finish_init_2(self):
        f = Finish(1.0, 0.2, 0.4, 0.6)
        self.assertAlmostEqual(f.ambient, 1.0)
        self.assertAlmostEqual(f.diffuse, 0.2)
        self.assertAlmostEqual(f.specular, 0.4)
        self.assertAlmostEqual(f.roughness, 0.6)

    def test_finish_eq_1(self):
        f1 = Finish(0.0, 0.0, 0.0, 0.0)
        f2 = Finish(0.0, 0.0, 0.0, 0.0)
        self.assertTrue(f1 == f2)

    def test_finish_eq_2(self):
        f1 = Finish(1.0, 0.2, 0.4, 0.6)
        f2 = Finish(1.0, 0.2, 0.4, 0.6)
        self.assertTrue(f1 == f2)

    def test_light_init_1(self):
        light = Light(Point(0.0, 0.0, 0.0), Color(1.0, 1.0, 1.0))
        self.assertAlmostEqual(light.pt.x, 0.0)
        self.assertAlmostEqual(light.pt.y, 0.0)
        self.assertAlmostEqual(light.pt.z, 0.0)
        self.assertAlmostEqual(light.color.r, 1.0)
        self.assertAlmostEqual(light.color.g, 1.0)
        self.assertAlmostEqual(light.color.b, 1.0)

    def test_light_init_2(self):
        light = Light(Point(1.0, -4.2, 4.7), Color(0.0, 0.4, 0.6))
        self.assertAlmostEqual(light.pt.x, 1.0)
        self.assertAlmostEqual(light.pt.y, -4.2)
        self.assertAlmostEqual(light.pt.z, 4.7)
        self.assertAlmostEqual(light.color.r, 0.0)
        self.assertAlmostEqual(light.color.g, 0.4)
        self.assertAlmostEqual(light.color.b, 0.6)

    def test_light_eq_1(self):
        l1 = Light(Point(0.0, 0.0, 0.0), Color(1.0, 1.0, 1.0))
        l2 = Light(Point(0.0, 0.0, 0.0), Color(1.0, 1.0, 1.0))
        self.assertTrue(l1 == l2)

    def test_light_eq_2(self):
        l1 = Light(Point(1.0, -4.2, 4.7), Color(0.0, 0.4, 0.6))
        l2 = Light(Point(1.0, -4.2, 4.7), Color(0.0, 0.4, 0.6))
        self.assertTrue(l1 == l2)

    def test_occlude_1(self):
        s_c = Color(1.0, 1.0, 1.0)
        a_c = Color(1.0, 1.0, 1.0)
        s_f = Finish(0.2, 0.2, 0.2, 0.2)
        result = Color(0.2, 0.2, 0.2)
        self.assertEqual(occlude(s_c, s_f, a_c), result)

    def test_occlude_2(self):
        s_c = Color(1.0, 0.8, 0.4)
        a_c = Color(0.0, 1.0, 0.4)
        s_f = Finish(0.4, 0.2, 0.2, 0.2)
        result = Color(0.0, 0.32, 0.064)
        self.assertEqual(occlude(s_c, s_f, a_c), result)

    def test_diffuse_1(self):
        dot = 0.4
        l_c = Color(1.0, 1.0, 1.0)
        s_c = Color(1.0, 1.0, 1.0)
        s_f = Finish(0.2, 0.2, 0.2, 0.2)
        result = Color(0.08, 0.08, 0.08)
        self.assertEqual(diffuse(dot, l_c, s_c, s_f), result)

    def test_diffuse_2(self):
        dot = 1.0
        l_c = Color(1.0, 1.0, 1.0)
        s_c = Color(0.0, 1.0, 0.4)
        s_f = Finish(0.2, 0.4, 0.2, 0.2)
        result = Color(0.0, 0.4, 0.16)
        self.assertEqual(diffuse(dot, l_c, s_c, s_f), result)

    def test_glare_1(self):
        l_c = Color(1.0, 1.0, 1.0)
        s = Sphere(
            Point(4.2, 5.6, 7.8), 4.7, Color(1.0, 0.0, 0.0), 
            Finish(0.0, 0.2, 0.4, 1.0)
            )
        intensity = 0.5
        result = Color(0.4, 0.4, 0.4)

    def test_glare_2(self):
        l_c = Color(1.0, 1.0, 1.0)
        s = Sphere(
            Point(4.2, 5.6, 7.8), 4.7, Color(1.0, 0.0, 0.0), 
            Finish(0.0, 0.2, 0.4, 0.5)
            )
        intensity = 0.5
        result = Color(0.1, 0.1, 0.1)

    def test_add_1(self):
        c1 = Color(0.2, 0.2, 0.2)
        c2 = Color(0.0, 0.0, 0.0)
        c3 = Color(0.7, 0.4, 0.6)
        result = Color(0.9, 0.6, 0.8)
        self.assertEqual(add_colors(c1, c2, c3), result)

    def test_add_2(self):
        c1 = Color(0.2, 0.2, 0.2)
        c2 = Color(0.1, 0.2, 0.1)
        c3 = Color(0.3, 0.4, 0.6)
        result = Color(0.6, 0.8, 0.9)
        self.assertEqual(add_colors(c1, c2, c3), result)

    def test_first_collision_1(self):
        ray = Ray(Point(0.0, 0.0, 0.0), Vector(1.0, 0.0, 0.0))
        s1 = Sphere(
            Point (5.0, 0.0, 0.0), 2.0,
            Color(1.0, 0.0, 0.0), Finish(0.0, 0.2, 0.4, 1.0)
            )
        s2 = Sphere(
            Point (8.0, 0.0, 0.0), 3.0,
            Color(1.0, 0.0, 0.0), Finish(0.0, 0.2, 0.4, 1.0)
            )
        result = s1, Point(3.0, 0.0, 0.0)
        self.assertEqual(first_collision(ray, [s1, s2]), result)

    def test_first_collision_2(self):
        ray = Ray(Point(1.4, -2.5, -4.1), Vector(1.0, 4.0, 8.0))
        s1 = Sphere(
            Point (3.4, 5.5, 11.9), 9.0,
            Color(1.0, 0.0, 0.0), Finish(0.0, 0.2, 0.4, 1.0)
            )
        s2 = Sphere(
            Point (-4.6, -22.7, -88.1), 45.3,
            Color(1.0, 0.0, 0.0), Finish(0.0, 0.2, 0.4, 1.0)
            )
        s3 = Sphere(
            Point (-12.2, 45.0, 2.2), 3.2,
            Color(1.0, 0.0, 0.0), Finish(0.0, 0.2, 0.4, 1.0)
            )
        result = s1, Point(2.4, 1.5, 3.9)
        self.assertEqual(first_collision(ray, [s1, s2, s3]), result)

    def test_obscured_1(self):
        epsilon1 = Point(0.0, 0.0, 0.0)
        light1 = Light(Point(0.0, 10.0, 0.0), Color(1.0, 1.0, 1.0))
        light_normal1 = Vector(0.0, 1.0, 0.0)        
        s1 = Sphere(
            Point (8.0, 0.0, 0.0), 3.0,
            Color(1.0, 0.0, 0.0), Finish(0.0, 0.2, 0.4, 1.0)
            )
        self.assertFalse(is_obscured(epsilon1, light1.pt, light_normal1, [s1]))

    def test_obscured_2(self):
        epsilon2 = Point(0.0, 0.0, 0.0)
        light2 = Light(Point(10.0, 0.0, 0.0), Color(1.0, 1.0, 1.0))
        light_normal2 = Vector(1.0, 0.0, 0.0)        
        s2 = Sphere(
            Point (8.0, 0.0, 0.0), 3.0,
            Color(1.0, 0.0, 0.0), Finish(0.0, 0.2, 0.4, 1.0)
            )
        self.assertTrue(is_obscured(epsilon2, light2.pt, light_normal2, [s2]))

    def test_cast_light_1(self):
        black = Color(0.0, 0.0, 0.0)
        s1 = Sphere(
            Point (8.0, 0.0, 0.0), 3.0,
            Color(1.0, 0.0, 0.0), Finish(0.0, 0.2, 0.4, 1.0)
            )
        light = Light(Point(10.0, 0.0, 0.0), Color(1.0, 1.0, 1.0))
        epsilon = Point(0.0, 0.0, 0.0)
        dot_product = -12.0
        light_normal = Vector(1.0, 0.0, 0.0)
        self.assertEqual(
            cast_light(s1, light, epsilon, dot_product, light_normal, [s1]),
            black
            )

    def test_cast_light_2(self):
        black = Color(0.0, 0.0, 0.0)
        s1 = Sphere(
            Point (8.0, 0.0, 0.0), 3.0,
            Color(1.0, 0.0, 0.0), Finish(0.0, 0.2, 0.4, 1.0)
            )
        light = Light(Point(10.0, 0.0, 0.0), Color(1.0, 1.0, 1.0))
        epsilon = Point(0.0, 0.0, 0.0)
        dot_product = 2.0
        light_normal = Vector(1.0, 0.0, 0.0)
        self.assertEqual(
            cast_light(s1, light, epsilon, dot_product, light_normal, [s1]),
            black
            )

    def test_speculate_1(self):
        s1 = Sphere(
            Point (8.0, 0.0, 0.0), 3.0,
            Color(1.0, 0.0, 0.0), Finish(0.0, 0.2, 0.9, 1.0)
            )  
        normal = Vector(-1.0, 0.0, 0.0)
        light_normal = Vector(1.0, 0.0, 0.0)
        epsilon = Point(4.99, 0.0, 0.0)
        dot_product = -22.0
        eye_point = Point(5, 0, -1)
        lt_color = Color(1.5, 1.5, 1.5)
        result = Color(
            0.580470977177, 0.580470977177, 0.580470977177
            )
        self.assertEqual(
            speculate(
            s1, normal, light_normal, epsilon, 
            dot_product, eye_point, lt_color
            ),
            result
            )

    def test_speculate_2(self):
        s1 = Sphere(
            Point (8.0, 0.0, 0.0), 3.0,
            Color(1.0, 0.0, 0.0), Finish(0.0, 0.2, 0.9, 1.0)
            )
        normal = Vector(-1.0, 0.0, 0.0)
        light_normal = Vector(1.0, 0.0, 0.0)
        epsilon = Point(4.99, 0.0, 0.0)
        dot_product = -1.0
        eye_point = Point(1, 0, -1)
        lt_color = Color(1.5, 1.5, 1.5)
        result = Color(0.0, 0.0, 0.0)
        self.assertEqual(
            speculate(
            s1, normal, light_normal, epsilon, 
            dot_product, eye_point, lt_color
            ),
            result
            )

    def test_window_1(self):
        min_x = -4
        max_x = 4
        min_y = -2
        max_y = 2
        width = 4
        height = 2
        pt_list = [Point(-4, 2, 0), Point(-2, 2, 0),
            Point(0, 2, 0), Point(2, 2, 0),
            Point(-4, 0, 0), Point(-2, 0, 0),
            Point(0, 0, 0), Point(2, 0, 0)]
        self.assertEqual(
            get_window(min_x, max_x, min_y, max_y, width, height),
            pt_list)

    def test_window_2(self):
        min_x = 0
        max_x = 8
        min_y = 0
        max_y = 4
        width = 4
        height = 2
        pt_list = [Point(0, 4, 0), Point(2, 4, 0),
            Point(4, 4, 0), Point(6, 4, 0),
            Point(0, 2, 0), Point(2, 2, 0),
            Point(4, 2, 0), Point(6, 2, 0)]
        self.assertEqual(
            get_window(min_x, max_x, min_y, max_y, width, height),
            pt_list)

    def test_cast_ray_1(self):
        ray = Ray(Point(0, 0, 0), Vector(0, 1, 0))
        s1 = Sphere(
            Point (8.0, 0.0, 0.0), 3.0,
            Color(1.0, 0.0, 0.0), Finish(0.2, 0.2, 0.4, 1.0)
            )
        color = Color(1.0, 1.0, 1.0)
        light = Light(Point(0, 8, 0), Color(1.0, 0.0, 0.0))
        eye_point = Point(5, 0, -5)
        self.assertEqual(
            cast_ray(ray, [s1], color, light, eye_point),
            Color(1.0, 1.0, 1.0)
            )

    def test_cast_ray_2(self):
        ray = Ray(Point(0, 0, 0), Vector(0, 1, 0))
        s1 = Sphere(
            Point (1.0, 1.0, 0.0), 2.0,
            Color(0.0, 1.0, 0.0), Finish(0.2, 0.4, 0.5, 0.05)
            )
        color = Color(1.0, 1.0, 1.0)
        light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
        eye_point = Point(0.0, 0.0, -14.0)
        self.assertEqual(
            cast_ray(ray, [s1], color, light, eye_point),
            Color(0.0, 0.669229397996, 0.0)
            )
     

if __name__ == "__main__":
   unittest.main()

