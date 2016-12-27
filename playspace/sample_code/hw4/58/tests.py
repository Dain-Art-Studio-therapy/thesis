import unittest
import math
import data
import vector_math
import collisions
import cast


class Tests(unittest.TestCase):
# new DATA.PY test cases
# data.Finish(ambient)
    def test_Finish_1(self):
        finish = data.Finish(1.0, 0.4, 0.5, 0.05)
        self.assertTrue(finish.__eq__(data.Finish(1.0, 0.4, 0.5, 0.05)))
    def test_Finish_2(self):
        finish = data.Finish(0.4, 0.0, 0.0, 1.0)
        self.assertTrue(finish.__eq__(data.Finish(0.4, 0.0, 0.0, 1.0)))


# data.Sphere(center, rad, color, finish)
    def test_sphere_1(self):
        cent1 = data.Point(1, 2, 3)
        rad1 = 10
        color1 = data.Color(1.0, 0.0, 0.0)
        finish1 = data.Finish(0.8, 0.4, 0.6, 0.03)
        sphere1 = data.Sphere(cent1, rad1, color1, finish1)

        self.assertEqual(sphere1.center.x, 1)
        self.assertEqual(sphere1.center.y, 2)
        self.assertEqual(sphere1.center.z, 3)
        self.assertAlmostEqual(sphere1.rad, 10)
        self.assertEqual(sphere1.color, data.Color(1.0, 0.0, 0.0))
        self.assertEqual(sphere1.finish, data.Finish(0.8, 0.4, 0.6, 0.03))

    def test_sphere_2(self):
        cent2 = data.Point(68, 69, 70)
        rad2 = 40.3
        color2 = data.Color(0.0, 0.0, 0.0)
        finish2 = data.Finish(1.0, .66, .003, 0.002)
        sphere2 = data.Sphere(cent2, rad2, color2, finish2)

        self.assertEqual(sphere2.center.x, 68)
        self.assertEqual(sphere2.center.y, 69)
        self.assertEqual(sphere2.center.z, 70)
        self.assertAlmostEqual(sphere2.rad, 40.3)
        self.assertEqual(sphere2.color, data.Color(0.0, 0.0, 0.0))
        self.assertEqual(sphere2.finish, data.Finish(1.0, .66, .003, 0.002))




# COLLISIONS.PY tests
# sphere_intersection_point(ray, sphere) test cases
     # sphere(center, rad, color, finish)
    def test_sphere_intersection_1(self):
        ray1 = data.Ray(data.Point(0, 0, 0), data.Vector(4, 0, 0))
        sphere1 = data.Sphere(data.Point(8, 0, 0), 6, data.Color(1.0, 1.0, 1.0), \
            data.Finish(1.0, .3, 0.8, 1.0))
        intersection_pt_1 = data.Point(2, 0, 0)  

        self.assertTrue(collisions.sphere_intersection_point(ray1, \
            sphere1).__eq__(intersection_pt_1))

    def test_sphere_intersection_2(self):
        ray2 = data.Ray(data.Point(0, 0, 0), data.Vector(6, 8, 0))
        sphere2 = data.Sphere(data.Point(9, 12, 0), 10, data.Color(1.0, 1.0, 1.0),\
            data.Finish(1.0, 5.0, 0.9, -0.3))
        intersection_pt_2 = data.Point(3, 4, 0)

        self.assertTrue(collisions.sphere_intersection_point(ray2, \
            sphere2).__eq__(intersection_pt_2))
 
    def test_sphere_intersection_3(self):
        ray3 = data.Ray(data.Point(0, 0, 9), data.Vector(0, 0, -9))
        sphere3 = data.Sphere(data.Point(0, 0, 5), 3, data.Color(1.0, 1.0, 1.0), \
            data.Finish(1.0, .2, -0.0, 0.0))
        intersection_pt_3 = data.Point(0, 0, 8)
   
        self.assertTrue(collisions.sphere_intersection_point(ray3, \
            sphere3).__eq__(intersection_pt_3))         
  
    def test_sphere_intersection_4(self):
        ray4 = data.Ray(data.Point(-8, -8, -4), data.Vector(16, 16, 8))
        sphere4 = data.Sphere(data.Point(0, 0, 0), 3, data.Color(1.0, 1.0, 1.0), \
            data.Finish(1.0, 1.0, 1.3, 0.9))
        intersection_pt_4 = data.Point(-2, -2, -1)
        self.assertTrue(collisions.sphere_intersection_point(ray4, \
            sphere4).__eq__(intersection_pt_4))         
      

