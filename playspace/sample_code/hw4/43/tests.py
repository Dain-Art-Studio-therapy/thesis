import unittest
import data
import vector_math
import collisions
import math
import utility
import cast
class TestData(unittest.TestCase):

############################  INIT  ############################

    def test_point_class(self):
        myPoint = data.Point(1, 1, 1)
        self.assertAlmostEqual(myPoint.x, 1)
        self.assertAlmostEqual(myPoint.y, 1)
        self.assertAlmostEqual(myPoint.z, 1)

    def test_point_class_again(self):
        myPoint1 = data.Point(1.5, 2, 2.5)
        self.assertAlmostEqual(myPoint1.x, 1.5)
        self.assertAlmostEqual(myPoint1.y, 2.0)
        self.assertAlmostEqual(myPoint1.z, 2.5)

    def test_vector_class(self):
        myVector = data.Vector(2, 2, 2)
        self.assertAlmostEqual(myVector.x, 2)
        self.assertAlmostEqual(myVector.y, 2)
        self.assertAlmostEqual(myVector.z, 2)

    def test_vector_class_again(self):
        myVector1 = data.Vector(0.5, 3.6, 4.6)
        self.assertAlmostEqual(myVector1.x, 0.5)
        self.assertAlmostEqual(myVector1.y, 3.6)
        self.assertAlmostEqual(myVector1.z, 4.6)

    def test_ray_class(self):
        myRay = data.Ray(data.Point(3, 3, 3), data.Vector(4, 4, 4))
        self.assertAlmostEqual(myRay.pt.x, 3)
        self.assertAlmostEqual(myRay.pt.y, 3)
        self.assertAlmostEqual(myRay.pt.z, 3)
        self.assertAlmostEqual(myRay.dir.x, 4)
        self.assertAlmostEqual(myRay.dir.y, 4)
        self.assertAlmostEqual(myRay.dir.z, 4)

    def test_ray_class_again(self):
        myRay1 = data.Ray(data.Point(6.3, 7.3, 8.3), data.Vector(0.5, 1.5, 2.5))
        self.assertAlmostEqual(myRay1.pt.x, 6.3)
        self.assertAlmostEqual(myRay1.pt.y, 7.3)
        self.assertAlmostEqual(myRay1.pt.z, 8.3)
        self.assertAlmostEqual(myRay1.dir.x, 0.5)
        self.assertAlmostEqual(myRay1.dir.y, 1.5)
        self.assertAlmostEqual(myRay1.dir.z, 2.5)

    def test_sphere_class(self):
        mySphere = data.Sphere(data.Point(5, 5, 5), 6, data.Color(0, 0, 0), data.Finish(1, 2, 3, 4))
        self.assertAlmostEqual(mySphere.center.x, 5)
        self.assertAlmostEqual(mySphere.center.y, 5)
        self.assertAlmostEqual(mySphere.center.z, 5)
        self.assertAlmostEqual(mySphere.radius, 6)
        self.assertAlmostEqual(mySphere.color.r, 0)
        self.assertAlmostEqual(mySphere.color.g, 0)
        self.assertAlmostEqual(mySphere.color.b, 0)
        self.assertAlmostEqual(mySphere.finish.ambient, 1)
        self.assertAlmostEqual(mySphere.finish.diffuse, 2)
        self.assertAlmostEqual(mySphere.finish.specular, 3)
        self.assertAlmostEqual(mySphere.finish.roughness, 4)

    def test_sphere_class_again(self):
        mySphere1 = data.Sphere(data.Point(4.9, 5.9, 6.9), 2.9, data.Color(50, 60, 70), data.Finish(6, 2, 1, 3))
        self.assertAlmostEqual(mySphere1.center.x, 4.9)
        self.assertAlmostEqual(mySphere1.center.y, 5.9)
        self.assertAlmostEqual(mySphere1.center.z, 6.9)
        self.assertAlmostEqual(mySphere1.radius, 2.9)
        self.assertAlmostEqual(mySphere1.color.r, 50)
        self.assertAlmostEqual(mySphere1.color.g, 60)
        self.assertAlmostEqual(mySphere1.color.b, 70)
        self.assertAlmostEqual(mySphere1.finish.ambient, 6)
        self.assertAlmostEqual(mySphere1.finish.diffuse, 2)
        self.assertAlmostEqual(mySphere1.finish.specular, 1)
        self.assertAlmostEqual(mySphere1.finish.roughness, 3)


    def test_color_class(self):
        myColor = data.Color(255, 255, 255)
        self.assertAlmostEqual(myColor.r, 255)
        self.assertAlmostEqual(myColor.g, 255)
        self.assertAlmostEqual(myColor.b, 255)

    def test_color_class_again(self):
        myColor = data.Color(123, 234, 0)
        self.assertAlmostEqual(myColor.r, 123)
        self.assertAlmostEqual(myColor.g, 234)
        self.assertAlmostEqual(myColor.b, 0)

    def test_finish_class(self):
        myFinish = data.Finish(5, 6, 7, 8)
        self.assertAlmostEqual(myFinish.ambient, 5)
        self.assertAlmostEqual(myFinish.diffuse, 6)
        self.assertAlmostEqual(myFinish.specular, 7)
        self.assertAlmostEqual(myFinish.roughness, 8)

    def test_finish_class_again(self):
        myFinish = data.Finish(4, 3, 2, 1)
        self.assertAlmostEqual(myFinish.ambient, 4)
        self.assertAlmostEqual(myFinish.diffuse, 3)
        self.assertAlmostEqual(myFinish.specular, 2)
        self.assertAlmostEqual(myFinish.roughness, 1)

    def test_light_class_(self):
        myLight = data.Light(data.Point(1, 2, 3), data.Color(3, 2, 1))
        self.assertTrue(data.Point.__eq__(myLight.pt, data.Point(1, 2, 3)))
        self.assertAlmostEqual(myLight.color.r, 3)
        self.assertAlmostEqual(myLight.color.g, 2)
        self.assertAlmostEqual(myLight.color.b, 1)

    def test_light_class_again(self):
        myLight = data.Light(data.Point(4, 5, 6), data.Color(7, 8, 9))
        self.assertTrue(data.Point.__eq__(myLight.pt, data.Point(4, 5, 6)))
        self.assertAlmostEqual(myLight.color.r, 7)
        self.assertAlmostEqual(myLight.color.g, 8)
        self.assertAlmostEqual(myLight.color.b, 9)



