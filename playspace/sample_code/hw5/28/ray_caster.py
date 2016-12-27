from cast import *
from commandline import * 
from data import *

sphere_list = sphere_list_maker(filename)
min_x = view_check(argv)
max_x = view_check(argv)
min_y = view_check(argv)
max_y = view_check(argv)
width = view_check(argv)
height = view_check(argv)
eye_point = eye_check(argv)

file_contents = cast_all_rays(min_x, max_x, min_y, max_y, width, height,
		eye_point, sphere_list, ambient_light, light)
fout.write(file_contents)
fout.close()