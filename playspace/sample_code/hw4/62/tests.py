import unittest
import data
import utility
import vector_math
import collisions


class TestData(unittest.TestCase):


   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

         
#HW1
   def test_point_1(self): 
      point = data.Point(4,5,6)
      self.assertEqual(point.x, 4) 
      self.assertEqual(point.y, 5) 
      self.assertEqual(point.z, 6)
      
   def test_point_2(self): 
      point = data.Point(8.5, 4.2, 88)
      self.assertEqual(point.x, 8.5) 
      self.assertEqual(point.y, 4.2) 
      self.assertEqual(point.z, 88)



   def test_vector_1(self): 
      vec = data.Vector(7,4,5)
      self.assertEqual(vec.x, 7)
      self.assertEqual(vec.y, 4)
      self.assertEqual(vec.z, 5)
      
   def test_vector_2(self): 
      vec = data.Vector(8.2,4.6,2.2)
      self.assertEqual(vec.x, 8.2)
      self.assertEqual(vec.y, 4.6)
      self.assertEqual(vec.z, 2.2)
      
      
      
   def test_ray_1(self): 
      point = data.Point(1,2,3)
      vec = data.Vector(2,3,4)
      ray = data.Ray(point, vec)
      self.assertEqual(point.x, 1) 
      self.assertEqual(point.y, 2) 
      self.assertEqual(point.z, 3) 
      self.assertEqual(vec.x, 2) 
      self.assertEqual(vec.y, 3) 
      self.assertEqual(vec.z, 4) 
      
   def test_ray_2(self): 
      point = data.Point(1.0, 2.2, 3.2)
      vec = data.Vector(8,12,14)
      ray = data.Ray(point, vec)
      self.assertEqual(point.x, 1.0) 
      self.assertEqual(point.y, 2.2) 
      self.assertEqual(point.z, 3.2) 
      self.assertEqual(vec.x, 8) 
      self.assertEqual(vec.y, 12) 
      self.assertEqual(vec.z, 14)
      
      
   
   def test_sphere_1(self): 
      cent = data.Point(1,2,3)
      rad = 12
      color = data.Color(0,0,0)
      finish = data.Finsih(.5)
      circle = data.Sphere(cent, rad, color, finish)
      self.assertEqual(cent.x, 1) 
      self.assertEqual(cent.y, 2) 
      self.assertEqual(cent.z, 3)
      self.assertEqual(rad, 12) 
      self.assertEqual(color.r, 0)
      self.assertEqual(color.g, 0)
      self.assertEqual(color.b, 0)
      self.assertEqual(finish, .5)
      
   def test_sphere_2(self): 
      cent = data.Point(4.0,2.5,6.8)
      rad = 55
      color = data.Color(1,1,1)
      finsih = data.Finsih(5)
      circle = data.Sphere(cent, rad, color)
      self.assertEqual(cent.x, 4.0) 
      self.assertEqual(cent.y, 2.5) 
      self.assertEqual(cent.z, 6.8)
      self.assertEqual(rad, 55)
      self.assertEqual(color.r, 1)
      self.assertEqual(color.g, 1)
      self.assertEqual(color.b, 1)
      self.assertEqual(finish, 5)
     

     
     
     
