import unittest
import data
import vector_math
import collisions
import cast

class DataTests(unittest.TestCase):
    def test_spec_intense(self):
        L_dir = data.Vector(1,0,0)
        dotter = 1
        N = data.Vector(0,1,0)
        eye_point = data.Point(0,1,0)
        Pe = data.Point(1,1,0)
        self.assertEqual(cast.spec_intense(L_dir,dotter,N,eye_point,Pe), True)

    def test_spec_intense_1(self):
        L_dir = data.Vector(1,0,0)
        dotter = 1
        N = data.Vector(0,1,0)
        eye_point = data.Point(1,1,0)
        Pe = data.Point(2,1,0)
        self.assertEqual(cast.spec_intense(L_dir,dotter,N,eye_point,Pe), True)

    def test_path(self):
        Pe = data.Point(1,1,0)
        L_dir = data.Vector(1,0,0)
        ray = data.Ray(Pe,L_dir)
        sphere_list = []
        the_light = data.Light(data.Point(50,1,0), data.Color(0,0,0))
        self.assertEqual(cast.in_its_path(ray,sphere_list
                         ,Pe,L_dir,the_light), False)

    def test_path_1(self):
        Pe = data.Point(2,1,0)
        L_dir = data.Vector(1,0,0)
        ray = data.Ray(Pe, L_dir)
        sphere_list = [data.Sphere(data.Point(10000,100001
                                   ,12932),1,data.Color(0
                                   ,0,0), data.Finish(.1,.2,.3,.4))]
        Pe = data.Point(2,1,0)
        L_dir = data.Vector(1,0,0)
        the_light = data.Light(data.Point(50,1,0), data.Color(0,0,0))
        self.assertEqual(cast.in_its_path(ray,sphere_list
                                          ,Pe,L_dir,the_light), False)
    def test_cast_ray_1(self):
        ray = data.Ray(data.Point(0,0,0), data.Vector(5,5,5))
        sphere_list = [data.Sphere(data.Point(4
                                   ,4,4),1, data.Color(.5
                                   ,.5,.5), data.Finish(.1,.1,.1,.1))]
        color = data.Color(1,1,1)
        the_light = data.Light(data.Point(50,50,50), data.Color(0,0,0))
        eye_point = data.Point(0,0,0)
        self.assertEqual(cast.cast_ray(ray,sphere_list
                                       ,color,the_light,eye_point),data.Color(
                                        .05,.05,.05))

    def test_cast_ray_2(self):
        ray = data.Ray(data.Point(0,0,0), data.Vector(5,5,0))
        sphere_list = [data.Sphere(data.Point(3
                                   ,3,0),1, data.Color(.2
                                   ,.7,.8), data.Finish(.9,.6,.2,.4))]
        color = data.Color(.8,.6,1)
        the_light = data.Light(data.Point(31,23,12), data.Color(1,.7,1))
        eye_point = data.Point(0,0,0)
        self.assertEqual(cast.cast_ray(ray,sphere_list
                                       ,color,the_light,eye_point), data.Color(
                                           .144,.378,.720))
        

                             



                              
    



if __name__ == '__main__':
   unittest.main()
