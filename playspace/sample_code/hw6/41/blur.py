__author__ = 'Jarrett'

import sys
import file

# takes an average of the color components
# of each pixel in an area
def pixel_avg(pixels):
    r_sum = 0
    g_sum = 0
    b_sum = 0
    num = len(pixels)

    for i in range(len(pixels)):
        r_sum = r_sum + pixels[i][0]
        g_sum = g_sum + pixels[i][1]
        b_sum = b_sum + pixels[i][2]
        # print i, r_sum, g_sum, b_sum

    r_ave = r_sum / num
    g_ave = g_sum / num
    b_ave = b_sum / num

    # print r_ave, g_ave, b_ave

    return str.format("{0} {1} {2}\n", r_ave, g_ave, b_ave)


# creates a 2-D list of the pixels that
# represent the pixels of the picture at
# their respective locations
def pixel_grid(pixels, width):
    col_list = []
    row_list = []

    for i in range(len(pixels)):
        col_list.append(pixels[i])

        if ((i % width == 0) and (i != 0)):
            row_list.append(col_list)
            col_list = []

    # this is misleading but it is a 2-D list
    # a grid of the pixels but each column is
    # "in" the row
    print len(row_list[-2])
    return row_list

# determine the reach by checking to see if the reach
# goes out of the bounds of the image
def set_reach(pixel_col, pixel_row, height, width, reach):
    up = reach
    down = reach
    left = reach
    right = reach

    if (reach >= pixel_row):
        up = pixel_row

    if (reach >= (height - pixel_row)):
        down = height - pixel_row - 1

    if (reach >= pixel_col):
        left = pixel_col

    if (reach >= (width - pixel_col)):
        right = width - pixel_col - 1

    # print pixel_col, pixel_row, height, width, up, down, left, right

    return (up, down, left, right)

# makes a list of pixels that is the group
# that is being blurred together by looking at
# the position of the pixel and looking at the
# reach of the pixel
def set_blurred_area(pixels, x, y, height, width, reach):
    new_reach = set_reach(x, y, height, width, reach)

    area = []
    up = new_reach[0]
    down = new_reach[1]
    left = new_reach[2]
    right = new_reach[3]

    for i in range(len(pixels)):
        if ((i >= (y - up)) and (i <= (y + down))):
            for j in range(len((pixels[i]))):
                if (j >= (x - left) and (j <= (x + right))):
                    # print str.format("row: {5} col: {4}\nx from {0} to {1}\ny from {2} to {3}",
                    #                  x - left, x + right, y - up, y + down, i, j)
                    area.append(pixels[i][j])

    # print area
    # print len(area)
    return area

# iterates through all of the pixels blurring each one
def blur(pixels, height, width, reach):
    blurred_list = []
    pixel_row = 0
    pixel_col = 0

    for e in pixels:
        for j in range(len(e)):
            # print pixel_col, pixel_row
            area = set_blurred_area(pixels, pixel_col, pixel_row, height, width, reach)
            new_pixel = pixel_avg(area)
            # print new_pixel

            blurred_list.append(new_pixel)

            pixel_col = j + 1
            if ((pixel_col % width) == 0):
                pixel_row = pixel_row + 1
                pixel_col = 0

    return blurred_list

def main(argv):
    f = file.open_file(argv, "r")

    try:
        reach = int(argv[2])
    except:
        reach = 4

    str_list = file.read_file(f)
    format = file.parse_format(str_list)
    pixels = file.parse_pixels(str_list)
    height = file.parse_height(str_list)
    width = file.parse_width(str_list)

    grid = pixel_grid(pixels, width)

    new_pixels = blur(grid, height, width, reach)

    file.write_file("blurred.ppm", format, new_pixels)


if __name__ == "__main__":
    main(sys.argv)