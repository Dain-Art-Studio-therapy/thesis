import sys
from blur_clr_avg import *
from groups import *

default_blur = 4


def main(argv):
    with open_file(argv[1], 'rb') as in_img:
        with open_file('blurred.ppm', 'wb') as blur_img:

            in_blur = default_blur
	    if len(argv) == 3:
                in_blur = int(argv[2])

            print >> blur_img, in_img.readline()
            resolution = get_resolution(in_img)
            print >> blur_img, resolution[0], resolution[1]
            print >> blur_img, in_img.readline()
            
            pixel_list = process_img(in_img)
            pixel_grid = make_pixel_grid(pixel_list, resolution[0])
            
	    for row_i in range(len(pixel_grid)):
                for col_i in range(len(pixel_grid[row_i])):
                    clr = blur_clr_avg(pixel_grid, row_i, col_i, in_blur)
                    print >> blur_img, int(clr[0]), int(clr[1]), int(clr[2])


def make_pixel_grid(pixel_list, pic_width):
    pixel_grid = []
    row = []
    for pixel in pixel_list:
        if len(row) < pic_width:
            row.append(pixel)
        else:
            pixel_grid.append(row)
            row = []
            row.append(pixel)
    return pixel_grid


def process_img(infl):
    data_list = []
    for line in infl:
        data = line.split()
        for num in data:
            data_list.append(int(num))
    data_list = groups_of_3(data_list)
    return data_list


def get_resolution(fl):
    line = fl.readline()
    data = line.split()
    width = int(data[0])
    height = int(data[1])
    return width, height


def open_file(in_file, mode):
    try:
        return open(in_file, mode)
    except IOError as e:
        print >> sys.stderr, 'Cannot open file'.format(in_file, e.strerror)
	exit()


if __name__ == '__main__':
    main(sys.argv)

