import unittest
import data
import collisions
from math import sqrt
from vector_math import *
import cast


#test cases for hw4, parts 3-5


class TestData(unittest.TestCase):
    def test_cast_ray_4(self):
        sp_list = [data.Sphere(data.Point(10, 10, 10), 10, 
		               data.Color(1.0, 0.0, 0.0),
		               data.Finish(.5, 1, 0, 1)),
		   data.Sphere(data.Point(20, 20, 20), 5, 
			       data.Color(0.0, 1.0, 0.0),
		               data.Finish(.25, 1, 10, 100)),
		   data.Sphere(data.Point(30, 30, 30), 2.5, 
			       data.Color(0.0, 0.0, 1.0),
		               data.Finish(.125, 1, 10, 10))]

	self.assertEqual(cast.cast_ray(data.Ray(data.Point(0, 0, 0),
		                                data.Vector(40, 40, 40)),
		                       sp_list, data.Color(3.0, 3.0, 3.0), 
			               data.Light(data.Point(0, 0, 0),
				                  data.Color(0.0, 0.0, 0.0)),
			               data.Point(0, 0, 0)),
			 data.Color(1.0, 0.0, 0.0))

    def test_cast_ray_5(self):
        sp_list = [data.Sphere(data.Point(30, 0, 0), 10, 
		               data.Color(1.0, 0.0, 0.0),
		               data.Finish(.5, 1, 1, 1)),
		   data.Sphere(data.Point(0, 30, 0), 5, 
			       data.Color(0.0, 1.0, 0.0),
		               data.Finish(.25, 2, 1, 1)),
		   data.Sphere(data.Point(0, 0, 30), 2.5, 
			       data.Color(0.0, 0.0, 1.0),
		               data.Finish(.125, 3, 1, 1))]

	self.assertEqual(cast.cast_ray(data.Ray(data.Point(0, 0, 0),
		                                data.Vector(40, 40, 40)),
		                       sp_list, data.Color(3.0, 3.0, 3.0), 
			               data.Light(data.Point(0, 0, 0),
					          data.Color(1.0, 1.0, 1.0)),
			               data.Point(0, 0, 0)),
			 data.Color(1.0, 1.0, 1.0))

    def test_point_off_sphere_1(self):
        self.assertEqual(cast.point_off_sphere(data.Sphere(data.Point(0.0, 0.0,
		                                                      0.0), 
					       2, data.Color(1.0, 1.0, 1.0),
					       data.Finish(.5, 1, 1, 1)),
					       data.Point(2.0, 0.0, 0.0)),
                         data.Point(2.01, 0, 0))

    def test_point_off_sphere_2(self):
        self.assertEqual(cast.point_off_sphere(data.Sphere(data.Point(0.0, 0.0, 
		                                                      0.0), 
					       5, data.Color(1.0, 1.0, 1.0),
					       data.Finish(.5, 1, 1, 1)),
					       data.Point(0.0, 5.0, 0.0)),
                         data.Point(0.0, 5.01, 0))

    def test_scale_normal_1(self):
	self.assertEqual(cast.scale_normal(data.Sphere(data.Point(0.0, 0.0, 
		                                                  0.0), 10,
		                                       data.Color(1.0, 0.0, 
							          0.0),
						       data.Finish(1, .5, 
							           1, 1)),
						       data.Point(0.0, 0.0, 
							          10.0)),
                         data.Vector(0.0, 0.0, 0.01))

    def test_scale_normal_2(self):
	self.assertEqual(cast.scale_normal(data.Sphere(data.Point(10.0, 4.0, 
		                                                  0.0), 4,
		                                       data.Color(1.0, 0.0, 
							          0.0),
						       data.Finish(1, .5, 
							           1, 1)),
						       data.Point(10.0, 0.0, 
							          0.0)),
                         data.Vector(0.0, -0.01, 0.0))



if __name__ == "__main__":
     unittest.main()

