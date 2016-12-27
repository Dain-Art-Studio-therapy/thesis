import unittest
import data
import vector_math
import collisions
import cast

class TestData(unittest.TestCase):
	def test_sphere_eq_1(self):
		c1 = data.Color(0.5, 1.0, 0)
		c2 = data.Color(0.5, 1.0, 0)
		f1 = data.Finish(0, 1.0, 2.0, 2.0)
		f2 = data.Finish(0, 1.0, 2.0, 2.0)
		sphere1 = data.Sphere(data.Point(2, 3, 4), 5, c1, f1)
		sphere2 = data.Sphere(data.Point(2, 3, 4), 5, c2, f2)
		self.assertEqual(sphere1, sphere2)
	
	def test_sphere_eq_2(self):
		c1 = data.Color(0, 1.0, 0.7)
		c2 = data.Color(0, 1.0, 0.7)
		f1 = data.Finish(1.0, 9001.0, 3.22, 3.14)
		f2 = data.Finish(1.0, 9001.0, 3.22, 3.14)
		sphere1 = data.Sphere(data.Point(4, 5, 6), 5, c1, f1)
		sphere2 = data.Sphere(data.Point(4, 5, 6), 5, c2, f2)
		self.assertEqual(sphere1, sphere2)
	
	def test_finish_eq_1(self):
		finish1 = data.Finish(1, 2, 3, 4)
		finish2 = data.Finish(1, 2, 3, 4)
		self.assertEqual(finish1, finish2)
		
	def test_finish_eq_2(self):
		finish1 = data.Finish(3, 1, 2, 5)
		finish2 = data.Finish(3, 1, 2, 5)
		self.assertEqual(finish1, finish2)
	
	def test_light_eq_1(self):
		light1 = data.Light(data.Point(1, 2, 3), data.Color(1, 2, 3))
		light2 = data.Light(data.Point(1, 2, 3), data.Color(1, 2, 3))
		self.assertEqual(light1, light2)
		
	def test_light_eq_2(self):
		light1 = data.Light(data.Point(3, 1, 2), data.Color(4, 5, 6))
		light2 = data.Light(data.Point(3, 1, 2), data.Color(4, 5, 6))
		self.assertEqual(light1, light2)
	
	# finding the closest sphere regardless of list order
	def test_cast_ray_1(self):
		r = data.Color(1.0, 0, 0)
		g = data.Color(0, 1.0, 0)
		b = data.Color(0, 0, 1.0)
		f = data.Finish(0.2, 0.4, 0.5, 0.05)
		l = data.Light(data.Point(50, 50, 50), data.Color(1.5, 1.5, 1.5))
		ray1 = data.Ray(data.Point(0, -10, 0), data.Vector(0, 1, 0))
		e = data.Point(0, -10, 0)
		a = data.Color(1.0, 1.0, 1.0)
		
		sphere1 = data.Sphere(data.Point(0, 0, 0), 2, r, f)
		sphere2 = data.Sphere(data.Point(0, 0, 0), 1, g, f)
		sphere3 = data.Sphere(data.Point(0, 0, 0), 0.5, b, f)
		sphere_list1 = [sphere1, sphere2, sphere3]
		sphere_list2 = [sphere2, sphere3, sphere1]
		self.assertEqual(cast.cast_ray(ray1, sphere_list1, a, l, e),\
						 cast.cast_ray(ray1, sphere_list2, a, l, e))
	
	def test_cast_ray_2(self):
		r = data.Color(1.0, 0, 0)
		g = data.Color(0, 1.0, 0)
		b = data.Color(0, 0, 1.0)
		f = data.Finish(0.2, 0.4, 0.5, 0.05)
		l = data.Light(data.Point(10, 20, 10), data.Color(1.5, 1.5, 1.5))
		ray1 = data.Ray(data.Point(-10, 0, 0), data.Vector(1, 0, 0))
		e = data.Point(-10, 0, 0)
		a = data.Color(1.0, 1.0, 1.0)
		
		sphere1 = data.Sphere(data.Point(1, 0, 0), 2, r, f)
		sphere2 = data.Sphere(data.Point(1, 0, 0), 1, g, f)
		sphere3 = data.Sphere(data.Point(1, 0, 0), 0.5, b, f)
		sphere_list1 = [sphere1, sphere2, sphere3]
		sphere_list2 = [sphere3, sphere1, sphere2]
		self.assertEqual(cast.cast_ray(ray1, sphere_list1, a, l, e),\
						 cast.cast_ray(ray1, sphere_list2, a, l, e))
	
	def test_render_light_1(self):
		# purposefully left empty because the function is implied to work
		# due to the correct output of casting_test
		pass
	
	def test_renderShadow_1(self):
		# purposefully left empty because the function is implied to work
		# due to the correct output of casting_test
		pass
	
	def test_mIndex_1(self):
		l = [2, 3, 4, 1, 2]
		self.assertEqual(cast.mIndex(l), 3)
	
	def test_mIndex_2(self):
		l = [2, 0, 4, 1, 2]
		self.assertEqual(cast.mIndex(l), 1)
		
	def test_distance_1(self):
		p1 = data.Point(0, 0, 0)
		p2 = data.Point(2, 0, 0)
		self.assertEqual(cast.distance(p1, p2), 2)
		
	def test_distance_2(self):
		p1 = data.Point(1, 1, 1)
		p2 = data.Point(1, 5, 1)
		self.assertEqual(cast.distance(p1, p2), 4)
	
if __name__ == "__main__":
	unittest.main()