import unittest
import data
import vector_math
import math
import collisions
import cast


#_____________________________________________________________
#HW 1 TESTS BY CHECKING EACH #
#____________________________________________________________



class assignment1tests (unittest.TestCase):
   def test_Point1(self):
      point1 = data.Point(1,2,3)
      self.assertEqual (point1.x,1)
      self.assertEqual (point1.y,2)
      self.assertEqual (point1.z,3)
   def test_Point2(self):
      point2 = data.Point(4,5,6)
      self.assertEqual (point2.x,4)
      self.assertEqual (point2.y,5)
      self.assertEqual (point2.z,6)

   def test_vector1(self):
      vector1 = data.Vector (1,2,3)
      self.assertEqual (vector1.x,1)
      self.assertEqual (vector1.y,2)
      self.assertEqual (vector1.z,3)
   def test_vector2(self):
      vector2 = data.Vector (4,5,6)
      self.assertEqual (vector2.x,4)
      self.assertEqual (vector2.y,5)
      self.assertEqual (vector2.z,6)

   def test_Ray1(self):
      ray1 = data.Ray (data.Point(1,2,3),data.Vector(3,4,5))
      self.assertEqual (ray1.pt.x,1)
      self.assertEqual (ray1.pt.y,2)
      self.assertEqual (ray1.pt.z,3)
      self.assertEqual (ray1.dir.x,3)
      self.assertEqual (ray1.dir.y,4)
      self.assertEqual (ray1.dir.z,5)
   def test_Ray2(self):
      ray2 = data.Ray (data.Point(6,7,8),data.Vector(9,1,2))
      self.assertEqual (ray2.pt.x,6)
      self.assertEqual (ray2.pt.y,7)
      self.assertEqual (ray2.pt.z,8)
      self.assertEqual (ray2.dir.x,9)
      self.assertEqual (ray2.dir.y,1)
      self.assertEqual (ray2.dir.z,2)

   def test_Sphere1(self):
      sphere1 = data.Sphere (data.Point(1,2,3),4,data.Color(0,0,0),data.finish(1.0))
      self.assertEqual (sphere1.center.x,1)
      self.assertEqual (sphere1.center.y,2)
      self.assertEqual (sphere1.center.z,3)
      self.assertEqual (sphere1.radius,4)
   def test_Sphere2(self):
      sphere2 = data.Sphere (data.Point(5,6,7),8,data.Color(0,0,0),data.finish(1.0))
      self.assertEqual (sphere2.center.x,5)
      self.assertEqual (sphere2.center.y,6)
      self.assertEqual (sphere2.center.z,7)
      self.assertEqual (sphere2.radius,8)

#________________________________________________________________________
# __EQ__ EQUALITY TESTS
#_______________________________________________________________________

   def test_point3(self):
      pt = data.Point(1,2,3)
      pt1 = data.Point(1,2,3)
      self.assertEqual(pt,pt1)
   def test_point4(self):
      pt = data.Point(2,3,4)
      pt1 = data.Point(2,3,4)
      self.assertEqual(pt,pt1)

   def test_vector3(self):
      v = data.Vector(1,2,3)
      v1 = data.Vector(1,2,3)
      self.assertEqual(v,v1)
   def test_vector4(self):
      v = data.Vector(2,3,4)
      v1 = data.Vector(2,3,4)
      self.assertEqual(v,v1)

   def test_ray3(self):
      ray = data.Ray(data.Point(1,2,3),data.Vector(2,3,4))
      ray2 = data.Ray(data.Point(1,2,3),data.Vector(2,3,4))
      self.assertEqual(ray,ray2)
   def test_ray4(self):
      ray = data.Ray(data.Point(3,4,5),data.Vector(6,3,4))
      ray2 = data.Ray(data.Point(3,4,5),data.Vector(6,3,4))
      self.assertEqual(ray,ray2)

   def test_sphere3(self):
      sphere = data.Sphere(data.Point(1,2,3),5,data.Color(0,0,0),data.finish(1.0))
      sphere2 = data.Sphere(data.Point(1,2,3),5,data.Color(0,0,0),data.finish(1.0))
      self.assertEqual(sphere,sphere2)
   def test_sphere4(self):
      sphere = data.Sphere(data.Point(3,4,5),6,data.Color(0,0,0),data.finish(1.0))
      sphere2 = data.Sphere(data.Point(3,4,5),6,data.Color(0,0,0),data.finish(1.0))
      self.assertEqual(sphere,sphere2)