##############################  EQ  ##############################

    def test_point_eq(self):
        self.assertTrue(data.Point.__eq__(data.Point(1, 2, 3), data.Point(1, 2, 3)))

    def test_point_eq_again(self):
        self.assertFalse(data.Point.__eq__(data.Point(1, 2, 3), data.Point(1, 2, 4)))

    def test_vector_eq(self):
        self.assertTrue(data.Vector.__eq__(data.Vector(4, 5, 6), data.Vector(4, 5, 6)))

    def test_vector_eq_again(self):
        self.assertFalse(data.Vector.__eq__(data.Vector(4, 5, 6), data.Vector(4, 5, 7)))

    def test_ray_eq(self):
        myRay = data.Ray(data.Point(1, 2, 3), data.Vector(1, 2, 3))
        self.assertTrue(data.Ray.__eq__(myRay, data.Ray(data.Point(1, 2, 3), data.Vector(1, 2, 3))))

    def test_ray_eq_again(self):
        myRay = data.Ray(data.Point(1, 2, 3), data.Vector(1, 2, 3))
        self.assertFalse(data.Ray.__eq__(myRay, data.Ray(data.Point(1, 2, 4), data.Vector(1, 2, 3))))

    def test_sphere_eq(self):
        mySphere = data.Sphere(data.Point(1, 2, 3), 4, data.Color(0, 0, 0), data.Finish(1, 2, 3, 4))
        self.assertTrue(data.Sphere.__eq__(mySphere, data.Sphere(data.Point(1, 2, 3), 4, data.Color(0, 0, 0), data.Finish(1, 2, 3, 4))))

    def test_sphere_eq_again(self):
        mySphere = data.Sphere(data.Point(1, 2, 3), 4, data.Color(50, 60, 70), data.Finish(6, 2, 1, 3))
        self.assertFalse(data.Sphere.__eq__(mySphere, data.Sphere(data.Point(1, 2, 3), 5, data.Color(50, 60, 70), data.Finish(6, 2, 1, 3))))

