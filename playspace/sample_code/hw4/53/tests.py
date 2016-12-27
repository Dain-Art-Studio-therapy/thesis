import unittest
import data
import utility
import vector_math
import math
import collisions
import cast
class TestData(unittest.TestCase):
    def test_point_1(self):
        pt1  = data.Point(1.0,2.0,3.0)
        self.assertAlmostEqual(pt1.x, 1.0)
        self.assertAlmostEqual(pt1.y, 2.0)
        self.assertAlmostEqual(pt1.z, 3.0)
    def test_point_2(self):
        pt2 = data.Point(5.0, 6.0, 7.0)
        self.assertAlmostEqual(pt2.x,5.0)
        self.assertAlmostEqual(pt2.y,6.0)
        self.assertAlmostEqual(pt2.z,7.0)
    def test_vector(self):
        vector = data.Vector(3.0,4.0,5.0)
        self.assertAlmostEqual(vector.x, 3.0)
        self.assertAlmostEqual(vector.y,4.0)
        self.assertAlmostEqual(vector.z,5.0)
    def test_vector2(self):
        vector2 = data.Vector(7.0,8.0,9.0)
        self.assertAlmostEqual(vector2.x, 7.0)
        self.assertAlmostEqual(vector2.y,8.0)
        self.assertAlmostEqual(vector2.z,9.0)
    def test_ray(self):
        r = data.Ray(data.Point(3,5,4), data.Vector(4,9,2))
        self.assertAlmostEqual(r.pt.x,3)
        self.assertAlmostEqual(r.pt.y,5)
        self.assertAlmostEqual(r.pt.z,4)
        self.assertAlmostEqual(r.dir.x,4)
        self.assertAlmostEqual(r.dir.y,9)
        self.assertAlmostEqual(r.dir.z,2)
    def test_ray2(self):
        r2 = data.Ray(data.Point(4,7,1), data.Vector(2,6,3))
        self.assertAlmostEqual(r2.pt.x,4)
        self.assertAlmostEqual(r2.pt.y,7)
        self.assertAlmostEqual(r2.pt.z,1)
        self.assertAlmostEqual(r2.dir.x,2)
        self.assertAlmostEqual(r2.dir.y,6)
        self.assertAlmostEqual(r2.dir.z,3)
    def test_sphere(self):
        s = data.Sphere(data.Point(2,2,1), data.Vector(3,2,1),data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0))
        self.assertAlmostEqual(s.center.x,2)
        self.assertAlmostEqual(s.center.y,2)
        self.assertAlmostEqual(s.center.z,1)
        self.assertAlmostEqual(s.radius.x,3)
        self.assertAlmostEqual(s.radius.y,2)
        self.assertAlmostEqual(s.radius.z,1)
    def test_sphere2(self):
        s2 = data.Sphere(data.Point(3,2,8), 2,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0))
        self.assertAlmostEqual(s2.center.x,3)
        self.assertAlmostEqual(s2.center.y,2)
        self.assertAlmostEqual(s2.center.z,8)
        self.assertAlmostEqual(s2.radius,2)
    def test_point_eq1(self):
        self.assertTrue(data.Point(3,6,3) == data.Point(3,6,3))
    def test_point_eq2(self):
        self.assertTrue(data.Point(1,2,3) == data.Point(1,2,3))
    def test_vector_eq1(self):
        self.assertTrue(data.Vector(2,3,4) == data.Vector(2,3,4))
    def test_vector_eq2(self):
        self.assertTrue(data.Vector(5,6,7) == data.Vector(5,6,7))
    def test_ray_eq1(self):
        self.assertTrue(data.Ray(data.Point(3,4,5),data.Vector(7,8,9)) == data.Ray(data.Point(3,4,5), data.Vector(7,8,9)))
    def test_ray_eq2(self):
        self.assertTrue(data.Ray(data.Point(1,7,8),data.Vector(3,0,2)) == data.Ray(data.Point(1,7,8), data.Vector(3,0,2)))
    def test_sphere_eq1(self):
        self.assertTrue(data.Sphere(data.Point(2,5,6), 5,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0)) == data.Sphere(data.Point(2,5,6),5,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0)))
    def test_sphere_eq2(self):
        self.assertTrue(data.Sphere(data.Point(6,8,7), 2,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0)) == data.Sphere(data.Point(6,8,7),2,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0)))
    def test_scale_vector1(self):
        self.assertEqual(vector_math.scale_vector(data.Vector(2,3,4),2), data.Vector(4,6,8))
    def test_scale_vector2(self):
        self.assertEqual(vector_math.scale_vector(data.Vector(2,3,4),3), data.Vector(6,9,12))
    def test_dot_vector1(self):
        self.assertEqual(vector_math.dot_vector(data.Vector(2,3,4),data.Vector(1,2,3)), 20)
    def test_dot_vector2(self):
        self.assertEqual(vector_math.dot_vector(data.Vector(3,4,5), data.Vector(3,3,4)), 41)
    def test_length_vector1(self):
        self.assertAlmostEqual(vector_math.length_vector(data.Vector(1,1,1)), math.sqrt(3))
    def test_length_vector2(self):
        self.assertAlmostEqual(vector_math.length_vector(data.Vector(2,2,2)), math.sqrt(12))
    def test_normalize_vector1(self):
        self.assertEqual(vector_math.normalize_vector(data.Vector(2,3,4)),data.Vector(2/math.sqrt(29), 3/math.sqrt(29), 4/math.sqrt(29)))
    def test_normalize_vector2(self):
        self.assertEqual(vector_math.normalize_vector(data.Vector(4,5,6)),data.Vector(4/math.sqrt(77), 5/math.sqrt(77), 6/math.sqrt(77)))
    def test_difference_point1(self):
        self.assertEqual(vector_math.difference_point(data.Point(3,4,5), data.Point(1,2,3)), data.Vector(2,2,2))
    def test_difference_point2(self):
        self.assertEqual(vector_math.difference_point(data.Point(7,6,3), data.Point(6,3,1)), data.Vector(1,3,2))
    def test_difference_vector1(self):
        self.assertEqual(vector_math.difference_vector(data.Point(5,4,3), data.Point(1,1,1)), data.Point(4,3,2))
    def test_difference_vector2(self):
        self.assertEqual(vector_math.difference_vector(data.Point(6,3,2), data.Point(2,1,1)), data.Point(4,2,1))
    def test_translate_point(self):
        self.assertEqual(vector_math.translate_point(data.Point(3,2,1),data.Vector(3,2,1)), data.Point(6,4,2))
    def test_translate_point2(self):
        self.assertEqual(vector_math.translate_point(data.Point(2,1,6),data.Vector(6,3,5)), data.Point(8,4,11))
    def test_vector_from_to(self):
        self.assertEqual(vector_math.vector_from_to(data.Point(3,2,1), data.Point(5,6,7)), data.Point(2,4,6))
    def test_vector_from_to2(self):
        self.assertEqual(vector_math.vector_from_to(data.Point(1,3,2), data.Point(7,8,9)), data.Point(6,5,7))

    def test_single_ray_sphere_intersection(self):
        s = data.Sphere(data.Point(10,0,0), 5, data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0))
        r = data.Ray(data.Point(0,0,0), data.Vector(5,0,0))
        self.assertEqual(collisions.sphere_intersection_point(r, s), data.Point(5,0,0))
    def test_single_ray_sphere_intersection2(self):
        s = data.Sphere(data.Point(10,10,0), 5,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0))
        r = data.Ray(data.Point(0,0,0), data.Vector(5,5,0))
        self.assertEqual(collisions.sphere_intersection_point(r, s), data.Point(6.464466094,6.464466094,0))
    def test_find_intersection_points(self):
        a = data.Sphere(data.Point(2,0,0),4,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0))
        b = data.Sphere(data.Point(12,0,0),2,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0))
        spherelist = [a,b,data.Sphere(data.Point(8,5,7),3,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0)),data.Point(0.0,0.0,0.0)]
        r = data.Ray(data.Point(-6,0,0), data.Vector(1,0,0))
        e = (data.Sphere(data.Point(2,0,0),4,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0)))
        f =  data.Point(-2,0,0)
        l = [(e,f),(data.Sphere(data.Point(12,0,0),2,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0)),data.Point(10,0,0))]
        self.assertEqual(collisions.find_intersection_point(spherelist,r),l)
    def test_find_intersection_points2(self):
        a = data.Sphere(data.Point(5,0,0),2,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0))
        b = data.Sphere(data.Point(10,0,0),2,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0))
        c = data.Sphere(data.Point(-5,-9,-6),2,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0))
        spherelist2 = [a,b,c]
        r = data.Ray(data.Point(-1,0,0), data.Vector(1,0,0))
        e = (data.Sphere(data.Point(5,0,0),2,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0)))
        f = data.Point(3,0,0)
        l = [(e,f),(data.Sphere(data.Point(10,0,0),2,data.Color(0.0,0.0,1.0),data.Finish(0.0,0.0,0.0,0.0)),data.Point(8,0,0))]
        self.assertEqual(collisions.find_intersection_point(spherelist2,r),l)
    def test_sphere_at_point(self):
        a = data.Point(-5,9,0)
        b = data.Color(0.0,0.0,1.0)
        c = data.Point(-5,5,0)
        d = data.Vector(0,-1,0)
        e = data.Finish(0.0,0.0,0.0,0.0)
        light = (data.Point(-100,100,-100),data.Color(1.5,1.5,1.5))
        self.assertEqual(collisions.sphere_normal_at_point(data.Sphere(a,4,b,e),c), d)
    def test_sphere_at_point2(self):
        a = data.Point(15,0,0)
        b = data.Color(0.0,0.0,1.0)
        c = data.Point(10,0,0)
        d = data.Vector(-1/5,0,0)
        e = data.Finish(0.0,0.0,0.0,0.0)
        light = (data.Point(-100,100,-100),data.Color(1.5,1.5,1.5))
        self.assertEqual(collisions.sphere_normal_at_point(data.Sphere(a,5,b,e),c),d)
    def test_cast_ray1(self):
        finish = data.Finish(0.0,0.0,0.0,0.0)
        a = data.Sphere(data.Point(5,0,0),2,data.Color(1.0,0.0,0.0),finish)
        b = data.Sphere(data.Point(10,0,0),2,data.Color(0.0,0.0,1.0),finish)
        c = data.Sphere(data.Point(-5,-9,-6),2, data.Color(1.0,0.0,0.0),finish)
        sphere_list = [a,b,c,data.Point(0.0,0.0,0.0)]
        color = data.Color(1.0,0.0,0.0)
        light = (data.Point(-100,100,-100),data.Color(1.5,1.5,1.5))
        r = data.Ray(data.Point(-1,0,0), data.Vector(1,0,0))
        point = data.Point(0.0,0.0,0.0)
        self.assertEqual(cast.cast_ray(r, sphere_list,color,light,point),color)
    #def test_cast_ray2(self):
        #a = data.Sphere(data.Point(20,0,0),2,data.Color(1.0,0.0,0.0),data.Finish(0.2,0.2))
        #b = data.Sphere(data.Point(12,0,0),4,data.Color(0.0,0.0,1.0),data.Finish(0.2,0.2))
        #c = data.Sphere(data.Point(32,0,0),6,data.Color(0.0,1.0,0.0),data.Finish(0.2,0.2))
        #color = data.Color(0.0, 0.0, 1.0)
        #sphere_list = [a,b,c]
        #light = (data.Point(-100,100,-100),data.Color(1.5,1.5,1.5))
        #r = data.Ray(data.Point(5,0,0), data.Vector(1,0,0))
        #self.assertEqual(cast.cast_ray(r,sphere_list,color,light), data.Color(0.2,0.2,0.4))
if __name__ == "__main__":
    unittest.main()
