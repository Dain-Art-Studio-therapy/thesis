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
    out_fh = open('faded.ppm', 'w')
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
                if (count + 1) % 3 == 0:
                    raster.append(color)
                    color = []
            else: 
                print value 
            count += 1
    return raster

def fade(raster, row, column, radius, width, height): 
    new_raster = []
    for i in xrange(width * height):
        y = i/width
        x = i - y * width
        distance = dist(x, y, row, column)
        scale = max(0.2, (radius - distance)/radius) 
        color = []
        for value in raster[i]:
            color.append(int(scale*value))
        new_raster.append(color) 
    return new_raster                 
            
def dist(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2) 
         
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
    file_name = sys.argv[1]
    row = int(sys.argv[2])
    column = int(sys.argv[3])
    radius = float(sys.argv[4])
    file_handle = try_open(file_name)
    width, height = get_size(file_handle) 
    raster = make_raster(file_handle)
    faded = fade(raster, row, column, radius, width, height)
    output(file_name, faded)
    


if __name__ == '__main__':
    main() 
