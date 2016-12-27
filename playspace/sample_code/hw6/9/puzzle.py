import sys

max_clr_value = 255
num_of_pixel_components = 3
decode_value = 10


def main(argv):
    if len(argv) < 2:
        print 'Input P3 ppm file to decode!'
        return None
    
    with open_file(argv[1], 'rb') as puzzle_img:
        with open_file('hidden.ppm', 'wb') as decoded_img:
            
            print_header(puzzle_img, decoded_img)
            process_pixel(puzzle_img, decoded_img)


def process_pixel(infl, outfl):
    pixel = []
    for line in infl:
        data = line.split()
        for num in data:
            if len(pixel) < num_of_pixel_components:
                pixel.append(int(num))
            else:
                clr = pixel[0] * decode_value
                if clr > max_clr_value:
                    clr = max_clr_value
                print >> outfl, clr, clr, clr
                pixel = []
                pixel.append(int(num))


def print_header(fl, out_fl):
    print >> out_fl, fl.readline(), fl.readline(), fl.readline()


def open_file(fl, mode):
    try:
        return open(fl, mode)
    except IOError as e:
        print >> sys.stderr, 'Cannot open file'.format(fl, e.strerror)
        exit()


if __name__ == '__main__':
    main(sys.argv)