#HW2
   
   #data pt2
   
   def test_eqal_point(self): 
      point = data.Point(2,3,7)
      self.assertEqual(point, data.Point(2,3,7))
      
   
   def test_eqal_vector(self): 
      vec = data.Vector(8,5,6)
      self.assertEqual(vec, data.Vector(8,5,6))
      
      
   def test_eqal_ray(self): 
      ray = data.Ray(data.Point(2,5,8), data.Vector(5,4,7))
      self.assertEqual(ray, data.Ray(data.Point(2,5,8), data.Vector(5,4,7)))

   
   def test_eqal_sphere(self): 
      sphere = data.Sphere(data.Point(2,5,6), 45, data.Color(0,1,0))
      self.assertEqual(sphere, data.Sphere(data.Point(2,5,6), 45, data.Color(0,1,0)))
      
      
   #Vector_math 

   def test_scale_vector_1(self): 
      vector = data.Vector(2,4,5)
      scalar = 2
      scaled = vector_math.scale_vector(vector, scalar)
      self.assertEqual(scaled, data.Vector(4,8,10))
      
   def test_scale_vector_2(self):
      vector = data.Vector(4.0,2.2,3.5)
      scalar = 0.5
      scaled = vector_math.scale_vector(vector, scalar)
      self.assertEqual(scaled, data.Vector(2.0, 1.1, 1.75))
      
      
   def test_dot_vector_1(self): 
      vec1 = data.Vector(1,2,2)
      vec2 = data.Vector(2,4,1)
      dot = vector_math.dot_vector(vec1, vec2)
      self.assertEqual(dot, 12)
      
   def test_dot_vector_2(self): 
      vec1 = data.Vector(2.0,2.1,1)
      vec2 = data.Vector(1,2,3)
      dot = vector_math.dot_vector(vec1, vec2)
      self.assertAlmostEqual(dot, 9.2 )
      
      
   def test_length_vector_1(self): 
      len = vector_math.length_vector(data.Vector(2,3,6))
      self.assertEqual(len, 7)
      
   def test_length_vector_2(self): 
      len = vector_math.length_vector(data.Vector(10,11,2))
      self.assertEqual(len, 15)
      
      
   def test_normalize_vector_1(self): 
      norm = vector_math.normalize_vector(data.Vector(2,3,6))
      self.assertEqual(norm, data.Vector(2.0/7, 3.0/7, 6.0/7))
      
   def test_normalize_vector_2(self): 
      norm = vector_math.normalize_vector(data.Vector(3,4,0))
      self.assertEqual(norm, data.Vector(.6, .8, 0))

   
   def test_difference_point_1(self): 
      pt1 = data.Point(7,8,9)
      pt2 = data.Point(4,5,6)
      dif = vector_math.difference_point(pt1, pt2)
      self.assertEqual(dif, data.Point(3,3,3))
   
   def test_difference_point_2(self): 
      pt1 = data.Point(5.73,7.8,3.6)
      pt2 = data.Point(2.35,1,0)
      dif = vector_math.difference_point(pt1, pt2)
      self.assertEqual(dif, data.Point(3.38, 6.8, 3.6))
      
      
   def test_difference_vector_1(self): 
      vec1 = data.Vector(7,3,5)
      vec2 = data.Vector(8,8,0)
      dif = vector_math.difference_vector(vec1, vec2)
      self.assertEqual(dif, data.Vector(-1, -5, 5))
      
   def test_difference_vector_2(self): 
      vec1 = data.Vector(4.8, 0.9, 3.1)
      vec2 = data.Vector(7, 0.1, 5.3)
      dif = vector_math.difference_vector(vec1, vec2)
      self.assertEqual(dif, data.Vector(-2.2, 0.8, -2.2))
      
      
   def test_translate_point_1(self): 
      pt = data.Point(5,3,8)
      vec = data.Vector(7,4,0)
      translate = vector_math.translate_point(pt, vec)
      self.assertEqual(translate, data.Point(12,7,8))
      
   def test_translate_point_2(self): 
      pt = data.Point(7.4, 8.0, 9.1)
      vec = data.Vector(8.6, 3.5, 5.3)
      translate = vector_math.translate_point(pt, vec)
      self.assertEqual(translate, data.Point(16.0, 11.5, 14.4))
      
      
   def test_vector_from_to_1(self): 
      topt = data.Point(9,2,0)
      frompt = data.Point(7,3,6)
      tofrom = vector_math.vector_from_to(frompt, topt)
      self.assertEqual(tofrom, data.Point(2, -1, -6))
      
   def test_vector_from_to_2(self): 
      topt = data.Point(3.5,5.4,3.0)
      frompt = data.Point(9.8,4.4,6.5)
      tofrom = vector_math.vector_from_to(frompt, topt)
      self.assertEqual(tofrom, data.Point(-6.3, 1.0, -3.5))      
      

 #HW 3

   #Collisions-----------


   def test_sphere_intersection_point_1(self): 
      ray = data.Ray(data.Point(-20,0,0), data.Vector(3,0,0))
      sphere = data.Sphere(data.Point(50,0,0), 25, data.Color(0,0,0), data.Finish(12))
      intersection = collisions.sphere_intersection_point(ray, sphere)
      self.assertEqual(intersection, data.Point(25,0,0))

   def test_sphere_intersection_point_2(self): 
      ray = data.Ray(data.Point(0,-60,0), data.Vector(0,10,0))
      sphere = data.Sphere(data.Point(0,70,0), 20, data.Color(1,1,1), data.Finish(1))
      intersection = collisions.sphere_intersection_point(ray, sphere)
      self.assertEqual(intersection, data.Point(0,50,0))

   

   def test_find_intersection_points_1(self): 
      sphere_list = [
      data.Sphere(data.Point(0,0,0), 10, data.Color(0,0,0), data.Finish(.2)), 
      data.Sphere(data.Point(0,0,20), 10, data.Color(1,1,1), data.Finish(12)) ] 
      ray = data.Ray(data.Point(0,0,-20), data.Vector(0,0,5))
      newlist = collisions.find_intersection_points(sphere_list, ray)
      self.assertAlmostEqual(newlist, 
      [(data.Sphere(data.Point(0,0,0), 10, data.Color(0,0,0)), data.Point(0,0,-10)), 
      (data.Sphere(data.Point(0,0,20), 10, data.Color(1,1,1)), data.Point(0,0,10))])
       
   def test_find_intersection_points_2(self): 
      sphere_list = [
      data.Sphere(data.Point(15,0,0), 5, data.Color(0,0,0), data.Finish(2)), 
      data.Sphere(data.Point(500,0,0), 100, data.Color(0,0,0),data.Finish(2)), 
      data.Sphere(data.Point(0,0,0), 5, data.Color(1,1,1),data.Finish(2)), 
      data.Sphere(data.Point(500,500,500), 10, data.Color(0,0,0), data.Finish(2)), 
      data.Sphere(data.Point(-5,0,0), 5, data.Color(1,1,1), data.Finish(2)) ] 
      ray = data.Ray(data.Point(-50,0,0), data.Vector(10,0,0))
      newlist = collisions.find_intersection_points(sphere_list, ray)
      self.assertAlmostEqual(newlist, 
      [(data.Sphere(data.Point(-5,0,0), 5, data.Color(1,1,1)), data.Point(-10,0,0), data.Finish(2)), 
       (data.Sphere(data.Point(0,0,0), 5, data.Color(1,1,1)), data.Point(-5,0,0), data.Finish(2)),
       (data.Sphere(data.Point(15,0,0), 5, data.Color(0,0,0)), data.Point(10,0,0), data.Finish(2)),
       (data.Sphere(data.Point(500,0,0), 100, data.Color(0,0,0)), data.Point(400,0,0), data.Finish(2)) ])
       
       
        
   def test_sphere_normal_at_point_1(self): 
      sphere = data.Sphere(data.Point(0,0,0), 10, data.Color(0,0,0), data.Finish(2))
      point = data.Point(-3, -4, 0)
      norm = collisions.sphere_normal_at_point(sphere, point)
      self.assertAlmostEqual(norm, data.Vector(3.0/5.0,4.0/5.0,0))     
       
   def test_sphere_normal_at_point(self):
   #center - point (to - from)
      sphere = data.Sphere(data.Point(2,3,6), 8, data.Color(1,1,1), data.Finish(2))
      point = data.Point(0,0,0)
      norm = collisions.sphere_normal_at_point(sphere, point)
      self.assertAlmostEqual(norm, data.Vector(-2.0/7.0, -3.0/7.0, -6.0/7.0))     



#HW4

   #Cast 
   
   #Data
   
   def test_color_1(self): 
      r = 1
      g = 1 
      b = 1 
      color = data.Color(r,g,b)
      self.assertEqual(color, data.Color(1,1,1))
      
   def test_color_2(self)
      r = 255
      g = 255
      b = 255 
      color = data.Color(r,g,b)
      self.assertEqual(color, data.Color(255,255,255))
   
   
   def test_finish_1(self): 
      finish = data.Finish(12)
      self.assertEqual(finish, data.Finish(12))
      
   def test_finish_2(self): 
      finish = data.Finish(.0006)
      self.assertEqual(finish, data.Finish(.0006))

   

   
       

if __name__ == "__main__":
     unittest.main()
