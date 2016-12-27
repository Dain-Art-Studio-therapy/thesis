from cast import *
from data import *

min_x = -10
max_x = 10
min_y = -7.5
max_y = 7.5
w = 1024
h = 768

sphere1_point = Point(1.0,1.0,0.0)
sphere1_color = Color(0.0,0.0,1.0)
sphere1_finish = Finish(0.2,0.4,0.5,0.05)
sphere1 = Sphere(sphere1_point,2.0,sphere1_color,sphere1_finish)

sphere2_point = Point(0.5,1.5,-3.0)
sphere2_color = Color(1.0,0.0,0.0)
sphere2_finish = Finish(0.4,0.4,0.5,0.05)
sphere2 = Sphere(sphere2_point,0.5,sphere2_color,sphere2_finish)

sph_lst = [sphere1, sphere2]
eye_pt = Point(0.0,0.0,-14.0)
amb = Color(1.0,1.0,1.0)

lte_pt = Point(-100.0,100.0,-100.0)
lte_color = Color(1.5,1.5,1.5)
lte = Light(lte_pt,lte_color)

cast_all_rays(min_x, max_x, min_y, max_y, w, h,eye_pt,sph_lst,amb,lte)