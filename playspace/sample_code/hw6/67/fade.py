import sys
import math

def open_file(name, mode):
    try:
        return open(name, mode)
    except IOError as e:
        print >> sys.stderr, '{0}: {1}'.format(name, e.strerror)
        exit(1)

def groups_of_3(nums):
    newlist = []
    for i in range(0, len(nums), 3):
        temp = nums[i:i+3]
        newlist.append(temp)
    return newlist

def groups_of_width(nums, width):
    newlist = []
    w = int(width)
    for i in range(0, len(nums), w):
        temp = nums[i:i+w]
        newlist.append(temp)
    return newlist

def process(f, faded, argv):
    # process each line of pixels
    n = f.read().split()
    p3 = n[0]
    width = (n[1])
    height = (n[2])
    max_col = (n[3])
    newlist = []
    for i in range(4, len(n)):
        newlist.append(int(n[i]))        
    num_list = groups_of_3(newlist)
    out(width, height, max_col, faded, num_list, argv)

def out(width, height, max_col, faded, num_list, argv):
    faded.write('P3\n')
    faded.write(width + ' ' + height + '\n' + max_col +'\n')
    two_d = groups_of_width(num_list, width)
    fade(argv, two_d, faded)

def calc(row, col, trow, tcol, radius):
    d = math.sqrt(((row -trow)**2) + ((col - tcol)**2))
    r = float(radius)
    f = (r - d) / r
    if f < 0.2 :
        f = .2
    return f

def fade(argv, two_d, faded):
    radius = int(argv[4])
    row = int(argv[2])
    col = int(argv[3])
    for i in range(len(two_d)):
        for j in range(len(two_d[i])):
            # trow = i tcol = j
            f = calc(row, col, i, j, radius)
            r = float(two_d[i][j][0])
            g = float(two_d[i][j][1])
            b = float(two_d[i][j][2])
            r = str(int(r*f))
            g = str(int(g*f))
            b = str(int(b*f))
            faded.write(r + ' ' + g + ' ' + b + ' ')

def check_arg(argv):
    if len(argv) == 1:
        print >> sys.stderr, 'File not chosen.'
        exit(1)
    if len(argv) == 2:
        print >> sys.stderr, 'x position and radius not chosen.'
        exit(1)
    if len(argv) == 3:
        print >> sys.stderr, 'radius not chosen.'
        exit(1)
    if len(argv) == 4:
        try:
            int(argv[2])
            int(argv[3])
            int(argv[4])
        except:
            print >> sys.stderr, 'Last three arguments should be integers'
            exit(1)

def main(argv):
    check_arg(argv)    
    with open_file(argv[1], 'rb') as f:
        with open_file('faded.ppm', 'wb') as faded:
            process(f, faded, argv)

if __name__ == "__main__":
    main(sys.argv)
