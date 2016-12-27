import sys
import math

def try_open(file_name):
    try:
        file_handle = open(file_name, 'r')
        return file_handle
    except:
        print 'Error - Does not open'
        exit()

def output(file_name, raster):
    out_fh = open('blurred.ppm', 'w')
    initialize(file_name, out_fh)
    for color in raster:
        for val in color:
            out_fh.write(str(val)+'\n')

def make_raster(file_handle):
    raster = []
    count = 0
    color = []
    for line in file_handle:
        for value in line.split():
            if count > 0:
                color.append(int(value))
                if count % 3 == 0:
                    raster.append(color)
                    color = []
            else:
                print value
            count += 1
    return raster


def blur(raster, width, height, reach):
    all_blurs = [] 
    for i in xrange(width * height):
        y = i/width
        x = i - y * width 
        blur1 = []
        bounds = 2 * reach + 1 
        for p in xrange(bounds**2):
           yp = p/bounds
           xp = p - yp * bounds - reach  
           index = (x + xp) + (y + yp - reach) * width
           #if x + xp >= 0 and x + xp <=  width: 
           try: 
               blur1.append(raster[index]) 
           except:
               pass
        all_blurs.append(blur_list(blur1))  
    return all_blurs

def blur_list(pixel_list):
    r = 0 
    g = 0
    b = 0 
    for color in pixel_list:
        r += color[0]
        g += color[1]
        b += color[2] 
    return [r/len(pixel_list), g/len(pixel_list), b/len(pixel_list)]


def get_size(file_handle):
    count = 0
    for line in file_handle:
        if count == 1:
            size = line.split()
            return (int(size[0]), int(size[1]))
        count += 1


def initialize(file_name, out_fh):
    a = open(file_name, 'r')
    out_fh.write(a.readline())
    out_fh.write(a.readline())
    out_fh.write(a.readline())
    a.close()

def main():
    try:
        file_name = sys.argv[1]
    except:
        print 'tried to open bad file' 
        exit()
    try:
        reach = int(sys.argv[2])
    except:
        reach = 4 
    file_handle = try_open(file_name) 
    width, height = get_size(file_handle)
    raster = make_raster(file_handle)
    blurred = blur(raster, width, height, reach) 
    output(file_name, blurred)

if __name__ == '__main__':
    main()
