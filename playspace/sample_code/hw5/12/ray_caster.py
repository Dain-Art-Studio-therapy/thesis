__author__ = 'Jarrett'

import sys
import cast
import data
import commandline


def convert_float(string):
    num_list = []

    for e in string:
        try:
            num = float(e)
        except:
            print "Please input float values for each sphere parameter"
            sys.exit()

        num_list.append(num)

    return num_list


def create_sphere(parameters):
    # parameters should be in the order of:
    # x y z radius r g b ambient diffuse specular roughness
    center = data.Point(parameters[0], parameters[1], parameters[2])
    radius = parameters[3]
    color = data.Color(parameters[4], parameters[5], parameters[6])
    finish = data.Finish(parameters[7], parameters[8], parameters[9], parameters[10])

    return data.Sphere(center, radius, color, finish)


def main(cast_args, file = "image.ppm"):
    min_x = cast_args[0][0]
    max_x = cast_args[0][1]
    min_y = cast_args[0][2]
    max_y = cast_args[0][3]
    height = cast_args[0][4]
    width = cast_args[0][5]
    eye = cast_args[1]
    ambient = cast_args[2]
    light = cast_args[3]
    sphere_list = cast_args[4]

    with open(file, "w") as f:
        pixel_list = cast.cast_all_rays(min_x, max_x, min_y, max_y, height, width, eye, sphere_list, ambient, light)

        f.write(pixel_list)


if (__name__ == "__main__"):

    cmd_arguments = sys.argv
    x = commandline.command_inputs(sys.argv)
    main(x)



