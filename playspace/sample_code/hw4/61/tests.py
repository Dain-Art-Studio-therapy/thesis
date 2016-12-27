from data import *
from cast import *
import unittest

class Test_cases(unittest.TestCase):
    def test_cast_ray1(self):
        s1 = Sphere(Point(0,0,0),1,Color(1.0,1.0,0),Finish(0.4,0.1,0.5,0.05))
        s2 = Sphere(Point(0,2,0),1,Color(1.0,1.0,1.0),Finish(0.6,0.1,0.5,0.05))
        s3 = Sphere(Point(-3,0,0),1,Color(0,0,1.0),Finish(0.2,0.3,0.5,0.05))
        sphere_list = [s1,s2,s3]
        r = Ray(Point(0,-3,0),Vector(0,1,0))
        clr = Color(1.0,0,0)
        point = Point(-100,100,-100)
        light = Light(Point(-100,100,-100),Color(1.0,0.0,1.0))
        self.assertEqual(cast_ray(r,sphere_list,clr,light,point),Color(0.4,0,0))

    def test_find2(self):
        s1 = Sphere(Point(10,-2,-3),5,Color(0,1.0,0),Finish(0.1,0.2,0.5,0.05))
        s2 = Sphere(Point(1,-2,16),6,Color(1.0,0,0),Finish(0.3,0.2,0.5,0.05))
        s3 = Sphere(Point(-4,-5,-10),1,Color(0,0,1.0),Finish(0.9,0.2,0.5,0.05))
        sphere_list = [s1,s2,s3]
        r = Ray(Point(1,2,3),Vector(4,-2,3))
        clr = Color(0,1.0,1.0)
        point = Point(-100,100,-100)
        light = Light(Point(-100,100,-100),Color(1.0,1.0,1.0))
        self.assertEqual(cast_ray(r,sphere_list,clr,light,point),Color(1.0,1.0,1.0))

if __name__ == '__main__':
    unittest.main()
