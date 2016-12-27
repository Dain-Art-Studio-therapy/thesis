# Contains test cases

import unittest
import data
import utility
import vector_math
import collisions
import cast

f = data.Finish(0,0,0,0)

class Tests(unittest.TestCase):

   

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def assertListEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertEqual(el1, el2)

   def test_point(self):
      pt1 = data.Point(0,1,2)
      self.assertEqual(pt1,data.Point(0,1,2))
   def test_point_again(self):
      pt2 = data.Point(-3,4.5,72)
      self.assertEqual(pt2,data.Point(-3,4.5,72))

   def test_vector(self):
      v1 = data.Vector(1,3,6)
      self.assertEqual(v1,data.Vector(1,3,6))
   def test_vector_again(self):
      v2 = data.Vector(-2.1,9.88,0)
      self.assertEqual(v2,data.Vector(-2.1,9.88,0))

   def test_ray(self):
      r1 = data.Ray(data.Point(2,4,-5.1),data.Vector(1.2,-4,0))
      self.assertEqual(r1,data.Ray(data.Point(2,4,-5.1),data.Vector(1.2,-4,0)))
   def test_ray_again(self):
      r2 = data.Ray(data.Point(-2,9.2,1),data.Vector(49,-5.3,7.9))
      self.assertEqual(r2,data.Ray(data.Point(-2,9.2,1),data.Vector(49,-5.3,7.9)))

   def test_sphere(self):
      s1 = data.Sphere(data.Point(1.01,-5,0),30.3,data.Color(0,0,0),f)
      self.assertEqual(s1,data.Sphere(data.Point(1.01,-5,0),30.3,data.Color(0,0,0),f))
   def test_sphere_again(self):
      s2 = data.Sphere(data.Point(5.02,4,-3),2.1,data.Color(0,0,0),f)
      self.assertEqual(s2,data.Sphere(data.Point(5.02,4,-3),2.1,data.Color(0,0,0),f))

   def test_scale_vector(self):
      v = data.Vector(1,-.3,6.5)
      s = 5.5
      v1 = vector_math.scale_vector(v,s)
      self.assertEqual(v1,data.Vector(5.5,-1.65,35.75))
   def test_scale_vector_again(self):
      v = data.Vector(3.6,-4.5,-93.6)
      s = -.5
      v1 = vector_math.scale_vector(v,s)
      self.assertEqual(v1,data.Vector(-1.8,2.25,46.8))

   def test_dot_vector(self):
      v1 = data.Vector(3.5,-2.4,0)
      v2 = data.Vector(1.3,2,980.256)
      dv = vector_math.dot_vector(v1,v2)
      self.assertAlmostEqual(dv,-0.25)
   def test_dot_vector_again(self):
      v1 = data.Vector(5,7.2,-2)
      v2 = data.Vector(8.98,-5,-6.4)
      dv = vector_math.dot_vector(v1,v2)
      self.assertAlmostEqual(dv,21.7)

   def test_length_vector(self):
      v1 = data.Vector(3,4,0)
      length = vector_math.length_vector(v1)
      self.assertAlmostEqual(length,5)
   def test_length_vector_again(self):
      v1 = data.Vector(-2.5,4.76,21.1)
      length = vector_math.length_vector(v1)
      self.assertAlmostEqual(length,21.774241663)

   def test_normalize_vector(self):
      v1 = vector_math.normalize_vector(data.Vector(3,6,-2.1))
      v2 = data.Vector(0.4267896,0.8535792,-0.29875272)
      self.assertEqual(v1,v2)
   def test_normalize_vector_again(self):
      v1 = vector_math.normalize_vector(data.Vector(5.5,-6.3,1))
      v2 = data.Vector(0.653005888,-0.747988563,0.118728343)
      self.assertEqual(v1,v2)      
   
   def test_difference_point(self):
      v1 = vector_math.difference_point(data.Point(1,2,3),data.Point(4,5,6))
      v2 = data.Vector(-3,-3,-3)
      self.assertEqual(v1,v2)
   def test_difference_point_again(self):
      v1 = vector_math.difference_point(data.Point(2.5,-4.2,1),data.Point(4.5,2.1,-6.3))
      v2 = data.Vector(-2,-6.3,7.3)
      self.assertEqual(v1,v2)

   def test_difference_vector(self):
      v1 = vector_math.difference_vector(data.Vector(1,2,3),data.Vector(-2,4,-6))
      v2 = data.Vector(3,-2,9)
      self.assertEqual(v1,v2)
   def test_difference_vector_again(self):
      v1 = vector_math.difference_vector(data.Vector(-2.3,4.5,7.2),data.Vector(-3.6,-5.4,2.2))
      v2 = data.Vector(1.3,9.9,5)
      self.assertEqual(v1,v2)

   def test_translate_point(self):
      pt1 = vector_math.translate_point(data.Point(3.5,4.6,-5.5),data.Vector(2.1,-3.1,1.5))
      pt2 = data.Point(5.6,1.5,-4)
      self.assertEqual(pt1,pt2)
   def test_translate_point_again(self):
      pt1 = vector_math.translate_point(data.Point(1.2,4.6,-2.2),data.Vector(-1.1,-5.8,4.2))
      pt2 = data.Point(0.1,-1.2,2)
      self.assertEqual(pt1,pt2)
   
   def test_vector_from_to(self):
      v1 = vector_math.vector_from_to(data.Point(1.2,-4.5,8.1),data.Point(4.5,1.3,-6.5))
      v2 = data.Vector(3.3,5.8,-14.6)
      self.assertEqual(v1,v2)
   def test_vector_from_to_again(self):
      v1 = vector_math.vector_from_to(data.Point(5.4,1.2,-3.3),data.Point(-4.2,0.2,1.8))
      v2 = data.Vector(-9.6,-1,5.1)
      self.assertEqual(v1,v2)

   def test_quad_eqn(self):
      l = collisions.quad_eqn(3,-5,4)
      self.assertEqual(l, [None, None])
   def test_quad_eqn_again(self):
      l = collisions.quad_eqn(-.9375,3,-2.4)
      self.assertAlmostEqual(l[0], [1.6,None][0])
      self.assertEqual(l[1], [1.6,None][1])
   def test_quad_eqn_2(self):
      l = collisions.quad_eqn(6.5,2,-5.6)
      self.assertListAlmostEqual(l, [0.787008299,-1.094700606])

   def test_intersect_t(self):
      t = collisions.intersect_t(3,-5,4)
      self.assertEqual(t, None)
   def test_intersect_t_again(self):
      t = collisions.intersect_t(-.9375,3,-2.4)
      self.assertAlmostEqual(t,1.6)
   def test_intersect_t_2(self):
      t = collisions.intersect_t(6.5,2,-5.6)          
      self.assertAlmostEqual(t,0.787008299)

   def test_sphere_intersection_point(self):
      pt = collisions.sphere_intersection_point(data.Ray(data.Point(0,1,0),data.Vector(1,0,0)), data.Sphere(data.Point(5,0,0),1,data.Color(0,0,0),f))
      self.assertEqual(pt,data.Point(5,1,0))
      pass
   def test_sphere_intersection_point_again(self):
      pt = collisions.sphere_intersection_point(data.Ray(data.Point(0,0,0),data.Vector(5,2,0)), data.Sphere(data.Point(10,4,0),2.5,data.Color(0,0,0),f))
      self.assertEqual(pt,data.Point(7.67880827279,3.07152330911,0))
      pass
   def test_sphere_intersection_point_2(self):
      pt = collisions.sphere_intersection_point(data.Ray(data.Point(0,-1,0),data.Vector(1.5,1,2)), data.Sphere(data.Point(3,2,4),2,data.Color(0,0,0),f))
      self.assertEqual(pt,data.Point(2.2200628950859178,0.48004193005727869,2.9600838601145574))      
      pass

   def test_find_intersection_points(self):
      list_of_spheres = [data.Sphere(data.Point(5,0,0),1,data.Color(0,0,0),f), data.Sphere(data.Point(7,0,0),.7,data.Color(0,0,0),f), data.Sphere(data.Point(3,1,0),.3,data.Color(0,0,0),f)]
      ray0 = data.Ray(data.Point(0,1,0), data.Vector(1,0,0))
      list_of_pairs = collisions.find_intersection_points(list_of_spheres,ray0)
      self.assertListEqual(list_of_pairs, [(data.Sphere(data.Point(5,0,0),1,data.Color(0,0,0),f),data.Point(5,1,0)), (data.Sphere(data.Point(3,1,0),.3,data.Color(0,0,0),f),data.Point(2.7,1,0))])
   def test_find_intersection_points_again(self):      
      list_of_spheres = [data.Sphere(data.Point(0,5,0),2,data.Color(0,0,0),f), data.Sphere(data.Point(1,6,0),1,data.Color(0,0,0),f), data.Sphere(data.Point(0,7,1),1,data.Color(0,0,0),f)]
      ray0 = data.Ray(data.Point(0,0,0), data.Vector(0,1,0))
      list_of_pairs = collisions.find_intersection_points(list_of_spheres,ray0)
      self.assertListEqual(list_of_pairs, [(data.Sphere(data.Point(0,5,0),2,data.Color(0,0,0),f),data.Point(0,3,0)), (data.Sphere(data.Point(1,6,0),1,data.Color(0,0,0),f),data.Point(0,6,0)), (data.Sphere(data.Point(0,7,1),1,data.Color(0,0,0),f),data.Point(0,7,0)),])      
      pass

   def test_sphere_normal_at_point(self):
      v0 = collisions.sphere_normal_at_point(data.Sphere(data.Point(1,5,4),2,data.Color(0,0,0),f),data.Point(3,5,4))
      self.assertEqual(v0, data.Vector(1,0,0))
      pass
   def test_sphere_normal_at_point_again(self):
      v0 = collisions.sphere_normal_at_point(data.Sphere(data.Point(1,1,1),1,data.Color(0,0,0),f),data.Point(.6,.5,1.76811457479))
      self.assertEqual(v0, data.Vector(-.4,-.5,.76811457479))
      pass

   def test_crange(self):
      self.assertListAlmostEqual(cast.crange(1,2,0.1),[1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9])
   def test_crange_again(self):
      self.assertListAlmostEqual(cast.crange(5,1,-.5),[5,4.5,4,3.5,3,2.5,2,1.5])

   def test_cast_ray(self):
      list_of_spheres = [data.Sphere(data.Point(0,5,0),2,data.Color(0,0,1),data.Finish(.4,.3,.5,.6)), data.Sphere(data.Point(1,6,0),1,data.Color(1,0,0),data.Finish(.3,.4,.5,.6)), data.Sphere(data.Point(0,7,1),1,data.Color(0,1,0),data.Finish(.7,.6,.5,.4))]
      ray0 = data.Ray(data.Point(0,1,0), data.Vector(1,0,0))
      amb = data.Color(0.5,1.0,0.8)
      light = data.Light(data.Point(150.0,-100,105),data.Color(0.5,1.0,0.9))
      eyepoint = data.Point(-1,4,6)
      c = cast.cast_ray(ray0, list_of_spheres,amb,light,eyepoint)
      self.assertTrue(c == data.Color(1.0,1.0,1.0))
   def test_cast_ray_again(self):
      list_of_spheres = [data.Sphere(data.Point(5,0,0),1,data.Color(0,0,1),data.Finish(.3,.3,.2,.1)), data.Sphere(data.Point(7,0,0),.7,data.Color(0,1,0),data.Finish(.6,.7,.6,.7)), data.Sphere(data.Point(3,1,0),.3,data.Color(1,0,0),data.Finish(.5,.2,.7,.5))]
      ray0 = data.Ray(data.Point(0,1,0), data.Vector(1,0,0))
      amb = data.Color(1.0,0.9,0.8)
      light = data.Light(data.Point(100.0,-100,100),data.Color(1.6,1.6,1.8))
      eyepoint = data.Point(0,0,0)
      c = cast.cast_ray(ray0, list_of_spheres,amb,light,eyepoint)
      self.assertTrue(c == data.Color(0.5,0,0))

if __name__ == "__main__":
   unittest.main()
      
