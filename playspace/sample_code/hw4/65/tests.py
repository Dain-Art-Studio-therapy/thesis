import data
import vector_math
import unittest
import collisions
import math
import cast
import data


class TestCases(unittest.TestCase):    
    
    def test_cast_ray_pts1(self):
        point = data.Point(0.0, 0.0, -14.0)
        sphere1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0, 0, 1.0),data.Finish(0.2, 0.4, 0.5, 0.05))
        sphere2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1.0, 0, 0), data.Finish(0.4, 0.4, 0.5, 0.05))
        sphere_list = [sphere1, sphere2]
        amb = data.Color(0,0,0)
        light = data.Light(data.Point(100.0, -100.0, 100.0), data.Color(1.5,1.5,1.5))
        vec1 = vector_math.vector_from_to(point, data.Point(3.0,1.0,1.0))
        ray = data.Ray(point, vec1)
        final = cast.cast_ray(ray, sphere_list, amb, light, point)

    def test_cast_ray_pts2(self):
        point = data.Point(4.6, 1.4, -14.0)
        sphere1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(1.0, 0, 1.0),data.Finish(0.2, 0.4, 0.5, 0.05))
        sphere2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1.0, 0, 1.2), data.Finish(0.4, 0.4, 0.5, 0.05))
        sphere_list = [sphere1, sphere2]
        amb = data.Color(0,0,0)
        light = data.Light(data.Point(100.0, -100.0, 100.0), data.Color(1.5,1.5,1.5))
        vec1 = vector_math.vector_from_to(point, data.Point(3.0,1.0,1.0))
        ray = data.Ray(point, vec1)
        final = cast.cast_ray(ray, sphere_list, amb, light, point)
if __name__ == '__main__':
    unittest.main()
