# Name: Allison Lee
# Instructor: Aaron Keen
# Section: 09

import unittest
import data
import vector_math
import collisions
import cast

class CastTests(unittest.TestCase):
    def test_color(self):
        color = data.Color(.1,0,1)
        self.assertEqual(data.Color(.1,0,1),color)
        self.assertEqual(color.r,.1)
        self.assertEqual(color.g,0)
        self.assertEqual(color.b,1)
        
    def test_color_1(self):
        color = data.Color(0,.5,1)
        self.assertEqual(data.Color(0,.5,1),color)
        self.assertEqual(color.r,0)
        self.assertEqual(color.g,.5)
        self.assertEqual(color.b,1)

    def test_dist(self):
        point = data.Point(0,0,0)
        vector = data.Vector(10,10,10)
        ray = data.Ray(point,vector)
        point2 = data.Point(4,4,4)
        self.assertAlmostEqual(cast.dist(ray,point2),6.9282032302)

    def test_dist_2(self):
        point = data.Point(1,2,3)
        vector = data.Vector(-.2,0,4)
        ray = data.Ray(point,vector)
        point2 = data.Point(7,.4,-1)
        self.assertAlmostEqual(cast.dist(ray,point2),7.3864741250478)

    def test_colorprint(self):
        color = data.Color(1,1,1)
        self.assertEqual(cast.colorprint(color),(255,255,255))

    def test_colorprint_2(self):
        color = data.Color(.5,0,1)
        self.assertEqual(cast.colorprint(color),(127,0,255))
        
    def test_finish(self):
        finish = data.Finish(1,.5,0,0)
        self.assertEqual(data.Finish(1,.5,0,0),finish)

    def test_finish2(self):
        finish = data.Finish(1,20,1,0)
        self.assertEqual(data.Finish(1,20,1,0),finish)
        
    def test_light(self):
        pt = data.Point(1,2,3)
        color = data.Color(.1,1,.3)
        light = data.Light(pt,color)
        self.assertEqual(data.Light(pt,color),light)

    def test_light2(self):
        pt = data.Point(0,0,.4)
        color = data.Color(1,0,1)
        light = data.Light(pt,color)
        self.assertEqual(data.Light(pt,color),light)
        
    def test_cast_ray_a(self):
        light = data.Light(data.Point(-10,0,0),data.Color(1,1,1))
        color = data.Color(0,0,0)
        colorcorrect = data.Color(1,1,1)
        eye_point = data.Point(0,0,0)
        ambient = .5
        diffuse = .5
        specular = .5
        roughness = .5
        ray = data.Ray(data.Point(0,0,0),data.Vector(1,-1.5,0))
        finish = data.Finish(ambient,diffuse,specular,roughness)
        sphere1 = data.Sphere(data.Point(-10,0,0),.5,color,finish)
        sphere2 = data.Sphere(data.Point(5,-7.5,0),1.802775637732,color,finish)
        sphere3 = data.Sphere(data.Point(2,3,0),1.802775637732,colorcorrect,finish)
        sphere_list = [sphere1,sphere2,sphere3]
        self.assertEqual(cast.cast_ray(ray,sphere_list,color,light,eye_point),data.Color(0.350631539452,0.350631539452,0.350631539452))

    def test_cast_ray_2(self):
        eye_point = data.Point(0,0,0)
        color = data.Color(0,0,0)
        colorcorrect = data.Color(.5,0,1)
        specular = .5
        diffuse = 1
        roughness = .2
        light = data.Light(data.Point(0,0,0),data.Color(1,1,1))
        ambient = .5
        ray = data.Ray(data.Point(1,0,2),data.Vector(.3,1,2))
        sphere3 = data.Sphere(data.Point(1.6,2,6),2.2561028345357,colorcorrect,data.Finish(ambient,diffuse,specular,roughness))
        sphere2 = data.Sphere(data.Point(2.2,4,10),2.2561028345357,color,data.Finish(ambient,diffuse,specular,roughness))
        sphere1 = data.Sphere(data.Point(4,10,22),4.5122056690714,color,data.Finish(ambient,diffuse,specular,roughness))
        sphere_list = [sphere1,sphere2,sphere3]
        self.assertEqual(cast.cast_ray(ray,sphere_list,color,light,eye_point),data.Color(0.707103705765,0.225826325153,1.18838108638))


if __name__ == "__main__":
    unittest.main()
