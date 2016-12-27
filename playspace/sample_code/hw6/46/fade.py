import sys
from math import sqrt

usage = 'usage: python fade.py <filename> <row> <col> <radius>'

def groups_of_3(t):

    if len(t)%3 == 0:
        loops = len(t)/3
    else:
        loops = len(t)/3 + 1

    master = []

    for i in range(loops):
        sub = []
        start = 3*i
        end = 3*(i+1)
        if end <= len(t):
            for j in range(start, end):
                sub.append(t[j])
        else:
            for j in range(start, len(t)):
                sub.append(t[j])
        master.append(sub)

    return master


def read_file(argv):

    try:
        infile = open(argv[1], 'rb')
        return infile
    except:
        print >> sys.stderr, 'invalid or missing filename\n', usage
        sys.exit(1)


def read_args(argv):

    if len(argv) < 3:
        print >> sys.stderr, 'row missing\n', usage
        sys.exit(1)

    if len(argv) < 4:
        print >> sys.stderr, 'col missing\n', usage
        sys.exit(1)

    if len(argv) < 5:
        print >> sys.stderr, 'radius missing\n', usage

    try:
        row = int(argv[2])
        col = int(argv[3])
        radius = int(argv[4])
        return col, row, radius
    except:
        print >> sys.stderr, 'integer arguments expected\n', usage
        sys.exit(1)


def get_pixels(infile):

    lines = infile.readlines()
    master = []
    
    for line in lines:
        sub = line.split()
        for num in sub:
            master.append(num)
    master = map(int, master)
    pixels = groups_of_3(master)
    return pixels


def get_header(infile):

    header = []

    for i in range(0, 3):
        line = infile.readline()
        header.append(line)

    return header


def get_distance(col1, row1, col2, row2):

    dx = col2 - col1
    dy = row2 - row1
    hyp_squared = dx**2 + dy**2
    return sqrt(hyp_squared)


def locate(pindex, width):

    for i in range(width):
        if pindex < width * (i+1):
            col = pindex - width*i
            row = i
            return col, row
    

def fade(pixels, width, col, row, radius):

    new_pixels = []

    for i in range(len(pixels)):
        p = locate(i, width)
        distance = get_distance(p[0], p[1], col, row)
        scale = abs(radius - distance) / radius
        new_pixels.append((
            int(pixels[i][0] * max(scale, 0.2)),
            int(pixels[i][1] * max(scale, 0.2)),
            int(pixels[i][2] * max(scale, 0.2))
            ))

    return new_pixels


def main(argv):

    infile = read_file(argv)
    outfile = open('faded.ppm', 'wb')

    header = get_header(infile)
    pixels = get_pixels(infile)
    col = read_args(argv)[0]
    row = read_args(argv)[1]
    radius = read_args(argv)[2]
    width = int(header[1].split()[0])
    
    new_pixels = fade(pixels, width, col, row, radius)

    for h in header:
        outfile.write(h)

    for p in new_pixels:
        outfile.write('{0} {1} {2}\n'.format(p[0], p[1], p[2]))

    infile.close()
    outfile.close()


if __name__ == '__main__':
    main(sys.argv)
