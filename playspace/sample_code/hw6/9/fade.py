import sys
from fade_scale import *

max_clr_value = 255
num_of_pixel_components = 3


def main(argv):
    if len(argv) < 4:
        print 'Usage: <filename>, row(y-value), column(x-value), radius'
        return None
    
    with open_file(argv[1], 'rb') as in_img:
        with open_file('faded.ppm', 'wb') as fade_img:
            
            print >> fade_img, in_img.readline()
            resolution = get_resolution(in_img)
            print >> fade_img, resolution[0], resolution[1]
            print >> fade_img, in_img.readline()
            
            process_pixel(in_img, fade_img, resolution, argv)


def process_pixel(infl, outfl, resolution, argv):
    pixel = []
    y = 0
    x = 0
    for line in infl:
        data = line.split()
        for num in data:
            if len(pixel) < num_of_pixel_components:
                pixel.append(int(num))
            else:
                r = pixel[0]
                if r > max_clr_value:
                    r = max_clr_value
                
                g = pixel[1]
                if g > max_clr_value:
                    g = max_clr_value
                
                b = pixel[2]
                if b > max_clr_value:
                    b = max_clr_value
                
                scale = fade_scale(x, y, argv)
                
                print >> outfl, int(r * scale), int(g * scale), int(b * scale)
                
                pixel = []
                x += 1
                if x == resolution[0]:
                    x = 0
                    y += 1
                pixel.append(int(num))


def get_resolution(fl):
    line = fl.readline()
    data = line.split()
    width = int(data[0])
    height = int(data[1])
    return width, height


def open_file(fl, mode):
    try:
        return open(fl, mode)
    except IOError as e:
        print >> sys.stderr, 'Cannot open file'.format(fl, e.strerror)
	exit()


if __name__ == '__main__':
    main(sys.argv)

