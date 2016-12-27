__author__ = 'Jarrett'

import sys
import data
import ray_caster as caster

def read_spheres(file):
    sphere_list = []
    line_number = 1

    try:
        f = open(file, "r")
    except:
        print "Please input a valid file name."
        sys.exit()

    for line in f:
        num_list = line.split()

        if (len(num_list) != 11):
            print str.format("malformed sphere on line {0} ... skipping.", line_number)

        else:
            sphere_parameters = caster.convert_float(num_list)
            new_sphere = caster.create_sphere(sphere_parameters)
            sphere_list.append(new_sphere)

        line_number = line_number + 1

    return sphere_list


def check_eye(argv):
    # set the default eye values
    eye_x = 0.0
    eye_y = 0.0
    eye_z = -14.0

    for i in range(len(argv)):
            if (argv[i] == "-eye"):
                try:
                    eye_x = float(argv[i + 1])
                except:
                    print "Please input a float value for the x coordinate."
                    sys.exit()

                try:
                    eye_y = float(argv[i + 2])
                except:
                    print "Please input a float value for the y coordinate."
                    sys.exit()

                try:
                    eye_z = float(argv[i + 3])
                except:
                    print "Please input a float value for the z coordinate."
                    sys.exit()

    return data.Point(eye_x, eye_y, eye_z)

def check_window(argv):
    # set the default window values
    min_x = -10.0
    max_x = 10.0
    min_y = -7.5
    max_y = 7.5
    width = 1024
    height = 768

    for i in range(len(argv)):
        if (argv[i] == "-view"):
            try:
                min_x = float(argv[i + 1])
            except:
                print "Please input a float value for the min_x view value."
                sys.exit()

            try:
                max_x = float(argv[i + 2])
            except:
                print "Please input a float value for the max_x scene value."
                sys.exit()

            try:
                min_y = float(argv[i + 3])
            except:
                print "Please input a float value for the min_y view value."
                sys.exit()

            try:
                max_y = float(argv[i + 4])
            except:
                print "Please input a float value for the max_y view value."
                sys.exit()

            try:
                width = float(argv[i + 5])
            except:
                print "Please input a float value for the scene width value."
                sys.exit()

            try:
                height = float(argv[i + 6])
            except:
                print "Please input a float value for the scene height value."
                sys.exit()

    return (min_x, max_x, min_y, max_y, width, height)


def check_light(argv):
    # set default light values
    light_x = -100.0
    light_y = 100.0
    light_z = -100.0
    light_r = 1.5
    light_g = 1.5
    light_b = 1.5

    for i in range(len(argv)):
        if (argv[i] == "-light"):
            try:
                light_x = float(argv[i + 1])
            except:
                print "Please input a float value for the light's x coordinate."
                sys.exit()

            try:
                light_y = float(argv[i + 2])
            except:
                print "Please input a float value for the light's y coordinate."
                sys.exit()

            try:
                light_z = float(argv[i + 3])
            except:
                print "Please input a float value for the light's z coordinate."
                sys.exit()

            try:
                light_r = float(argv[i + 4])
            except:
                print "Please input a float value for the light's red color value."
                sys.exit()

            try:
                light_g = float(argv[i + 5])
            except:
                print "Please input a float value for the light's green color value."
                sys.exit()

            try:
                light_b = float(argv[i + 6])
            except:
                print "Please input a float value for the light's blue color value."
                sys.exit()

    return data.Light(data.Point(light_x, light_y, light_z), data.Color(light_r, light_g, light_b))


def check_ambient(argv):
    # set the default ambient values
    ambient_r = 1.0
    ambient_g = 1.0
    ambient_b = 1.0

    for i in range((len(argv))):
        if (argv[i] == "-ambient"):
            try:
                ambient_r = float(argv[i + 1])
            except:
                print "Please input a float value for the ambient's red color value."
                sys.exit()

            try:
                ambient_g = float(argv[i + 2])
            except:
                print "Please input a float value for the ambient's green color value."
                sys.exit()

            try:
                ambient_b = float(argv[i + 3])
            except:
                print "Please input a float value for the ambient's blue color value."
                sys.exit()

    return data.Color(ambient_r, ambient_g, ambient_b)



def command_inputs(argv):
    if (len(argv) == 1 and argv[1] == "ray_caster.py"):
        print "usage: python ray_caster.py <filename> [-eye x y z]" \
              "[-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]"
        sys.exit()

    else:
        file = argv[1]

        spheres = read_spheres(file)
        window = check_window(argv)
        eye = check_eye(argv)
        ambient = check_ambient(argv)
        light = check_light(argv)

        return [window, eye, ambient, light, spheres]


