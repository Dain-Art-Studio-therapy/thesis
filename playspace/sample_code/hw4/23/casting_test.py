from cast import *


def main():


   eye_point = Point(0.0, 0.0, -14.0)
   s1 = Sphere(Point(1.0, 1.0, 0.0), 2.0, Color(0.0, 0.0, 1.0), Finish(0.2, 
      0.4, 0.5, 0.05))
   s2 = Sphere(Point(0.5, 1.5, -3.0), 0.5, Color(1.0, 0.0, 0.0), Finish(0.4, 
      0.4, 0.5, 0.05))
   sphere_list = [s1, s2]
   ambient_color = Color(1.0, 1.0, 1.0)
   width = 1024
   height = 768
   min_x = -10
   max_x = 10
   min_y = -7.5
   max_y = 7.5
   pt_light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))


   cast_all_rays(min_x, max_x, min_y, max_y, width, height, 
      eye_point, sphere_list, ambient_color, pt_light, eye_point)


if __name__ == '__main__':
   main()
