import sys
import math
MAX_PIXEL_VAL = -1

def main(argv):
    input_tuple = process_cmd(argv)

    input_file = open_file(input_tuple[0], 'rb')
    output_file = open_file('blurred.ppm', 'w')
    
    process_image(input_file, output_file, input_tuple[1])
    
    input_file.close()
    output_file.close()

def process_cmd(args):
    # check number of args
    if len(args) == 2:
        return args[1], 4
    elif len(args) == 3:
        return args[1], int(args[2])
    else:
        print >> sys.stderr, "Invalid cmd args"
        exit(1)

def open_file(file_name, mode):
    # return valid, opened file
    try:
        return open(file_name, mode)
    except:
        print >> sys.stderr, "File opening error"
        exit(1)

def process_header(f):
    lines = []
    for i in range(3):
        lines.append(f.readline())
    if str.strip(lines[0]) != 'P3':
        print >> sys.stderr, "Not a ppm image"
        exit(1)
    try:
        global MAX_PIXEL_VAL
        MAX_PIXEL_VAL = int(lines[2])

        s = lines[1].split(' ')
        if len(s) == 2:
            return int(s[0]), int(s[1])
        else:
            print >> sys.stderr, "Invalid 2nd line"
            exit(1)
    except:
        print >> sys.stderr, "Invalid height and/or width and/or max pixel val"
        exit(1)

def read_number(f):
    # reads next number from the file f
    num = []
    char = f.read(1)
    while char.isdigit() == True:
        num.append(char)
        char = f.read(1)
    return int(''.join(num))

def read_pixel(f):
    # reads next pixel from the file f
    color = []
    for i in range(3):
        color.append(read_number(f))
    return color

def process_image(input_file, output_file, reach):
    hw = process_header(input_file)
    write_header(output_file, hw)

    array2d = [[]]
    for y in range(hw[1]):
        array2d.append([])
        for x in range(hw[0]):
            pixel = read_pixel(input_file)
            array2d[y].append(pixel)

    for y in range(hw[1]):
        for x in range(hw[0]):
            color = sum_sub_list(array2d, reach, x, y)
            #color = array2d[y][x]
            write_color(color, output_file)

def sum_sub_list(array2d, reach,  x, y):
    sum = (0,0,0)
    count = 0
    for cur_y in bounded_range(y - reach, y + reach + 1, 0, len(array2d) - 1):
        for cur_x in bounded_range(x - reach, x + reach + 1, 0, len(array2d[0]) - 1):
            sum = add_color(sum, array2d[cur_y][cur_x])
            count += 1

    sum = color_scale(sum, 1.0 / count)

    return sum

def bounded_range(min, max, low_bound, upper_bound):
    one = min
    two = max
    if min < low_bound:
        one = low_bound
    if max > upper_bound:
        two = upper_bound
    #print "min", min, one
    #print "max", max, two
    return range(one, two)

def color_scale(color, scale):
    return [scale * a for a in color]

def cap_color(color):
    if color[0] > MAX_PIXEL_VAL:
        color[0] = MAX_PIXEL_VAL
    if color[1] > MAX_PIXEL_VAL:
        color[1] = MAX_PIXEL_VAL
    if color[2] > MAX_PIXEL_VAL:
        color[2] = MAX_PIXEL_VAL
    return color

def add_color(one, two):
    return (one[0] + two[0], one[1] + two[1], one[2] + two[2])

def write_color(color, f):
    f.write(str(int(color[0])) + " " + str(int(color[1])) + " " + str(int(color[2])) + " ")

def write_header(f, hw):
    f.write("P3\n")
    f.write(str(hw[0]) + " " + str(hw[1]) + "\n")
    f.write(str(MAX_PIXEL_VAL) + "\n")

if __name__ == '__main__':
    main(sys.argv)
