import commandline
import data
import cast
import sys

def create_file():
   args = commandline.main(sys.argv)
   sphere_list = args[0]
   eye_point = args[1][0]
   view = args[1][1]
   light = args[1][2]
   ambient = args[1][3]

   cast.cast_all_rays(view[0], view[1], view[2], view[3], view[4], view[5], \
   eye_point, sphere_list, ambient, light)

if __name__ == '__main__':
   create_file()
