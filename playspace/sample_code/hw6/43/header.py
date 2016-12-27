import sys
#read line for width and height of input file


def main(argv):
    with open_file(argv[1], 'r') as f:
        lines = f.readlines()


    with open_file('test_write.ppm', 'w') as file_object:
        print >> file_object, lines[0],
        print >> file_object, lines[1],
        print >> file_object, lines[2],


def open_file(name, mode):
    try:
        return open(name, mode)
    except IOError as e:
        print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
        exit(1)



new_list = []
    for row_index in range(len(pixel_grid)):
        pixel_x = row_index
        new_list.append(pixel_x)
        for col_index in range(len(pixel_grid[row_index])):
            pixel_y = col_index
            new_list.extend(pixel_y)
    print new_list



if __name__ == '__main__':
    main(sys.argv)