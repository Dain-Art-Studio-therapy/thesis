import vector_math
import utility
import unittest
import data
import collisions

class TestData(unittest.TestCase):

   def test_point_1(self):
      point1 = data.Point(1,2,3)
      self.assertEqual(point1.x,1)
      self.assertEqual(point1.y,2)
      self.assertEqual(point1.z,3)
   def test_point_2(self):
      point2 = data.Point(6,5,4)
      self.assertEqual(point2.x,6)
      self.assertEqual(point2.y,5)
      self.assertEqual(point2.z,4)

   def test_vector_1(self):
      vector1 = data.Vector(1,2,3)
      self.assertEqual(vector1.x,1)
      self.assertEqual(vector1.y,2)
      self.assertEqual(vector1.z,3)
   def test_vector_2(self):
      vector2 = data.Vector(6,5,4)
      self.assertEqual(vector2.x,6) 
      self.assertEqual(vector2.y,5)
      self.assertEqual(vector2.z,4)

   def test_ray_1(self):
      point1 = data.Point(1,2,3)
      ray1 = data.Ray(point1,"right")
      self.assertEqual(ray1.pt.x,1)
      self.assertEqual(ray1.pt.y,2)
      self.assertEqual(ray1.pt.z,3)
      self.assertEqual(ray1.dir, "right")
   def test_ray_2(self):
      point2 = data.Point(6,5,4)
      ray2 = data.Ray(point2,"left")
      self.assertEqual(ray2.pt.x,6)
      self.assertEqual(ray2.pt.y,5)
      self.assertEqual(ray2.pt.z,4)
      self.assertEqual(ray2.dir, "left")

   def test_sphere_1(self):
      point1 = data.Point(1,2,3)
      sphere1 = data.Sphere(point1, 3.14)
      self.assertEqual(sphere1.center.x,1)
      self.assertEqual(sphere1.center.y,2)
      self.assertEqual(sphere1.center.z,3)
      self.assertEqual(sphere1.radius,3.14)
   def test_sphere_2(self):
      point2 = data.Point(6,5,4)
      sphere2 = data.Sphere(point2, 8.577)
      self.assertEqual(sphere2.center.x,6)
      self.assertEqual(sphere2.center.y,5)
      self.assertEqual(sphere2.center.z,4)
      self.assertEqual(sphere2.radius,8.577)


   def test_point_eq_1(self):
      point1 = data.Point(6,5,4)
      point2 = data.Point(6,5,4)
      self.assertEqual(data.Point.__eq__(point1, point2), True)
   def test_point_eq_2(self):
      point1 = data.Point(6,5,4)
      point2 = data.Point(4,5,7)
      self.assertEqual(data.Point.__eq__(point1, point2), False)

   def test_vector_eq_1(self):
      vector1 = data.Vector(6,5,4)
      vector2 = data.Vector(6,5,4)
      self.assertEqual(data.Vector.__eq__(vector1, vector2), True)
   def test_vector_eq_2(self):
      vector1 = data.Vector(6,5,4)
      vector2 = data.Vector(5,6,7)
      self.assertEqual(data.Vector.__eq__(vector1, vector2), False)

   def test_ray_eq_1(self):
      point1 = data.Point(6,5,4)
      point2 = data.Point(6,5,4)
      vector1 = data.Vector(1,2,3)
      vector2 = data.Vector(1,2,3)
      ray1 = data.Ray(point1, vector1)
      ray2 = data.Ray(point2, vector2)
      self.assertEqual(data.Ray.__eq__(ray1, ray2), True)
   def test_ray_eq_2(self):
      point1 = data.Point(4,5,6)
      point2 = data.Point(6,5,4)
      vector1 = data.Vector(3,2,1)
      vector2 = data.Vector(1,2,3)
      ray1 = data.Ray(point1, vector1)
      ray2 = data.Ray(point2, vector2)
      self.assertEqual(data.Ray.__eq__(ray1, ray2), False)

   def test_sphere_eq_1(self):
      point1 = data.Point(6,5,4)
      point2 = data.Point(6,5,4)
      sphere1 = data.Sphere(point1, 3)
      sphere2 = data.Sphere(point2, 3)
      self.assertEqual(data.Sphere.__eq__(sphere1, sphere2), True)
   def test_sphere_eq_2(self):  
      point1 = data.Point(4,5,6)
      point2 = data.Point(6,5,4)  
      sphere1 = data.Sphere(point1, 2)      
      sphere2 = data.Sphere(point2, 3)       
      self.assertEqual(data.Sphere.__eq__(sphere1, sphere2), False)

   def test_scale_1(self):
      vector1 = data.Vector(1,2,3)
      vector2 = data.Vector(2,4,6)
      self.assertEqual(vector_math.scale_vector(vector1,2) , vector2)
   def test_scale_2(self):
      vector1 = data.Vector(4,1,3)
      vector2 = data.Vector(12,3,9)
      self.assertEqual(vector_math.scale_vector(vector1,3) , vector2)

   def test_dot_product_1(self):
      vector1 = data.Vector(1,2,3)
      vector2 = data.Vector(3,2,1)
      self.assertEqual(vector_math.dot_vector(vector1, vector2) , 10)
   def test_dot_product_test_2(self):
      vector1 = data.Vector(2,4,5)
      vector2 = data.Vector(3,4,5)
      self.assertEqual(vector_math.dot_vector(vector1, vector2) , 47)

   def test_length_1(self):
      vector = data.Vector(1,2,2)
      vector_math.length_vector(vector) == 3
   def test_length_2(self):
      vector = data.Vector(2,3,6)
      vector_math.length_vector(vector) == 7

   def test_normalize_1(self):
      vector1 = data.Vector(2,0,0)
      vector2 = data.Vector(1,0,0)
      vector_math.normalize_vector(vector1) == vector2
   def test_normalize_2(self):
      vector1 = data.Vector(0,3,0)
      vector2 = data.Vector(0,1,0)
      vector_math.normalize_vector(vector1) == vector2

   def test_difference_point_1(self):
      point1 = data.Point(1,2,3)
      point2 = data.Point(3,4,5)
      vector = data.Vector(2,2,2)
      vector_math.difference_vector(point1, point2) == vector
   def test_difference_point_2(self):
      point1 = data.Point(5,2,4)
      point2 = data.Point(3,4,5)
      vector = data.Vector(-2,2,-1)
      vector_math.difference_vector(point1, point2) == vector

   def test_difference_vector_1(self):
      vector1 = data.Vector(1,2,3)
      vector2 = data.Vector(3,4,5)
      vector3 = data.Vector(2,2,2)
      vector_math.difference_vector(vector1, vector2) == vector3
   def test_difference_vector_2(self):   
      vector1 = data.Vector(5,2,4)   
      vector2 = data.Vector(3,4,5)   
      vector3 = data.Vector(-2,2,-1)     
      vector_math.difference_vector(vector1, vector2) == vector3
     
   def test_translate_1(self):
      point1 = data.Point(1,2,3)
      vector = data.Vector(3,3,3)
      point2 = data.Point(4,5,6)
      vector_math.translate_point(point1,vector) == point2
   def test_translate_2(self):       
      point1 = data.Point(3,4,1)
      vector = data.Vector(2,2,2)     
      point2 = data.Point(5,6,3)      
      vector_math.translate_point(point1,vector) == point2         

   def test_vector_from_to_1(self):
      point1 = data.Point(0,0,0)
      point2 = data.Point(1,4,3)
      vector = data.Vector(1,4,3)
      vector_math.vector_from_to(point1,point2) == vector
   def test_vector_from_to_2(self):
      point1 = data.Point(2,5,1)   
      point2 = data.Point(5,1,5)
      vector = data.Vector(3,-4,4)
      vector_math.vector_from_to(point1,point2) == vector

   def test_sphere_intersection_point_1(self):
      point1 = data.Point(0,0,0)
      vector = data.Vector(0,0,4)
      ray = data.Ray(point1, vector)
      point2= data.Point(0,0,0)
      sphere = data.Sphere(point2, 3,123)
      point3= data.Point(0,0,3)
      self.assertEqual(collisions.sphere_intersection_point(ray,sphere),point3)

   def test_sphere_intersection_point_2(self):
      point1 = data.Point(0,0,0)
      vector = data.Vector(4,0,0)
      ray = data.Ray(point1, vector)
      point2= data.Point(0,0,0)
      sphere = data.Sphere(point2, 3,123)
      point3= data.Point(3,0,0)
      self.assertEqual(collisions.sphere_intersection_point(ray,sphere), point3)

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)       

   def test_sphere_normal_at_point_1(self):   
      point1 = data.Point(0,0,10) 
      point2= data.Point(0,0,0)    
      sphere1 = data.Sphere(point2, 5)
      vector1 = data.Vector(0,0,1)
      vector2 = collisions.sphere_normal_at_point(sphere1, point1)
      self.assertEqual(vector1, vector2)

   def test_sphere_normal_at_point_2(self):
      point1 = data.Point(3,4,0)        
      point2= data.Point(0,0,0)   
      sphere1 = data.Sphere(point2,10)   
      vector1 = data.Vector(.6,.8,0)
      vector2 = collisions.sphere_normal_at_point(sphere1, point1)
      self.assertEqual(vector1, vector2)      

   def test_cast_ray_1(self):
      point1 = data.Point(0,0,0)
      vector = data.Vector(0,0,5)
      ray = data.Ray(point1, vector)
      point2= data.Point(0,0,0)
      sphere1 = data.Sphere(point2, 3)
      point3= data.Point(1,0,0)
      sphere2 = data.Sphere(point3, 4)
      spherelist = [sphere1,sphere2]
      self.assertEqual(cast.cast_ray(ray,spherelist), True)

   def test_cast_ray_2(self):
      point1 = data.Point(100,100,100)
      vector = data.Vector(0,0,.5)
      ray = data.Ray(point1, vector)
      point2= data.Point(0,0,0)
      sphere1 = data.Sphere(point2, 5)
      point3= data.Point(1,0,0)
      sphere2 = data.Sphere(point3, 6)
      spherelist = [sphere1,sphere2]
      self.assertEqual(cast.cast_ray(ray,spherelist), False)

   def test_distance_1(self):
      point1 = data.Point(0,0,0)
      point2 = data.Point(5,0,0)
      point3 = data.Point(0,4,0)
      sphere1 = data.Sphere(1,point2)
      sphere2 = data.Sphere(2,point3)
      sphere_list = [sphere1,sphere2]      

if __name__ == "__main__":
     unittest.main()




