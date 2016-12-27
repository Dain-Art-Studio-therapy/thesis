import sys
#read line for width and height of input file
def main(argv):
    test_length(argv)
    with open_file(argv[1], 'r') as f:
        splits = split_pixels(f)
        floats = float_list(splits)
        pixels = groups_of_3(floats)
        new_pixels = reveal(pixels)
        lines = f.readlines()


    with open_file('test_write.ppm', 'w') as file_object:
        print_new_pixels(new_pixels, file_object)
        print >> file_object, lines[0],
        print >> file_object, lines[1],
        print >> file_object, lines[2],


def open_file(name, mode):
    try:
        return open(name, mode)
    except IOError as e:
        print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
        exit(1)


def test_length(argv):
    if len(argv) <= 1:
        print 'No file entered!'
        exit(1)
    else:
        pass

def make_floats(n):
    try:
        return float(n)
    except TypeError:
        print 'not a float'
    return 0


def float_list(split_list): #[P3, H, W, P, 255, 255, 255, 255]
    new_list = []
    for i in range(4, len(split_list)):
        n = make_floats(split_list[i])
        new_list.append(n)
    return new_list


def split_pixels(f):
    count = 0
    new_list = []
    for line in f:
        values = line.split()
        count += 1
        if len(line) == 0:
            print 'No pixels entered on line ' + str(count) + '...'
        else:
            new_list.extend(values)
    return new_list


def groups_of_3(float_list):
    new_list = []
    for i in range(0, len(float_list), 3):
        if (i + 2) < len(float_list):
            new_list.append((float_list[i], float_list[i + 1], float_list[i + 2]))
        elif (i + 1) < len(float_list):
            new_list.append((float_list[i], float_list[i + 1]))
    return new_list


def reveal(pixel_list): #[(r,g,b),(r,g,b),(r,g,b)]
    new_list = []
    for tuple in pixel_list:
        red = tuple[0]
        new_red = red * 10
        if new_red > 255.0:
            new_red = 255.0
        new_green = new_red
        new_blue = new_red
        new_list.append((new_red, new_green, new_blue))
    return new_list

def print_new_pixels(new_pixels, file_object):
    for tuple in new_pixels:
        print >> file_object, tuple[0], tuple[1], tuple[2]










if __name__ == '__main__':
    main(sys.argv)
