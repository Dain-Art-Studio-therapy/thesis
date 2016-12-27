import sys
import commandline
import cast

def main(argv):
   view = commandline.get_view(argv)
   eye = commandline.get_eye(argv)
   light = commandline.get_light(argv)         
   ambient = commandline.get_ambient(argv)
   sphere_list = commandline.get_sphere_list(argv[1])
   cast.cast_all_rays(view[0],view[1],view[2],
                      view[3],int(view[4]),int(view[5]),
                      eye,sphere_list,ambient,light)

if __name__ == '__main__':
   main(sys.argv)
