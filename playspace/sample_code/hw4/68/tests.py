import unittest
import vector_math
import data
import collisions
import cast


class TestCases(unittest.TestCase):
    def test_scale(self):
        pass
        v = data.Vector(3, 4, 5)
        v2 = data.Vector(15, 20, 25)
        self.assertEqual(vector_math.scale_vector(v, 5), v2)

    def test_dot(self):
        pass
        v = data.Vector(3, 4, 5)
        v2 = data.Vector(6, 7, 8)
        self.assertEqual(vector_math.dot_vector(v, v2), 86)

    def test_length(self):
        pass
        v = data.Vector(1, 2, 3)
        self.assertEqual(vector_math.length_vector(v), 3.7416573867739413)

    def test_normalize(self):
        pass
        v = data.Vector(2, 4, 6)
        v2 = data.Vector(1, 2, 3)
        self.assertEqual(vector_math.normalize_vector(v), v2)

    def test_difference_point(self):
        pass
        p = data.Point(3, 4, 5)
        p1 = data.Point(1, 2, 4)
        v = data.Vector(2, 2, 1)
        self.assertEqual(vector_math.difference_point(p, p1), v)

    def test_difference_vec(self):
        pass
        v = data.Vector(5, 4, 3)
        v2 = data.Vector(1, 2, 1)
        v3 = data.Vector(4, 2, 2)
        self.assertEqual(vector_math.difference_vector(v, v2), v3)

    def test_translate(self):
        pass
        p = data.Point(5, 4, 3)
        v = data.Vector(1, 2, 1)
        p2 = data.Point(6, 6, 4)
        self.assertEqual(vector_math.translate_point(p, v), p2)

    def test_from_to(self):
        pass
        p = data.Point(5, 4, 3)
        p2 = data.Point(1, 2, 1)
        v = data.Vector(4, 2, 2)
        self.assertEqual(vector_math.vector_from_to(p2, p), v)

    def test_intersection(self):
        pass
        p = data.Point(0, 0, 0)
        v = data.Vector(1.0, 0.0, 0.0)
        p2 = data.Point(4, 0, 0)
        p3 = data.Point(3, 0, 0)
        s = data.Sphere(p2, 1.0)
        r = data.Ray(p, v)
        self.assertEqual(collisions.sphere_intersection_point(r, s), p3)

    def test_intersection1(self):
        pass
        p = data.Point(0, 0, 0)
        p2 = data.Point(5, 4, 2)
        v = data.Vector(-1.0, 2.0, 3.0)
        s = data.Sphere(p2, 1.0)
        r = data.Ray(p, v)
        self.assertEqual(collisions.sphere_intersection_point(r, s), None)

    def test_find(self):
        pass
        p = data.Point(0, 0, 0)
        p2 = data.Point(4, 0, 0)
        p3 = data.Point(4, 0, 0)
        p4 = data.Point(-4, 3, 4)
        v = data.Vector(1.0, 0.0, 0.0)
        s = data.Sphere(p2, 1.0)
        s2 = data.Sphere(p4, 2.0)
        r = data.Ray(p, v)
        t = [(s, p3)]
        newlist = [s, s2]
        self.assertEquals(collisions.find_intersection_point(newlist, r), t)

    def test_find1(self):
        pass
        p = data.Point(-4, 5, 4)
        p2 = data.Point(4, 0, 0)
        p4 = data.Point(-4, 3, 4)
        v = data.Vector(1.0, 0.0, 0.0)
        s = data.Sphere(p2, 1.0)
        s2 = data.Sphere(p4, 2.0)
        r = data.Ray(p, v)
        t = [(s2, p)]
        newlist = [s, s2]
        self.assertEquals(collisions.find_intersection_point(newlist, r), t)

    def test_normal(self):
        pass
        point_on_sphere = data.Point(1, 0, 0)
        p2 = data.Point(0, 0, 0)
        v = data.Vector(1.0, 0.0, 0.0)
        s = data.Sphere(p2, 1.0)
        self.assertEquals(collisions.sphere_normal_at_point(s, point_on_sphere), v)

    def test_normal1(self):
        pass
        point_on_sphere = data.Point(2, 0, 0)
        p2 = data.Point(1, 0, 0)
        v = data.Vector(1.0, 0.0, 0.0)
        s = data.Sphere(p2, 1.0)
        self.assertEquals(collisions.sphere_normal_at_point(s, point_on_sphere), v)

    def test_cast(self):
        pass
        # s is hit and color is 255,127,255
        p1 = data.Point(0.0, 0.0, 0.0)
        s = data.Sphere(p1, 1.0, data.Color(1.0, .5, 1.0), data.Finish(.4, .2))
        r = data.Ray(data.Point(0.0, 0.0, 0.0), data.Vector(2.0, 2.0, 2.0))
        sphere_list = [s]
        alight = data.Color(1.0, 1.0, 1.0)
        light = data.Light(data.Point(1, 0, 0), data.Color(.2, .2, .2))
        (cast.cast_ray(r, sphere_list, alight, light) == data.Color(.4, .2, .4))

    def test_cast2(self):
        pass
        p1 = data.Point(0.0, 0.0, 0.0)
        s = data.Sphere(p1, 1.0, data.Color(.8, .25, 1.0), data.Finish(.2, .3))
        s2 = data.Sphere(p1, 0.5, data.Color(0.0, 1.0, 0.0), data.Finish(.1, .6))
        r = data.Ray(data.Point(0.0, 0.0, 0.0), data.Vector(2.0, 2.0, 2.0))
        sphere_list = [s, s2]
        alight = data.Color(1.0, 1.0, 1.0)
        light = data.Light(data.Point(1, 5, 3), data.Color(.2, .2, .2))
        (cast.cast_ray(r, sphere_list, alight, light) == data.Color(.16, .05, .2))


if __name__ == '__main__':
    unittest.main()
