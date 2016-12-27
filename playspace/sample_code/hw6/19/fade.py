import sys
import math

def main(argv):

    if len(argv) < 5:
        print >> sys.stderr, 'Not enough arguments!'
        exit(1)

    input_file = open_file(argv[1], 'rb')
    output_file = open_file('faded.ppm', 'w')

    list = input_file.read().split()

    width = int(list[1])
    height = int(list[2])

    file_props(list, output_file)


    try:
        center_x = int(argv[3])
        center_y = int(argv[2])
        radius = int(argv[4])
    except:
        print >> sys.stderr, 'Invalid arguments.'
        exit(1)


    process_file(list, width, height, center_x, center_y, radius, output_file)


def process_file(list, width, height, center_x, center_y, radius, output_file):

    for i in range(4):
        list.pop(0)

    list_int = [int(i) for i in list]

    pixels = groups_of_3(list_int)

    for y in range(height):
        for x in range(width):
            pixel = pixels[(width*y) + x]

            distance_from_center = distance(x, y, center_x, center_y)

            scale = (radius - distance_from_center) / float(radius)

            scale_max = max(scale, 0.2)

            r = int(pixel[0] * scale_max)
            g = int(pixel[1] * scale_max)
            b = int(pixel[2] * scale_max)

            write_pixel(r, g, b, output_file)


def distance(x1, y1, x2, y2):
    return math.sqrt((((x2 - x1)**2)) + (((y2 - y1)**2)))


def write_pixel(r, g, b, output_file):
    if r > 255:
        r = 255

    if g > 255:
        g = 255

    if b > 255:
        b = 255

    output_file.write(str(r) + ' ' + str(g) + ' ' + str(b) + '\n')


def file_props(list, output_file):
    format = list[0]
    width = list[1]
    height = list[2]
    max_color = list[3]

    output_file.write(str(format + ' ' + width + ' ' + height + ' ' +
                          max_color + '\n'))


def open_file(name, mode):
    try:
        return open(name, mode)
    except:
        print >> sys.stderr, 'File could not be opened.'
        exit(1)


def groups_of_3(input_list):
    output = []
    for i in range(0, len(input_list), 3):
        if i + 2 < len(input_list):
            output.append([input_list[i], input_list[i+1], input_list[i+2]])
        elif i + 2 == len(input_list):
            output.append([input_list[i], input_list[i+1]])
        elif i + 1 == len(input_list):
            output.append([input_list[i]])

    return output

if __name__=='__main__':
    main(sys.argv)