from sys import argv
from data import *


def float_default(string, num):

    try:
        return float(string)
    except:
        return num


def get_file_name(argv):

    try:        
        return argv[1]
    except:
        print 'usage: python ray_caster.py <filename> [-eye x y z]'
        print '[-view min_x max_x min_y max_y width height]'
        print '[-light x y z r g b] [-ambient r g b]'
        exit()


def get_eye(argv):

    if '-eye' in argv:
        i = argv.index('-eye')
        x = float_default(argv[i+1], 0.0)
        y = float_default(argv[i+2], 0.0)
        z = float_default(argv[i+3], -14.0)
        return Point(x, y, z)
    else:
        return Point(0.0, 0.0, -14.0)


def get_light(argv):

    if '-light' in argv:
        i = argv.index('-light')
        x = float_default(argv[i+1], -100.0)
        y = float_default(argv[i+2], 100.0)
        z = float_default(argv[i+3], -100.0)
        r = float_default(argv[i+4], 1.5)
        g = float_default(argv[i+5], 1.5)        
        b = float_default(argv[i+6], 1.5)
        return Light(Point(x, y, z), Color(r, g, b))
    else:
        return Light(
            Point(-100.0, 100.0, -100.0),
            Color(1.5, 1.5, 1.5)
            )


def get_ambient(argv):

    if '-ambient' in argv:
        i = argv.index('-ambient')
        r = float_default(argv[i+1], 1.0)
        g = float_default(argv[i+2], 1.0)
        b = float_default(argv[i+3], 1.0)
        return Color(r, g, b)
    else:
        return Color(1.0, 1.0, 1.0)


def get_view(argv):

    if '-view' in argv:
        i = argv.index('view')
        min_x = float_default(argv[i+1], -10.0)
        max_x = float_default(argv[i+2], 10.0)
        min_y = float_default(argv[i+3], -7.5)
        max_y = float_default(argv[i+4], 7.5)
        width = float_default(argv[i+5], 1024)
        height = float_default(argv[i+6], 768)
        return min_x, max_x, min_y, max_y, width, height
    else:
        return -10.0, 10.0, -7.5, 7.5, 1024, 768

