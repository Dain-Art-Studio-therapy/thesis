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

    usage = 'python blur.py <filename> <reach>'

    try:
        infile = open(argv[1], 'rb')
        return infile
    except:
        print >> sys.stderr, 'invalid or missing filename\n', usage
        sys.exit(1)


def get_reach(argv):

    try:
        reach = int(argv[2])
    except:
        reach = 4

    return reach


def get_header(infile):

    header = []

    for i in range(0, 3):
        line = infile.readline()
        header.append(line)

    return header


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


def locate(pindex, width):

    for i in range(width):
        if pindex < width * (i+1):
            col = pindex - width*i
            row = i
            return col, row


def delocate(col, row, width):

    return width * row + col 


def find_neighbors(center, reach):

    neighbors = []
    
    for i in range(reach*2 + 1):
        for j in range(reach*2 + 1):
            neighbors.append((
                center[0]-reach + i,
                center[1]-reach + j
                ))

    return neighbors


def average(pixels):

    r = 0
    g = 0
    b = 0
    total = 0

    for pixel in pixels:
        total += 1
        r += pixel[0]
        g += pixel[1]
        b += pixel[2]

    r_avg = r // total
    g_avg = g // total
    b_avg = b // total

    return r_avg, g_avg, b_avg 


def blur(pixels, width, reach):

    new_pixels = []

    for i in range(len(pixels)):
        square = []
        center = locate(i, width)
        neighbors = find_neighbors(center, reach)
        for neighbor in neighbors:
            if (
                (0 <= neighbor[0] < width) and 
                (0 <= neighbor[1] < len(pixels)/width)
                ):
                    index = delocate(neighbor[0], neighbor[1], width)
                    square.append(pixels[index])
        new_pixels.append(average(square))
                        
    return new_pixels
        
    
def main(argv):

    infile = read_file(argv)
    outfile = open('blurred.ppm', 'wb')

    header = get_header(infile)
    pixels = get_pixels(infile)
    reach = get_reach(argv)
    width = int(header[1].split()[0])
    
    new_pixels = blur(pixels, width, reach)
 
    for h in header:
        outfile.write(h)

    for p in new_pixels:
        outfile.write('{0} {1} {2}\n'.format(p[0], p[1], p[2]))

    infile.close()
    outfile.close()


if __name__ == '__main__':
    main(sys.argv)
