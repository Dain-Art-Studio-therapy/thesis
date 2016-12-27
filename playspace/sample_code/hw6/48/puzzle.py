import sys
from groups import *

OUTFILE = 'hidden.ppm'


def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'usage: python puzzle.py <filename>'
        exit(1)
    outfile = open_file(OUTFILE, 'w')
    with open_file(argv[1], 'rb') as f:
        process_file(f, outfile)    # list
    outfile.close()


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

    pixel = []
    for line in infile:
        pixel_lines = line.split()
        for e in pixel_lines:
            try:
                pixel.append(int(e))
            except ValueError:
                pixel.append(e)
        if len(pixel) == 3:
            new_pixel = process_pixel(pixel)
            print >> outfile, new_pixel[0], new_pixel[1], new_pixel[2]
            pixel = []


def process_pixel(pixel_in_list):
    r = pixel_in_list[0] * 10
    if r > 255:
        r = 255
    return [r, r, r]


def open_file(name, mode):       # opens file, if not possible: prints error
    try:
        return open(name, mode)
    except IOError as e:
        print >> sys.stderr, '{0}:{1}'.format(name, e.strerror)
        exit(1)


if __name__ == '__main__':
    main(sys.argv)