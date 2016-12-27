from cast import *
import unittest
from data import *
import math 

class TestCases(unittest.TestCase):

    def test_cast_ray(self):
        sphere_list =[Sphere(Point(10,0,0),2,Color(1.0,1.0,1.0)), Sphere(Point(0,0,0),2,Color(0,.5,.5)), Sphere(Point(20,0,0),2,Color(.2,.2,.2)) ]
        A = cast_ray(Ray(Point(-5,0,0),Vector(1,0,0)), sphere_list)
        self.assertEqual(A,Color(0,.5,.5))

    def test_cast_ray_1(self):
        sphere_list = [ Sphere(Point(0,0,0),2,Color(0,.5,0)) ]
        B = cast_ray(Ray(Point(10,0,0),Vector(1,1,1)), sphere_list )
        self.assertEqual(B,Color(1,1,1))

    def test_distance1(self):
        A = point_distance(Point(0,5,0),Point(0,10,0))
        self.assertEqual(A,5)



    def test_distance2(self):
        B = point_distance(Point(1,1,1) , Point(5,5,5))
        self.assertEqual(B,math.sqrt(48))



if __name__ == "__main__":
    unittest.main()
