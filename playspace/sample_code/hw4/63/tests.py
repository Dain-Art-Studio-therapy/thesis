from cast import *
from data import *
import unittest


class Test(unittest.TestCase):

    def test_cast_ray(self):

        s1 = Sphere(Point(4,0,0), 2, Color(0.25,0.25,0.25), Finish(0.5, 0.5, 0.5, 0.5))
        list1 = [s1]
        ray1 = Ray(Point(0,0,0), Vector(2,0,0))
        amb_lt = Color(0.5, 0.5, 0.5)
        lt1 = Light(Point(0, 0, 0), Color(0.5, 0.5, 0.5))
        e_pt1 = Point(0,0,0) 
        color1 = Color(0.375, 0.375, 0.375)
        
        s2 = Sphere(Point(7,0,0), 2, Color(0.5,0.25,0.5), Finish(0.5, 0.55, 0.52, 0.45))
        list2 = [s2]
        ray2 = Ray(Point(0,0,0), Vector(3,0,0))
        amb_lt2 = Color(0.5, 0.34, 0.75)
        lt2 = Light(Point(0, 0, 0), Color(0.25, 0.45, 0.15))
        e_pt2 = Point(0,0,0)
        color2 = Color(0.32375, 0.338375, 0.30675)

                            
        list3 = []
        ray3 = Ray(Point(0,0,0), Vector(0,7,4))
        light3 = Color(0.4, 0.4, 0.4)
        amb_lt3 = Color(0.5, 0.5, 0.5)
        lt3 = Light(Point(0, 0, 0), Color(0.5, 0.5, 0.5))
        e_pt3 = Point(0,0,0)
        color3 = Color(1.0, 1.0, 1.0)

        self.assertTrue(color1 == cast_ray(ray1, list1, amb_lt, lt1, e_pt1))
        self.assertTrue(color3 == cast_ray(ray3, list3, amb_lt3, lt3, e_pt3))
        self.assertTrue(color2 == cast_ray(ray2, list2, amb_lt2, lt2, e_pt2))
        pass

if __name__ == '__main__':
    unittest.main() 
