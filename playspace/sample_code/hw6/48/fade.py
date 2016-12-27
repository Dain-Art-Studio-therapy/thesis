import sys
import math
from fade_data imp

OUTFILE = 'faded.ppm'


# (1)file (2)row-y (3)column-x (4)radius


def main(argv):
    if len(argv) < 5:
        print >> sys.stderr, 'usage: python puzzle.py <filename> row column radius'
        exit(1)
    with open_file(OUTFILE, 'w') as outfile:
        with open_file(argv[1], 'rb') as f:
            process_file(f, outfile, argv[4], Pixel(argv[2], argv[3]))


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


def distance(center, pixel):
    return math.sqrt((center.row - pixel.row)**2 +
                     (center.column - pixel.column)**2)


def process_file(infile, outfile, radius, center):
    header = find_header(infile)
    print_header(header, outfile)

    pixel_comp = []
    row = 0
    column = 0
    for line in infile:
        pixel_lines = line.split()
        for i in range(len(pixel_lines)):
            try:
                pixel_comp.append(int(pixel_lines[i]))
            except ValueError:
                pixel_comp.append(pixel_lines[i])
        if len(pixel_comp) == 3:
            new_pixel = scale_pixel_components(pixel_comp, radius, center, Pixel(row, column))
            print >> outfile, new_pixel[0], new_pixel[1], new_pixel[2]
            pixel_comp = []
            column += 1
        if column == header[1]:
            row += 1
            column = 0


def scale_pixel_components(pixel_comp, in_radius, in_center, pixel):
    try:
        radius = int(in_radius)
        center = Pixel(int(in_center.row), int(in_center.column))
    except ValueError:
        print >> sys.stderr, 'Enter only integer values'
        exit(1)
    scale_factor = (radius - distance(center, pixel))/radius
    if scale_factor < .2:
        scale_factor = .2
    r = pixel_comp[0] * scale_factor
    g = pixel_comp[1] * scale_factor
    b = pixel_comp[2] * scale_factor
    return [int(r), int(g), int(b)]


def open_file(name, mode):       # opens file, if not possible: prints error
    try:
        return open(name, mode)
    except IOError as e:
        print >> sys.stderr, '{0}:{1}'.format(name, e.strerror)
        exit(1)


if __name__ == '__main__':
    main(sys.argv)