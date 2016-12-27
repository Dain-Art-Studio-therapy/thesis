import unittest
import data
import vector_math
import utility
import math
import collisions
import cast

class TestData(unittest.TestCase):
   # creates point and verifies that attributes were properly initialized
   def test_point(self):
       pt = data.Point(3,6.4,9.9)
       self.assertAlmostEqual(pt.x, 3)
       self.assertAlmostEqual(pt.y, 6.4)
       self.assertAlmostEqual(pt.z, 9.9)

   def test_point_again(self):
       pt = data.Point(-3,5.4,9)
       self.assertAlmostEqual(pt.x, -3)
       self.assertAlmostEqual(pt.y, 5.4)
       self.assertAlmostEqual(pt.z, 9)

   # creates vector and verifies that attributes were properly initialized
   def test_vector(self):
       vct = data.Vector(6,7.2,-7.8)
       self.assertAlmostEqual(vct.x, 6)
       self.assertAlmostEqual(vct.y, 7.2)
       self.assertAlmostEqual(vct.z, -7.8)

   def test_vector_again(self):
       vct = data.Vector(-8.5,0,0)
       self.assertAlmostEqual(vct.x, -8.5)
       self.assertAlmostEqual(vct.y, 0)
       self.assertAlmostEqual(vct.z, 0)

   # creates ray and verifies that attributes were properly initialized
   def test_ray(self):
       ray = data.Ray(data.Point(0,0,0), data.Vector(-4.4,6,0))
       self.assertAlmostEqual(ray.pt.x, 0)
       self.assertAlmostEqual(ray.pt.y, 0)
       self.assertAlmostEqual(ray.pt.z, 0)
       self.assertAlmostEqual(ray.dir.x, -4.4)
       self.assertAlmostEqual(ray.dir.y, 6)
       self.assertAlmostEqual(ray.dir.z, 0)

   def test_ray_again(self):
       ray = data.Ray(data.Point(-1,2,4), data.Vector(5,5,5))
       self.assertAlmostEqual(ray.pt.x, -1)
       self.assertAlmostEqual(ray.pt.y, 2)
       self.assertAlmostEqual(ray.pt.z, 4)
       self.assertAlmostEqual(ray.dir.x, 5)
       self.assertAlmostEqual(ray.dir.y, 5)
       self.assertAlmostEqual(ray.dir.z, 5)

   # creates sphere and verifies that attributes were properly initialized
   def test_sphere(self):
       sphere = data.Sphere(data.Point(0,0,1),
                            9,
                            data.Color(0,0,0),
                            data.Finish(0.5,0.4,0.5,0.05))
       self.assertAlmostEqual(sphere.center.x, 0)
       self.assertAlmostEqual(sphere.center.y, 0)
       self.assertAlmostEqual(sphere.center.z, 1)
       self.assertAlmostEqual(sphere.radius, 9)
       self.assertEqual(sphere.color,data.Color(0,0,0))
       self.assertEqual(sphere.finish,data.Finish(0.5,0.4,0.5,0.05))

   def test_sphere_again(self):
       sphere = data.Sphere(data.Point(-3,-4.3,8.4),
                            2,
                            data.Color(0,0,0),
                            data.Finish(0.3,0.4,0.5,0.05))
       self.assertAlmostEqual(sphere.center.x, -3)
       self.assertAlmostEqual(sphere.center.y, -4.3)
       self.assertAlmostEqual(sphere.center.z, 8.4)
       self.assertAlmostEqual(sphere.radius, 2)
       self.assertEqual(sphere.color,data.Color(0,0,0))
       self.assertEqual(sphere.finish,data.Finish(0.3,0.4,0.5,0.05))

   def test_point_eq(self):
       pt1 = data.Point(1,-1,2.2)
       pt2 = data.Point(1,-1,2.2)
       self.assertEqual(pt1,pt2)

   def test_point_eq_again(self):
       pt1 = data.Point(0,0,0)
       pt1_1 = data.Point(0,0,0)
       self.assertEqual(pt1,pt1_1)

   def test_vector_eq(self):
       vect1 = data.Vector(1,-1,2.2)
       vect2 = data.Vector(1,-1,2.2)
       self.assertEqual(vect1,vect2)

   def test_vector_eq_again(self):
       vect1 = data.Vector(0,0,0)
       vect1_1 = data.Vector(0,0,0)
       self.assertEqual(vect1,vect1_1)

   def test_ray_eq(self):
       ray1 = data.Ray(data.Point(1,-1,1.1),data.Vector(5,-2,5.5))
       ray2 = data.Ray(data.Point(1,-1,1.1),data.Vector(5,-2,5.5))
       self.assertEqual(ray1,ray2)

   def test_ray_eq_again(self):
       ray1 = data.Ray(data.Point(0,0,0),data.Vector(7,-7,7.7))
       ray1_1 = data.Ray(data.Point(0,0,0),data.Vector(7,-7,7.7))
       self.assertEqual(ray1,ray1_1)

   def test_sphere_eq(self):
       sphere1 = data.Sphere(data.Point(1,-1,1.1),
                             7.7,
                             data.Color(1.0,1.0,1.0),
                             data.Finish(0.3,0.4,0.5,0.05))
       sphere2 = data.Sphere(data.Point(1,-1,1.1),
                             7.7,
                             data.Color(1.0,1.0,1.0),
                             data.Finish(0.3,0.4,0.5,0.05))
       self.assertEqual(sphere1,sphere2)

   def test_sphere_eq_again(self):
       sphere1 = data.Sphere(data.Point(0,0,0),
                             1,
                             data.Color(0,0,0),
                             data.Finish(0.5,0.4,0.5,0.05))
       sphere1_1 = data.Sphere(data.Point(0,0,0),
                               1,
                               data.Color(0,0,0),
                               data.Finish(0.5,0.4,0.5,0.05))
       self.assertEqual(sphere1,sphere1_1)

   def test_scale_vector(self):
       sv = vector_math.scale_vector(data.Vector(1,2,3),1.5)
       self.assertEqual(sv, data.Vector(1.5,3,4.5))         

   def test_scale_vector_again(self):
       sv = vector_math.scale_vector(data.Vector(-3.5,5,7.5),2)
       self.assertEqual(sv, data.Vector(-7,10,15))

   def test_dot_vector(self):
       dv = vector_math.dot_vector(data.Vector(1,2,3),
                                   data.Vector(1.5,2.5,-2))
       self.assertAlmostEqual(dv,0.5)

   def test_dot_vector_again(self):
       dv = vector_math.dot_vector(data.Vector(-1,2.2,4),
                                   data.Vector(-3,5.5,4.4))
       self.assertAlmostEqual(dv,32.7)

   def test_length_vector(self):
       lv = vector_math.length_vector(data.Vector(1,2,2))
       self.assertAlmostEqual(lv,3)

   def test_length_vector_again(self):
       lv = vector_math.length_vector(data.Vector(3.4,5.5,-7.2))
       self.assertAlmostEqual(lv,9.67729301)

   def test_normalize_vector(self):
       nv = vector_math.normalize_vector(data.Vector(-2,3,4))
       self.assertEqual(nv,data.Vector(-2 / math.sqrt(29),
                                       3 / math.sqrt(29),
                                       4 / math.sqrt(29)))       

   def test_normalize_vector_again(self):
       nv = vector_math.normalize_vector(data.Vector(2,1,2))
       self.assertEqual(nv,data.Vector(2.0 / 3,
                                       1.0 / 3,
                                       2.0 / 3))

   def test_difference_point(self):
       dp = vector_math.difference_point(data.Point(1,-2,3),
                                         data.Point(3,3,3))
       self.assertEqual(dp,data.Vector(-2,-5,0))

   def test_difference_point_again(self):
       dp = vector_math.difference_point(data.Point(2.2,-4.5,9),
                                         data.Point(1,0,2))
       self.assertEqual(dp,data.Vector(1.2,-4.5,7))

   def test_difference_vector(self):
       dv = vector_math.difference_vector(data.Vector(2.2,-4,7),
                                          data.Vector(6,-2,3))
       self.assertEqual(dv,data.Vector(-3.8,-2,4))

   def test_difference_vector_again(self):
       dv = vector_math.difference_vector(data.Vector(0,2,-4),
                                          data.Vector(0,3,0))
       self.assertEqual(dv,data.Vector(0,-1,-4))

   def test_translate_point(self):
       tp = vector_math.translate_point(data.Point(9,0,1),
                                        data.Vector(1,2,3))
       self.assertEqual(tp,data.Point(10,2,4))

   def  test_translate_point_again(self):
       tp = vector_math.translate_point(data.Point(10,-4,7.4),
                                        data.Vector(3.1,-7,0.6))
       self.assertEqual(tp,data.Point(13.1,-11,8))

   def test_vector_from_to(self):
       vft = vector_math.vector_from_to(data.Point(3,-6,2.9),
                                        data.Point(7,-7,0.3))
       self.assertEqual(vft,data.Vector(4,-1,-2.6))

   def test_vector_from_to_again(self):
       vft = vector_math.vector_from_to(data.Point(0,0,1),
                                        data.Point(-3.3,8,9.9))
       self.assertEqual(vft,data.Vector(-3.3,8,8.9))

   def test_sphere_intersection_point(self):
       ray = data.Ray(data.Point(0,-4,0),
                      data.Vector(0,1,0))
       sphere = data.Sphere(data.Point(0,0,0),
                            2,
                            data.Color(0,0,0),
                            data.Finish(0.5,0.4,0.5,0.05))
       sip = collisions.sphere_intersection_point(ray,sphere)
       self.assertEqual(sip,data.Point(0,-2,0))

   def test_sphere_intersection_point_2(self):
       ray = data.Ray(data.Point(0,0,-4),
                      data.Vector(0,0,-5))
       sphere = data.Sphere(data.Point(0,0,1),
                            3,
                            data.Color(1.0,1.0,1.0),
                            data.Finish(0.5,0.4,0.5,0.05))
       sip = collisions.sphere_intersection_point(ray,sphere)
       self.assertEqual(sip,None) 

   def test_sphere_intersection_point_3(self):
       ray = data.Ray(data.Point(0,0,0),
                      data.Vector(0,0,1))
       sphere = data.Sphere(data.Point(0,0,0),
                            6,
                            data.Color(0,0,0),
                            data.Finish(0.5,0.4,0.5,0.05))
       sip = collisions.sphere_intersection_point(ray,sphere)
       self.assertEqual(sip,data.Point(0,0,6))

   def test_sphere_intersection_point_4(self):
       ray = data.Ray(data.Point(-10,0,3),
                      data.Vector(1,0,0))
       sphere = data.Sphere(data.Point(0,0,0),
                            3,
                            data.Color(1.0,1.0,1.0),
                            data.Finish(0.5,0.4,0.5,0.05))
       sip = collisions.sphere_intersection_point(ray,sphere)
       self.assertEqual(sip,data.Point(0,0,3))

   def test_sphere_intersection_point_5(self):
       ray = data.Ray(data.Point(1,-11,-12),
                      data.Vector(0,3,3))
       sphere = data.Sphere(data.Point(0,0,0),
                            10,
                            data.Color(1.0,1.0,1.0),
                            data.Finish(0.5,0.4,0.5,0.05))
       sip = collisions.sphere_intersection_point(ray,sphere)
       self.assertEqual(sip,data.Point(1,-6.51783442,-7.51783442))

   def test_sphere_intersection_point_6(self):
       ray = data.Ray(data.Point(0,-7,0),
                      data.Vector(0,5,0))
       sphere = data.Sphere(data.Point(20.3,20,-100),
                            1,
                            data.Color(0,0,0),
                            data.Finish(0.5,0.4,0.5,0.05))
       sip = collisions.sphere_intersection_point(ray,sphere)
       self.assertEqual(sip,None)

   def test_find_intersection_points(self):
       sphere_list = [data.Sphere(data.Point(0,0,0),
                                  2,
                                  data.Color(1,0.5,0.3),
                                  data.Finish(0.5,0.4,0.5,0.05)),
                      data.Sphere(data.Point(0,20,0),
                                  1,
                                  data.Color(1.0,0.0,0.4),
                                  data.Finish(0.5,0.4,0.5,0.05))]
       ray = data.Ray(data.Point(0,-20,0),
                      data.Vector(0,1.3,0))
       fip = collisions.find_intersection_points(sphere_list,ray)
       result_list = [(sphere_list[0],
                       collisions.sphere_intersection_point(ray,
                                                            sphere_list[0])),
                      (sphere_list[1],
                       collisions.sphere_intersection_point(ray,
                                                            sphere_list[1]))]
       self.assertEqual(fip,result_list)

   def test_find_intersection_points_2(self):
       sphere_list = [data.Sphere(data.Point(0,0,0),
                                  2,
                                  data.Color(0.23,0.23,0.23),
                                  data.Finish(0.5,0.4,0.5,0.05)),
                      data.Sphere(data.Point(20.3,20,-100),
                                  1,
                                  data.Color(0.45,0.45,0.67),
                                  data.Finish(0.5,0.4,0.5,0.05))]
       ray = data.Ray(data.Point(0,-7,0),
                      data.Vector(0,5,0))
       fip = collisions.find_intersection_points(sphere_list,ray)
       result_list = [(sphere_list[0],
                       collisions.sphere_intersection_point(ray,
                                                            sphere_list[0]))]
       self.assertEqual(fip,result_list)

   def test_find_intersection_points_3(self):
       sphere_list = [data.Sphere(data.Point(-5,2,9),
                                  2,
                                  data.Color(0.23,0.12,0.2),
                                  data.Finish(0.5,0.4,0.5,0.05)),
                      data.Sphere(data.Point(0,0,-9),
                                  1,
                                  data.Color(0.24,0.14,0.68),
                                  data.Finish(0.5,0.4,0.5,0.05))]
       ray = data.Ray(data.Point(0,-7,0),
                      data.Vector(0,5,0))
       fip = collisions.find_intersection_points(sphere_list,ray)
       result_list = []
       self.assertEqual(fip,result_list)

   def test_sphere_normal_at_point(self):
       sphere = data.Sphere(data.Point(0,0,0),
                            5,
                            data.Color(0.22,0.23,0.24),
                            data.Finish(0.5,0.4,0.5,0.05))
       point = data.Point(0,0,5)
       snap = collisions.sphere_normal_at_point(sphere,point)
       self.assertEqual(snap,data.Vector(0,0,1))

   def test_sphere_normal_at_point_2(self):
       sphere = data.Sphere(data.Point(0,3,4),
                            5,
                            data.Color(0.2,0.2,0.2),
                            data.Finish(0.5,0.4,0.5,0.05))
       point = data.Point(0,0,0)
       snap = collisions.sphere_normal_at_point(sphere,point)
       self.assertEqual(snap,data.Vector(0,
                                         -3 / 5.0,
                                         -4 / 5.0)) 

   def test_sphere_normal_at_point_3(self):
       sphere = data.Sphere(data.Point(2,32,-8),
                            7,
                            data.Color(120,130,140),
                            data.Finish(0.5,0.4,0.5,0.05))
       point = data.Point(2,
                          32 - math.sqrt(29),
                          -8 - math.sqrt(20))
       snap = collisions.sphere_normal_at_point(sphere,point)
       self.assertEqual(snap,data.Vector(0,
                                         - math.sqrt(29) / 7.0,
                                         - math.sqrt(20) / 7.0))
   def test_color(self):
       color = data.Color(0,120,255)
       self.assertAlmostEqual(color.r,0)
       self.assertAlmostEqual(color.g,120)
       self.assertAlmostEqual(color.b,255)

   def test_color_again(self):
       color = data.Color(255,117,77)
       self.assertAlmostEqual(color.r,255)
       self.assertAlmostEqual(color.g,117)
       self.assertAlmostEqual(color.b,77)

   def test_distance(self):
       pt1 = data.Point(0,5,6)
       pt2 = data.Point(0,2,2)
       d = cast.distance(pt1,pt2)
       self.assertAlmostEqual(d,5)

   def test_distance_again(self):
       pt1 = data.Point(4,10,7)
       pt2 = data.Point(9,7,-3)
       d = cast.distance(pt1,pt2)
       self.assertAlmostEqual(d,math.sqrt(134))

   def test_cast_ray(self):
       ray = data.Ray(data.Point(0,0,0),
                      data.Vector(0,3,0))
       sphere_list = [data.Sphere(data.Point(0,20,0),
                                  2,
                                  data.Color(0.255,0.255,0.255),
                                  data.Finish(0.5,0.4,0.5,0.05)),
                      data.Sphere(data.Point(0,10,0),
                                  0.5,
                                  data.Color(0,0.17,0.145),
                                  data.Finish(0.5,0.4,0.5,0.05))]
       ambient_color = data.Color(0.25,0.5,0.75)
       light = data.Light(data.Point(-100.0,100.0,-100.0),
                          data.Color(1.5,1.5,1.5))
       eye_position = data.Point(0,0,-14)
       cr = cast.cast_ray(ray,sphere_list,ambient_color,light,eye_position)
       inter_point = collisions.sphere_intersection_point(ray,
                                                          sphere_list[1])
       normal = collisions.sphere_normal_at_point(sphere_list[1],
                                                  inter_point)
       off_pt = cast.find_pt_off_sphere(inter_point,normal)
       l_dir = vector_math.normalize_vector(
                 vector_math.vector_from_to(off_pt,
                                            light.pt))
       l_dot_n = vector_math.dot_vector(normal,l_dir)
       diffuse_list = cast.determine_diffuse_contribution(sphere_list[1],
                                                          off_pt,
                                                          light,normal,
                                                          sphere_list,l_dir,
                                                          l_dot_n)
       spec_list = cast.determine_specular_contribution(l_dir,l_dot_n,normal,
                                                        eye_position, off_pt,light.color,
                                                        sphere_list[1].finish)
       self.assertEqual(cr, data.Color(0 + diffuse_list[0] + spec_list[0],
                                       0.0425 + diffuse_list[1] + spec_list[1],
                                       0.054375 + diffuse_list[2] + spec_list[2]))

   def test_cast_ray_1(self):
       ray = data.Ray(data.Point(0,10,6),
                      data.Vector(0,0,-2))
       sphere_list = [data.Sphere(data.Point(0,10,-2),
                                  3,
                                  data.Color(0,0.5,1.0),
                                  data.Finish(0.5,0.4,0.5,0.05)),
                      data.Sphere(data.Point(0,10,-20),
                                  0.5,
                                  data.Color(0,0.3,0.2),
                                  data.Finish(0.5,0.4,0.5,0.05))]
       ambient_color = data.Color(0.25,0.5,0.75)
       light = data.Light(data.Point(-100.0,100.0,-100.0),
                          data.Color(1.5,1.5,1.5))
       eye_position = data.Point(0,0,-14)
       cr = cast.cast_ray(ray,sphere_list,ambient_color,light,eye_position)
       inter_point = collisions.sphere_intersection_point(ray,
                                                          sphere_list[0])
       normal = collisions.sphere_normal_at_point(sphere_list[0],
                                                  inter_point)
       off_pt = cast.find_pt_off_sphere(inter_point,normal)
       l_dir = vector_math.normalize_vector(
                 vector_math.vector_from_to(off_pt,
                                            light.pt))
       l_dot_n = vector_math.dot_vector(normal,l_dir)
       diffuse_list = cast.determine_diffuse_contribution(sphere_list[0],
                                                          off_pt,
                                                          light,normal,
                                                          sphere_list,
                                                          l_dir,l_dot_n)
       spec_list = cast.determine_specular_contribution(l_dir,l_dot_n,normal,
                                                        eye_position, off_pt,light.color,
                                                        sphere_list[0].finish)
       self.assertEqual(cr,data.Color(0 + diffuse_list[0]+ spec_list[0],
                                      0.125 + diffuse_list[1] + spec_list[1],
                                      0.375 + diffuse_list[2] + spec_list[2]))

   def test_cast_ray_2(self):
       ray = data.Ray(data.Point(0,10,6),
                      data.Vector(0,0,-2))
       sphere_list = [data.Sphere(data.Point(20,10,-2),
                                  3,
                                  data.Color(0.0,0.0,0.0),
                                  data.Finish(0.5,0.4,0.5,0.05)),
                      data.Sphere(data.Point(30,10,-20),
                                  0.5,
                                  data.Color(0,0.0,0.0),
                                  data.Finish(0.5,0.4,0.5,0.05))]
       ambient_color = data.Color(0.25,0.5,0.75)
       light = data.Light(data.Point(-100.0,100.0,-100.0),
                          data.Color(1.5,1.5,1.5))
       eye_position = data.Point(0,0,-14)
       cr = cast.cast_ray(ray,sphere_list,ambient_color,light,eye_position)
       self.assertEqual(cr, ambient_color)      
   
   def test_frange(self):
       min_i = -1
       max_i = 1
       jump = .5
       result_list = cast.frange(min_i,max_i,jump)
       self.assertEqual(result_list,[-1,-0.5,0,0.5])

   def test_frange_again(self):
       min_i = 20.08
       max_i = 20.11
       jump = .01
       result_list = cast.frange(min_i,max_i,jump)
       self.assertEqual(result_list,[20.08,20.09,20.1])

   def test_reverse_frange(self):
       min_i = -1
       max_i = 1
       jump = 0.5
       result_list = cast.reverse_frange(min_i,max_i,jump)
       self.assertEqual(result_list,[1,0.5,0,-0.5])

   def test_reverse_frange_again(self):
       min_i = 20.08
       max_i = 20.11
       jump = 0.01
       result_list = cast.reverse_frange(min_i,max_i,jump)
       self.assertAlmostEqual(result_list[0],20.11)
       self.assertAlmostEqual(result_list[1],20.1)
       self.assertAlmostEqual(result_list[2],20.09)

   def test_color_eq(self):
       color1 = data.Color(0.127,0.25,0.54)
       color2 = data.Color(0.127,0.25,0.54)
       self.assertEqual(color1,color2)

   def test_color_eq_again(self):
       color1 = data.Color(0.1,0,0.255)
       color2 = data.Color(0.1,0,0.255)
       self.assertEqual(color1,color2)

   def test_float_to_ppm(self):
       result = cast.float_to_ppm(data.Color(0.2,0.3,0.4))
       self.assertEqual(result,data.Color(51,77,102))

   def test_float_to_ppm_again(self):
       result = cast.float_to_ppm(data.Color(1.0,0,0.43))
       self.assertEqual(result,data.Color(255,0,110))   

   def test_finish(self):
       fin = data.Finish(0.4,0.5,0.5,0.05)
       self.assertAlmostEqual(fin.ambient,0.4)
       self.assertAlmostEqual(fin.diffuse,0.5)

   def test_finish_again(self):
       fin = data.Finish(0.0,0.5,0.5,0.05)
       self.assertAlmostEqual(fin.ambient,0.0)
       self.assertAlmostEqual(fin.diffuse,0.5)

   def test_finish_eq(self):
       fin1 = data.Finish(0.42,0.5,0.5,0.05)
       fin2 = data.Finish(0.42,0.5,0.5,0.05)
       self.assertEqual(fin1,fin2)

   def test_finish_eq_again(self):
       fin1 = data.Finish(0.0,0.3,0.5,0.05)
       fin2 = data.Finish(0.0,0.3,0.5,0.05)
       self.assertEqual(fin1,fin2)

   def test_light(self):
       light = data.Light(data.Point(0,0,0),
                          data.Color(1.5,1.5,1.5))
       self.assertEqual(light.pt,data.Point(0,0,0))
       self.assertEqual(light.color,data.Color(1.5,1.5,1.5))

   def test_light_again(self):
       light = data.Light(data.Point(-100,100,-100),
                          data.Color(1.2,1.2,1.2))
       self.assertEqual(light.pt,data.Point(-100,100,-100))
       self.assertEqual(light.color,data.Color(1.2,1.2,1.2))

   def test_light_eq(self):
       light1 = data.Light(data.Point(0,0,0),
                           data.Color(1.5,1.5,1.5))
       light2 = data.Light(data.Point(0,0,0),
                           data.Color(1.5,1.5,1.5))
       self.assertEqual(light1,light2)

   def test_light_eq_again(self):
       light1 = data.Light(data.Point(-100,100,-100),
                           data.Color(1.2,1.2,1.2))
       light2 = data.Light(data.Point(-100,100,-100),
                           data.Color(1.2,1.2,1.2))
       self.assertEqual(light1,light2)

   def test_find_pt_off_sphere(self):
       sphere = data.Sphere(data.Point(0,0,0),
                            1,
                            data.Color(0,0,0),
                            data.Finish(0.5,0.5,0.5,0.05))
       point = data.Point(0,0,1)
       normal = collisions.sphere_normal_at_point(sphere,point)
       off_pt = cast.find_pt_off_sphere(point,normal)
       self.assertEqual(off_pt, data.Point(0,0,1.01))                      

   def test_find_pt_off_sphere_again(self):
       sphere = data.Sphere(data.Point(1,6,2),
                            2,
                            data.Color(1,1,1),
                            data.Finish(0.2,0.7,0.5,0.05))
       point = data.Point(1,8,2)
       normal = collisions.sphere_normal_at_point(sphere,point)
       off_pt = cast.find_pt_off_sphere(point,normal)
       self.assertEqual(off_pt, data.Point(1,8.01,2))

   def test_get_diffuse_contribution(self):
       sphere = data.Sphere(data.Point(0,0,0),
                            1,
                            data.Color(0.5,0.7,0.8),
                            data.Finish(0.5,0.5,0.5,0.05))
       light = data.Light(data.Point(0,0,100),
                          data.Color(1.5,1.2,1.3))
       inter_point = data.Point(0,0,1)
       normal = collisions.sphere_normal_at_point(sphere,inter_point)
       inter_list = []
       off_pt = cast.find_pt_off_sphere(inter_point,normal)
       dir_vect = vector_math.normalize_vector(vector_math.vector_from_to(
                                                           off_pt,
                                                           light.pt))
       ray = data.Ray(off_pt,dir_vect)
       result = cast.get_diffuse_contribution(sphere,light,ray,inter_list,
                                            normal,dir_vect,off_pt)
       self.assertEqual(result[0],(vector_math.dot_vector(normal,
                                                          dir_vect) *
                                   1.5 * 0.5 * 0.5))
       self.assertEqual(result[1],(vector_math.dot_vector(normal,
                                                          dir_vect) *
                                   1.2 * 0.7 * 0.5))
       self.assertEqual(result[2],(vector_math.dot_vector(normal,
                                                          dir_vect) *
                                   1.3 * 0.8 * 0.5))  

   def test_get_diffuse_contribution_1(self):
       sphere = data.Sphere(data.Point(0,0,0),
                            1,
                            data.Color(0.5,0.7,0.8),
                            data.Finish(0.5,0.5,0.5,0.05))
       light = data.Light(data.Point(0,0,100),
                          data.Color(1.5,1.2,1.3))
       inter_point = data.Point(0,0,1)
       normal = collisions.sphere_normal_at_point(sphere,inter_point)
       inter_list = [(data.Sphere(data.Point(0,0,20),
                                  1,
                                  data.Color(0.5,0.7,0.8),
                                  data.Finish(0.5,0.5,0.5,0.05)),
                      data.Point(0,0,19))]
       off_pt = cast.find_pt_off_sphere(inter_point,normal)
       dir_vect = vector_math.normalize_vector(vector_math.vector_from_to(
                                                           off_pt,
                                                           light.pt))
       ray = data.Ray(off_pt,dir_vect)
       result = cast.get_diffuse_contribution(sphere,light,ray,inter_list,
                                            normal,dir_vect,off_pt)
       self.assertEqual(result[0],0)
       self.assertEqual(result[1],0)
       self.assertEqual(result[2],0)

   def test_get_diffuse_contribution_2(self):
       sphere = data.Sphere(data.Point(0,0,0),
                            1,
                            data.Color(0.5,0.7,0.8),
                            data.Finish(0.5,0.5,0.5,0.05))
       light = data.Light(data.Point(0,0,100),
                          data.Color(1.5,1.2,1.3))
       inter_point = data.Point(0,0,1)
       normal = collisions.sphere_normal_at_point(sphere,inter_point)
       inter_list = [(data.Sphere(data.Point(0,0,102),
                                  1,
                                  data.Color(0.5,0.7,0.8),
                                  data.Finish(0.5,0.5,0.5,0.05)),
                      data.Point(0,0,101))]
       off_pt = cast.find_pt_off_sphere(inter_point,normal)
       dir_vect = vector_math.normalize_vector(vector_math.vector_from_to(
                                                           off_pt,
                                                           light.pt))
       ray = data.Ray(off_pt,dir_vect)
       result = cast.get_diffuse_contribution(sphere,light,ray,inter_list,
                                              normal,dir_vect,off_pt)
       self.assertEqual(result[0],(vector_math.dot_vector(normal,
                                                          dir_vect) *
                                   1.5 * 0.5 * 0.5))
       self.assertEqual(result[1],(vector_math.dot_vector(normal,
                                                          dir_vect) *
                                   1.2 * 0.7 * 0.5))
       self.assertEqual(result[2],(vector_math.dot_vector(normal,
                                                          dir_vect) *
                                   1.3 * 0.8 * 0.5))

   def test_determine_diffuse_contribution(self):
       sphere = data.Sphere(data.Point(0,0,0),
                            1,
                            data.Color(0.5,0.7,0.8),
                            data.Finish(0.5,0.5,0.5,0.05))
       light = data.Light(data.Point(0,0,100),
                          data.Color(1.5,1.2,1.3))
       inter_point = data.Point(0,0,1)
       inter_list = [(data.Sphere(data.Point(0,0,102),
                                  1,
                                  data.Color(0.5,0.7,0.8),
                                  data.Finish(0.5,0.5,0.5,0.05)),
                      data.Point(0,0,101))]
       normal = collisions.sphere_normal_at_point(sphere,inter_point)
       off_pt = cast.find_pt_off_sphere(inter_point,normal)
       dir_vect = vector_math.normalize_vector(vector_math.vector_from_to(
                                                           off_pt,
                                                           light.pt))
       ray = data.Ray(off_pt,dir_vect)
       sphere_list = []
       l_dir = vector_math.normalize_vector(
                 vector_math.vector_from_to(off_pt,
                                            light.pt))
       l_dot_n = vector_math.dot_vector(normal,l_dir)
       result = cast.determine_diffuse_contribution(sphere,off_pt,light,
                                                    normal,sphere_list,
                                                    l_dir,l_dot_n)
       self.assertEqual(result[0],
                        cast.get_diffuse_contribution(sphere,light,ray,
                                                      inter_list,normal,
                                                      dir_vect,off_pt)[0])
       self.assertEqual(result[1],
                        cast.get_diffuse_contribution(sphere,light,ray,
                                                      inter_list,normal,
                                                      dir_vect,off_pt)[1])
       self.assertEqual(result[2],
                        cast.get_diffuse_contribution(sphere,light,ray,
                                                      inter_list,normal,
                                                      dir_vect,off_pt)[2])

   def test_determine_diffuse_contribution_again(self):
       sphere = data.Sphere(data.Point(0,0,0),
                            1,
                            data.Color(0.5,0.7,0.8),
                            data.Finish(0.5,0.5,0.5,0.05))
       light = data.Light(data.Point(0,0,-100),
                          data.Color(1.5,1.2,1.3))
       inter_point = data.Point(0,0,1)
       inter_list = [(data.Sphere(data.Point(0,0,102),
                                  1,
                                  data.Color(0.5,0.7,0.8),
                                  data.Finish(0.5,0.5,0.5,0.05)),
                      data.Point(0,0,101))]
       normal = collisions.sphere_normal_at_point(sphere,inter_point)
       off_pt = cast.find_pt_off_sphere(inter_point,normal)
       dir_vect = vector_math.normalize_vector(vector_math.vector_from_to(
                                                           off_pt,
                                                           light.pt))
       ray = data.Ray(off_pt,dir_vect)
       sphere_list = []
       l_dir = vector_math.normalize_vector(
                 vector_math.vector_from_to(off_pt,
                                            light.pt))
       l_dot_n = vector_math.dot_vector(normal,l_dir)
       result = cast.determine_diffuse_contribution(sphere,off_pt,light,
                                                    normal,sphere_list,
                                                    l_dir,l_dot_n)
       self.assertEqual(result[0],0)
       self.assertEqual(result[1],0)
       self.assertEqual(result[2],0)   

   def test_determine_specular_contribution(self):
       l_dir = data.Vector(1,0,0)
       l_dot_n = 0
       normal = data.Vector(0,0,1)
       eye_position = data.Point(5,5,5)
       off_pt = data.Point(7,7,7)
       light_color = data.Color(0.5,0.5,0.5)
       finish = data.Finish(0.5,0.5,0.5,0.05)
       result = cast.determine_specular_contribution(l_dir,l_dot_n,normal,
                                                     eye_position,off_pt,
                                                     light_color,finish)
       self.assertAlmostEqual(result[0],0)
       self.assertAlmostEqual(result[1],0)
       self.assertAlmostEqual(result[2],0)

   def test_determine_specular_contribution(self):
       l_dir = data.Vector(1,0,0)
       l_dot_n = 0
       normal = data.Vector(0,1,0)
       eye_position = data.Point(3,3,3)
       off_pt = data.Point(4,4,4)
       light_color = data.Color(0.5,0.2,0.7)
       finish = data.Finish(0.5,0.5,0.5,0.5)
       result = cast.determine_specular_contribution(l_dir,l_dot_n,normal,
                                                     eye_position,off_pt,
                                                     light_color,finish)
       self.assertAlmostEqual(result[0],0.0833333)
       self.assertAlmostEqual(result[1],0.0333333)
       self.assertAlmostEqual(result[2],0.11666666)
       
      








 


if __name__ == "__main__":
    unittest.main()
