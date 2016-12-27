import sys
import data
import cast


def find_flags(argv):
    eye = 0
    view = 0
    light = 0
    ambient = 0
    for i in range(len(argv)):
        eye = eye_flag(argv)
        view = view_flag(argv)
        light = light_flag(argv)
        ambient = ambient_flag(argv)
    return [eye, view, light, ambient]

#argv = [[-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]]

def light_flag(argv):
    default_point = data.Point(-100.0, 100.0, -100.0)
    default_color = data.Color(1.5, 1.5, 1.5)
    default_light = data.Light(default_point, default_color)
    if '-light' in argv:
        l = argv.index('-light')
        try:
            point_x = float(argv[l + 1])
            point_y = float(argv[l + 2])
            point_z = float(argv[l + 3])
            color_r = float(argv[l + 4])
            color_g = float(argv[l + 5])
            color_b = float(argv[l + 6])
            color = data.Color(color_r, color_g, color_b)
            point = data.Point(point_x, point_y, point_z)
            default_light = data.Light(point, color)

        except:
            pass
    return default_light


def view_flag(argv):
    def_min_x = -10.0
    def_max_x = 10.0
    def_min_y = -7.5
    def_max_y = 7.5
    def_width = 1024
    def_height = 768
    if '-view' in argv:
        v = argv.index('-view')
        try:
            min_x = float(argv[v + 1])
            max_x = float(argv[v + 2])
            min_y = float(argv[v + 3])
            max_y = float(argv[v + 4])
            width = int(argv[v + 5])
            height = int(argv[v + 6])
            return [min_x, max_x, min_y, max_y, width, height]

        except:
            pass

    else:
        return [def_min_x, def_max_x, def_min_y, def_max_y, def_width, def_height]


def eye_flag(argv):
    default_eye = data.Point(0.0, 0.0, -14.0)
    if '-eye' in argv:
        e = argv.index('-eye')
        try:
            eye_x = float(argv[e + 1])
            eye_y = float(argv[e + 2])
            eye_z = float(argv[e + 3])
            return data.Point(eye_x, eye_y, eye_z)
        except:
            pass
    return default_eye


def ambient_flag(argv):
    def_ambient_r = 1.0
    def_ambient_g = 1.0
    def_ambient_b = 1.0
    default_ambient = data.Color(def_ambient_r, def_ambient_g, def_ambient_b)
    if '-ambient' in argv:
        a = argv.index('-ambient')
        try:
            ambient_r = float(argv[a + 1])
            ambient_g = float(argv[a + 2])
            ambient_b = float(argv[a + 3])
            return data.Color(ambient_r, ambient_g, ambient_b)
        except:
            pass

    return default_ambient









