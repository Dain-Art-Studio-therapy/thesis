from cast import *
from data import *


if __name__ == '__main__':
  color1 = Color(0.0, 0.0, 1.0)
  finish1 = Finish(0.2, 0.4, 0.5, 0.05)
  sphere1 = Sphere(Point(1.0, 1.0, 0.0), 2, color1, finish1)
  color2 = Color(1.0, 0.0, 0.0)
  finish2 = Finish(0.4, 0.4, 0.5, 0.05)
  sphere2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, color2, finish2)
  eye_point = Point(0.0, 0.0, -14.0)
  light_point = Point(-100.0, 100.0, -100.0)
  light_color = Color(1.5, 1.5, 1.5)
  light = Light(light_point, light_color)

  ambient_light = Color(1.0, 1.0, 1.0)

  sphere_list = [sphere1, sphere2]
  cast_all_rays(-10, 10, -7.5, 7.5, 1024, 768,
                eye_point, sphere_list, ambient_light, light)