# find_intersection_points(sphere_list, ray) 
    def test_find_points_1(self):
        sphere1 = data.Sphere(data.Point( 0, 3, 0), 2, \
            data.Color(1.0, 1.0, 1.0), data.Finish(1.0, 0.4, -0.4, 0.0)) # should pass
        sphere2 = data.Sphere(data.Point(0, 9, 0), 4, \
            data.Color(1.0, 1.0, 1.0), data.Finish(1.0, 0.4, 0, 0)) #should pass 
        sphere3 = data.Sphere(data.Point(-10, -20, -30), 2, \
            data.Color(1.0, 1.0, 1.0), data.Finish(1.0, 0.4, .3, .4)) # should NOT pass 

        sphere_list_1 = [sphere1, sphere2, sphere3]
        ray1 = data.Ray(data.Point(0, 0, 0), data.Vector(0, 12, 0))
        result_list_1 = [(sphere1, data.Point(0, 1, 0)), \
            (sphere2, data.Point(0, 5, 0))]
     
        self.assertEqual(collisions.find_intersection_points(sphere_list_1, ray1), \
            result_list_1)
    
    def test_find_points_2(self):
        sphere1 = data.Sphere(data.Point(0, 0, 0), 3,\
            data.Color(1.0, 1.0, 1.0), data.Finish(1.0, 0.3, -1, .2)) # should pass 
        sphere2 = data.Sphere(data.Point(-5, -10, -10), 6, \
            data.Color(1.0, 1.0, 1.0), data.Finish(1.0, 0.3, 0, 0)) # should pass
        sphere3 = data.Sphere(data.Point(60, 10, -4), 7, \
            data.Color(1.0, 1.0, 1.0), data.Finish(1.0, 0.3, .1, 0)) # should NOT pass
        sphere4 = data.Sphere(data.Point(30, -30, 25), 10, \
            data.Color(1.0, 1.0, 1.0), data.Finish(1.0, 0.2, 0, 0)) # should NOT pass
        sphere_list_2 = [sphere1, sphere2, sphere3, sphere4]
        ray2 = data.Ray(data.Point(5,10, 10), data.Point(-5, -10, -10))
        result_list_2 = [(sphere1, data.Point(1, 2, 2)), \
            (sphere2, data.Point(-3, -6, -6))]  
      
        self.assertEqual(collisions.find_intersection_points(sphere_list_2, ray2),\
            result_list_2) 


# sphere_normal_at_point(sphere, point) Test Cases
    def test_normal_vector_1(self):
        sphere1 = data.Sphere(data.Point(0, 0, 0), 40, \
            data.Color(1.0, 1.0, 1.0), data.Finish(1.0, 1.0, 0.4, 0.04))
        point1 = data.Point(0, 0, 3)
        normal_vector_1 = data.Vector(0, 0, 1)
   
        self.assertEqual(collisions.sphere_normal_at_point(sphere1, point1), \
            normal_vector_1)

    def test_normal_vector_2(self):
        sphere2 = data.Sphere(data.Point(1, 2, 2), 2, \
            data.Color(1.0, 1.0, 1.0), data.Finish(1.0, 1.0, .55, 0.001))
        point2 = data.Point(0, 0, 0)
        normal_vector_2 = data.Vector(-.33333, -.66666, -.66666)
 
        self.assertEqual(collisions.sphere_normal_at_point(sphere2, point2), \
            normal_vector_2)

    def test_normal_vector_3(self):
        sphere3 = data.Sphere(data.Point(0, 0, 0), 20, \
            data.Color(1.0, 1.0, 1.0), data.Finish(1.0, .6666, 0.0, 0.6))
        point3 = data.Point(1, 2, 2)
 
        normal_vector_3 = data.Vector(.33333, .66666, .66666)

        self.assertEqual(collisions.sphere_normal_at_point(sphere3, point3),\
            normal_vector_3)




# CAST.PY TEST CASES
  # cast_ray(ray, sphere_list, color, light) test cases
    # data.Sphere(center, radius, color)
    def test_cast_ray_1(self):
        sphere1 = data.Sphere(data.Point(0, 0, 0), 3, data.Color(0, 255, 0),\
            data.Finish(1.0, 1.01, 0.3, 4.0))
        sphere2 = data.Sphere(data.Point(-1, -2, -2), 3, data.Color(255, 0, 0),\
            data.Finish(1.0, .222, 0.03, 0.1))
        sphere_list = [sphere1, sphere2]
        ray = data.Ray(data.Point(5, 10, 10), data.Vector(-10, -20, -20))

        self.assertEqual(cast.cast_ray(ray, sphere_list, data.Color(0, 1.0, 0.0),\
            data.Light(data.Point(0, 0, 0), data.Color(0, 0, 0)), data.Point(1, 1, 1)),\
            data.Color(0, 255, 0))
         
    def test_cast_ray_2(self):
        sphere_list = []
        ray = data.Ray(data.Point(0, 0, 0), data.Point(8, 3, 1))
 
        self.assertEqual(cast.cast_ray(ray, sphere_list, data.Color(1.0, 1.0, 1.0),\
            data.Light(data.Point(-100, 100, -100), data.Color(1.0, 1.0, 1.0)),\
            data.Point(-100, 300, -100)),\
            data.Color(1.0, 1.0, 1.0))
 

# distance helper function test cases
    def test_distance_1(self):
        pt1 = data.Point(0, 0, 0)
        pt2 = data.Point(3, 4, 0)
        distance = vector_math.distance(pt2, pt1)
        self.assertEqual(distance, 5)

    def test_distance_2(self):
        pt1 = data.Point(-1, -2, -2)
        pt2 = data.Point(1, 2, 2)
        distance = vector_math.distance(pt1, pt2)
        self.assertEqual(distance, 6)        
   

# find closest sphere helper function test cases
  # find_closest_sphere(ray, sphere_list):
  # sphere(self, center, rad, color, finish):
    def test_find_closest_sphere_1(self):
        sphere1 = data.Sphere(data.Point(0, 0, 0), 3, data.Color(1.0, 1.0, 1.0),\
            data.Finish(1.0, 0.4, 0.5, 0.05))
        sphere2 = data.Sphere(data.Point(2, 4, 4), 3, data.Color(0.0, 0.0, 0.0), \
            data.Finish(1.0, 0.4, 0.5, 0.05))
        sphere_list = [sphere1, sphere2]
        ray = data.Ray(data.Point(-3, -6, -6), data.Vector(9, 18, 18))

        self.assertEqual(cast.find_closest_sphere(ray, sphere_list),\
            (sphere1, data.Point(-1, -2, -2)))
 
if __name__ == "__main__":
    unittest.main()

