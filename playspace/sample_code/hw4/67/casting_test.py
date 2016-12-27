from cast import *

def test_cast_all_rays():
   eye_point = Point(0.0, 0.0, -14.0)
   sphere_1 = Sphere(Point(1.0, 1.0, 0.0), 2.0, Color(0.0, 0.0, 1.0), Finish(0.2, 0.4, 0.5, 0.05))
   sphere_2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0), Finish(0.4, 0.4, 0.5, 0.05))
   # sphere_3 = Sphere(Point(2.0, 3.0, 0.0), 1.0, Color(0.0, 1.0, -1.0), Finish(0.5, 0.4, 0.5, 0.05))
   sphere_list = [sphere_1, sphere_2]
   light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
   cast_all_rays(-10.0, 10.0, -7.5, 7.5, 1024, 768, eye_point, sphere_list, Color(1.0, 1.0, 1.0), light)
   # cast_all_rays(0.05859357, 0.44921857, 2.03125, 2.421875, 20.0, 20.0, eye_point, sphere_list)

if __name__ == "__main__":
  test_cast_all_rays()
