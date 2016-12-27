__author__ = 'Jarrett'

import sys
import file
import math

# computes the distance between two pixels
def distance(row, col, pixel_row, pixel_col):
    delta_x = col - pixel_col
    delta_y = row - pixel_row

    dist = math.sqrt(delta_x**2 + delta_y**2)

    return dist


# determines the how much fade there is from the
# distance between the center of the fade and the
# radius of the fade
def fade_contribution(pixel, distance, radius):
    effect = max(((radius - distance) / radius), 0.2)

    red = int(pixel[0] * effect)
    green = int(pixel[1] * effect)
    blue = int(pixel[2] * effect)

    faded_pixel = str.format("{0} {1} {2}\n", red, green, blue)

    return faded_pixel

# iterates through all the pixels to fade each one
def fade(row, col, radius, pixels, width):
    pixel_list = []
    pixel_row = 0
    pixel_col = 0

    for i in range(len(pixels)):
        pixel_dist = distance(row, col, pixel_row, pixel_col)
        new_pixel = fade_contribution(pixels[i], pixel_dist, radius)

        pixel_list.append(new_pixel)

        pixel_col = i % width
        if ((i % width) == 0):
            pixel_row = (i - pixel_col) / width
            # pixel_row = pixel_row + 1

        print pixel_col, pixel_col

    return pixel_list


def main(argv):
    # opens the file
    f = file.open_file(argv, "r")
    row = int(argv[2])
    col = int(argv[3])
    radius = int(argv[4])

    # reads and closes the file
    str_list = file.read_file(f)
    format = file.parse_format(str_list)
    pixels = file.parse_pixels(str_list)
    width = file.parse_width(str_list)

    # calculates the faded pixels
    new_pixels = fade(row, col, radius, pixels, width)

    file.write_file("faded.ppm", format, new_pixels)

if (__name__ == "__main__"):
    main(sys.argv)