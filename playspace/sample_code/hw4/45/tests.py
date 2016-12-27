import unittest
import data
import vector_math
import collisions
from cast import *
from collisions import *

class TestData(unittest.TestCase):


#ASSIGNMENT 4 TESTS

    def test_cast_ray(self):
        ray1 = data.Ray(data.Point(0,0,0),data.Vector(1,0,0))
        s0 = data.Sphere(data.Point(5,0,0),2,data.Color(0.0,0.0,1.0),data.Finish(0.2,0.4,0.5,0.05))
        s1 = data.Sphere(data.Point(8,0,0),1,data.Color(0.0,0.0,1.0),data.Finish(0.2,0.4,0.5,0.05))
        s2 = data.Sphere(data.Point(12,0,0),1,data.Color(0.0,0.0,1.0),data.Finish(0.2,0.4,0.5,0.05))
        s3 = data.Sphere(data.Point(4,17,0),3,data.Color(0.0,0.0,1.0),data.Finish(0.2,0.4,0.5,0.05))
        light = data.Light(data.Point(-100.0, 100.0, -100.0),data.Color(1.0,0.0,1.0))
        point = data.Point(0,0,0)
        self.assertEqual(cast_ray(ray1,[s0,s1,s2,s3],data.Color(1.0,0.0,0.0),light,point),data.Color(0.0,0.0,0.0))

    def test_cast_ray_2(self):
        s0 = data.Sphere(data.Point(7,0,0),3,data.Color(0.0,0.0,1.0),data.Finish(0.2,0.4,0.5,0.05))
        s1 = data.Sphere(data.Point(15,0,0),1,data.Color(0.0,0.0,1.0),data.Finish(0.2,0.4,0.5,0.05))
        s2 = data.Sphere(data.Point(-22,1,0),4,data.Color(0.0,0.0,1.0),data.Finish(0.2,0.4,0.5,0.05))
        ray = data.Ray(data.Point(0,3,0),data.Vector(0,1,0))
        light = data.Light(data.Point(-200.0, 200.0, -100.0),data.Color(1.0,1.0,1.0))
        point = data.Point(0,0,0)
        self.assertEqual(cast_ray(ray,[],data.Color(1.0,1.0,1.0),light,point),data.Color(1.0,1.0,1.0))



if __name__ == "__main__":
     unittest.main()
