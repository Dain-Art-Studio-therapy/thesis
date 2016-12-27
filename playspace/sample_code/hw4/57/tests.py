import unittest
import data
import cast
 
g_sphere_1 = data.Sphere(data.Point(0, 0, 0), 2, data.Color(1.0, 0.0, 0.0), data.Finish(0.5, 0.5, 0.5, 0.05))
g_sphere_2 = data.Sphere(data.Point(3, 0, 0), 1, data.Color(0.0, 1.0, 0.0), data.Finish(0.4, 0.4, 0.4, 0.04))
g_sphere_list = [g_sphere_1, g_sphere_2]

g_ray = data.Ray(data.Point(-3, 0, 0), data.Vector(1, 0, 0))

g_color_1 = data.Color(1.0, 1.0, 1.0)


class TestCases(unittest.TestCase):
       
    def test_ray1(self):
        eye_point = data.Point(1.0, 0.0, -14.0)
        sphere = data.Sphere(data.Point(0.0, 0.0, 0.0), 4.0, data.Color(0.0, 0.0, 1.0))
        sphere1 = data.Sphere(data.Point(1.0, 0.0, -5.0), 1.0, data.Color(1.0, 0.0, 0.0))
        sphere_list = [sphere, sphere1] 
        ray = data.Ray(eye_point, data.Vector(0, 0, 1)) 
        self.assertEqual(cast.cast_ray(ray, sphere_list), data.Color(1.0, 0.0, 0.0)) 

    def test_ray2(self):
        eye_point = data.Point(-1.0, 0.0, -14.0)
        sphere = data.Sphere(data.Point(0.0, 0.0, 0.0),4.0, data.Color(0.0, 0.0, 1.0))
        sphere1 = data.Sphere(data.Point(1.0, 0.0, -5.0), 1.0, data.Color(1.0, 0.0, 0.0))
        sphere_list = [sphere, sphere1]
        ray = data.Ray(eye_point, data.Vector(0, 0, 1))
        self.assertEqual(cast.cast_ray(ray, sphere_list), data.Color(0.0, 0.0, 1.0))

    def test_ray3(self):
        eye_point = data.Point(1.0, 0.0, -14.0)
        sphere = data.Sphere(data.Point(0.0, 0.0, 0.0),4.0, data.Color(0.0, 0.0, 1.0))
        sphere1 = data.Sphere(data.Point(1.0, 0.0, -5.0), 1.0, data.Color(1.0, 0.0, 0.0))
        sphere_list = [sphere, sphere1]
        ray = data.Ray(eye_point, data.Vector(0, 0, 1))
        self.assertEqual(cast.cast_ray(ray, sphere_list), data.Color(1.0, 0.0, 0.0))

    def test_ray4(self):
        eye_point = data.Point(10.0, 0.0, -14.0)
        sphere = data.Sphere(data.Point(0.0, 0.0, 0.0),4.0, data.Color(0.0, 0.0, 1.0))
        sphere1 = data.Sphere(data.Point(1.0, 0.0, -5.0), 1.0, data.Color(1.0, 0.0, 0.0))
        sphere_list = [sphere, sphere1]
        ray = data.Ray(eye_point, data.Vector(0, 0, 1))
        self.assertEqual(cast.cast_ray(ray, sphere_list), data.Color(1.0, 1.0, 1.0))
    
    def test_closest_sphere(self):
        list_of_spheres = [data.Sphere(data.Point(0.0, 0.0, 0.0), 2.0, data.Color(0.0, 0.0, 1.0)), data.Sphere(data.Point(0.0, 0.0, -5.0), 3.0, data.Color(1.0, 0.0, 0.0)), data.Sphere(data.Point(0.0, 0.0, 5.0), 3.0, data.Color(0.0, 0.0, 1.0))] 
        list_of_tuples = [(0, list_of_spheres[0].center), (1, list_of_spheres[1].center), (2, list_of_spheres[2].center)] 
        sphere = cast.closest_sphere(list_of_tuples, data.Point(0, 0, -20))
        self.assertAlmostEqual(sphere, 1) 

    def test_distance(self):
        point= data.Point(0, 0, 0)  
        point1= data.Point(3, 4, 0)
        self.assertAlmostEqual(cast.distance(point1, point), 5) 

    def test_finish_ambient(self):
        #self.assertEqual(
        a = cast.finish_ambient(g_color_1, g_sphere_1)#, data.Color(0.5, 0.0, 0.0)) 
        print a.r, a.g, a.b

    def test_finish_ambient_1(self):
        self.assertEqual(cast.finish_ambient(g_color_1, g_sphere_2), data.Color(0.0, 0.5, 0.0)) 
 
    def test_find_n(self):
        pass

    def test_find_n_1(self): 
        pass

    def test_find_new_point(self):
        pass

    def test_find_new_point_1(self):
        pass

    def test_light_dir(self):
        pass

    def test_light_dir_1(self):
        pass

    def test_find_point_normal(self):
        pass

    def test_find_point_normal_1(self):
        pass

    def test_finish_diffuse(self):
        pass

    def test_finish_diffuse_1(self):
        pass

    def finish_specular(self):
        pass

    def finish_specular_1(self):
        pass

    def finish_all(self):
        pass

    def finish_all_1(self):
        pass 





if __name__== '__main__':
    unittest.main()
