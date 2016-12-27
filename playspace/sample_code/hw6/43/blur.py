import sys
import puzzle
import math

def main(argv): #input file , blur value
    puzzle.test_length(argv)
    with open_file(argv[1], 'r') as f:
        blur = int(blur_value(argv))
        splits = puzzle.split_pixels(f)
        floats = puzzle.float_list(splits)
        pixels = groups_of_3(floats)
        width = int(splits[1])
        height = int(splits[2])
        loc = make_grid(pixels, width, height)
        image = blur_image(loc, width, height, blur)

    with open_file('blurred.ppm', 'w') as file_object:
        print>> file_object, splits[0]
        print>> file_object, splits[1] + " " + splits[2]
        print>> file_object, splits[3]
        print_new_pixels(image, file_object)


def open_file(name, mode):
    try:
        return open(name, mode)
    except IOError as e:
        print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
        exit(1)


def groups_of_3(float_list):
    new_list = []
    for i in range(0, len(float_list), 3):
        if (i + 2) < len(float_list):
            new_list.append([float_list[i], float_list[i + 1], float_list[i + 2]])
        elif (i + 1) < len(float_list):
            new_list.append([float_list[i], float_list[i + 1]])
    return new_list


def blur_value(argv):
    if len(argv) == 3:
        blur = argv[2]
        return blur
    else:
        blur = 4
        return blur


def make_grid(pixel_grid, width, height):
    new_pixel_list = []
    pos = 0
    for y in range(int(height)):
        new_row = []
        for x in range(int(width)):
            new_row.append(pixel_grid[pos])
            pos += 1
        new_pixel_list.append(new_row)
    return new_pixel_list


def find_averages(pos_grid, x, y, blur, height, width):
    target_x = x - blur #start point
    target_y = y - blur #start point
    blur_dimension = (blur * 2) + 1
    rgb_totals = [0, 0, 0]
    r_total = rgb_totals[0]
    g_total = rgb_totals[1]
    b_total = rgb_totals[2]
    count = 0
    for y in range(blur_dimension):
        for x in range(blur_dimension):
            if target_y + y < height and target_y + y >= 0:
                if target_x + x < width and target_x + x >= 0:
                    count += 1
                    r_total += pos_grid[target_y + y][target_x + x][0]
                    g_total += pos_grid[target_y + y][target_x + x][1]
                    b_total += pos_grid[target_y + y][target_x + x][2]
    rgb_average = [int(r_total/count), int(g_total/count), int(b_total/count)]
    return rgb_average


def blur_image(pos_grid, width, height, blur):
    new_list = []
    for y in range(height):
        for x in range(width):
            pixel_avg = find_averages(pos_grid, x, y, blur, height, width)
            new_list.append(pixel_avg)
    return new_list


def print_new_pixels(new_pixels, file_object):
    output = ''
    for list in new_pixels:
        output += str(list[0]) + ' ' + str(list[1]) + ' ' + str(list[2]) + ' '
    print >> file_object, output

if __name__ == '__main__':
    main(sys.argv)









