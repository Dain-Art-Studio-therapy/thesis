import sys
from cast import *
from commandline import *
from data import *


def main(argv):
    if len(argv) < 2:
        print 'Usage: python ray_caster <filename>\n\
              [-eye x y z]\n\
              [-view min_x max_x min_y max_y width height]\n\
              [-light x y z r g b]\n\
              [-ambient r g b]'
       	return None
    
    with open_file(argv[1], 'rb') as in_fl:
        sphere_list = process_spheres(in_fl)

#--------------------default values--------------------

    eye_point = [0.0, 0.0, -14.0]
    view = [-10, 10, -7.5, 7.5, 1024, 768]
    light = [-100.0, 100.0, -100.0, 1.5, 1.5, 1.5]
    amb_lght_clr = [1.0, 1.0, 1.0]

#------------------------------------------------------

    if len(argv) > 2:
        for cm in range(len(argv)):
            if argv[cm] == '-eye':
                eye_point = process_eye_flag(argv, cm, eye_point)
            if argv[cm] == '-view':
                view = process_view_flag(argv, cm, view)
            if argv[cm] == '-light':
                light = process_light_flag(argv, cm, light)
            if argv[cm] == '-ambient':
                amb_lght_clr = process_ambient_flag(argv, cm, amb_lght_clr)

    with open('image.ppm', 'wb') as out_fl:
        cast_all_rays(view[0], view[1], view[2], view[3], view[4], view[5], 
                      Point(eye_point[0], eye_point[1], eye_point[2]), 
                      sphere_list, 
                      Color(amb_lght_clr[0], amb_lght_clr[1], 
                            amb_lght_clr[2]),
                      Light(Point(light[0], light[1], light[2]),
                            Color(light[3], light[4], light[5])), 
                      out_fl)

#-------------------------------helper functions-------------------------------

def open_file(in_fl, mode):
    try:
        return open(in_fl, mode)
    except IOError as e:
        print >> sys.stderr, 'Cannot open file'.format(in_fl, e.strerror)
        exit()


def process_spheres(in_fl):
    expected_nums_in_line = 11
    spheres = []
    sphere_number = 0
    for line in in_fl:
        sphere_number += 1
        data = line.split()
        if len(data) == expected_nums_in_line:
            try:
                sphere = Sphere(Point(float(data[0]), float(data[1]), 
                                      float(data[2])),
                                float(data[3]),
                                Color(float(data[4]), float(data[5]), 
                                      float(data[6])),
                                Finish(float(data[7]), float(data[8]), 
                                       float(data[9]), float(data[10])))
                spheres.append(sphere)
            except:
                print 'Sphere', sphere_number, 'not valid'
        else:
            print 'Sphere', sphere_number, 'not valid'
    return spheres


if __name__ == '__main__':
    main(sys.argv)