##########################  VECTOR MATH  ##########################

    def test_scale_vector(self):
        v = data.Vector(1, 2, 3)
        s = 2
        self.assertTrue(data.Vector.__eq__(vector_math.scale_vector(v, s),
                        data.Vector(2, 4, 6)))

    def test_scale_vector_again(self):
        v = data.Vector(1.1, 2.2, 3.3)
        s = 3
        self.assertTrue(data.Vector.__eq__(vector_math.scale_vector(v, s),
                        data.Vector(3.3, 6.6, 9.9)))

    def test_dot_vector(self):
        v1 = data.Vector(2, 3, 4)
        v2 = data.Vector(3, 4, 5)
        self.assertAlmostEqual(vector_math.dot_vector(v1, v2), 38)

    def test_dot_vector_again(self):
        v1 = data.Vector(1.1, 2.2, 3.3)
        v2 = data.Vector(4, 5, 7)
        self.assertAlmostEqual(vector_math.dot_vector(v1, v2), 38.5)

    def test_length_vector(self):
        v = data.Vector(1, 0, 0)
        self.assertAlmostEqual(vector_math.length_vector(v), 1)

    def test_length_vector_again(self):
        v = data.Vector(1, 1, 1)
        self.assertAlmostEqual(vector_math.length_vector(v), math.sqrt(3))

    def test_normalize_vector(self):
        v = data.Vector(1, math.sqrt(2), 1)
        self.assertTrue(data.Vector.__eq__(vector_math.normalize_vector(v),
                                           data.Vector(0.5, math.sqrt(2) / 2, 0.5)))

    def test_normalize_vector_again(self):
        v = data.Vector(1, 0, 0)
        self.assertTrue(data.Vector.__eq__(vector_math.normalize_vector(v),
                                           data.Vector(1, 0, 0)))

    def test_difference_point(self):
        pt1 = data.Point(1, 1, 1)
        pt2 = data.Point(0, 0, 0)
        self.assertTrue(data.Vector.__eq__(vector_math.difference_point(pt1, pt2), data.Vector(1, 1, 1)))

    def test_difference_point_again(self):
        pt1 = data.Point(5, 6, 7)
        pt2 = data.Point(1, 1, 1)
        self.assertTrue(data.Vector.__eq__(vector_math.difference_point(pt1, pt2), data.Vector(4, 5, 6)))

    def test_difference_vector(self):
        v1 = data.Vector(4, 5, 6)
        v2 = data.Vector(1, 2, 3)
        self.assertTrue(data.Vector.__eq__(vector_math.difference_vector(v1, v2),
                                           data.Vector(3, 3, 3)))

    def test_difference_vector_again(self):
        v1 = data.Vector(7, 8, 9)
        v2 = data.Vector(3, 2, 1)
        self.assertTrue(data.Vector.__eq__(vector_math.difference_vector(v1, v2),
                                           data.Vector(4, 6, 8)))

    def test_translate_point(self):
        p = data.Point(1, 1, 1)
        v = data.Vector(0, 0, 0)
        self.assertTrue(data.Point.__eq__(vector_math.translate_point(p, v),
                                          data.Point(1, 1, 1)))

    def test_translate_point_again(self):
        p = data.Point(1, 1, 1)
        v = data.Vector(1, 1, 1)
        self.assertTrue(data.Point.__eq__(vector_math.translate_point(p, v),
                                          data.Point(2, 2, 2)))

    def test_vector_from_to(self):
        p1 = data.Point(1, 1, 1)
        p2 = data.Point(2, 2, 2)
        self.assertTrue(data.Vector.__eq__(vector_math.vector_from_to(p1, p2),
                                           data.Vector(1, 1, 1)))

    def test_vector_from_to_again(self):
        p1 = data.Point(0, 0, 0)
        p2 = data.Point(3, 4, 5)
        self.assertTrue(data.Vector.__eq__(vector_math.vector_from_to(p1, p2), data.Vector(3, 4, 5)))

