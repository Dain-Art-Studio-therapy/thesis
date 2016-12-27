import math
import cast
import data
import collisions
import vector_math
import sys
import commandline

def main():
   f = commandline.open_file()
   sphere_list = commandline.get_sphere(f)
   view_list = commandline.check_view()
   eye_point = commandline.check_eye()
   light = commandline.check_light()
   ambience = commandline.check_ambience()
   
   min_x = view_list[0]
   max_x = view_list[1]
   min_y = view_list[2]
   max_y = view_list[3]
   width = view_list[4]
   height = view_list[5]
   print ambience.r
   print ambience.g
   print ambience.b
   
   cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambience, light)


if __name__ == '__main__':
   main()