#__________________________________________________________________________
#FUNCTION TESTS
#_________________________________________________________________________

   def test_Scale_vector(self):
      vector = data.Vector(1,2,3)
      self.assertEqual (vector_math.scale_vector(vector,2),(data.Vector(2,4,6)))
   def test_Scale_vector2(self):
      vector = data.Vector(2,3,3)
      self.assertEqual (vector_math.scale_vector(vector,3),(data.Vector(6,9,9)))

   def test_dot_vector(self):
      vector1 = data.Vector(1,2,3)
      vector2 = data.Vector(4,5,6)
      self.assertEqual (vector_math.dot_vector(vector1,vector2),32)
   def test_dot_vector1(self):
      vector1 = data.Vector(7,8,9)
      vector2 = data.Vector(1,1,1)
      self.assertEqual (vector_math.dot_vector(vector1,vector2),24)
  
   def test_length_vector(self):
      vector = data.Vector(1,2,3)
      self.assertEqual (vector_math.length_vector(vector),math.sqrt(14))
   def test_length_vector2(self):
      vector = data.Vector(3,4,5)
      self.assertEqual (vector_math.length_vector(vector),math.sqrt(50))

   def test_normalize_vector(self):
      vector = data.Vector(1,2,3)
      mag = math.sqrt(1**2 + 2**2 + 3**2)
      self.assertEqual (vector_math.normalize_vector(vector),data.Vector(1/mag,2/mag,3/mag)) 
   def test_normalize_vector2(self):
      vector = data.Vector(3,4,5)
      mag = math.sqrt(3**2 + 4**2 + 5**2)
      self.assertEqual (vector_math.normalize_vector(vector),data.Vector(3/mag,4/mag,5/mag))

   def test_difference_point(self):
      point = data.Point(1,2,3)
      point2 = data.Point(3,4,5)
      self.assertEqual (vector_math.difference_point(point,point2),
                       (data.Point(-2,-2,-2)))
   def test_difference_point2(self):
      point = data.Point(4,5,6)
      point2 = data.Point(1,3,3)
      self.assertEqual (vector_math.difference_point(point,point2),
                       (data.Point(3,2,3)))

   def test_difference_vector(self):
      vector = data.Vector (1,2,3)
      vector2 = data.Vector (1,1,1)
      self.assertEqual (vector_math.difference_vector(vector,vector2),(data.Vector(0,1,2)))
   def test_difference_vector2(self):
      vector = data.Vector (2,3,3)
      vector2 = data.Vector (0,0,1)
      self.assertEqual (vector_math.difference_vector(vector,vector2),(data.Vector(2,3,2)))

   def test_translate_point(self):
      point = data.Point(1,1,1)
      vector= data.Vector (2,3,2)
      self.assertEqual (vector_math.translate_point(point,vector),(data.Point(3,4,3)))
   def test_translate_point2(self):
      point = data.Point(3,4,6)
      vector = data.Vector (2,2,1)
      self.assertEqual (vector_math.translate_point (point,vector),(data.Point(5,6,7)))

   def test_vector_from_to(self):
      from_point = data.Point(1,2,3)
      to_point = data.Point(4,5,6)
      self.assertEqual (vector_math.vector_from_to (from_point,to_point),(data.Vector(3,3,3)))
   def test_vector_from_to2(self):
      from_point = data.Point(1,1,1)
      to_point = data.Point(3,4,5)
      self.assertEqual (vector_math.vector_from_to (from_point,to_point),(data.Vector(2,3,4)))

