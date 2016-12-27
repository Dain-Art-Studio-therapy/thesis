import sys

def main(argv):

    if len(argv) < 2:
        print >> sys.stderr, 'No file provided.'
        exit(1)

    try:
        blur_factor = int(argv[2])
    except:
        blur_factor = 4
        print >> sys.stderr, 'Using default blur factor: 4.'


    with open_file(argv[1], 'rb') as input_file:
        list_input = input_file.read().split()

        width = int(list_input[1])
        height = int(list_input[2])

        with open_file('blurred.ppm', 'w') as output_file:

            file_props(list_input, output_file)

            process_file(list_input, width, height, blur_factor, output_file)


def process_file(list_input, width, height, blur_factor, output_file):

    for i in range(4):
        list_input.pop(0)

    list_int = convert_list_to_int(list_input)

    pixels = two_dimension_list(groups_of_3(list_int), width, height)

    for y in range(height):
        for x in range(width):

            blurred_pixel = blur(x, y, pixels, width, height, blur_factor)

            write_pixel(blurred_pixel[0], blurred_pixel[1], blurred_pixel[2],
                        output_file)


def blur(x, y, pixels, width, height, blur_factor):
    # "blurs" one pixel by averaging the colors of neighboring pixels

    neighbor_pixels = []

    start_y = max(0, y - blur_factor)
    end_y = min(height, y + blur_factor)

    start_x = max(0, x - blur_factor)
    end_x = min(width, x + blur_factor)

    for i in range(start_y, end_y + 1):
        for j in range(start_x, end_x + 1):
            try:
                neighbor = pixels[i][j]
                neighbor_pixels.append(neighbor)
            except:
                pass

    neighbors_average = average_colors(neighbor_pixels)

    return neighbors_average


def average_colors(list_colors):
    # averages a list of colors [ [r,g,b], [r,g,b] ]

    sum_colors = [0, 0, 0]

    for pixel in list_colors:
        sum_colors[0] += pixel[0]
        sum_colors[1] += pixel[1]
        sum_colors[2] += pixel[2]

    return [int(float(i) / len(list_colors)) for i in sum_colors]


def two_dimension_list(list_in, width, height):
    result = []

    for y in range(height):
        l = []

        for x in range(width):
            l.append(list_in[(width*y) + x])

        result.append(l)

    return result


def write_pixel(r, g, b, output_file):
    if r > 255:
        r = 255

    if g > 255:
        g = 255

    if b > 255:
        b = 255

    output_file.write(str(r) + ' ' + str(g) + ' ' + str(b) + '\n')


def file_props(list_input, output_file):
    format = list_input[0]
    width = list_input[1]
    height = list_input[2]
    max_color = list_input[3]

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


def convert_list_to_int(list_in):
    return [int(i) for i in list_in]


if __name__=='__main__':
    main(sys.argv)