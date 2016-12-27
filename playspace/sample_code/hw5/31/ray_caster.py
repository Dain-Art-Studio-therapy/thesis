import sys
from cast import *
from commandline import *

def main(argv):
    sphere_list = get_spheres(open_file(argv))
    eye = find_eye(argv)
    view = find_view(argv)
    light = find_light(argv)
    ambient = find_ambient(argv)
    file = open_image_file('image.ppm', 'wb')    
    
    print >> file,  'P3'
    print >> file, view[4], view[5]
    print >> file, 255
    cast_all_rays(view[0], view[1], view[2], view[3], view[4],
                  view[5], eye, sphere_list, ambient, light, file)
        




if  __name__ == '__main__':
     main(sys.argv)


