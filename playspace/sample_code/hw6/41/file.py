__author__ = 'Jarrett'

import sys
import utility
# opens a file from the commandline arguments
def open_file(argv, mode):
    if(len(argv) == 1):
        print "Please input a file."
        sys.exit()

    else:
        try:
            f = open(argv[1], mode)
        except:
            print "Please input a valid file name."
            sys.exit()

    return f

# reads a file
def read_file(file):
    str_list = []

    for line in file:
        this_line = line.split()
        for e in this_line:
            str_list.append(e)

    file.close()
    return str_list


def parse_format(list):
    format_list = []

    for i in range(len(list)):
        if (i < 4):
            format_list.append(list[i])

    ppm_format = str.format("{0}\n{1} {2}\n{3}",
                            format_list[0], format_list[1],
                            format_list[2], format_list[3])

    return ppm_format


def parse_width(list):
    return int(list[1])


def parse_height(list):
    return int(list[2])


def parse_pixels(list):
    pixel_list = []

    for i in range(len(list)):
        if (i >= 4):
            pixel_list.append(int(list[i]))

    grouped_pixel_list = utility.groups_of_three(pixel_list)
    return grouped_pixel_list


def write_file(name, ppm_format, pixels):
    f = open(name, "w")

    f.write(ppm_format)
    f.write("\n")
    for e in pixels:
        f.write(e)

    f.close()