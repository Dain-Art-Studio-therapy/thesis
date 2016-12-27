from __future__ import with_statement
import sys
import cast
import commandline
from data import *

def main(argv):

    with open_file(argv[1], 'rb') as in_file:

        sphere_list = input_file(in_file)

        if sphere_list == []:
            print >> sys.stderr, 'Input file empty. ' \
                                 'Generating blank image... Hehe'


    settings = commandline.arguments(argv)

    min_x = settings[0]
    max_x = settings[1]
    min_y = settings[2]
    max_y = settings[3]
    width = settings[4]
    height = settings[5]
    eye_point = settings[6]
    light = settings[7]
    ambient_light = settings[8]


    with open_file('image2.ppm', 'w') as output:
        #output.write('P3')
        #output.write(width, height)
        #output.write('255')

        cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height,
                        eye_point, sphere_list, ambient_light, light, output)


def input_file(in_file):

    sphere_list = []
    line_count = 1

    for line in in_file:
        try:
            values = line.split()

            if len(values) == 11:
                sphere_x = convert_to_float(values[0])
                sphere_y = convert_to_float(values[1])
                sphere_z = convert_to_float(values[2])
                sphere_radius = convert_to_float(values[3])
                sphere_r = convert_to_float(values[4])
                sphere_g = convert_to_float(values[5])
                sphere_b = convert_to_float(values[6])
                sphere_ambient = convert_to_float(values[7])
                sphere_diffuse = convert_to_float(values[8])
                sphere_specular = convert_to_float(values[9])
                sphere_roughness = convert_to_float(values[10])
                sphere_point = Point(sphere_x, sphere_y, sphere_z)
                sphere_color = Color(sphere_r, sphere_g, sphere_b)
                sphere_finish = Finish(sphere_ambient, sphere_diffuse,
                                       sphere_specular, sphere_roughness)
                new_sphere = Sphere(sphere_point, sphere_radius,
                                    sphere_color, sphere_finish)
                sphere_list.append(new_sphere)
            else:
                print >> sys.stderr, 'Invalid sphere at line ', \
                    line_count, ' Skipping..'

            line_count += 1
        except:
            print >> sys.stderr, 'Invalid sphere at line ', \
                line_count, ' Skipping...'
            line_count += 1

    return sphere_list


def output_file(output, color):
    string = convert_color_string(color)
    output.write(string[0] + ' ' + string[1] + ' ' + string[2] + '\n')


def convert_color_string(color):
    r = convert_to_string(color.r)
    g = convert_to_string(color.g)
    b = convert_to_string(color.b)

    return (r, g, b)

def convert_to_string(value):
    return str(value)

def convert_to_float(string):
    return float(string)

def open_file(name, mode):
    try:
        return open(name, mode)
    except: #IOError as e:
        print >> sys.stderr, '{0}:{1}'.format(name, e.strerror)
        exit(1)


if __name__ == '__main__':
    main(sys.argv)