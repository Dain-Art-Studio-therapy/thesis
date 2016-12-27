import sys

MAX_PIXEL_VAL = -1

def main(argv):
    input_file_name = process_cmd(argv)

    input_file = open_file(input_file_name, 'rb')
    output_file = open_file('hidden.ppm', 'w')
    
    process_image(input_file, output_file)
    
    input_file.close()
    output_file.close()

def process_cmd(args):
    # check number of args
    if len(args) == 2:
        return args[1]
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

def process_image(input_file, output_file):
    # read pixel
    # r x 10, g = r, b = r
    # output pixel
    hw = process_header(input_file)
    num_of_pix = hw[0] * hw[1]

    write_header(output_file, hw)
    for i in range(num_of_pix):
        pixel = read_pixel(input_file)
        r10 = pixel[0] * 10
        pixel_new = (r10, r10, r10)
        write_color(pixel_new, output_file)

def cap_color(color):
    if color[0] > MAX_PIXEL_VAL:
        color[0] = MAX_PIXEL_VAL
    if color[1] > MAX_PIXEL_VAL:
        color[1] = MAX_PIXEL_VAL
    if color[2] > MAX_PIXEL_VAL:
        color[2] = MAX_PIXEL_VAL
    return color

def write_color(color, f):
    f.write(str(int(color[0])) + " " + str(int(color[1])) + " " + str(int(color[2])) + " ")

def write_header(f, hw):
    f.write("P3\n")
    f.write(str(hw[0]) + " " + str(hw[1]) + "\n")
    f.write(str(MAX_PIXEL_VAL) + "\n")

if __name__ == '__main__':
    main(sys.argv)
