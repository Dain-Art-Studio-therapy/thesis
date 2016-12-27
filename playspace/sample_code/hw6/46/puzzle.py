import sys

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
        print >> sys.stderr, 'invalid or missing filename'
        print >> sys.stderr, 'usage: python puzzle.py <filename>'
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
        

def decode(argv):

    infile = read_file(argv)
    outfile = open('hidden.ppm', 'wb')
    
    header = get_header(infile)
    pixels = get_pixels(infile)

    for h in header:
        outfile.write(h)

    for p in pixels:
        r = p[0] * 10
        if r > 255:
            r = 255
        outfile.write('{0} {1} {2}\n'.format(r, r, r))

    infile.close()
    outfile.close()


if __name__ == '__main__':
    decode(sys.argv)
