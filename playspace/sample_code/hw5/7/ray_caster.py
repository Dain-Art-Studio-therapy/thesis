#ray_caster
#functionality for commandline.py to use
#open file for sphere_list
#is the file actually being run

import commandline
import cast
import sys

def main(argv):

  sphere_list = commandline.main(argv)

  eye = commandline.cmdline_eye(argv)

  view = commandline.cmdline_view(argv)

  ambient = commandline.cmdline_ambient(argv)

  light = commandline.cmdline_light(argv)

  cast.cast_all_rays(view[0], view[1], view[2], view[3],
                 view[4], view[5], eye, sphere_list, ambient, light)





if __name__ == '__main__':
   main(sys.argv)



