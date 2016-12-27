import sys

def main(argv):

    if len(argv) < 2:
        print >> sys.stderr, 'No input file specified.'
        exit(1)

    input_file = open_file(argv[1], 'rb')
    output_file = open_file('hidden.ppm', 'w')

    list = input_file.read().split()

    file_props(list, output_file)

    process_file(list, output_file)


def process_file(list, output_file):

    for i in range(4):
        list.pop(0)

    pixels = groups_of_3(list)

    for pixel in pixels:
        r = int(pixel[0]) * 10
        g = r
        b = r

        write_pixel(r, g, b, output_file)


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