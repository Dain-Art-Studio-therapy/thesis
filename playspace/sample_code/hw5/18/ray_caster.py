import sys
from commandline import *
from cast import *


# argv = ['ray_caster', 'filename', '-eye', '-view', 'etc...']


OUTFOUTFILE_NAME = 'image.ppm'


def main(argv):
    if len(argv) < 2:
        print 'usage: python ray_caster.py <filename> [-eye x y z]\
               [-view min_x max_x min_y max_y width height]\
               [-light x y z r g b] [-ambient r g b]'
        exit(1)

    with file_open(argv[1], 'rb') as f:
        sphere_list = process_file(f)  # will return LIST of spheres

    view_ = find_view(argv)

    with file_open(OUTFOUTFILE_NAME, 'w') as f:
        cast_all_rays(view_[0], view_[1], view_[2], view_[3], view_[4],\
                      view_[5], find_eye(argv), sphere_list,\
                      find_ambient(argv), find_light(argv), f)


def process_file(f):
    sphere_list = []
    try:
        for line in f:
            elements = line.split()
            ctr = Point(float(elements[0]), float(elements[1]),\
                        float(elements[2]))
            rad = float(elements[3])
            col = Color(float(elements[4]), float(elements[5]),\
                        float(elements[6]))
            finish = Finish(float(elements[7]), float(elements[8]),\
                            float(elements[9]), float(elements[10]))
            sphere_list.append(Sphere(ctr, rad, col, finish))
    except IndexError:
        print 'malformed sphere on line {0} ... skipping'.format(line + 1)
    except ValueError:
        print 'malformed sphere on line {0} ... skipping'.format(line + 1)
    return sphere_list


def file_open(name, mode):
    try:
        return open(name, mode)
    except IOError as e:
        print >> sys.stderr, '{0}:{1}'.format(name, e.strerror)
        exit(1)


if __name__ == '__main__':
    main(sys.argv)
