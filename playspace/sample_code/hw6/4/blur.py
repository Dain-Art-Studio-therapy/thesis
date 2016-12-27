# Name: Audrey Chan
# Instructor: Aaron Keen
# Section: 09

# Description: program will output the blurred image to a file named blurred.ppm

import sys
import blur_pixel

def main(argv):
    try:
        reach = argv[2]
    except:
        reach = 4
    
    try:
        with open(argv[1], 'rb') as f:
            process_file(f, int(reach))
    except:
        print "invalid commandline entry: file not valid"

def pixel_avg(neighbor_list):
    # Description: this function takes a list of neighboring pixels and
    #              average all the values, returning one pixel
    
    total_r = 0
    total_g = 0
    total_b = 0

    for n in neighbor_list:
        total_r += n.r
        total_g += n.g
        total_b += n.b
    
    avg_r = int(total_r / len(neighbor_list))
    avg_g = int(total_g / len(neighbor_list))
    avg_b = int(total_b / len(neighbor_list))

    return blur_pixel.Pixel(avg_r, avg_g, avg_b)

def pixel_neighbors(pixel_r, pixel_c, grid, reach):
    # Description: this function takes pixels location on a grid of pixels  and 
    #              returns all neighboring pixels within specified neighbor reach

    neighbor_list = []

    for i in range(1, reach + 1):
        if pixel_r + i < len(grid):
            neighbor_list.append(grid[pixel_r + i][pixel_c])
            if pixel_c + i < len(grid[0]):
                neighbor_list.append(grid[pixel_r + i][pixel_c + i])
            if pixel_c - i >= 0:
                neighbor_list.append(grid[pixel_r + i][pixel_c - i])
        if pixel_r - i >= 0:
            neighbor_list.append(grid[pixel_r - i][pixel_c])
            if pixel_c + i < len(grid[0]):
                neighbor_list.append(grid[pixel_r - i][pixel_c + i])
            if pixel_c - i >= 0:
                neighbor_list.append(grid[pixel_r - i][pixel_c - i])
        if pixel_c + i < len(grid[0]):
            neighbor_list.append(grid[pixel_r][pixel_c + i])
        if pixel_c - i >= 0:
            neighbor_list.append(grid[pixel_r][pixel_c - i])

    return neighbor_list


def pixel_2D(ppm_lines, row, col):
    # Description: stores pixels from the input list of ppm file lines into a 2D array
    #              and returns that 2D array
    
    pix2D = []
    pixel_list = []
    
    for l in range(3, len(ppm_lines), 3):
        pixel = blur_pixel.Pixel(int(ppm_lines[l]), 
                                 int(ppm_lines[l+1]),
                                 int(ppm_lines[l+2]))
        pixel_list.append(pixel)

    p = 0

    for r in range(row):
        pix2D.append([])
        for c in range(col):
            pix2D[r].append(pixel_list[p])
            p += 1

    return pix2D


def process_file(input_file, reach):
    # Description: implements the above functions to edit each pixel in the image

    blurred = open('blurred.ppm', 'w')
    
    ppm_lines = input_file.readlines()
    blurred.writelines(ppm_lines[0:3])

    max_col_idx = int(ppm_lines[1].split()[0])
    max_row_idx = int(ppm_lines[1].split()[1])

    pix2D = pixel_2D(ppm_lines, max_row_idx, max_col_idx)

    for r_idx in range(len(pix2D)):
        for c_idx in range(len(pix2D[r_idx])):
            pix = pix2D[r_idx][c_idx]
            neighbor_list = pixel_neighbors(r_idx, c_idx, pix2D, reach)
            pix = pixel_avg(neighbor_list)

            print >> blurred, pix.r, pix.g, pix.b,

    blurred.close()


main(sys.argv)