#________________________________________________________________________
#   COLLISION TESTS
#_______________________________________________________________________

   def test_intersection_point(self):
       ray = data.Ray(data.Point(0,0,0),data.Vector(1,0,0))
       sphere = data.Sphere(data.Point(3,3,0),3,data.Color(0,0,0))
       int_pt = collisions.sphere_intersection_point(ray,sphere)
       check_pt = data.Point(3,0,0)
       self.assertEqual(int_pt,check_pt)
   def test_intersection_point2(self):
       ray = data.Ray(data.Point(1,1,1),data.Vector(-1,-1,-1))
       sphere = data.Sphere(data.Point(2,3,1),1,data.Color(0,0,0))
       int_pt = collisions.sphere_intersection_point(ray,sphere)
       check_pt = None
       self.assertEqual(int_pt,check_pt)
   def test_intersection_point3(self):
       ray = data.Ray(data.Point(0,1,0),data.Vector(0,1,0))
       sphere = data.Sphere(data.Point(0,0,0),3,data.Color(0,0,0))
       int_pt = collisions.sphere_intersection_point(ray,sphere)
       check_pt = data.Point(0,3,0)
       self.assertEqual(int_pt,check_pt)
   def test_intersection_point4(self):
       ray = data.Ray(data.Point(1,1,1),data.Vector(0,1,0))
       sphere = data.Sphere(data.Point(-10,-10,-10),1,data.Color(0,0,0))
       int_pt = collisions.sphere_intersection_point(ray,sphere)
       check_pt = None
       self.assertEqual(int_pt,check_pt)

   def test_find_intersection_points(self):
       S1 = data.Sphere(data.Point(2,2,0),2,data.Color(0,0,0),data.finish(1.0))
       S2 = data.Sphere(data.Point(6,0,0),1,data.Color(0,0,0),data.finish(1.0))
       S3 = data.Sphere(data.Point(-10,-10,-10),3,data.Color(0,0,0),data.finish(1.0))
       ray = data.Ray(data.Point(0,0,0),data.Vector(2,0,0))
       sphere_list = [S1,S2,S3]
       int_list = collisions.find_intersection_points(sphere_list,ray)
       check_list = [(S1,data.Point(2,0,0)),(S2,data.Point(5,0,0))]
       self.assertEqual(int_list,check_list)
   def test_find_intersection_points2(self):
       S1 = data.Sphere(data.Point(3,6,1),2,data.Color(0,0,0),data.finish(1.0))
       S2 = data.Sphere(data.Point(-10,-10,-10),1,data.Color(0,0,0),data.finish(1.0))
       S3 = data.Sphere(data.Point(-2,4,1),3,data.Color(0,0,0),data.finish(1.0))
       ray = data.Ray(data.Point(1,1,1),data.Vector(0,1,0))
       sphere_list = [S1,S2,S3]
       int_list = collisions.find_intersection_points(sphere_list,ray)
       check_list = [(S1,data.Point(1,6,1)),(S3,data.Point(1,4,1))]
       self.assertEqual(int_list,check_list)
  
   def test_sphere_normal_at_point(self):
       sphere = data.Sphere(data.Point(0,0,0),2,data.Color(0,0,0),data.finish(1.0))
       point = data.Point(0,2,0)
       int = collisions.sphere_normal_at_point(sphere,point)
       check = data.Vector(0,1,0)
       self.assertEqual(int,check)
      
   def test_sphere_normal_at_point2(self):
       sphere = data.Sphere(data.Point(1,1,1),3,data.Color(0,0,0),data.finish(1.0))
       point = data.Point(1,1,4)
       int = collisions.sphere_normal_at_point(sphere,point)
       check = data.Vector(0,0,1)
       self.assertEqual(int,check)
      
#____________________________________________________________________
#   RAY CASTING TESTS
#___________________________________________________________________

   def test_cast_ray1(self):
       S1 = data.Sphere(data.Point(3,6,1),2,data.Color(0,0,0),data.finish(1.0))
       S2 = data.Sphere(data.Point(-10,-10,-10),1,data.Color(0,0,0),data.finish(1.0))
       S3 = data.Sphere(data.Point(-2,4,1),3,data.Color(0,0,0),data.finish(1.0))
       sphere_list = [S1,S2,S3]
       ray = data.Ray(data.Point(1,1,1),data.Vector(0,1,0))
       fun_call = cast.cast_ray(ray,sphere_list)
       check = data.Color(0,0,0)
       self.assertEqual(fun_call,check)
   def test_cast_ray2(self):
       S1 = data.Sphere(data.Point(5,5,5),2,data.Color(0,0,0),data.finish(1.0))
       S2 = data.Sphere(data.Point(6,3,7),1,data.Color(0,0,0),data.finish(1.0))
       sphere_list = [S1,S2]
       ray = data.Ray(data.Point(0,0,0), data.Vector(-1,-1,-1))
       fun_call = cast.cast_ray(ray,sphere_list)
       check = data.Color(1,1,1)
       self.assertEqual(fun_call,check)

   def test_pix_list1(self):
      min = 0
      max = 5
      delta = 1
      self.assertEqual(cast.pix_list(min,max,delta), [0,1,2,3,4])


   def test_pix_list2(self):
      min = -10
      max = 10
      delta = 2
      self.assertEqual(cast.pix_list(min,max,delta), [-10,-8,-6,-4,-2,0,2,4,6,8])

      



if  __name__ == '__main__':
   unittest.main()


