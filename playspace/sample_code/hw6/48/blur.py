import sys
from blur_groups import *


# (0)-blur.py (1)-infile (2)-[int, neighbor reach]
# neighbor reach - 4

OUTFILE = 'blurred.ppm'
DEFAULT_REACH = 4


def main(argv):
    if len(argv) < 2:
        print 'usage: python blur.py <filename> [neighbor reach]'

    with file_open(OUTFILE, 'w') as out:
        with file_open(argv[1], 'rb') as f:
            pixels = process_file(f, out)
            grid = pixels_to_grid(pixels, f)
            try:
                blur(grid, argv[2], out)
            except IndexError:
                blur(grid, DEFAULT_REACH, out)


def process_pixel(grid, pos_x, pos_y, in_reach, outfile):
    r = 0
    g = 0
    b = 0
    try:
        reach = int(float(in_reach))
    except ValueError:
        print "'{0}' not an integer. Enter an integer."
        exit(1)
    counter = 0
    for y in range(-reach, reach+1):
        for x in range(-reach, reach+1):
            try:
                pixel = grid[pos_y + y][pos_x + x]
                r += pixel.r
                g += pixel.g
                b += pixel.b
                counter += 1
            except IndexError:
                pass
    finalpixel = average_pixel(r, g, b, counter)
    print >> outfile, finalpixel.r, finalpixel.g, finalpixel.b


def blur(grid, n_reach, outfile):
    for y in range(401):
        for x in range(493):
            process_pixel(grid, x, y, n_reach, outfile)


def average_pixel(r, g, b, grid_dimension):
    fR = r/grid_dimension
    fG = g/grid_dimension
    fB = b/grid_dimension
    if fR > 255:
        fR = 255
    if fG > 255:
        fG = 255
    if fB > 255:
        fB = 255
    return Pixel(fR, fG, fB)


def pixels_to_grid(pixel_list, infile):
    header = find_header(infile)
    width = header[1]
    height = header[2]

    grid = [[0 for x in range(width)] for x in range(height)]
    index = 0
    for y in range(height):
        for x in range(width):
            grid[y][x] = pixel_list[index]
            index += 1
    return grid


def find_header(infile):
    counter = 1
    while counter < 4:
        some_line = infile.readline()
        one_line = some_line.split()
        if counter == 1:
            file_format = one_line[0]
        if counter == 2:
            (width, height) = (int(one_line[0]), int(one_line[1]))
        if counter == 3:
            max_value = int(one_line[0])
        counter += 1
    return file_format, width, height, max_value


def print_header(header, outfile):
    print >> outfile, header[0]
    print >> outfile, header[1], header[2]
    print >> outfile, header[3]


def process_file(infile, outfile):
    header = find_header(infile)
    print_header(header, outfile)

    all_pixel_comp = []
    for line in infile:
        for num in line.split():
            all_pixel_comp.append(int(num))
    pixels = groups_of_3(all_pixel_comp)
    all_pixels = [Pixel(e[0], e[1], e[2]) for e in pixels]
    infile.seek(0)
    return all_pixels


def file_open(name, mode):
    try:
        return open(name, mode)
    except IOError as e:
        print >> sys.stderr, '{0}: {1}'.format(name, e.strerror)


if __name__ == '__main__':
    main(sys.argv)