import sys
import puzzle
import math



def main(argv):  #inputfile, row, col, radius
    cmdline_length(argv)
    with open_file(argv[1], 'r') as f:
        splits = puzzle.split_pixels(f)
        floats = puzzle.float_list(splits)
        pixels = fade_groups_of_3(floats)
        width = splits[1]
        height = splits[2]
        loc = find_position(pixels, width, height, argv)






    with open_file('faded.ppm', 'w') as file_object:
        print>> file_object, splits[0]
        print>> file_object, splits[1] + " " + splits[2]
        print>> file_object, splits[3]
        print_new_pixels(loc, file_object)


def cmdline_length(argv):
    if 1 <= len(argv) < 4:
        print 'Not enough arguments'
        exit(1)


def open_file(name, mode):
    try:
        return open(name, mode)
    except IOError as e:
        print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
        exit(1)


def fade_groups_of_3(float_list):
    new_list = []
    for i in range(0, len(float_list), 3):
        if (i + 2) < len(float_list):
            new_list.append([float_list[i], float_list[i + 1], float_list[i + 2]])
        elif (i + 1) < len(float_list):
            new_list.append([float_list[i], float_list[i + 1]])
    return new_list


def find_position(pixel_grid, width, height, argv):
    new_pixel_list = []
    pos = 0
    for y in range(int(height)):
        for x in range(int(width)):
            r = pixel_grid[pos][0] #row position for each [r g b]
            g = pixel_grid[pos][1]
            b = pixel_grid[pos][2]
            pos += 1
            new_pixel = [r, g, b]
            scaled_pix = scale_pixel(new_pixel, argv, x, y)
            new_pixel_list.append(scaled_pix)
    return new_pixel_list


def find_distance(x, y, argv):
    input_x = int(argv[3])
    input_y = int(argv[2])
    distance = math.sqrt(((input_x - x)**2) + ((input_y - y)**2))
    return distance


def check_scalar(scalar):
    if scalar < 0.2:
        scalar = 0.2
        return scalar
    else:
        return scalar

def scale_pixel(new_pixel, argv, col, row): #new_pixel = (r, g, b)
    radius = int(argv[4])
    old_red = new_pixel[0]
    old_green = new_pixel[1]
    old_blue = new_pixel[2]

    dist = find_distance(col, row, argv)
    scalar = (radius - dist) / radius
    scalar = check_scalar(scalar)
    new_red = old_red * scalar
    new_green = old_green * scalar
    new_blue = old_blue * scalar
    return [new_red, new_green, new_blue]


def print_new_pixels(new_pixels, file_object):
    for list in new_pixels:
        print >> file_object, int(list[0]), int(list[1]), int(list[2]),
    print '\n'

if __name__ == '__main__':
    main(sys.argv)



