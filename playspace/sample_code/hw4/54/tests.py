import unittest
from cast import *
from data import *

class Tests(unittest.TestCase):
    
    def test_cast1(self):
        ray = Ray(Point(0,0,-5),Vector(5,5,0))

        point1 = Point(10,10,0)
        point2 = Point(2,4,0)
        point3 = Point(1,5,0)

        color1 = Color(1.0,0.0,0.0)
        color2 = Color(0.0,1.0,0.0)
        color3 = Color(0.0,0.0,1.0)

        finish1 = Finish(1.0,0.5,0.5,0.025)
        finish2 = Finish(1.0,0.5,0.5,0.025)
        finish3 = Finish(1.0,0.5,0.5,0.025)

        sphere1 = Sphere(point1,2,color1,finish1)
        sphere2 = Sphere(point2,3,color2,finish2)
        sphere3 = Sphere(point3,5,color3,finish3)
        sphere_list = [sphere1,sphere2,sphere3]

        ambience_color = Color(1.0,1.0,1.0)

        lte_pt = Point(-100.0,100.0,-100.0)
        lte_color = Color(1.5,1.5,1.5)
        light = Light(lte_pt,lte_color)

        eye_point = Point(0.0,0.0,-14.0)

        cast_test = cast_ray(ray,sphere_list,ambience_color,light,eye_point)

        self.assertTrue(cast_test == Color(1.0,1.0,1.0))

    def test_cast2(self):
    	ray = Ray(Point(0,2,-10),Vector(4,5,0))

    	point1 = Point(2,2,0)
        point2 = Point(2,3,0)
        point3 = Point(1,1,0)

        color1 = Color(1.0,0.0,0.0)
        color2 = Color(0.0,1.0,0.0)
        color3 = Color(0.0,0.0,1.0)

        finish1 = Finish(1.0,0.4,0.5,0.04)
        finish2 = Finish(1.0,0.4,0.5,0.04)
        finish3 = Finish(1.0,0.4,0.5,0.04)

        sphere1 = Sphere(point1,1,color1,finish1)
        sphere2 = Sphere(point2,5,color2,finish2)
        sphere3 = Sphere(point3,4,color3,finish3)
        sphere_list = [sphere1,sphere2,sphere3]

        ambience_color = Color(1.0,1.0,1.0)

        lte_pt = Point(-200.0,100.0,-150.0)
        lte_color = Color(1.5,1.5,1.5)
        light = Light(lte_pt,lte_color)

        eye_point = Point(0.0,0.0,-20.0)

        cast_test = cast_ray(ray,sphere_list,ambience_color,light,eye_point)

        self.assertTrue(cast_test == Color(1.0,1.0,1.0))

    def test_checkMin(self):
        color = Color(24,230,260)
        red_test = checkMin(color.r)
        green_test = checkMin(color.g)
        blue_test = checkMin(color.b)

        self.assertTrue(red_test == 24)
        self.assertTrue(green_test == 230)
        self.assertTrue(blue_test == 255)

    def test_checkMin2(self):
        color = Color(500,30,260)
        red_test = checkMin(color.r)
        green_test = checkMin(color.g)
        blue_test = checkMin(color.b)

        self.assertTrue(red_test == 255)
        self.assertTrue(green_test == 30)
        self.assertTrue(blue_test == 255)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()