############################ COLLISIONS #########################################

    def test_sphere_intersection_point(self):
        sphere = data.Sphere(data.Point(3, 0, 0), 1, data.Color(50, 60, 70), data.Finish(6, 2, 1, 3))
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(1, 0, 0))
        self.assertTrue(collisions.sphere_intersection_point(ray, sphere) == data.Point(2, 0, 0))

    def test_sphere_intersection_point_again(self):
        sphere = data.Sphere(data.Point(3, 4, 0), 5, data.Color(50, 60, 70), data.Finish(6, 2, 1, 3))
        ray = data.Ray(data.Point(-6, -7, 5), data.Vector(9, 11, 0))
        self.assertTrue(collisions.sphere_intersection_point(ray, sphere) == data.Point(3, 4, 5))

    def test_sphere_intersection_point_3(self):
        sphere = data.Sphere(data.Point(5, 12, 0), 13, data.Color(50, 60, 70), data.Finish(6, 2, 1, 3))
        ray = data.Ray(data.Point(-5, -12, -13), data.Vector(5, 12, 13))
        self.assertTrue(collisions.sphere_intersection_point(ray, sphere) == data.Point(0, 0, 0))

    def test_sphere_intersection_point_4(self):
        sphere = data.Sphere(data.Point(0, 0, 0), 10, data.Color(50, 60, 70), data.Finish(6, 2, 1, 3))
        ray = data.Ray(data.Point(2, 2, 2), data.Vector(0, 12, 4))
        #self.assertTrue(collisions.sphere_intersection_point(ray, sphere) == data.Point(2, ))

    def test_sphere_intersection_point_5(self):
        sphere = data.Sphere(data.Point(1, 2, 3), 1, data.Color(50, 60, 70), data.Finish(6, 2, 1, 3))
        ray = data.Ray(data.Point(7, 0, 0), data.Vector(1, 0, 0))
        self.assertTrue(collisions.sphere_intersection_point(ray, sphere) == None)

    def test_sphere_intersection_point_6(self):
        sphere = data.Sphere(data.Point(5, 6, 7), 3, data.Color(50, 60, 70), data.Finish(6, 2, 1, 3))
        ray = data.Ray(data.Point(1, 1, 1), data.Vector(-2, -2, -2))
        self.assertTrue(collisions.sphere_intersection_point(ray, sphere) == None)

    def test_sphere_normal_at_point(self):
        sphere = data.Sphere(data.Point(1, 2, 3), 4, data.Color(50, 60, 70), data.Finish(6, 2, 1, 3))
        pt = data.Point(1, 2, 7)
        self.assertTrue(collisions.sphere_normal_at_point(sphere, pt) == data.Vector(0, 0, 1))

    def test_sphere_normal_at_point2(self):
        sphere = data.Sphere(data.Point(3, 4, 0), 5, data.Color(50, 60, 70), data.Finish(6, 2, 1, 3))
        pt = data.Point(3, 4, 5)
        self.assertTrue(collisions.sphere_normal_at_point(sphere, pt) == data.Vector(0, 0, 1))

    def test_color_covert(self):
        myColor = data.Color(0, 0, 1)
        newColor = data.Color(0, 0, 255)
        self.assertAlmostEqual(newColor.r, utility.convert_color(myColor).r)
        self.assertAlmostEqual(newColor.g, utility.convert_color(myColor).g)
        self.assertAlmostEqual(newColor.b, utility.convert_color(myColor).b)

    def test_color_covert_again(self):
        myColor = data.Color(0, 1, 0.5)
        newColor = data.Color(0, 255, 127.5)
        self.assertAlmostEqual(newColor.r, utility.convert_color(myColor).r)
        self.assertAlmostEqual(newColor.g, utility.convert_color(myColor).g)
        self.assertAlmostEqual(newColor.b, utility.convert_color(myColor).b)

    def test_color_covert_3(self):
        myColor = data.Color(0.8, 1, 0.5)
        newColor = data.Color(204, 255, 127.5)
        self.assertAlmostEqual(newColor.r, utility.convert_color(myColor).r)
        self.assertAlmostEqual(newColor.g, utility.convert_color(myColor).g)
        self.assertAlmostEqual(newColor.b, utility.convert_color(myColor).b)

    def test_cast_ray(self):
        myColor = cast.cast_ray(data.Ray(data.Point(-3, -3, 5), data.Vector(-1, -1, 7)),
                                [data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0, 0, 1), data.Finish(6, 2, 1, 3)),
                                 data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1, 0, 0), data.Finish(6, 4, 1, 1))],
                                data.Color(1, 1, 1), data.Light(data.Point(1, 2, 3), data.Color(1, 1 , 1)), data.Point(3, 2, 1))
        self.assertTrue(myColor == data.Color(1, 1, 1))

    def test_cast_ray_again(self):
        myColor = cast.cast_ray(data.Ray(data.Point(-5, 0, 0), data.Vector(1, 0, 0)),
                                [data.Sphere(data.Point(0, 0, 0), math.sqrt(3), data.Color(0, 0, 1), data.Finish(6, 2, 1, 3)),
                                 data.Sphere(data.Point(10, 7, 6), 0.5, data.Color(1, 0, 0), data.Finish(6, 4, 1, 1))],
                                data.Color(1, 1, 1), data.Light(data.Point(1, 2, 3), data.Color(1, 1 , 1)), data.Point(3, 2, 1))
        self.assertAlmostEqual(myColor.r, 1)
        self.assertAlmostEqual(myColor.g, 1)
        self.assertAlmostEqual(myColor.b, 7)

    def test_color_mult(self):
        color1 = data.Color(1, 2, 3)
        color2 = data.Color(1, 2, 3)
        myColor = utility.color_mult(color1, color2)
        self.assertAlmostEqual(myColor.r, 1)
        self.assertAlmostEqual(myColor.g, 4)
        self.assertAlmostEqual(myColor.b, 9)

    def test_color_mult_again(self):
        color1 = data.Color(3, 2, 1)
        color2 = data.Color(1, 2, 3)
        myColor = utility.color_mult(color1, color2)
        self.assertAlmostEqual(myColor.r, 3)
        self.assertAlmostEqual(myColor.g, 4)
        self.assertAlmostEqual(myColor.b, 3)

    def test_color_add(self):
        color1 = data.Color(1, 1, 1)
        color2 = data.Color(2, 3, 4)
        myColor = utility.color_add(color1, color2)
        self.assertAlmostEqual(myColor.r, 3)
        self.assertAlmostEqual(myColor.g, 4)
        self.assertAlmostEqual(myColor.b, 5)


    def test_color_add_again(self):
        color1 = data.Color(1, 1, 1)
        color2 = data.Color(6, 1, 4)
        myColor = utility.color_add(color1, color2)
        self.assertAlmostEqual(myColor.r, 7)
        self.assertAlmostEqual(myColor.g, 2)
        self.assertAlmostEqual(myColor.b, 5)

    def test_color_scale(self):
        color = data.Color(1, 2, 3)
        scalar = 3
        myColor = utility.color_scale(color, scalar)
        self.assertAlmostEqual(myColor.r, 3)
        self.assertAlmostEqual(myColor.g, 6)
        self.assertAlmostEqual(myColor.b, 9)

    def test_color_scale_again(self):
        color = data.Color(4, 5, 6)
        scalar = 2
        myColor = utility.color_scale(color, scalar)
        self.assertAlmostEqual(myColor.r, 8)
        self.assertAlmostEqual(myColor.g, 10)
        self.assertAlmostEqual(myColor.b, 12)

if __name__ == '__main__':
   unittest.main()
