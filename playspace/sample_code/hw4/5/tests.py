import unittest
import data
import vector_math
import math
import collisions
import cast

class TestData(unittest.TestCase):
   def test_point(self):
      point = data.Point(15, 4, 6)
      self.assertAlmostEqual(point.x, 15)
      self.assertAlmostEqual(point.y, 4)
      self.assertAlmostEqual(point.z, 6)
   
   def test_point_again(self):
      point = data.Point(2, -67, 8)
      self.assertAlmostEqual(point.x, 2)
      self.assertAlmostEqual(point.y, -67)
      self.assertAlmostEqual(point.z, 8)

   def test_vector(self):
      vector = data.Vector(7, 3, -14)
      self.assertAlmostEqual(vector.x, 7)
      self.assertAlmostEqual(vector.y, 3)
      self.assertAlmostEqual(vector.z, -14)

   def test_vector_again(self):
      vector = data.Vector(-12.0, 6.0, 2.5)
      self.assertAlmostEqual(vector.x, -12.0)
      self.assertAlmostEqual(vector.y, 6.0)
      self.assertAlmostEqual(vector.z, 2.5)

   def test_ray(self):
      ray = data.Ray(data.Point(3.5, 7.9, 4),data.Vector(3, 5.6, -2.3))
      self.assertAlmostEqual(ray.pt.x, 3.5)
      self.assertAlmostEqual(ray.pt.y, 7.9)
      self.assertAlmostEqual(ray.pt.z, 4)
      self.assertAlmostEqual(ray.dir.x, 3)
      self.assertAlmostEqual(ray.dir.y, 5.6)
      self.assertAlmostEqual(ray.dir.z, -2.3)

   def test_ray_again(self):
      ray = data.Ray(data.Point(14, 8.7, 9),data.Vector(-5, 3.4, 2))
      self.assertAlmostEqual(ray.pt.x, 14)
      self.assertAlmostEqual(ray.pt.y, 8.7)
      self.assertAlmostEqual(ray.pt.z, 9)
      self.assertAlmostEqual(ray.dir.x, -5)
      self.assertAlmostEqual(ray.dir.y, 3.4)
      self.assertAlmostEqual(ray.dir.z, 2)

   def test_sphere(self):
      sphere = data.Sphere(data.Point(34, 21, 4.5),15.5,\
      data.Color(0.0,0.0,13.0),data.Finish(1.0,0.5,0.4,1.0))
      self.assertAlmostEqual(sphere.center.x, 34)
      self.assertAlmostEqual(sphere.center.y, 21)
      self.assertAlmostEqual(sphere.center.z, 4.5)
      self.assertAlmostEqual(sphere.radius, 15.5)
      self.assertAlmostEqual(sphere.color.r, 0.0)
      self.assertAlmostEqual(sphere.color.g, 0.0)
      self.assertAlmostEqual(sphere.color.b, 13.0)
      self.assertAlmostEqual(sphere.finish.ambient, 1.0)
      self.assertAlmostEqual(sphere.finish.diffuse, 0.5)
      self.assertAlmostEqual(sphere.finish.specular, 0.4)
      self.assertAlmostEqual(sphere.finish.roughness, 1.0)

   def test_sphere_again(self):
      sphere = data.Sphere(data.Point(12, 2.3, 7),3.4,\
      data.Color(0.0,4.0,0.0),data.Finish(0.5,0.3,0.0,0.6))
      self.assertAlmostEqual(sphere.center.x, 12)
      self.assertAlmostEqual(sphere.center.y, 2.3)
      self.assertAlmostEqual(sphere.center.z, 7)
      self.assertAlmostEqual(sphere.radius, 3.4)
      self.assertAlmostEqual(sphere.color.r, 0.0)
      self.assertAlmostEqual(sphere.color.g, 4.0)
      self.assertAlmostEqual(sphere.color.b, 0.0)
      self.assertAlmostEqual(sphere.finish.ambient, 0.5)
      self.assertAlmostEqual(sphere.finish.diffuse, 0.3)
      self.assertAlmostEqual(sphere.finish.specular, 0.0)
      self.assertAlmostEqual(sphere.finish.roughness, 0.6)

   def test_color(self):
      color = data.Color(1.0,0.4,0.2)
      self.assertAlmostEqual(color.r, 1.0)
      self.assertAlmostEqual(color.g, 0.4)
      self.assertAlmostEqual(color.b, 0.2)
 
   def test_color_again(self):
      color = data.Color(0.0,0.3,1.0)
      self.assertAlmostEqual(color.r, 0.0)
      self.assertAlmostEqual(color.g, 0.3)
      self.assertAlmostEqual(color.b, 1.0)

   def test_finish(self):
      finish = data.Finish(0.2,1.0,0.5,0.05)
      self.assertAlmostEqual(finish.ambient, 0.2)
      self.assertAlmostEqual(finish.diffuse, 1.0)
      self.assertAlmostEqual(finish.specular, 0.5)
      self.assertAlmostEqual(finish.roughness, 0.05)

   def test_finish_again(self):
      finish = data.Finish(1.0,0.5,1.4,0.0)
      self.assertAlmostEqual(finish.ambient, 1.0)
      self.assertAlmostEqual(finish.diffuse, 0.5)
      self.assertAlmostEqual(finish.specular, 1.4)
      self.assertAlmostEqual(finish.roughness, 0.0)

   def test_light(self):
      light = data.Light(data.Point(1.0,-0.5,3.0),data.Color(0.4,1.0,0.0))
      self.assertAlmostEqual(light.pt.x, 1.0)
      self.assertAlmostEqual(light.pt.y, -0.5)
      self.assertAlmostEqual(light.pt.z, 3.0)
      self.assertAlmostEqual(light.color.r, 0.4)
      self.assertAlmostEqual(light.color.g, 1.0)
      self.assertAlmostEqual(light.color.b, 0.0)

   def test_light_again(self):
      light = data.Light(data.Point(0.4,12.0,-5.5),data.Color(0.7,0.0,1.0))
      self.assertAlmostEqual(light.pt.x, 0.4)
      self.assertAlmostEqual(light.pt.y, 12.0)
      self.assertAlmostEqual(light.pt.z, -5.5)
      self.assertAlmostEqual(light.color.r, 0.7)
      self.assertAlmostEqual(light.color.g, 0.0)
      self.assertAlmostEqual(light.color.b, 1.0)

   def test_point_eq(self):
      point1 = data.Point(3,8,10)
      point2 = data.Point(3,8,10)
      self.assertEqual(point1, point2)
   
   def test_point_eq_again(self):
      point1 = data.Point(4,52,-13)
      point2 = data.Point(4,52,-13)
      self.assertEqual(point1,point2)

   def test_vector_eq(self):
      vector1 = data.Point(12,79,-5)
      vector2 = data.Point(12,79,-5)
      self.assertEqual(vector1, vector2)

   def test_vector_eq_again(self):
      vector1 = data.Point(4,-32,-27)
      vector2 = data.Point(4,-32,-27)
      self.assertEqual(vector1, vector2)
   
   def test_ray_eq(self):
      ray1 = data.Ray(data.Point(35,-6,17),data.Vector(3,9,10))
      ray2 = data.Ray(data.Point(35,-6,17),data.Vector(3,9,10))
      self.assertEqual(ray1, ray2)

   def test_ray_eq_again(self):
      ray1 = data.Ray(data.Point(2,45,-4),data.Vector(87,32,10))
      ray2 = data.Ray(data.Point(2,45,-4),data.Vector(87,32,10))
      self.assertEqual(ray1, ray2)
 
   def test_sphere_eq(self):
      sphere1 = data.Sphere(data.Point(2,7,15),34.5,data.Color(0.0,3.0,15.0),data.Finish(1.0,0.5,0.6,0.4))
      sphere2 = data.Sphere(data.Point(2,7,15),34.5,data.Color(0.0,3.0,15.0),data.Finish(1.0,0.5,0.6,0.4))
      self.assertEqual(sphere1, sphere2)

   def test_sphere_eq_again(self):
      sphere1 = data.Sphere(data.Point(-45,6,13),12.7,data.Color(0.0,1.0,1.0),data.Finish(0.0,0.6,1.0,0.0))
      sphere2 = data.Sphere(data.Point(-45,6,13),12.7,data.Color(0.0,1.0,1.0),data.Finish(0.0,0.6,1.0,0.0))
      self.assertEqual(sphere1, sphere2)

   def test_color_eq(self):
      color1 = data.Color(0.3,0.0,0.5)
      color2 = data.Color(0.3,0.0,0.5)
      self.assertEqual(color1, color2)

   def test_color_eq_again(self):
      color1 = data.Color(0.0,0.6,1.2)
      color2 = data.Color(0.0,0.6,1.2)
      self.assertEqual(color1, color2)

   def test_finish_eq(self):
      finish1 = data.Finish(0.9,0.2,0.3,0.5)
      finish2 = data.Finish(0.9,0.2,0.3,0.5)
      self.assertEqual(finish1, finish2)
   
   def test_finish_eq_again(self):
      finish1 = data.Finish(0.3,1.0,0.07,1.0)
      finish2 = data.Finish(0.3,1.0,0.07,1.0)
      self.assertEqual(finish1, finish2)

   def test_light_eq(self):
      light1 = data.Light(data.Point(-1.0,4.5,10.0),data.Color(1.5,1.5,1.5))
      light2 = data.Light(data.Point(-1.0,4.5,10.0),data.Color(1.5,1.5,1.5))
      self.assertEqual(light1, light2)

   def test_light_eq(self):
      light1 = data.Light(data.Point(13.4,2.3,-1.5),data.Color(0.0,1.4,0.0))
      light2 = data.Light(data.Point(13.4,2.3,-1.5),data.Color(0.0,1.4,0.0))
      self.assertEqual(light1,light2)

   def test_scale_vector(self):
      scaled = vector_math.scale_vector(data.Vector(4,2,3), 10)
      self.assertEqual(scaled, data.Vector(40,20,30))

   def test_scale_vector_again(self):
      scaled = vector_math.scale_vector(data.Vector(5,8,12), 3)
      self.assertEqual(scaled, data.Vector(15,24,36))

   def test_dot_vector(self):
      dot = vector_math.dot_vector(data.Vector(6,2,3),data.Vector(10,3,4))
      self.assertAlmostEqual(dot, 78)
      
   def test_dot_vector_again(self):
      dot = vector_math.dot_vector(data.Vector(7,23,45),data.Vector(9,2,7))
      self.assertAlmostEqual(dot, 424)

   def test_length_vector(self):
      length_vec = vector_math.length_vector(data.Vector(3,6,12))
      self.assertAlmostEqual(length_vec, math.sqrt(189))
   
   def test_length_vector_again(self):
      length_vec = vector_math.length_vector(data.Vector(11,-34,2))
      self.assertAlmostEqual(length_vec, math.sqrt(1281))
   
   def test_normalize_vector(self):
      normal = vector_math.normalize_vector(data.Vector(4,6,-3))
      self.assertEqual(normal, data.Vector((4/math.sqrt(61)),(6/math.sqrt(61)),(-3/math.sqrt(61))))

   def test_normalize_vector_again(self):
      normal = vector_math.normalize_vector(data.Vector(10,7,2))
      self.assertEqual(normal, data.Vector((10/math.sqrt(153)),(7/math.sqrt(153)),(2/math.sqrt(153))))

   def test_difference_point(self):
      p_difference = vector_math.difference_point(data.Point(12,-3,6),data.Point(8,35,17))
      self.assertEqual(p_difference, data.Vector(4,-38,-11))

   def test_difference_point_again(self):
      p_difference = vector_math.difference_point(data.Point(46,14,4),data.Point(32,2,23))
      self.assertEqual(p_difference, data.Vector(14,12,-19))

   def test_difference_vector(self):
      v_difference = vector_math.difference_vector(data.Vector(34,14,-7),data.Vector(21,9,56))
      self.assertEqual(v_difference, data.Vector(13,5,-63))
   
   def test_difference_vector_again(self):
      v_difference = vector_math.difference_vector(data.Vector(-12,4,67),data.Vector(51,-3,5))
      self.assertEqual(v_difference, data.Vector(-63,7,62))

   def test_translate_point(self):
      translation = vector_math.translate_point(data.Point(2,19,7),\
      data.Vector(-5,23,9))
      self.assertEqual(translation, data.Point(-3,42,16))

   def test_translate_point_again(self):
      translation = vector_math.translate_point(data.Point(-16,3,10),data.Vector(12,33,2))
      self.assertEqual(translation, data.Point(-4,36,12))

   def test_vector_from_to(self):
      test_vec = vector_math.vector_from_to(data.Point(34,14,6),data.Point(5,63,10))
      self.assertEqual(test_vec, data.Vector(-29,49,4))

   def test_vector_from_to_again(self):
      test_vec = vector_math.vector_from_to(data.Point(42,-19,12),data.Point(67,2,4))
      self.assertEqual(test_vec, data.Vector(25,21,-8))

   def test_sphere_intersection_1(self):
      sphere_intersect = collisions.sphere_intersection_point(data.Ray\
      (data.Point(1.0,2.0,4.0),data.Vector(2.0,1.0,3.0)),\
      data.Sphere(data.Point(3.0,1.0,1.0),2.0,data.Color(0.0,0.0,0.0),\
      data.Finish(1.0,0.5,0.7,9.0)))
      self.assertEqual(sphere_intersect, None)
      
   def test_sphere_intersection_2(self):
      sphere_intersect = collisions.sphere_intersection_point(data.Ray\
      (data.Point(3.0,11.0,5.0),data.Vector(1.0,3.0,1.0)),data.Sphere(\
      data.Point(5.0,7.0,2.0),10.0,data.Color(0.0,1.0,0.0),data.Finish(0.5,1.0,0.0,0.4)))
      self.assertEqual(sphere_intersect, data.Point(4.62018819, 15.86056457,\
      6.62018819))

   def test_sphere_intersection_3(self):
      sphere_intersect = collisions.sphere_intersection_point(data.Ray\
      (data.Point(2,0,5),data.Vector(4,1,1)),data.Sphere(data.Point\
      (3,4,1),4,data.Color(0.0,3.0,0.0),data.Finish(0.6,0.0,1.0,0.05)))
      self.assertEqual(sphere_intersect, None)

   def test_find_intersection(self):
      sphere_list = [data.Sphere(data.Point(0,4,0),6,data.Color(0,0,0),\
      data.Finish(1.0,0.4,0.6,0.7)),data.Sphere(data.Point(0,9,0),11,\
      data.Color(0.0,4.0,0.0),data.Finish(0.0,0.2,1.0,1.5))]
      ray = data.Ray(data.Point(0,-10,0),data.Vector(0,3,0))
      intersection = collisions.find_intersection_points(sphere_list, ray)
      self.assertEqual(intersection, [(data.Sphere(data.Point(0,4,0),6,\
      data.Color(0.0,0.0,0.0),data.Finish(1.0,0.4,0.6,0.7)),data.Point(0,-2,0)),\
      (data.Sphere(data.Point(0,9,0),11,data.Color(0.0,4.0,0.0),\
      data.Finish(0.0,0.2,1.0,1.5)),data.Point(0,-2,0))])

   def test_find_intersection_again(self):
      sphere_list = [data.Sphere(data.Point(0,0,0),2,data.Color\
      (0.0,0.0,14.0),data.Finish(1.0,0.0,0.3,1.0)),data.Sphere(data.Point(0,6,0),2,\
      data.Color(1.0,2.0,0.0),data.Finish(1.0,0.6,0.5,0.01))]
      ray = data.Ray(data.Point(0,-8,0),data.Vector(0,2,0))
      intersection = collisions.find_intersection_points(sphere_list,ray)
      self.assertEqual(intersection, [(data.Sphere(data.Point(0,0,0),2,\
      data.Color(0.0,0.0,14.0),data.Finish(1.0,0.0,0.3,1.0)),data.Point(0,-2,0)),\
      (data.Sphere(data.Point(0,6,0),2,data.Color(1.0,2.0,0.0),\
      data.Finish(1.0,0.6,0.5,0.01)),data.Point(0,4,0))])   

   def test_sphere_normal(self):
      normal = collisions.sphere_normal_at_point(data.Sphere(data.Point(3,12,4),25,\
      data.Color(0.0,2.0,0.0),data.Finish(0.0,0.5,1.0,0.6)),\
      data.Point(4.9402579,13.8207737,15.7012895))
      self.assertEqual(normal, data.Vector(0.16168816,0.1517311,0.97510748))

   def test_sphere_normal_again(self):
      normal = collisions.sphere_normal_at_point(data.Sphere(data.Point(8,2,6),8,\
      data.Color(1.0,1.0,1.0),data.Finish(0.4,0.7,0.0,0.03)),\
      data.Point(2.1556301,5.4668903,1.7781505))
      self.assertEqual(normal, data.Vector(-0.7305462,0.43336128,-0.52773118))

   def test_iteration_floats(self):
      float_list = cast.iteration_floats(4,9,0.5)
      self.assertEqual(float_list, [4,4.5,5,5.5,6,6.5,7,7.5,8,8.5])

   def test_iteration_floats_again(self):
      float_list = cast.iteration_floats(5,2,-0.25)
      self.assertEqual(float_list, [5,4.75,4.5,4.25,4,3.75,\
      3.5,3.25,3,2.75,2.5,2.25])

   def test_distance_differences(self):
      origin = data.Point(4,13,2)
      intersection = data.Point(45,-2,5)
      distance = cast.distance_difference(origin,intersection)
      self.assertEqual(distance, math.sqrt(1915))

   def test_distance_differences_again(self):
      origin = data.Point(-10,32,1)
      intersection = data.Point(12,3,7)
      distance = cast.distance_difference(origin,intersection)
      self.assertEqual(distance, math.sqrt(1361))

   def test_compare_distances(self):
      input_list = [(data.Sphere(data.Point(4,6,18),5,data.Color(0,0,0),\
      data.Finish(1.0,0.5,0.4,1.0)),\
      data.Point(2,45,32)),(data.Sphere(data.Point(2,5,0),4,\
      data.Color(0.0,0.0,0.0),data.Finish(1.0,0.6,0.0,0.6)),\
      data.Point(8,3,2)),(data.Sphere(data.Point(2,7,9),3,\
      data.Color(0.0,0.0,0.0),data.Finish(0.0,0.0,0.4,0.3)),\
      data.Point(34,5,76))]
      ray = data.Ray(data.Point(1,2,0),data.Vector(5,7,10))
      comparison = cast.compare_distances_sphere(input_list,ray)  
      self.assertEqual(comparison, (data.Sphere(data.Point(2,5,0),\
      4,data.Color(0.0,0.0,0.0),data.Finish(1.0,0.6,0.0,0.6)),data.Point(8,3,2)))

   def test_compare_distances_again(self):
      input_list = [(data.Sphere(data.Point(0,0,0),2,\
      data.Color(0.0,0.0,14.0),data.Finish(0.3,1.0,0.0,0.0)),data.Point(0,-2,0)),\
      (data.Sphere(data.Point(0,6,0),\
      2,data.Color(1.0,2.0,0.0),data.Finish(0.2,0.7,1.0,0.5)),data.Point(0,4,0))]
      ray = data.Ray(data.Point(0,-8,0),data.Vector(4,10,0)) 
      comparison = cast.compare_distances_sphere(input_list,ray)
      self.assertEqual(comparison, (data.Sphere(data.Point(0,0,0),\
      2,data.Color(0.0,0.0,14.0),data.Finish(0.3,1.0,0.0,0.0)),data.Point(0,-2,0)))

   def test_normal_sphere_vector(self):
      normal_vector = cast.normal_sphere_vector((data.Sphere(data.Point(0,4,0),6,\
      data.Color(0.0,4.0,0.0),data.Finish(1.0,0.2,0.5,1.0)),data.Point(0,-2,0)))
      self.assertEqual(normal_vector, data.Vector(0,-1,0))
  
   def test_normal_sphere_vector_again(self):
      normal_vector = cast.normal_sphere_vector((data.Sphere(data.Point(0,6,0),2,data.Color(1.0,2.0,0.0),\
      data.Finish(1.0,0.6,0.5,0.01)),data.Point(0,4,0)))
      self.assertEqual(normal_vector, data.Vector(0,-1,0))      

   def test_point_light(self):
      point_e = cast.point_light(data.Vector(0,-1,0),(data.Sphere(data.Point(0,4,0),6,\
      data.Color(0.0,4.0,0.0),data.Finish(1.0,0.2,0.5,1.0)),data.Point(0,-2,0)))
      self.assertEqual(point_e, data.Point(0,-2.01,0))

   def test_point_light_again(self):
      point_e = cast.point_light(data.Vector(0,-1,0),(data.Sphere(data.Point(0,6,0),2,data.Color(1.0,2.0,0.0),\
      data.Finish(1.0,0.6,0.5,0.01)),data.Point(0,4,0)))
      self.assertEqual(point_e, data.Point(0,3.99,0))

   def test_light_direction_vector(self):
      light_direction = cast.light_direction_vector(data.Point(0,-2.01,0),data.Light(\
      data.Point(4.0,1.5,3.2),data.Color(0.0,3.0,0.5)))
      self.assertEqual(light_direction, data.Vector(0.6441558,0.5652467,0.5153246))
  
   def test_light_direction_vector_again(self):
      light_direction = cast.light_direction_vector(data.Point(0,3.99,0),data.Light(data.Point(5.5,1.2,7.2),\
      data.Color(3.0,0.3,0.9)))
      self.assertEqual(light_direction, data.Vector(0.58015683,-0.2942977,0.75947803))

   def test_check_light_path(self):
      check_light = cast.check_light_path((data.Sphere(data.Point(0,6,0),2,data.Color(1.0,2.0,0.0),\
      data.Finish(1.0,0.6,0.5,0.01)),data.Point(0,4,0)),[data.Sphere(data.Point(0,6,0),2,\
      data.Color(1.0,2.0,0.0),data.Finish(1.0,0.6,0.5,0.01))],data.Vector(0,-1,0),data.Point(0,-2.01,0),\
      data.Vector(0.6441558,0.5652467,0.5153246))
      self.assertEqual(check_light, 0.0)
  
   def test_check_light_path_again(self):
      check_light = cast.check_light_path((data.Sphere(data.Point(0,4,0),6,\
      data.Color(0.0,4.0,0.0),data.Finish(1.0,0.2,0.5,1.0)),data.Point(0,2,0)),\
      [data.Sphere(data.Point(0,4,0),6,data.Color(0.0,4.0,0.0),data.Finish(1.0,0.2,0.5,1.0))],\
      data.Vector(0,1,0),data.Point(0,-2.01,0),data.Vector(0.6441558,0.5652467,0.5153246))
      self.assertEqual(check_light, 0.0)

   def test_check_specular_intensity(self):
      specular = cast.check_specular_intensity((data.Sphere(data.Point(0,6,0),2,data.Color(1.0,2.0,0.0),\
      data.Finish(1.0,0.6,0.5,0.01)),data.Point(0,4,0)),data.Point(10,12,3.5),data.Vector(0,-1,0),\
      data.Point(0,-2.01,0),data.Vector(0.6441558,0.5652467,0.5153246))
      self.assertEqual(specular, 0.0)

   def test_check_specular_intensity_again(self):
      specular = cast.check_specular_intensity((data.Sphere(data.Point(0,4,0),6,\
      data.Color(0.0,4.0,0.0),data.Finish(1.0,0.2,0.5,1.0)),data.Point(0,2,0)),\
      data.Point(3.6,19.0,2.0),data.Vector(0,1,0),data.Point(0,-2.01,0),\
      data.Vector(0.6441558,0.5652467,0.5153246))
      self.assertEqual(specular, 0.1991195116711294)

   def test_color_convert(self):
      convert = cast.color_convert((data.Sphere(data.Point(3,1,0),\
      5.0,data.Color(1.0,0.0,1.0),data.Finish(1.0,0.4,0.5,1.0)),data.Point(1,0,2)),\
      data.Color(1.0,1.0,1.0),data.Light(data.Point(-4,5,12),\
      data.Color(1.5,1.0,0.0)),[data.Sphere(data.Point(3,1,0),\
      5.0,data.Color(1.0,0.0,1.0),data.Finish(1.0,0.4,0.07,0.09))],\
      data.Point(-1.0,5.0,0.3),data.Vector(0,-1,0),data.Point(4,3,1),data.Vector(1.3,4.0,-2.0))
      self.assertEqual(convert, (716,307,255))
 
   def test_color_convert_again(self):
      convert = cast.color_convert((data.Sphere(data.Point(0,4,0),6,\
      data.Color(0.0,0.0,0.0),data.Finish(1.0,0.4,1.0,1.0)),\
      data.Point(0,-2,0)),data.Color(1.0,0.0,0.1),\
      data.Light(data.Point(4.5,1.0,0.0),data.Color(0.5,1.0,0.0)),\
      [(data.Sphere(data.Point(0,4,0),6,data.Color(0.0,0.0,0.0),\
      data.Finish(1.0,0.4,1.0,0.0)))],data.Point(-2.0,6.0,0.0),\
      data.Vector(1,5,-5),data.Point(4.5,0,1.5),data.Vector(1.0,0.0,-5.0))
      self.assertEqual(convert, (22893,45786,0))

   def test_cast_ray(self):
      cast_test = cast.cast_ray(data.Ray(data.Point(0,-10,0),\
      data.Vector(0,3,0)),[data.Sphere(data.Point(0,4,0),6,\
      data.Color(0.0,4.0,0.0),data.Finish(1.0,0.2,0.5,1.0)),\
      data.Sphere(data.Point(0,0,0),\
      2,data.Color(0.0,0.0,55.0),data.Finish(0.5,1.0,0.4,0.25)),data.Sphere\
      (data.Point(-5,4,7),3,data.Color(0.0,23.0,0.0),data.Finish(0.0,0.0,0.1,0.1))],\
      data.Color(1.0,1.0,1.0),data.Light(data.Point(1.4,3.0,2.0),data.Color(1.0,1.0,1.0)),\
      data.Point(4.0,5.0,-9.0))
      self.assertEqual(cast_test, (89,1109,89))

   def test_cast_ray_again(self):
      cast_test = cast.cast_ray(data.Ray(data.Point(1.0,2.0,4.0),\
      data.Vector(2.0,1.0,3.0)),[data.Sphere(data.Point(3.0,1.0,1.0),\
      2.0,data.Color(0.0,1.0,0.0),data.Finish(1.0,0.4,0.5,1.0)),\
      data.Sphere(data.Point(100,-40,3),5,data.Color(0.0,5.0,0.0),\
      data.Finish(0.0,1.0,0.1,0.2))],data.Color(1.0,1.0,0.0),data.Light(data.Point(0.3,2.0,-1.0),
      data.Color(0.5,1.0,3.2)),data.Point(-10.0,3.4,7.0))
      self.assertEqual(cast_test, (255, 255, 255))

if __name__ == "__main__":
   unittest.main()
