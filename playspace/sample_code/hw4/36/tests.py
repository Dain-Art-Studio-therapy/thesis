import unittest 
import data
import collisions
import cast
class TestCases(unittest.TestCase):

  
    def test_castray1(self):
       p1=data.Point(-3,2,0)
       v=data.Vector(10,0,0)
       r=data.Ray(p1,v)
       
       color1=data.Color(1.0,0.0,0.0)
       p2=data.Point(0,2,0)
       sp1=data.Sphere(p2,2,color1)
       
       color2=data.Color(0.0,1.0,0.0)
       p3=data.Point(5,2,0)
       sp2=data.Sphere(p3,1,color2)
       
       color3=data.Color(0.0,0.0,1.0)
       p4=data.Point(3,2,0)
       sp3=data.Sphere(p4,1,color3)
       
       spList= [sp3,sp2,sp1]
       testColor=data.Color(1.0,0.0,0.0)
       self.assertEqual(cast.cast_ray(r,spList),testColor)


    def test_castray2(self):
       p1=data.Point(1,1,1)
       v=data.Vector(0,8,0)
       r=data.Ray(p1,v)

       p2=data.Point(1,5,1)
       color1=data.Color(0.0,1.0,0.0)
       sp1=data.Sphere(p2,1,color1)
      

       p3=data.Point(1,8,1)
       color2=data.Color(0.0,0.0,1.0)
       sp2=data.Sphere(p3,1,color2)

       p4=data.Point(-9,-9,-10)
       color3=data.Color(1.0,1.0,1.0)
       sp3=data.Sphere(p4,1,color3)
    
       spList= [sp2,sp1,sp3]
       testColor=data.Color(0.0,1.0,0.0)
      
       self.assertEqual(cast.cast_ray(r,spList),testColor)





if __name__ == '__main__':     
   unittest.main()
