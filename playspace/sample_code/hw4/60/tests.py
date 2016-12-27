import unittest
from cast import *
from collisions import *
from data import *


class testsCast(unittest.TestCase):
	def assertListAlmostEqual(self,l1,l2):
		self.assertEqual(len(l1),len(l2))
		for el1, el2 in zip(l1, l2):
			self.assertAlmostEqual(el1,el2)
	
	def test_point1(self):
		pt = Point(0, 0, 0)
		self.assertEqual(pt.x, 0)
		self.assertEqual(pt.y, 0)
		self.assertEqual(pt.z, 0)
	def test_point_2(self):
		pt = Point(1, 2, 3)
		self.assertEqual(pt.x, 1)
		self.assertEqual(pt.y, 2)
		self.assertEqual(pt.z, 3)

	def test_equality_point1(self):
		pt1 = Point(0,1,2)
		pt2 = Point(0,1,2)
		self.assertEqual(pt1, pt2)
	def test_equality_point2(self):
		pt1 = Point(4,6,8)
		pt2 = Point(3,9,12)
		self.assertNotEqual(pt1, pt2)

	def test_vector1(self):
		vect = Vector(1, 1, 1)
		self.assertEqual(vect.x, 1)
		self.assertEqual(vect.y, 1)
		self.assertEqual(vect.z, 1)
	def test_vector2(self):
		vect = Vector(1, 2, 3)
		self.assertEqual(vect.x, 1)
		self.assertEqual(vect.y, 2)
		self.assertEqual(vect.z, 3)

	def test_ray1(self):
		p1=Point(0,0,0)
		v1=Vector(1,1,1)
		ray=Ray(p1,v1)
		self.assertEqual(ray.pt.x, 0)
		self.assertEqual(ray.pt.y, 0)
		self.assertEqual(ray.pt.z, 0)
		self.assertEqual(ray.dir.x, 1)
		self.assertEqual(ray.dir.y, 1)
		self.assertEqual(ray.dir.z, 1)
	def test_ray2(self):
		p1=Point(0,0,0)
		v1=Vector(-1,-1,-1)
		ray=Ray(p1,v1)
		self.assertEqual(ray.pt.x, -1)
		self.assertEqual(ray.pt.y, -1)
		self.assertEqual(ray.pt.z, -1)
		self.assertEqual(ray.dir.x, -1)
		self.assertEqual(ray.dir.y, -1)
		self.assertEqual(ray.dir.z, -1)

	def test_cast_ray1(self):
		s1 = Sphere(Point(0,0,0),1, Color(1,0,0))
		s2 = Sphere(Point(5,0,0),1, Color(1,1,1))
		ray = Ray(Point(6,0,0),Vector(-5,0,0))
		self.assertTrue (cast_ray(ray, [s1,s2]), [(s1, Point(1,0,0))])
	def test_cast_ray2(self):
		s1 = Sphere(Point(0,0,0),1, Color(1,0,0))
		s2 = Sphere(Point(0,4,0),1, Color(1,1,1))
		ray = Ray(Point(0,1,4),Vector(0,3,-4))
		self.assertTrue (cast_ray(ray, [s1,s2]), [(s2, Point(0,4,0))])

	def test_find_int_pt1(self):
		c1=Point(-20,0,0)
		c2=Point(5,0,0)
		co1=Color(1,1,0)
		co2=Color(1,1,0)
		s1=Sphere(c1,20,co1)
		s2=Sphere(c2,5,co2)
		a=[s1,s2]
		pr1=Point(-20,0,20)
		vr1=Vector(25,0,-15)
		r=Ray(pr1,vr1)
		p1=Point(-20,0,20)
		p2=Point=(5,0,5)
		self.assertListAlmostEqual(find_intersection_points(a,r),[(s1,p1),(s2,p2)])
	def test_find_int_pt2(self):
		c1=Point(0,0,-10)
		c2=Point(0,0,-4)
		c3=Point(0,0,0)
		c4=Point(0,0,20)
		pr1=Point(1,0,-15)
		vr1=Vector(0,0,60)
		s1=Sphere(c1,1)
		s2=Sphere(c2,1)
		s3=Sphere(c3,1)
		s4=Sphere(c4,1)
		a=[s1,s2,s3,s4]
		r=Ray(pr1,vr1)
		p1=Point(1,0,-10)
		p2=Point(1,0,-4)
		p3=Point(1,0,0)
		p4=Point(1,0,20)
		self.assertListAlmostEqual(find_intersection_points(a,r),[(s1,p1),(s2,p2),(s3,p3),(s4,p4)])
	
if __name__=='__main__':
	unittest.main()

