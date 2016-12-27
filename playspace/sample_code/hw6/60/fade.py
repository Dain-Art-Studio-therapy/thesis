import sys
import math
from fade_groups import *

def main(argv):
    if len(argv) != 5:
        print >> sys.stderr, 'Missing either file name, row, col, or radius'
        exit(1)

    with open_file(argv[1],'rb') as image:
        pixels = process_file(image)

    return update_pix(pixels,int(argv[2]),int(argv[3]),int(argv[4]))

def open_file(name,mode):
    try:
        return open(name,mode)
    except IOError as e:
        print >> sys.stderr, '{0}:{1}'.format(name,e.strerror)
        exit(1)

def process_file(infile):
    pixels = []

    for line in infile:
        pix = line.split()

        for p in pix:
            if p.isdigit():
                pixels.append(p)

    groups = groups_of_3(pixels)

    return groups

def update_pix(pixel_list,row,col,radius):
    output = open_file('fade.ppm','w')

    WIDTH = pixel_list[0][0]
    HEIGHT = pixel_list[0][1]
    COLOR = pixel_list[0][2]

    output.write('P3 '+WIDTH+' '+HEIGHT+' '+COLOR+' ')

    width = int(WIDTH)
    height = int(HEIGHT)

    i = 0
    for y in range(int(height)):
        for x in range(int(width)):
            distance = dist(x,y,row,col)
            scale_value = fade_cap((radius - distance)/radius)
            clr = faded_clr(pixel_list[i],scale_value)
            output.write(clr[0]+' '+clr[1]+' '+clr[2]+' ')
            i += 1

    output.close
    return output

def faded_clr(pixel,scale_value):
    r = str(float(pixel[0])*scale_value)
    g = str(float(pixel[1])*scale_value)
    b = str(float(pixel[2])*scale_value)    

    return [r,g,b]

def dist(pix_x,pix_y,row,col):
    return math.sqrt((pix_x-row)**2 + (pix_y-col)**2)

def capValue(int):
    if 0.0 <= int <= 255.0:
        return int
    else:
        return 255.0

def fade_cap(float):
    if float < 0.2:
        float == 0.2
    return float

if __name__ == '__main__':
    main(sys.argv)
