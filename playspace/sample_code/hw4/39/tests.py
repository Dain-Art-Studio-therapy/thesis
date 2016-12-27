import unittest
import math
import vector_math
import data
import collisions
import casts



class TestCases(unittest.TestCase):

    def test_castray(self):
        ray = data.Ray(data.Point(0,0,0), data.Vector(10,0,0))
        c1 = data.Color(100,100,100)
        c2 = data.Color(5,5,5)
        c3 = data.Color(1,1,1)
        sphereL = [ data.Sphere(data.Point(3,0,0),3,c1),
                    data.Sphere(data.Point(5,0,0),1,c2),
                    data.Sphere(data.Point(0,5,0),1,c3)
                    ]
        self.assertEqual(casts.cast_ray(ray,sphereL),c1)

    def test_castray_2(self):
        ray = data.Ray(data.Point(0,0,0), data.Vector(0,10,0))
        c1 = data.Color(100,100,100)
        c2 = data.Color(5,5,5)
        c3 = data.Color(1,1,1)
        sphereL = [ data.Sphere(data.Point(3,0,0),3,c1),
                    data.Sphere(data.Point(5,0,0),1,c2),
                    data.Sphere(data.Point(0,5,0),1,c3)
                    ]
        self.assertEqual(casts.cast_ray(ray,sphereL),c3)

if __name__ == "__main__":
    unittest.main()
