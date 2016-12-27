import unittest
import data
import vector_math
import collisions
import cast
import utility
import math
import sys

red = data.Color(1.0,0,0)

class TestData(unittest.TestCase):
    def testPoint(self):
        pt = data.Point(1,2,3)
        self.assertEqual(pt.x,1)
        self.assertEqual(pt.y,2)
        self.assertEqual(pt.z,3)
    def testPoint2(self):
        pt = data.Point(5.6,7.8,4.2)
        self.assertAlmostEqual(pt.x,5.6)
        self.assertAlmostEqual(pt.y,7.8)
        self.assertAlmostEqual(pt.z,4.2)
    def testVector(self):
        v = data.Vector(7,8,9)
        self.assertEqual(v.x,7)
        self.assertEqual(v.y,8)
        self.assertEqual(v.z,9)
    def testVector2(self):
        v = data.Vector(3.6,99.3,.5)
        self.assertAlmostEqual(v.x,3.6)
        self.assertAlmostEqual(v.y,99.3)
        self.assertAlmostEqual(v.z,.5)
    def testRay(self):
        pt = data.Point(5,9,-4)
        v = data.Vector(23,-48,60)
        r = data.Ray(pt,v)
        self.assertEqual(r.pt.x,5)
        self.assertEqual(r.pt.y,9)
        self.assertEqual(r.pt.z,-4)
        self.assertEqual(r.dir.x,23)
        self.assertEqual(r.dir.y,-48)
        self.assertEqual(r.dir.z,60)
    def testRay2(self):
        pt = data.Point(78.4,-573.3,-0.2)
        v = data.Vector(13.4,-4019834571490537,6734.24230917813)
        r = data.Ray(pt,v)
        self.assertAlmostEqual(r.pt.x,78.4)
        self.assertAlmostEqual(r.pt.y,-573.3)
        self.assertAlmostEqual(r.pt.z,-0.2)
        self.assertAlmostEqual(r.dir.x,13.4)
        self.assertAlmostEqual(r.dir.y,-4019834571490537)
        self.assertAlmostEqual(r.dir.z,6734.24230917813)
    def testSphere(self):
        pt = data.Point(54745,8742390324,-3458753)
        r = 3597832578925789.76675
        s = data.Sphere(pt,r,red,data.Finish(1,1,1,1))
        self.assertEqual(s.center.x,54745)
        self.assertEqual(s.center.y,8742390324)
        self.assertEqual(s.center.z,-3458753)
        self.assertAlmostEqual(s.radius,3597832578925789.76675)
    def testSphere2(self):
        pt = data.Point(538795.4532,-4654654984514,-451875.312)
        r = -357842789.76675
        s = data.Sphere(pt,r,red,data.Finish(1,1,1,1))
        self.assertAlmostEqual(s.center.x,538795.4532)
        self.assertAlmostEqual(s.center.y,-4654654984514)
        self.assertAlmostEqual(s.center.z,-451875.312)
        self.assertAlmostEqual(s.radius,-357842789.76675)
    #equality tests
    def test_point_equal(self):
        pt1 = data.Point(1,2,3)
        pt2 = data.Point(1,2,3)
        self.assertEqual(pt1,pt2)
    def test_point_equal2(self):
        pt1 = data.Point(3.4,-5.2,1.2)
        pt2 = data.Point(3.4,-5.2,1.2)
        self.assertEqual(pt1,pt2)
    def test_vector_equal(self):
        v1 = data.Vector(3,2,1)
        v2 = data.Vector(3,2,1)
        self.assertEqual(v1,v2)
    def test_vector_equal2(self):
        v1 = data.Vector(-3.5,24,1111)
        v2 = data.Vector(-3.5,24,1111)
        self.assertEqual(v1,v2)
    def test_ray_equal(self):
        pt = data.Point(4,5,6)
        v = data.Vector(7,8,9)
        r1 = data.Ray(pt,v)
        r2 = data.Ray(pt,v)
        self.assertEqual(r1,r2)
    def test_ray_equal2(self):
        pt = data.Point(-4,-5.4,-6)
        v = data.Vector(7,-8.7,9)
        r1 = data.Ray(pt,v)
        r2 = data.Ray(pt,v)
        self.assertEqual(r1,r2)
    def test_sphere_equal(self):
        pt = data.Point(5,2,80)
        r = .43987
        s1 = data.Sphere(pt,r,red,data.Finish(1,1,1,1))
        s2 = data.Sphere(pt,r,red,data.Finish(1,1,1,1))
        self.assertEqual(s1,s2)
    def test_sphere_equal2(self):
        pt = data.Point(-45,-3,0)
        r = 2350987
        s1 = data.Sphere(pt,r,red,data.Finish(1,1,1,1))
        s2 = data.Sphere(pt,r,red,data.Finish(1,1,1,1))
        self.assertEqual(s1,s2)

    #vector math tests
    def test_vscale(self):
        v1 = data.Vector(1,2,3)
        v2 = data.Vector(1.5,3,4.5)
        self.assertEqual(vector_math.scale_vector(v1,1.5),v2)
    def test_vscale2(self):
        v1 = data.Vector(-4,5.5,2.1)
        v2 = data.Vector(-8,11,4.2)
        self.assertEqual(vector_math.scale_vector(v1,2),v2)
    def test_dotvector(self):
        v1 = data.Vector(3,3,3)
        v2 = data.Vector(2,5,6)
        self.assertEqual(vector_math.dot_vector(v1,v2),39)
    def test_dotvector2(self):
        v1 = data.Vector(-2,-1.1,5)
        v2 = data.Vector(5,0,10)
        self.assertEqual(vector_math.dot_vector(v1,v2),40)
    def test_lvector(self):
        v1 = data.Vector(0,3,4)
        self.assertEqual(vector_math.length_vector(v1),5)
    def test_lvector2(self):
        v1 = data.Vector(5,8,11)
        self.assertAlmostEqual(vector_math.length_vector(v1),14.49137674618944)
    def test_nvector(self):
        v1 = data.Vector(2,4,5)
        self.assertAlmostEqual(vector_math.length_vector(vector_math.normalize_vector(v1)),1)
    def test_nvector2(self):
        v1 = data.Vector(-234,4,4539853.4)
        self.assertAlmostEqual(vector_math.length_vector(vector_math.normalize_vector(v1)),1)
    def test_diffpt(self):
        pt2 = data.Point(2,1,3)
        pt1 = data.Point(20,4,-10)
        v = data.Vector(18,3,-13)
        self.assertEqual(vector_math.difference_point(pt1,pt2),v)
    def test_diffpt2(self):
        pt2 = data.Point(2,1,3)
        pt1 = data.Point(20,4.5,-10)
        v = data.Vector(-18,-3.5,13)
        self.assertEqual(vector_math.difference_point(pt2,pt1),v)
    def test_diffvect(self):
        v2 = data.Vector(10,10,10)
        v1 = data.Vector(4,8,-17)
        v3 = data.Vector(-6,-2,-27)
        self.assertEqual(vector_math.difference_point(v1,v2),v3)
    def test_diffvect2(self):
        v2 = data.Vector(0,.5,-10)
        v1 = data.Vector(.3,2,5)
        v3 = data.Vector(.3,1.5,15)
        self.assertEqual(vector_math.difference_point(v1,v2),v3)
    def test_transpoint(self):
        pt1 = data.Point(0,0,0)
        pt2 = data.Point(9,5,4)
        v = data.Vector(9,5,4)
        self.assertEqual(vector_math.translate_point(pt1,v),pt2)
    def test_transpoint2(self):
        pt1 = data.Point(5,-10,3)
        pt2 = data.Point(14,-25,8)
        v = data.Vector(9,-15,5)
        self.assertEqual(vector_math.translate_point(pt1,v),pt2)       
    def test_vecfromto(self):
        pt1 = data.Point(0,-10,5)
        pt2 = data.Point(5,5,5)
        v = data.Vector(5,15,0)
        self.assertEqual(vector_math.vector_from_to(pt1,pt2),v)
    def test_vecfromto2(self):
        pt1 = data.Point(5.5,-10.1,5.3)
        pt2 = data.Point(1,3,2)
        v = data.Vector(-4.5,13.1,-3.3)
        self.assertEqual(vector_math.vector_from_to(pt1,pt2),v)

    #collision tests
        #sphere tests test X Y Z seperately, I can't math vectors for some reason
        
    def test_sphere_intersect(self): 
        pt1 = data.Point(0,0,0)
        pt2 = data.Point(4,0,0)
        pt3 = data.Point(2,0,0)
        v1 = data.Vector(4,0,0)
        s = data.Sphere(pt2,2,red,data.Finish(1,1,1,1))
        r = data.Ray(pt1,v1)
        self.assertEqual(collisions.sphere_intersection_point(r,s),pt3)
    def test_sphere_intersect2(self):
        pt1 = data.Point(1,1,1)
        pt2 = data.Point(1,5,1)
        pt3 = data.Point(1,3,1)
        v1 = data.Vector(0,5,0)
        s = data.Sphere(pt2,2,red,data.Finish(1,1,1,1))
        r = data.Ray(pt1,v1)
        self.assertEqual(collisions.sphere_intersection_point(r,s),pt3)
    def test_sphere_intersect3(self):
        pt1 = data.Point(2,1,-1)
        pt2 = data.Point(2,5,-1)
        pt3 = data.Point(2,4,-1)
        v1 = data.Vector(0,5,0)
        s = data.Sphere(pt2,1,red,data.Finish(1,1,1,1))
        r = data.Ray(pt1,v1)
        self.assertEqual(collisions.sphere_intersection_point(r,s),pt3)
    def test_findintpoint(self):
        pt1 = data.Point(0,0,0)
        pt2 = data.Point(4,0,0)
        pt3 = data.Point(2,0,0)
        v1 = data.Vector(10,0,0)
        s = data.Sphere(pt2,2,red,data.Finish(1,1,1,1))
        r = data.Ray(pt1,v1)
        pt4 = data.Point(8,0,0)
        pt5 = data.Point(6,0,0)
        s2 = data.Sphere(pt4,2,red,data.Finish(1,1,1,1))
        l = [s,s2]
        self.assertEqual(collisions.find_intersection_points(l,r),[(s,pt3),(s2,pt5)])
    def test_findintpoint2(self):
        pt1 = data.Point(1,1,1)
        pt2 = data.Point(1,5,1)
        pt3 = data.Point(1,3,1)
        v1 = data.Vector(0,10,0)
        s = data.Sphere(pt2,2,red,data.Finish(1,1,1,1))
        r = data.Ray(pt1,v1)
        pt4 = data.Point(1,10,1)
        pt5 = data.Point(1,8,1)
        s2 = data.Sphere(pt4,2,red,data.Finish(1,1,1,1))
        l = [s,s2]
        self.assertEqual(collisions.find_intersection_points(l,r),[(s,pt3),(s2,pt5)])
    def test_normalpoint(self):
        pt1 = data.Point(0,0,0)
        s = data.Sphere(pt1,3,red,data.Finish(1,1,1,1))
        pt2 = data.Point(0,5,0)
        v = data.Vector(0,1,0)
        self.assertEqual(collisions.sphere_normal_at_point(s,pt2),v)
    def test_normalpoint2(self):
        pt1 = data.Point(-5,2,3)
        s = data.Sphere(pt1,3,red,data.Finish(1,1,1,1))
        pt2 = data.Point(-10,2,3)
        v = data.Vector(-1,0,0)
        self.assertEqual(collisions.sphere_normal_at_point(s,pt2),v)

    #I hate colors
    def test_coloraq(self):
        
        s1 = data.Sphere(data.Point(4,0,0),1,data.Color(255,0,255),data.Finish(1,1,1,1))
        s2 = data.Sphere(data.Point(8,0,0),1,data.Color(255,0,0),data.Finish(1,1,1,1))
        sl = [(s1,data.Point(3,0,0)),(s2,data.Point(7,0,0))]
        pt = data.Point(0,0,0)
        self.assertEqual(cast.closest_color(sl,pt),data.Color(255,0,255))
        pass

    def test_distance3d(self):
        pt1 = data.Point(1,1,1)
        pt2 = data.Point(0,0,0)
        d = utility.distance_3d(pt1,pt2)
        self.assertEqual(d,math.sqrt(3))

