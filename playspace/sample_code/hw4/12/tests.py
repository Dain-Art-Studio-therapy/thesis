import unittest
from data import *
import vector_math
from collisions import *
from cast import *

class TestCases(unittest.TestCase):

#    def test_castColor(self):
#        sph = Sphere(Point(0,0,10),10,Color(1.0,0,0))
#        sphList = [sph]
#        ray = Ray(Point(0,0,-10), Vector(0,0,100))
#       self.assertEqual(cast_ray(ray,sphList),Color(1.0,0,0))

#    def test_castColor1(self):
#        sph = Sphere(Point(0,0,10),10,Color(1.0,1.0,0.999999))
#        sphList = [sph]
#        ray = Ray(Point(0,0,-10),Vector(0,0,100))
#        self.assertEqual(cast_ray(ray,sphList),Color(1.0,1.0,1.0))

    def test_cap(self):
        color = Color(255,256,1)
        self.assertEqual(capColor(color),Color(255,255,1))
    def test_cap1(self):
        color = Color(1,22,33)
        self.assertEqual(capColor(color),Color(1,22,33))

##DIDNT HAVE ENOUGH TIME... PLEASE FORGIVE ME FOR NEGLECTING THESE!
 
#run test
if __name__ == '__main__':
        unittest.main()

