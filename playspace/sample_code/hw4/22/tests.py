import unittest
import data
import vector_math
import collisions
import cast

class TestData(unittest.TestCase):   
   # Point
   def test_point_1(self):
        pt1 = data.Point(2.0, 4.0, 5.0)
        self.assertAlmostEqual(pt1.x, 2.0)
        self.assertAlmostEqual(pt1.y, 4.0)
        self.assertAlmostEqual(pt1.z, 5.0)   
   def test_point_2(self):
        pt2 = data.Point(4.6, 3.2, 5.9)
        self.assertAlmostEqual(pt2.x, 4.6)
        self.assertAlmostEqual(pt2.y, 3.2)
        self.assertAlmostEqual(pt2.z, 5.9)
   
   # Vector
   def test_vector_1(self):
        v1 = data.Vector(4.3, 6.7, 2.1)
        self.assertAlmostEqual(v1.x, 4.3)
        self.assertAlmostEqual(v1.y, 6.7)
        self.assertAlmostEqual(v1.z, 2.1)
   def test_vector_2(self):
        v2 = data.Vector(1.1, 3.2, 5.3)
        self.assertAlmostEqual(v2.x, 1.1)
        self.assertAlmostEqual(v2.y, 3.2)
        self.assertAlmostEqual(v2.z, 5.3)

   # Ray
   def test_ray_1(self):
        ray1 = data.Ray(data.Point(2.0, 4.0, 5.0), data.Vector(4.3, 6.7, 2.1))
        self.assertAlmostEqual(ray1.pt.x, 2.0)
        self.assertAlmostEqual(ray1.pt.y, 4.0)
        self.assertAlmostEqual(ray1.pt.z, 5.0)
        self.assertAlmostEqual(ray1.dir.x, 4.3)
        self.assertAlmostEqual(ray1.dir.y, 6.7)
        self.assertAlmostEqual(ray1.dir.z, 2.1)
   def test_ray_2(self):
        ray2 = data.Ray(data.Point(4.6, 3.2, 5.9), data.Vector(1.1, 3.2, 5.3))
        self.assertAlmostEqual(ray2.pt.x, 4.6)
        self.assertAlmostEqual(ray2.pt.y, 3.2)
        self.assertAlmostEqual(ray2.pt.z, 5.9)
        self.assertAlmostEqual(ray2.dir.x, 1.1)
        self.assertAlmostEqual(ray2.dir.y, 3.2)
        self.assertAlmostEqual(ray2.dir.z, 5.3)

   # Sphere
   def test_sphere_1(self):
        sphere1 = data.Sphere(data.Point(2.0, 4.0, 5.0), 4.5,
                  data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))
        self.assertAlmostEqual(sphere1.center.x, 2.0)
        self.assertAlmostEqual(sphere1.center.y, 4.0)
        self.assertAlmostEqual(sphere1.center.z, 5.0)
        self.assertAlmostEqual(sphere1.radius, 4.5)
        self.assertAlmostEqual(sphere1.color.r, 1.0)
        self.assertAlmostEqual(sphere1.color.g, 0.0)
        self.assertAlmostEqual(sphere1.color.b, 0.0)
        self.assertAlmostEqual(sphere1.finish.ambient, 0.1)
        self.assertAlmostEqual(sphere1.finish.diffuse, 0.2)
        self.assertAlmostEqual(sphere1.finish.specular, 0.0)
        self.assertAlmostEqual(sphere1.finish.roughness, 0.0)
   def test_sphere_2(self):
        sphere2 = data.Sphere(data.Point(4.6, 3.2, 5.9), 2.7,
                  data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))
        self.assertAlmostEqual(sphere2.center.x, 4.6)
        self.assertAlmostEqual(sphere2.center.y, 3.2)
        self.assertAlmostEqual(sphere2.center.z, 5.9)
        self.assertAlmostEqual(sphere2.radius, 2.7)
        self.assertAlmostEqual(sphere2.color.r, 1.0)
        self.assertAlmostEqual(sphere2.color.g, 0.0)
        self.assertAlmostEqual(sphere2.color.b, 0.0)
        self.assertAlmostEqual(sphere2.finish.ambient, 0.1)
        self.assertAlmostEqual(sphere2.finish.diffuse, 0.2)
        self.assertAlmostEqual(sphere2.finish.specular, 0.0)
        self.assertAlmostEqual(sphere2.finish.roughness, 0.0)

   # test __eq__ functions
   def test_point_eq_1(self):
        pt1 = data.Point(2.0, 4.0, 5.0)
        pt2 = data.Point(2.0, 4.0, 5.0)
        self.assertEqual(pt1, pt2)
   def test_point_eq_2(self):
        pt1 = data.Point(4.6, 3.2, 5.9)
        pt2 = data.Point(4.6, 3.2, 5.9)
        self.assertEqual(pt1, pt2)

   def test_vector_eq_1(self):
        v1 = data.Vector(4.3, 6.7, 2.1)
        v2 = data.Vector(4.3, 6.7, 2.1)
        self.assertEqual(v1, v2)
   def test_vector_eq_2(self):
        v1 = data.Vector(1.1, 3.2, 5.3)
        v2 = data.Vector(1.1, 3.2, 5.3)
        self.assertEqual(v1, v2)

   def test_ray_eq_1(self):
        ray1 = data.Ray(data.Point(2.0, 4.0, 5.0), data.Vector(4.3, 6.7, 2.1))
        ray2 = data.Ray(data.Point(2.0, 4.0, 5.0), data.Vector(4.3, 6.7, 2.1))
        self.assertEqual(ray1, ray2)
   def test_ray_eq_2(self):
        ray1 = data.Ray(data.Point(4.6, 3.2, 5.9), data.Vector(1.1, 3.2, 5.3))
        ray2 = data.Ray(data.Point(4.6, 3.2, 5.9), data.Vector(1.1, 3.2, 5.3))
        self.assertEqual(ray1, ray2)

   def test_sphere_eq_1(self):
        sphere1 = data.Sphere(data.Point(2.0, 4.0, 5.0), 4.5,
                  data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))
        sphere2 = data.Sphere(data.Point(2.0, 4.0, 5.0), 4.5,
                  data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))
        self.assertEqual(sphere1, sphere2)
   def test_sphere_eq_2(self):
        sphere1 = data.Sphere(data.Point(4.6, 3.2, 5.9), 2.7,
                  data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))
        sphere2 = data.Sphere(data.Point(4.6, 3.2, 5.9), 2.7,
                  data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))
        self.assertEqual(sphere1, sphere2)

   # test Scale
   def test_scale_vector_1(self):
        vector = data.Vector(1, 2, 3)
        scalar = 1.5
        new_vector = data.Vector(1.5, 3, 4.5)
        self.assertEqual(vector_math.scale_vector(vector, scalar), new_vector)
   def test_scale_vector_2(self):
	vector = data.Vector(0.5, 6.2, 3.4)
	scalar = 2
	new_vector = data.Vector(1, 12.4, 6.8)
	self.assertEqual(vector_math.scale_vector(vector, scalar), new_vector)

   # test Dot Product
   def test_dot_vector_1(self):
	vector1 = data.Vector(1, 2, 3)
	vector2 = data.Vector(4, 5, 6)
	self.assertAlmostEqual(vector_math.dot_vector(vector1, vector2), 32)
   def test_dot_vector_2(self):
	vector1 = data.Vector(2.5, 3, 6.5)
	vector2 = data.Vector(1, 3.5, 4.2)
	self.assertAlmostEqual(vector_math.dot_vector(vector1, vector2), 40.3)

   # test Length
   def test_length_vector_1(self):
	vector = data.Vector(1, 2, 3)
	self.assertAlmostEqual(vector_math.length_vector(vector), 3.741657387)
   def test_length_vector_2(self):
	vector = data.Vector(3, 4, 5)
	self.assertAlmostEqual(vector_math.length_vector(vector), 7.071067812)

   # test Normalize Vector
   def test_normalize_vector_1(self):
	vector = data.Vector(1, 2, 3)
	normal_vector = data.Vector(0.2672612, 0.5345225, 0.8017837)
	self.assertEqual(vector_math.normalize_vector(vector), normal_vector) 
   def test_normalize_vector_2(self):
	vector = data.Vector(3, 4, 5)
	normal_vector = data.Vector(0.42426407, 0.5656854, 0.7071068)
	self.assertEqual(vector_math.normalize_vector(vector), normal_vector)

   # test Point Difference
   def test_difference_point_1(self):
	pt1 = data.Point(1, 2, 3)
	pt2 = data.Point(3.5, 2.4, 6.8)
	difference = data.Vector(-2.5, -0.4, -3.8)
	self.assertEqual(vector_math.difference_point(pt1, pt2), difference)
   def test_difference_point_2(self):
	pt1 = data.Point(12, 14, 15)
	pt2 = data.Point(2, 7, 3)
	difference = data.Vector(10, 7, 12)
	self.assertEqual(vector_math.difference_point(pt1, pt2), difference) 

   # test Vector Difference
   def test_difference_vector_1(self):
	v1 = data.Vector(14, 16, 12)
	v2 = data.Vector(3, 6, 7)
	difference = data.Vector(11, 10, 5)
	self.assertEqual(vector_math.difference_vector(v1, v2), difference)
   def test_difference_vector_2(self):
	v1 = data.Vector(1.1, 3.2, 5.3)
	v2 = data.Vector(3, 6, 7)
	difference = data.Vector(-1.9, -2.8, -1.7)
	self.assertEqual(vector_math.difference_vector(v1, v2), difference)

   # test Translate Point
   def test_translate_point_1(self):
	pt = data.Point(9, 0, 1)
	v = data.Vector(1, 2, 3)
	trans_point = data.Point(10, 2, 4)
	self.assertEqual(vector_math.translate_point(pt, v), trans_point)
   def test_translate_point_2(self):
	pt = data.Point(6, 4, 3.5)
	v = data.Vector(12, 13.3, 2.9)
	trans_point = data.Point(18, 17.3, 6.4)
	self.assertEqual(vector_math.translate_point(pt, v), trans_point)

   # test Vector From To
   def test_vector_from_to_1(self):
	pt1 = data.Point(9, 0, 1)
	pt2 = data.Point(1, 2, 3)
	dir_vector = data.Vector(-8, 2, 2)
	self.assertEqual(vector_math.vector_from_to(pt1, pt2), dir_vector)
   def test_vector_from_to_2(self):
	pt1 = data.Point(6, 4, 3.5)
	pt2 = data.Point(12, 13.3, 2.9)
	dir_vector = data.Vector(6, 9.3, -0.6)
	self.assertEqual(vector_math.vector_from_to(pt1, pt2), dir_vector)

   # test Single Ray-Sphere Intersection
   def test_sphere_intersection_point_1(self):
	sphere = data.Sphere(data.Point(3, 0, 0), 1,
                 data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))
	ray = data.Ray(data.Point(0, 0, 0), data.Vector(1, 0, 0))
	collis_point = data.Point(2, 0, 0)
	self.assertEqual(collisions.sphere_intersection_point(ray, sphere),
                         collis_point)
   def test_sphere_intersection_point_2(self):
        sphere = data.Sphere(data.Point(0, 4, 0), 1,
                 data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(0, 1, 0))
        collis_point = data.Point(0, 3, 0)
        self.assertEqual(collisions.sphere_intersection_point(ray, sphere),
                         collis_point)
   def test_sphere_intersection_point_3(self):
        sphere = data.Sphere(data.Point(4, 10, 0), 2,
                 data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(1, 3, 0))
        collis_point = data.Point(2.8, 8.4, 0)
        self.assertEqual(collisions.sphere_intersection_point(ray, sphere),
                         collis_point)
   def test_sphere_intersection_point_4(self):
        sphere = data.Sphere(data.Point(2, 6, 0), 3,
                 data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(0, 0, -2))
        self.assertEqual(collisions.sphere_intersection_point(ray, sphere),
                         None)

   # test All Ray-Sphere Intersections
   def test_find_intersection_points_1(self):
        sphere_list = [data.Sphere(data.Point(3, 0, 0), 1,
               data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0)),
               data.Sphere(data.Point(0, 4, 0), 1,
               data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))]
	ray = data.Ray(data.Point(0, 0, 0), data.Vector(1, 0, 0))
	self.assertEqual(collisions.find_intersection_points(sphere_list, ray),
                  [(data.Sphere(data.Point(3, 0, 0), 1,
                  data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0)),
                  collisions.sphere_intersection_point(ray, sphere_list[0]))])
   def test_find_intersection_points_2(self):
        sphere_list = [data.Sphere(data.Point(3, 0, 0), 1,
                  data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0)),
                  data.Sphere(data.Point(4, 10, 0), 2,
                  data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0)),
                  data.Sphere(data.Point(3, 9, 0), 3,
                  data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))]
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(1, 3, 0))
        self.assertEqual(collisions.find_intersection_points(sphere_list, ray),
                 [(data.Sphere(data.Point(4, 10, 0), 2,
                 data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2,  0.0, 0.0)),
                 collisions.sphere_intersection_point(ray, sphere_list[1])),
                 (data.Sphere(data.Point(3, 9, 0), 3,
                 data.Color(1.0,0.0,0.0), data.Finish(0.1,0.2,0.0, 0.0)),
                 collisions.sphere_intersection_point(ray, sphere_list[2]))])
   
   # test Sphere Normal
   def test_sphere_normal_1(self):
        sphere = data.Sphere(data.Point(3, 0, 0), 1,
                 data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))
        point = data.Point(2, 0, 0)
        normal_vect = data.Vector(-1, 0, 0)
        self.assertEqual(collisions.sphere_normal_at_point(sphere, point),
                          normal_vect)
   def test_sphere_normal_2(self):
        sphere = data.Sphere(data.Point(4, 10, 0), 2,
                 data.Color(1.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.0, 0.0))
        point = data.Point(2.8, 8.4, 0)
        normal_vect = data.Vector(-0.6, -0.8, 0)
        self.assertEqual(collisions.sphere_normal_at_point(sphere, point),
                         normal_vect)


   #I didnt have time to make sufficient test cases
   def test_cast_ray_1(self):
	sphere_list = [data.Sphere(data.Point(-1.0, -1.0, 0.0), 2.0,
                 data.Color(0, 0, 1.0), data.Finish(0.0, 0.0, 0.0, 0.0)),
                 data.Sphere(data.Point(-0.5, 1.5, -3.0), 0.5,
                 data.Color(0.0, 0, 0), data.Finish(0.0, 0.0, 0.0, 0.0))]
        ray = data.Ray(data.Point(0, 0, -14.0), data.Vector(0, 0, 14))
	self.assertEqual(cast.cast_ray(ray, sphere_list, data.Color(0, 0, 1.0),
                 data.Light(data.Point(-100.0, 100.0, -100.0), 
                 data.Color(0.0, 0.0, 0.0)), data.Point(0.0, 0.0, 0.0)),
                 data.Color(0.0, 0.0, 0.0))

   def test_cast_ray_2(self):
	sphere_list = [data.Sphere(data.Point(-1.0, -1.0, 0.0), 2.0,
                 data.Color(0, 0, 1.0), data.Finish(0.0, 0.0, 0.0, 0.0)),
                 data.Sphere(data.Point(1, 1, 1), 0.5,
                 data.Color(0.0, 0, 0), data.Finish(0.0, 0.0, 0.0, 0.0))]
        ray = data.Ray(data.Point(0, 0, -14.0), data.Vector(0, 0, 14))
	self.assertEqual(cast.cast_ray(ray, sphere_list, data.Color(0, 0, 1.0),
                 data.Light(data.Point(-100.0, 100.0, -100.0), 
                 data.Color(0.0, 0.0, 0.0)), data.Point(0.0, 0.0, 0.0)),
                 data.Color(0.0, 0.0, 0.0))



if __name__ == "__main__":
        unittest.main()
