import unittest
from data import *
from utility import *
from vector_math import *
from collisions import *
from cast import *

class TestData(unittest.TestCase):
   def test_point_1(self):
      pt1 = Point(1, 2, 3)
      self.assertAlmostEqual(pt1.x, 1)
      self.assertAlmostEqual(pt1.y, 2)
      self.assertAlmostEqual(pt1.z, 3)
      pass

   def test_point_2(self):
      pt2 = Point(4, 5, 6)
      self.assertAlmostEqual(pt2.x, 4)
      self.assertAlmostEqual(pt2.y, 5)
      self.assertAlmostEqual(pt2.z, 6)
      pass

   def test_vec_1(self):
      vector1 = Vector(7, 8, 9)
      self.assertAlmostEqual(vector1.x, 7)
      self.assertAlmostEqual(vector1.y, 8)
      self.assertAlmostEqual(vector1.z, 9)
      pass

   def test_vec_2(self):
      vec2 = Vector(1, 2, 3)
      self.assertAlmostEqual(vec2.x, 1)
      self.assertAlmostEqual(vec2.y, 2)
      self.assertAlmostEqual(vec2.z, 3)
      pass

   def test_ray_1(self):
      raypt1 = Point(4, 5, 6)
      rayvec1 = Vector(7, 8, 9)
      ray1 = Ray(raypt1, rayvec1)
      self.assertAlmostEqual(ray1.pt.x, 4)
      self.assertAlmostEqual(ray1.pt.y, 5)
      self.assertAlmostEqual(ray1.pt.z, 6)
      self.assertAlmostEqual(ray1.dir.x, 7)
      self.assertAlmostEqual(ray1.dir.y, 8)
      self.assertAlmostEqual(ray1.dir.z, 9)
      pass

   def test_ray_2(self):
      raypt2 = Point(1, 2, 3)
      rayvec2 = Vector(4, 5, 6)
      ray2 = Ray(raypt2, rayvec2)
      self.assertAlmostEqual(ray2.pt.x, 1)
      self.assertAlmostEqual(ray2.pt.y, 2)
      self.assertAlmostEqual(ray2.pt.z, 3)
      self.assertAlmostEqual(ray2.dir.x, 4)
      self.assertAlmostEqual(ray2.dir.y, 5)
      self.assertAlmostEqual(ray2.dir.z, 6)
      pass

   def test_sphere_1(self):
      sphpt1 = Point(7, 8, 9)
      sph1 = Sphere(sphpt1, 1.2)
      self.assertAlmostEqual(sph1.center.x, 7)
      self.assertAlmostEqual(sph1.center.y, 8)
      self.assertAlmostEqual(sph1.center.z, 9)
      self.assertAlmostEqual(sph1.radius, 1.2)
      pass

   def test_sphere_2(self):
      sphpt2 = Point(1, 2, 3)
      sph2 = Sphere(sphpt2, 3.4)
      self.assertAlmostEqual(sph2.center.x, 1)
      self.assertAlmostEqual(sph2.center.y, 2)
      self.assertAlmostEqual(sph2.center.z, 3)
      self.assertAlmostEqual(sph2.radius, 3.4)
      pass

   def test_pointeq_1(self):
      pt1 = Point(1, 2, 3)
      pt2 = Point(1, 2, 4)
      self.assertFalse(pt1 ==  pt2)

   def test_pointeq_2(self):
      pt1 = Point(5, 6, 7)
      pt2 = Point(5, 6, 7)
      self.assertTrue(pt1 == pt2)

   def test_vectoreq_1(self):
      vec1 = Vector(2, 3, 4)
      vec2 = Vector(2, 3, 5)
      self.assertFalse(vec1 == vec2)

   def test_veceq_2(self):
      vec1 = Vector(3, 4, 5)
      vec2 = Vector(3, 4, 5)
      self.assertTrue(vec1 == vec2)

   def test_rayeq_1(self):
      pt1 = Point(1, 2, 3)
      dir1 = Vector(4, 5, 6)
      pt2 = Point(7, 8, 9)
      dir2 = Vector(1, 2, 3)
      ray1 = Ray(pt1, dir1)
      ray2 = Ray(pt2, dir2)
      self.assertFalse(ray1 == ray2)

   def test_rayeq_2(self):
      pt1 = Point(1, 2, 3)
      dir1 = Vector(1, 1, 1)
      pt2 = Point(1, 2, 3)
      dir2 = Vector(1, 1, 1)
      ray1 = Ray(pt1, dir1)
      ray2 = Ray(pt2, dir2)
      self.assertTrue(ray1 == ray2)

   def test_spheq_1(self):
      center1 = Point(1, 2, 3)
      center2 = Point(1, 2, 3)
      sph1 = Sphere(center1, 2)
      sph2 = Sphere(center2, 2)
      self.assertTrue(sph1 == sph2)

   def test_spheq_2(self):
      center1 = Point(5, 5, 5)
      center2 = Point(5, 5, 5)
      sph1 = Sphere(center1, 5)
      sph2 = Sphere(center2, 10)
      self.assertFalse(sph1 == sph2)

   def test_scale_1(self):
      vec = Vector(2, 4, 6)
      scaledvec = scale_vector(vec, 2)
      vectest = Vector(4, 8, 12)
      self.assertTrue(scaledvec == vectest)

   def test_scale_2(self):
      vec = Vector(1, 2, 3)
      scaledvec = scale_vector(vec, 1.5)
      vectest = Vector(1.5, 3, 4.5)
      self.assertTrue(scaledvec == vectest)

   def test_dot_1(self):
      vec1 = Vector(1, 2, 3)
      vec2 = Vector(4, 5, 6)
      self.assertAlmostEqual(dot_vector(vec1, vec2), 32)

   def test_dot_2(self):
      vec1 = Vector(7, 8, 9)
      vec2 = Vector(3, 6, 9)
      self.assertAlmostEqual(dot_vector(vec1, vec2), 150)

   def test_length_1(self):
      self.assertAlmostEqual(length_vector(Vector(1, 2, 3)), 3.74165738677)

   def test_length_2(self):
      self.assertAlmostEqual(length_vector(Vector(4, 5, 6)), 8.77496438739)

   def test_normal_1(self):
      vec = Vector(11, 22, 33)
      norm = normalize_vector(vec)
      length = length_vector(vec)
      self.assertTrue(norm.x == vec.x / length and norm.y == vec.y / length and norm.z == vec.z / length)

   def test_normal_2(self):
      vec = Vector(5, 6, 7)
      norm = normalize_vector(vec)
      length = length_vector(vec)
      self.assertAlmostEqual(norm.x, .4767312946)
      self.assertAlmostEqual(norm.y, .5720775535)
      self.assertAlmostEqual(norm.z, .6674238125)
  
   def test_ptdiff_1(self):
      pt1 = Point(0, 0, 0)
      pt2 = Point(4, 56, 7)
      vec = difference_point(pt1, pt2)
      vectest = Vector(-4, -56, -7)
      self.assertTrue(vec == vectest)

   def test_ptdiff_2(self):
      pt1 = Point(1, 2, 3)
      pt2 = Point(10, 10, 10)
      vec = difference_point(pt1, pt2)
      vectest = Vector(-9, -8, -7)
      self.assertTrue(vec == vectest)

   def test_vecdiff_1(self):
      vec1 = Vector(1, 2, 3)
      vec2 = Vector(10, 10, 10)
      vecdiff = difference_vector(vec1, vec2)
      vectest = Vector(-9, -8, -7)
      self.assertTrue(vecdiff == vectest)

   def test_vecdiff_2(self):
      vec1 = Vector(4, 5, 6)
      vec2 = Vector(100, 100, 100)
      vecdiff = difference_vector(vec1, vec2)
      vectest = Vector(-96, -95, -94)
      self.assertTrue(vecdiff == vectest)

   def test_transpt_1(self):
      pt = Point(0, 0, 0)
      vec = Vector(1, 2, 3)
      transpt = translate_point(pt, vec)
      pttest = Point(1, 2, 3)
      self.assertTrue(transpt == pttest)

   def test_transpt_2(self):
      pt = Point(1, 2, 3)
      vec = Vector(12, 34, 56)
      transpt = translate_point(pt, vec)
      pttest = Point(13, 36, 59)
      self.assertTrue(transpt == pttest)

   def test_fromto_1(self):
      frompt = Point(1, 2, 3)
      topt = Point(5, 6, 7)
      vec = vector_from_to(frompt, topt)
      vectest = Vector(4, 4, 4)
      self.assertTrue(vec == vectest)

   def test_fromto_2(self):
      frompt = Point(8, 9, 0)
      topt = Point(3, 2, 1)
      vec = vector_from_to(frompt, topt)
      vectest = Vector(-5, -7, 1)
      self.assertTrue(vec == vectest)

   def test_sphintersect_1(self):
      raypt = Point(0, 0, 0)
      raydir = Vector(0, 0, 1)
      ray = Ray(raypt, raydir)
      center = Point(0, 0, 10)
      sph = Sphere(center, 1)
      intersect = sphere_intersection_point(ray, sph)
      intersecttest = Point(0, 0, 9)
      self.assertTrue(intersect == intersecttest)

   def test_sphintersect_2(self):
      raypt = Point(5, 7, 0)
      raydir = Vector(-1,-1, 0)
      ray = Ray(raypt, raydir)
      center = Point(2, 6, 0)
      sph = Sphere(center, 2)
      intersect = sphere_intersection_point(ray, sph)
      intersecttest = Point(4, 6, 0)
      self.assertTrue(intersect == intersecttest)

   def test_sphintersect_3(self):
      raypt = Point(0, 0, 0)
      raydir = Vector(1, 0, 0)
      ray = Ray(raypt, raydir)
      center = Point(100, 0, 0)
      sph = Sphere(center, 55)
      intersect = sphere_intersection_point(ray, sph)
      intersecttest = Point(45, 0, 0)
      self.assertTrue(intersect == intersecttest)

   def test_sphintersect_4(self):
      raypt = Point(0, 0, 0)
      raydir = Vector(0, 1, 0)
      ray = Ray(raypt, raydir)
      center = Point(0, 20, 0)
      sph = Sphere(center, 4)
      intersect = sphere_intersection_point(ray, sph)
      intersecttest = Point(0, 16, 0)
      self.assertTrue(intersect == intersecttest)

   def test_intersectpts_1(self):
      center1 = Point(1, 1, 0)
      sph1 = Sphere(center1, 1)
      center2 = Point(2, 2, 0)
      sph2 = Sphere(center2, 1)
      sphs = [sph1, sph2]
      raypt = Point(-2, 5, 0)
      raydir = Vector(1, -1, 0)
      ray = Ray(raypt, raydir)
      intersects = find_intersection_points(sphs, ray)
      intersecttest1 = Point(1, 2, 0)
      intersecttest2 = Point(2, 1, 0)
      self.assertTrue(intersects == [(sphs[0], intersecttest1), (sphs[1], intersecttest1)])

   def test_intersectpts_2(self):
      center1 = Point(1, 1, 0)
      sph1 = Sphere(center1, 1)
      center2 = Point(1, -1, 0)
      sph2 = Sphere(center2, 1)
      sphs = [sph1, sph2]
      raypt = Point(0, 257, 0)
      raydir = Vector(0, -10, 0)
      ray = Ray(raypt, raydir)
      intersects = find_intersection_points(sphs, ray)
      intersecttest1 = Point(0, 1, 0)
      intersecttest2 = Point(0, -1, 0)
      self.assertTrue(intersects == [(sphs[0], intersecttest1), (sphs[1], intersecttest2)])

   def test_interceptpts_3(self):
      center1 = Point(1, 0, 0)
      sph1 = Sphere(center1, 1)
      center2 = Point(-1, 0, 0)
      sph2 = Sphere(center2, 1)
      sphs = [sph1, sph2]
      raypt = Point(0, 10, 0)
      raydir = Vector(0, -1, 0)
      ray = Ray(raypt, raydir)
      intersects = find_intersection_points(sphs, ray)
      intersecttest1 = Point(0, 0, 0)
      self.assertTrue(intersects == [(sphs[0], intersecttest1), (sphs[1], intersecttest1)])

   def test_interceptpts_4(self):
      center1 = Point(1, 0, 0)
      sph1 = Sphere(center1, 1)
      center2 = Point(3, 0, 0)
      sph2 = Sphere(center2, 1)
      sphs = [sph1, sph2]
      raypt = Point(2, -10, 0)
      raydir = Vector(0, 1, 0)
      ray = Ray(raypt, raydir)
      intersects = find_intersection_points(sphs, ray)
      intersecttest1 = Point(2, 0, 0)
      self.assertTrue(intersects == [(sphs[0], intersecttest1), (sphs[1], intersecttest1)])

   def test_spherenorm_1(self):
      center = Point(1, 1, 0)
      sph = Sphere(center, sqrt(2))
      pt = Point(0, 0, 0)
      sphnorm = sphere_normal_at_point(sph, pt)
      vectest = Vector(-sqrt(2), -sqrt(2), 0)
      normtest = normalize_vector(vectest)
      self.assertTrue(sphnorm == normtest)

   def test_spherenorm_2(self):
      center = Point(5, 5, 5)
      sph = Sphere(center, 5)
      pt = Point(5, 0, 5)
      sphnorm = sphere_normal_at_point(sph, pt)
      vectest = Vector(0, -5, 0)
      normtest = normalize_vector(vectest)
      self.assertTrue(sphnorm == normtest)

   def test_cast_1(self):
      center1 = Point(1, 0, 0)
      sph1 = Sphere(center1, 1)
      center2 = Point(3, 0, 0)
      sph2 = Sphere(center2, 1)
      sphs = [sph1, sph2]
      raypt = Point(2, -10, 0)
      raydir = Vector(0, 1, 0)
      ray = Ray(raypt, raydir)
      self.assertTrue(cast_ray(ray, sphs))

   def test_cast_2(self):
      center1 = Point(1, 0, 0)
      sph1 = Sphere(center1, 1)
      center2 = Point(3, 0, 0)
      sph2 = Sphere(center2, 1)
      sphs = [sph1, sph2]
      raypt = Point(2, -10, 0)
      raydir = Vector(0, -1, 0)
      ray = Ray(raypt, raydir)
      self.assertFalse(cast_ray(ray, sphs))

  
if __name__ == "__main__":
   unittest.main()
