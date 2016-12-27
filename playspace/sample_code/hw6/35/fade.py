import sys
import math

def main(argv):
    #get cmdline arguments
    if len(argv) < 4:
        print "Four commandline arguments required: \
        (1) input image, (2) row, (3) col, (4) radius."
        exit(1)
    else:
        try:
            input_image = sys.argv[1]
            row = int(sys.argv[2])
            col = int(sys.argv[3])
            radius = float(sys.argv[4])
        except:
            print "Wrong value types for commandline arguments."
        
    with open_file(input_image, "rb") as pic:
        header_1 = pic.readline()
        header_2 = pic.readline()
        header_3 = pic.readline()
        
        raw_pixels = []
        for line in pic:
            raw_pixels.append(int(line))
        pixels = groups_of_three(raw_pixels)
        
        width = int(header_2.split()[0])
        new_pixels = change_by_distance(pixels, row, col, radius, width)
        write_to_file(header_1, header_2, header_3, new_pixels)
        
def open_file(file, type):
    try:
        f = open(file, type)
        return f
    except IOError as e:
        print "{0}: {1}".format(sys.argv[1], e.strerror)

def groups_of_three(list):
    new = []
    
    for index in range(len(list)/3):
        newer = []
        for i in range(3):
            newer.append(list[i + index * 3])
        new.append(newer)
    
    #for when list is not divisible by 3
    remainder = len(list) % 3
    var0 = len(list) - remainder
    var1 = len(list) - remainder + 1
    remainder_list = []
    if remainder == 2:
        remainder_list.append(list[var0])
        remainder_list.append(list[var1])
        new.append(remainder_list)
    elif remainder == 1:
        remainder_list.append(list[var0])
        new.append(remainder_list)
            
    return new
    
def change_by_distance(pixel_list, row, col, radius, width):
    counter = 0
    for pixel in pixel_list:
        x = counter % width
        y = counter / width
        dist = euclidean_dist(x, y, row, col)
        fade = (radius - dist)/radius
        pixel[0] *= fade
        pixel[1] *= fade
        pixel[2] *= fade
        counter += 1
    return pixel_list
            
def euclidean_dist(from_row, from_col, to_row, to_col):
    return math.sqrt((from_row - to_row) **2 + (from_col - to_col) **2)
    
def write_to_file(h1, h2, h3, grid):
    with open_file("faded.ppm", "w") as f:
        print >> f, h1
        print >> f, h2
        print >> f, h3
        for [r, g, b] in grid:
            print >> f, r, g, b
                
if __name__ == '__main__':
    main(sys.argv)