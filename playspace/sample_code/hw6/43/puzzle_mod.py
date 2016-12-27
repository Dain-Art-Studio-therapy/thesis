import sys
#read line for width and height of input file

def main(argv):
    test_length(argv)
    #with open_file(argv[1], 'r') as f:
        #g = groups_of_3(f)
        #print g

    with open_file('test_write.ppm', 'w') as f:
        return header(f)


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


def header(f):
    for line in f:
    P3 = line[0]
    b = line [1]
    c = line [3]
    c = f.readline(3)
    print >> f, a
    print >> f, b
    print >> f, c


def groups_of_3(f):
    new_list = []
    for line in f:
        values = line.split()
        for i in range(0, len(values), 3):
            if (i + 2) < len(values):
                new_list.append((values[i], values[i + 1], values[i + 2]))
            elif (i + 1) < len(values):
                new_list.append((values[i], values[i + 1]))
            else:
                new_list.append((values[i],))
    return new_list



if __name__ == '__main__':
    main(sys.argv)