#I dont know how to test anything that isn't black by the nature of the large amount of nested float comps involved.
    def test_castray(self):
        pt1 = data.Point(2,1,-1)
        pt2 = data.Point(2,5,-1)
        v1 = data.Vector(0,5,0)
        s = data.Sphere(pt2,1,red,data.Finish(1,1,1,1))
        l = [s]
        r = data.Ray(pt1,v1)
        light = data.Light(data.Point(0,0,0),data.Color(0.0,0.0,0.0))
        eye = data.Point(0.0,0.0,-14.0)
        self.assertEqual(cast.cast_ray(r,l,light.col,light,eye),data.Color(0.0,0.0,0.0))

    def test_castray2(self): #updated for colors/specular
        pt1 = data.Point(0,0,0)
        pt2 = data.Point(4,0,0)
        v1 = data.Vector(8,0,0)
        s = data.Sphere(pt2,2,red,data.Finish(1,1,1,1))
        l = [s]
        light = data.Light(data.Point(0,0,0),data.Color(0.0,0.0,0.0))
        eye = data.Point(0.0,0.0,-14.0)
        r = data.Ray(pt1,v1)
        self.assertEqual(cast.cast_ray(r,l,light.col,light,eye),data.Color(0.0,0.0,0.0)) 
        

        
        

if __name__ == "__main__":
     unittest.main()
