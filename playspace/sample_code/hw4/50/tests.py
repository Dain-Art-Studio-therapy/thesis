import unittest
from data import *
from cast import *
from vector_math import *

class TestCast(unittest.TestCase):

    def test_clr_change(self):
        color = Color(1.0, 0.0, 0.0)
        self.assertEqual(Color(255, 0,0), color_change(color))

    def test_clr_change_2(self):
        color = Color(0.0,1.0,0.0)
        self.assertEqual(Color(0,255,0), color_change(color))

    def test_color_with_ambient(self):
        amb_col = Color(1.0,1.0,1.0)
        sphere = Sphere(Point(1,2,3), 3, Color(1.0,0.0,0.0), Finish(1,2,3,4)) 
        self.assertEqual(Color(1, 0,0), color_with_ambient(amb_col, sphere))
    def test_color_with_diffuse(self):
        vis = 2
        light = Light(Point(2,3,1), Color(1.0,0.0,0.0))
        s = Sphere(Point(1,2,3), 1, Color(1.0,0.0,1.0), Finish(2,1,3,4))
        self.assertEqual(Color(2,0,0), color_with_diffuse(vis, light, s))

    def test_color_with_intensity(self):
        light = Light(Point(1,2,3), Color(1.0,0.0,0.0))
        s = Sphere(Point(2,4,2), 4, Color(0.0,1.0,0.0), Finish(2,4,5,3))
        intensity = 3
        color = Color(5*(3**(1/3)),0,0)
        self.assertEqual(color, color_with_intensity(light, s, intensity))

    def test_ambient_and_diffuse(self):
        c1 = Color(3,4,3)
        c2 = Color(1,4,2)
        color = Color(4,8,5)
        self.assertEqual(color, ambient_and_diffuse(c1, c2))

    def test_ambient_diffuse_and_intensity(self):
        c1 = Color(2,5,2)
        c2 = Color(9,4,5)
        c3 = Color(8,3,5)
        color = Color(19, 12, 12)
        self.assertEqual(color, ambient_diffuse_and_intensity(c1,c2,c3))

    def test_shift_intersection_point(self):
        p = Point(1,2,3)
        v = Vector(3,5,5)
        s_v = Vector(0.03, 0.05, 0.05)
        s_p = Point(1.03, 2.05, 3.05)
        self.assertEqual(s_p, shift_intersection_point(p, v))

#old tests
'''
    def test_cast_ray(self):
        white = Color(1.0, 1.0, 1.0)
        black = Color(0.0, 0.0, 0.0)
        s1 = Sphere(Point(4,0,0), 1, white, Finish(0.2, 0.4))
        s2 = Sphere(Point(0,4,0), 2, black, Finish(0.4, 0.4))
        sList = [s1,s2]
        ambient_color = Color(1.0,1.0,1.0)
        r = Ray(Point(0,0,0), Vector(0,4,0))
        L2 = [(s2, Point(0,2,0))] 
        light = Light(Point(-100,100,-100), Color(1.5,1.5,1.5))
        self.assertTrue(cast_ray(r, sList, ambient_color, light))
        self.assertEqual(cast_ray(r, sList, ambient_color, light), black)

    def test_cast_ray1(self):
        s1 = Sphere(Point(4,0,0), 1, Color(1.0, 0.0, 0.0), Finish(0.2, 0.3))
        s2 = Sphere(Point(0,0,4),1, Color(0.0,0.0,1.0), Finish(0.5,0.3))
        sList = [s1,s2]
        r = Ray(Point(0,0,0), Vector(0,4,0))
        ambient_color = Color(1.0, 1.0, 1.0)
        self.assertEqual(cast_ray(r, sList, ambient_color, 4),\
 Color(1.0,1.0,1.0))
    
    def test_cast_ray2(self):
        sList = []
        r = Ray(Point(3,5,6), Vector(3,4,1))
        am_clr = Color(1.0, 1.0, 1.0)
        self.assertEqual(cast_ray(r, sList, am_clr, 4), Color(1.0,1.0,1.0))

    def test_ambient_color(self):
        s1 = Sphere(Point(2,2,0), 2, Color(0.0,0.0,1.0), Finish(0.3,0.3))
        s2 = Sphere(Point(3,3,0), 2, Color(1.0, 0.0, 0.0), Finish(0.2,0.5))
        sList = [s1, s2]
        r = Ray(Point(0,0,0), Vector(1,1,1))
        ambient_colr = Color(1.0,1.0,1.0)

        self.assertEqual(color_with_ambient(ambient_colr, s1),\
 Color(0.0,0.0,0.3))
        self.assertEqual(color_with_ambient(ambient_colr, s2).r,\
 Color(0.2, 0.0,0.0).r)

    def test_shift_intersection_point(self):
       s1 = Sphere(Point(4,0,0), 2, Color(1.0,0.0,1.0), Finish(0.1, 0.5))
       pt = Point(2,0,0)
       pt2 = Point((-1*0.1)+2, 0,0)
       N = sphere_normal_at_point(s1, pt)
       self.assertEqual(shift_intersection_point(s1, pt,N), pt2)

    def test_shift_intersection_point_2(self):
       s1 = Sphere(Point(0,0,6), 2, Color(0.0,0.0,0.0), Finish(0.3, 0.8))
       pt = Point(0,0,4)
       pt2 = Point(0,0,-0.1+4)
       N = sphere_normal_at_point(s1, pt)
       self.assertEqual(shift_intersection_point(s1,pt,N).z, pt2.z)


    def test_color_change(self):
        white = Color(1.0,1.0,1.0)
        rgb_white = 255, 255, 255
        self.assertEqual(color_change(white), rgb_white)

    def test_color_change1(self):
        white = Color(1.1, 1.3, 1.0)
        rgb_white = 255, 255, 255
        self.assertEqual(color_change(white), rgb_white)

    def test_color_change2(self):
        black = Color(0.0,0.0,0.3)
        rgb_black = 0, 0, 0
        self.assertEqual(color_change(black), rgb_black)
'''
if __name__ == '__main__':
     unittest.main()
