import unittest
import data
import vector_math
import math
import collisions
import cast

class TestData(unittest.TestCase):
	# Test cases from assignment #1
        def test_point_1(self):
                my_point_1 = data.Point(2, 3, 4)
                self.assertEqual(my_point_1.x, 2)
                self.assertEqual(my_point_1.y, 3)
                self.assertEqual(my_point_1.z, 4)

        def test_point_2(self):
                my_point_2 = data.Point(-1, 1.5, 5.25)
                self.assertAlmostEqual(my_point_2.x, -1)
                self.assertAlmostEqual(my_point_2.y, 1.5)
                self.assertAlmostEqual(my_point_2.z, 5.25)

        def test_vector_1(self):
                my_vector_1 = data.Vector(1.0, 2.0, 3.0)
                self.assertAlmostEqual(my_vector_1.x, 1.0)
                self.assertAlmostEqual(my_vector_1.y, 2.0)
                self.assertAlmostEqual(my_vector_1.z, 3.0)

        def test_vector_2(self):
                my_vector_2 = data.Vector(-1.0, 2.5, -3.75)
                self.assertAlmostEqual(my_vector_2.x, -1.0)
                self.assertAlmostEqual(my_vector_2.y, 2.5)
                self.assertAlmostEqual(my_vector_2.z, -3.75)

        def test_ray_1(self):
                my_ray_1 = data.Ray(data.Point(1.5, -2, 3), data.Vector(-2.0, 5.0, -1.5))
                self.assertAlmostEqual(my_ray_1.pt.x, 1.5)
                self.assertAlmostEqual(my_ray_1.pt.y, -2)
                self.assertAlmostEqual(my_ray_1.pt.z, 3)
                self.assertAlmostEqual(my_ray_1.dir.x, -2.0)
                self.assertAlmostEqual(my_ray_1.dir.y, 5.0)
                self.assertAlmostEqual(my_ray_1.dir.z, -1.5)

        def test_ray_2(self):
                my_ray_2 = data.Ray(data.Point(-5.5, 3.5, -1.5), data.Vector(2.5, 0.0, -4.5))
                self.assertAlmostEqual(my_ray_2.pt.x, -5.5)
                self.assertAlmostEqual(my_ray_2.pt.y, 3.5)
                self.assertAlmostEqual(my_ray_2.pt.z, -1.5)
                self.assertAlmostEqual(my_ray_2.dir.x, 2.5)
                self.assertAlmostEqual(my_ray_2.dir.y, 0.0)
                self.assertAlmostEqual(my_ray_2.dir.z, -4.5)

        def test_sphere_1(self):
                my_sphere_1 = data.Sphere(data.Point(5, 2.5, -3), 5, data.Color(0.0, 0.0, 0.0), data.Finish(0.1, 0.2, 0.3, 0.4))
                self.assertAlmostEqual(my_sphere_1.center.x, 5)
                self.assertAlmostEqual(my_sphere_1.center.y, 2.5)
                self.assertAlmostEqual(my_sphere_1.center.z, -3)
                self.assertAlmostEqual(my_sphere_1.radius, 5)
                self.assertAlmostEqual(my_sphere_1.color.r, 0.0)
                self.assertAlmostEqual(my_sphere_1.color.g, 0.0)
                self.assertAlmostEqual(my_sphere_1.color.b, 0.0)
                self.assertAlmostEqual(my_sphere_1.finish.ambient, 0.1)
                self.assertAlmostEqual(my_sphere_1.finish.diffuse, 0.2)
		self.assertAlmostEqual(my_sphere_1.finish.specular, 0.3)
		self.assertAlmostEqual(my_sphere_1.finish.roughness, 0.4)

        def test_sphere_2(self):
                my_sphere_2 = data.Sphere(data.Point(4.5, -3.5, 1.5), 3.5, data.Color(1.0, 0.0, 0.0), data.Finish(0.5, 0.4, 0.9, 0.8))
                self.assertAlmostEqual(my_sphere_2.center.x, 4.5)
                self.assertAlmostEqual(my_sphere_2.center.y, -3.5)
                self.assertAlmostEqual(my_sphere_2.center.z, 1.5)
                self.assertAlmostEqual(my_sphere_2.radius, 3.5)
                self.assertAlmostEqual(my_sphere_2.color.r, 1.0)
                self.assertAlmostEqual(my_sphere_2.color.g, 0.0)
                self.assertAlmostEqual(my_sphere_2.color.b, 0.0)
                self.assertAlmostEqual(my_sphere_2.finish.ambient, 0.5)
                self.assertAlmostEqual(my_sphere_2.finish.diffuse, 0.4)
		self.assertAlmostEqual(my_sphere_2.finish.specular, 0.9)
		self.assertAlmostEqual(my_sphere_2.finish.roughness, 0.8)

        ## Test cases for assignment #2
        # Equality Test for the Class initialization
        def test_point_equality_1(self):
                equal_point_1 = data.Point(1, 2.5, 5.5)
                self.assertEqual(equal_point_1, data.Point(1, 2.5, 5.5))

        def test_point_equality_2(self):
                equal_point_2 = data.Point(-3.5, 4.9, -1.3)
                self.assertEqual(equal_point_2, data.Point(-3.5, 4.9, -1.3))

        def test_vector_equality_1(self):
                equal_vector_1 = data.Vector(3.5, 2.5, 0.5)
                self.assertEqual(equal_vector_1, data.Vector(3.5, 2.5, 0.5))

        def test_vector_equality_2(self):
                equal_vector_2 = data.Vector(-5.0, 4.5, 0.0)
                self.assertEqual(equal_vector_2, data.Vector(-5.0, 4.5, 0.0))

        def test_ray_equality_1(self):
                equal_ray_1 = data.Ray(data.Point(2.5, -3.3, 4.0), data.Vector(3.0, 2.0, 1.0))
                self.assertEqual(equal_ray_1, data.Ray(data.Point(2.5, -3.3, 4.0), data.Vector(3.0, 2.0, 1.0)))

        def test_ray_equality_2(self):
                equal_ray_2 = data.Ray(data.Point(-3.5, 4.5, 5.5), data.Vector(-1.0, 3.5, -6.0))
                self.assertEqual(equal_ray_2, data.Ray(data.Point(-3.5, 4.5, 5.5), data.Vector(-1.0, 3.5, -6.0)))

        def test_sphere_equality_1(self):
                equal_sphere_1 = data.Sphere(data.Point(4.0, 3.0, 2.5), 2.5, data.Color(0.0, 1.0, 0.0), data.Finish(1.0, 0.9, 0.5, 0.3))
                self.assertEqual(equal_sphere_1, data.Sphere(data.Point(4.0, 3.0, 2.5), 2.5, data.Color(0.0, 1.0, 0.0), data.Finish(1.0, 0.9, 0.5, 0.3)))

        def test_sphere_equality_2(self):
                equal_sphere_2 = data.Sphere(data.Point(-3.5, 4.3, 0.0), 4.0, data.Color(0.0, 0.0, 1.0), data.Finish(0.2, 0.8, 0.1, 0.05))
                self.assertEqual(equal_sphere_2, data.Sphere(data.Point(-3.5, 4.3, 0.0), 4.0, data.Color(0.0, 0.0, 1.0), data.Finish(0.2, 0.8, 0.1, 0.05)))

        # Vector_math function test
        def test_scale_vector_1(self):
                # vector_math.scale_vector(data.Vector(1.0, 2.0, 3.0), 2) == data.Vector(2.0, 4.0, 6.0)
                self.assertEqual(vector_math.scale_vector(data.Vector(1.0, 2.0, 3.0), 2), data.Vector(2.0, 4.0, 6.0))

        def test_scale_vector_2(self):
                # vector_math.scale_vector(data.Vector(3.0, -5.0, 0.0), 0.5) == data.Vector(1.5, -2.5, 0.0)
                self.assertEqual(vector_math.scale_vector(data.Vector(3.0, -5.0, 0.0), 0.5), data.Vector(1.5, -2.5, 0.0))

        def test_dot_vector_1(self):
                # vector_math.dot_vector((data.Vector(1.0, 2.0, 3.0)), data.Vector(4.0, -2.0, 1.0)) == 3.0
                self.assertAlmostEqual(vector_math.dot_vector((data.Vector(1.0, 2.0, 3.0)), data.Vector(4.0, -2.0, 1.0)), 3.0)

        def test_dot_vector_2(self):
                # vector_math.dot_vector((data.Vector(-2.5, 3.0, 0.0)), data.Vector(2.0, 2.5, -5.0)) == 2.5
                self.assertAlmostEqual(vector_math.dot_vector((data.Vector(-2.5, 3.0, 0.0)), data.Vector(2.0, 2.5, -5.0)), 2.5)
	
	def test_length_vector_1(self):
		# vector_math.length_vector(data.Vector(2.0, 1.0, -3.0)) == math.sqrt(14.0)
		self.assertAlmostEqual(vector_math.length_vector(data.Vector(2.0, 1.0, -3.0)), math.sqrt(14.0))

	def test_length_vector_2(self):
		# vector_math.length_vector(data.Vector(5.0, -0.5, 2.0)) == math.sqrt(29.25)
		self.assertAlmostEqual(vector_math.length_vector(data.Vector(5.0, -0.5, 2.0)), math.sqrt(29.25))

	def test_normalize_vector_1(self):
		# vector_math.normalize_vector(data.Vector(2.0, 4.0, 6.0)) == data.Vector(2.0 / math.sqrt(56.0), 4.0 / math.sqrt(56.0), 6.0 / math.sqrt(56.0))
		self.assertEqual(vector_math.normalize_vector(data.Vector(2.0, 4.0, 6.0)), data.Vector(2.0 / math.sqrt(56.0), 4.0 / math.sqrt(56.0), 6.0 / math.sqrt(56.0)))

	def test_normalize_vector_2(self):
		# vector_math.normalize_vector(data.Vector(0.5, -3.0, 1.0)) == data.Vector(0.5 / math.sqrt(10.25), -3.0 / math.sqrt(10.25), 1.0 / math.sqrt(10.25))
		self.assertEqual(vector_math.normalize_vector(data.Vector(0.5, -3.0, 1.0)), data.Vector(0.5 / math.sqrt(10.25), -3.0 / math.sqrt(10.25), 1.0 / math.sqrt(10.25)))

	def test_difference_point_1(self):
		# vector_math.difference_point(data.Point(5.0, -3.5, 2.2), data.Point(4.3, 0.0, -1.0)) == data.Vector(0.7, -3.5, 3.2)
		self.assertEqual(vector_math.difference_point(data.Point(5.0, -3.5, 2.2), data.Point(4.3, 0.0, -1.0)), data.Vector(0.7, -3.5, 3.2))

        def test_difference_point_2(self):
                # vector_math.difference_point(data.Point(-2.5, 4.9, 0.0), data.Point(3.5, 2.1, 1.4)) == data.Vector(-6.0, 2.8, -1.4)
                self.assertEqual(vector_math.difference_point(data.Point(-2.5, 4.9, 0.0), data.Point(3.5, 2.1, 1.4)), data.Vector(-6.0, 2.8, -1.4))

        def test_difference_vector_1(self):
                # vector_math.difference_vector(data.Vector(3.5, -2.0, 0.5), data.Vector(2.5, 0.0, 1.0)) == data.Vector(1.0, -2.0, -0.5)
                self.assertEqual(vector_math.difference_vector(data.Vector(3.5, -2.0, 0.5), data.Vector(2.5, 0.0, 1.0)), data.Vector(1.0, -2.0, -0.5))

        def test_difference_vector_2(self):
                # vector_math.difference_vector(data.Vector(-4.4, 3.3, -2.2), data.Vector(4.0, -3.0, 2.0)) == data.Vector(-8.4, 6.3, -4.2)
                self.assertEqual(vector_math.difference_vector(data.Vector(-4.4, 3.3, -2.2), data.Vector(4.0, -3.0, 2.0)), data.Vector(-8.4, 6.3, -4.2))

        def test_translate_point_1(self):
                # vector_math.translate_point(data.Point(2.5, 3.0, -4.0), data.Vector(1.0, 2.5, 2.0)) == data.Point(3.5, 5.5, -2.0)
                self.assertEqual(vector_math.translate_point(data.Point(2.5, 3.0, -4.0), data.Vector(1.0, 2.5, 2.0)), data.Point(3.5, 5.5, -2.0))

        def test_translate_point_2(self):
                # vector_math.translate_point(data.Point(-1.0, 0.0, 1.5), data.Vector(-3.0, 2.5, -1.0)) == data.Point(-4.0, 2.5, 0.5)
                self.assertEqual(vector_math.translate_point(data.Point(-1.0, 0.0, 1.5), data.Vector(-3.0, 2.5, -1.0)), data.Point(-4.0, 2.5, 0.5))

        def test_vector_from_to_1(self):
                # vector_math.vector_from_to(data.Point(2.0, -1.5, 3.0), data.Point(3.0, -2.5, -1.5)) == data.Vector(1.0, -4.0, -4.5)
                self.assertEqual(vector_math.vector_from_to(data.Point(2.0, -1.5, 3.0), data.Point(3.0, -2.5, -1.5)), data.Vector(1.0, -1.0, -4.5))

        def test_vector_from_to_2(self):
                # vector_math.vector_from_to(data.Point(-1.0, 2.2, -1.9), data.Point(-1.2, 3.0, 0.0)) == data.Vector(-0.2, 0.8, 1.9)
                self.assertEqual(vector_math.vector_from_to(data.Point(-1.0, 2.2, -1.9), data.Point(-1.2, 3.0, 0.0)), data.Vector(-0.2, 0.8, 1.9))

        ## Test cases for assignment #3
        # Sphere intersection test
        def test_sphere_intersection_point_1(self):
                ray = data.Ray(data.Point(1, 0, 0), data.Vector(3, 0, 0))
                sphere = data.Sphere(data.Point(10, 0, 0), 2, data.Color(1.0, 0.5, 0.0), data.Finish(0.3, 0.4, 0.2, 0.3))
                self.assertEqual(collisions.sphere_intersection_point(ray, sphere), data.Point(8, 0, 0))

        def test_sphere_intersection_point_2(self):
                ray = data.Ray(data.Point(1.0, 2.0, 0.0), data.Vector(2.0, -1.0, 0.0))
                sphere = data.Sphere(data.Point(7.0, -4.5, 0.5), 2.5, data.Color(0.0, 0.5, 1.0), data.Finish(0.2, 0.1, 0.4, 0.5))
                self.assertEqual(collisions.sphere_intersection_point(ray, sphere), None)

        def test_find_intersection_points_1(self):
                ray = data.Ray(data.Point(1, 0, 0), data.Vector(3, 0, 0))
                sphere_1 = data.Sphere(data.Point(10, 0, 0), 2, data.Color(0.0, 0.25, 0.0), data.Finish(1.0, 0.1, 0.1, 0.1))
                sphere_2 = data.Sphere(data.Point(10, 2, 0), 2, data.Color(0.0, 0.1, 0.0), data.Finish(0.5, 0.5, 0.05, 0.05))
                sphere_3 = data.Sphere(data.Point(10, -2, 0), 2, data.Color(1.0, 0.0, 1.0), data.Finish(0.4, 0.3, 0.7, 0.7))
                self.assertEqual(collisions.find_intersection_points([sphere_1, sphere_2, sphere_3], ray), 
                        [(sphere_1, data.Point(8, 0, 0)), (sphere_2, data.Point(10, 0, 0)), (sphere_3, data.Point(10, 0, 0))])

        def test_find_intersection_points_2(self):
                ray = data.Ray(data.Point(1.0, 2.0, 0.0), data.Vector(2.0, -1.0, 0.0))
                sphere_1 = data.Sphere(data.Point(7.0, -4.5, 0.5), 2.5, data.Color(0.5, 0.5, 0.5), data.Finish(0.6, 0.5, 0.9, 0.9))
                sphere_2 = data.Sphere(data.Point(12.0, -3.0, 0.0), 1.0, data.Color(0.75, 0.5, 0.25), data.Finish(0.7, 1.0, 0.25, 0.75))
                sphere_3 = data.Sphere(data.Point(3.0, -1.0, 0.0), 4.0, data.Color(0.5, 0.25, 0.75), data.Finish(0.8, 0.9, 0.1, 0.9))
                self.assertEqual(collisions.find_intersection_points([sphere_1, sphere_2, sphere_3], ray),
                        [(sphere_2, data.Point(11.0, -3.0, 0.0)), (sphere_3, data.Point(7.0, -1.0, 0.0))])

        def test_sphere_normal_at_point_1(self):
                ray = data.Ray(data.Point(1, 0, 0), data.Vector(3, 0, 0))
                sphere = data.Sphere(data.Point(10, 0, 0), 2, data.Color(0.25, 0.75, 0.5), data.Finish(0.9, 0.1, 0.2, 0.8))
                self.assertEqual(collisions.sphere_normal_at_point(sphere, collisions.sphere_intersection_point(ray, sphere)), data.Vector(-1, 0, 0))

        def test_sphere_normal_at_point_2(self):
                ray = data.Ray(data.Point(1.0, 2.0, 0.0), data.Vector(2.0, -1.0, 0.0))
                sphere = data.Sphere(data.Point(3.0, -1.0, 0.0), 4.0, data.Color(0.1, 0.2, 0.3), data.Finish(1.0, 0.5, 0.2, 0.3))
                self.assertEqual(collisions.sphere_normal_at_point(sphere, collisions.sphere_intersection_point(ray, sphere)), data.Vector(1.0, 0.0, 0.0))


        # Test cases for assignment #4
        # Equality test for class initialization
        def test_color_equality_1(self):
                equal_color_1 = data.Color(1.0, 0.5, 0.0)
                self.assertEqual(equal_color_1, data.Color(1.0, 0.5, 0.0))

        def test_color_equality_2(self):
                equal_color_2 = data.Color(0.1, 0.2, 0.3)
                self.assertEqual(equal_color_2, data.Color(0.1, 0.2, 0.3))

        def test_finish_equality_1(self):
                equal_finish_1 = data.Finish(0.2, 0.4, 0.6, 0.8)
                self.assertEqual(equal_finish_1, data.Finish(0.2, 0.4, 0.6, 0.8))

        def test_finish_equality_2(self):
                equal_finish_2 = data.Finish(1.0, 0.5, 0.2, 0.1)
                self.assertEqual(equal_finish_2, data.Finish(1.0, 0.5, 0.2, 0.1))

        def test_light_equality_1(self):
                equal_light_1 = data.Light(data.Point(-1.0, 0.0, 1.0), data.Color(0.0, 0.5, 1.0))
                self.assertEqual(equal_light_1, data.Light(data.Point(-1.0, 0.0, 1.0), data.Color(0.0, 0.5, 1.0)))

        def test_light_equality_2(self):
                equal_light_2 = data.Light(data.Point(1.0, 2.0, 3.0), data.Color(0.3, 0.2, 0.1))
                self.assertEqual(equal_light_2, data.Light(data.Point(1.0, 2.0, 3.0), data.Color(0.3, 0.2, 0.1)))

	# Helper function and cast_ray test cases
	def test_closest_sphere_index_1(self):
		ray = data.Ray(data.Point(0.0, 1.0, 0.0), data.Vector(1.0, 0.0, 0.0))
		sphere_1 = data.Sphere(data.Point(5.0, 0.0, 0.0), 1.0, data.Color(1.0, 0.0, 0.0), data.Finish(0.5, 0.1, 0.5, 0.3))
		sphere_2 = data.Sphere(data.Point(10.0, 1.0, 0.0), 2.0, data.Color(1.0, 1.0, 0.0), data.Finish(0.1, 0.9, 0.3, 0.1))
		contact_sphere  = collisions.find_intersection_points([sphere_1, sphere_2], ray)
		self.assertEqual(cast.closest_sphere_index(ray, contact_sphere), 0)

	def test_closest_sphere_index_2(self):
		ray = data.Ray(data.Point(0.0, 0.0, 0.0), data.Vector(0.0, 0.0, 3.0))
		sphere_1 = data.Sphere(data.Point(0.0, 0.0, 5.0), 0.5, data.Color(0.0, 1.0, 1.0), data.Finish(0.25, 0.5, 0.1, 0.6))
		sphere_2 = data.Sphere(data.Point(1.0, 0.0, 3.0), 1.0, data.Color(1.0, 0.0, 1.0), data.Finish(0.75, 0.5, 0.6, 0.1))
		contact_sphere = collisions.find_intersection_points([sphere_1, sphere_2], ray)
		self.assertEqual(cast.closest_sphere_index(ray, contact_sphere), 1)

        def test_ambient_color_change_1(self):
                sphere = data.Sphere(data.Point(3.0, 4.0, 5.0), 4.0, data.Color(0.5, 0.5, 0.5), data.Finish(0.5, 0.5, 0.5, 0.5))
                ambient = data.Color(1.0, 1.0, 1.0)
                self.assertEqual(cast.ambient_color_change(sphere, ambient), data.Color(0.25, 0.25, 0.25))

        def test_ambient_color_change_2(self):
                sphere = data.Sphere(data.Point(-5.0, 3.0, 10.0), 1.5, data.Color(0.2, 0.4, 0.6), data.Finish(0.8, 0.2, 0.1, 0.05))
                ambient = data.Color(0.5, 0.5, 0.5)
                self.assertEqual(cast.ambient_color_change(sphere, ambient), data.Color(0.08, 0.16, 0.24))

        def test_diffuse_color_change_1(self):
                visible = 0.5
                sphere = data.Sphere(data.Point(0.0, 0.0, 10.0), 3.0, data.Color(0.8, 0.8, 0.8), data.Finish(0.5, 0.5, 0.25, 0.1))
                light = data.Light(data.Point(-1.0, 0.0, 1.0), data.Color(1.0, 1.0, 1.0))
                self.assertEqual(cast.diffuse_color_change(visible, sphere, light), data.Color(0.2, 0.2, 0.2))

        def test_diffuse_color_change_2(self):
                visible = -1.0
                sphere = data.Sphere(data.Point(-10.0, -5.0, 10.0), 2.5, data.Color(0.5, 1.0, 0.5), data.Finish(0.25, 0.8, 0.5, 0.08))
                light = data.Light(data.Point(1.0, 2.0, 3.0), data.Color(0.4, 0.5, 0.6))
                self.assertEqual(cast.diffuse_color_change(visible, sphere, light), data.Color(0.0, 0.0, 0.0))

        def test_specular_color_change_1(self):
                light = data.Light(data.Point(-1.5, 1.0, -0.5), data.Color(0.1, 0.2, 0.4))
                sphere = data.Sphere(data.Point(-1.0, -2.0, -3.0), 0.5, data.Color(0.5, 0.5, 0.5), data.Finish(0.4, 0.3, 0.5, 0.5))
                specular_intensity = 2
                self.assertEqual(cast.specular_color_change(light, sphere, specular_intensity), data.Color(0.2, 0.4, 0.8))

        def test_specular_color_change_2(self):
                light = data.Light(data.Point(5.0, 10.0, 0.0), data.Color(0.5, 0.7, 0.9))
                sphere = data.Sphere(data.Point(0.0, 5.0, 7.5), 4.5, data.Color(1.0, 1.0, 1.0), data.Finish(0.3, 0.5, 0.1, 0.05))
                specular_intensity = 0
                self.assertEqual(cast.specular_color_change(light, sphere, specular_intensity), data.Color(0.0, 0.0, 0.0))

        def test_cast_ray_1(self):
                ray = data.Ray(data.Point(1.0, 0.0, 0.0), data.Vector(-2.0, 0.0, 0.0))
                sphere_1 = data.Sphere(data.Point(-10.0, 0.0, 0.0), 2.0, data.Color(1.0, 0.0, 0.0), data.Finish(0.2, 0.8, 0.5, 0.05))
                sphere_2 = data.Sphere(data.Point(-5.0, 4.0, 0.0), 4.0, data.Color(0.0, 1.0, 0.0), data.Finish(0.5, 0.1, 0.2, 0.02))
                ambient = data.Color(1.0, 1.0, 1.0)
                light = data.Light(data.Point(-1.0, 0.0, 1.0), data.Color(0.5, 0.5, 0.5))
                eye_point = data.Point(0.0, 0.0, 0.0)
                self.assertEqual(cast.cast_ray(ray, [sphere_1, sphere_2], ambient, light, eye_point), data.Color(0.0, 0.5, 0.0))

        def test_cast_ray_2(self):
                ray = data.Ray(data.Point(2.0, 0.0, 0.0), data.Vector(0.0, 3.0, 0.0))
                sphere_1 = data.Sphere(data.Point(0.0, 10.0, 0.0), 2.5, data.Color(0.0, 0.0, 1.0), data.Finish(0.25, 0.75, 0.8, 0.2))
                sphere_2 = data.Sphere(data.Point(1.0, 0.0, 0.0), 3.0, data.Color(1.0, 0.0, 1.0), data.Finish(0.9, 0.3, 0.4, 0.6))
                ambient = data.Color(0.5, 0.5, 0.5)
                light = data.Light(data.Point(0.0, 0.5, 10.0), data.Color(1.0, 0.0, 0.0))
                eye_point = data.Point(0.0, 0.0, 10.0)
                self.assertEqual(cast.cast_ray(ray, [sphere_1, sphere_2], ambient, light, eye_point), data.Color(0.45, 0.0, 0.45))

if __name__ == "__main__":
        unittest.main()
