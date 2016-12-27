__author__ = 'Jarrett'

import sys
import file
import utility

def format_ppm(pixels):
    print "in format_ppm"
    format_list = pixels.split()
    new_format = str.format("{0}\n{1} {2}\n{3}\n",
                            format_list[0], format_list[1],
                            format_list[2], format_list[3])
    print new_format
    return new_format

def decode(pixels):
    decoded_pixels = []

    for e in pixels:
        red = min((e[0] * 10), 255)
        print red
        green = red
        blue = red
        new_pixel = str.format("{0} {1} {2}\n", red, green, blue)
        decoded_pixels.append(new_pixel)

    print "decoded pixels"
    return decoded_pixels

def main(argv):
    print "in main"
    f = file.open_file(argv, "r")
    str_list = file.read_file(f)
    print "finished reading file"
    format_list = file.parse_format(str_list)
    pixel_list = file.parse_pixels(str_list)

    ppm_format = format_ppm(format_list)
    new_pixels = decode(pixel_list)

    file.write_file("hidden.ppm", ppm_format, new_pixels)


if (__name__ == "__main__"):
    arguments = sys.argv
    main(arguments)