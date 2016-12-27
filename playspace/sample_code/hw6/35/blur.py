import sys

OUTPUT_FILE = "blurred.ppm"

#Right now, the neighbor_reach will decide how many extra babies to print
#try with a neighbor_reach of 1 and ^^ will make sense

def main(argv):
    
    input_file = argv[1]
    if len(argv) < 3:
        neighbor_reach = 4
    else:
        neighbor_reach = int(argv[2])
        
    with open_file(input_file, "rb") as pic:
        header_1 = pic.readline()
        header_2 = pic.readline()
        header_3 = pic.readline()
        
        counter = 0
        pixels = []
        for line in pic:
            pixels.append(int(line))
        
        pixels = groups_of_three(pixels)  
        
        dimentions = header_2.split()
        width = int(dimentions[0])
        height = int(dimentions[1])
        pixels = make_two_dim_list(pixels, width, height)
        pixels = blur_pixels(pixels, neighbor_reach, width, height)
        
        write_to_file(OUTPUT_FILE, header_1, header_2, header_3, pixels)
        
def write_to_file(filename, h1, h2, h3, pixels):
    with open_file(filename, "w") as f:
        print >> f, h1
        print >> f, h2
        print >> f, h3
        for [r, g, b] in pixels:
            print >> f, r, g, b
        
        
def blur_pixels(pixels, neighbor_reach, width, height):
    blurred = []
    for row in range(len(pixels)):
        for col in range(len(pixels[row])):
            pixel = blur_pixel(pixels, neighbor_reach, row, col, width, height)
            blurred.append(pixel)
    return blurred
            
def blur_pixel(pixels, neighbor_reach, row, col, width, height):
    nearby = []
    for i in range(-neighbor_reach, neighbor_reach + 1):
        #weed out out of range --> doesn't work
        if 0 <= row + i <= width:
            if 0 <= col + i <= height:
                try:
                    nearby.append(pixels[row + i][col + i])
                except IndexError as e:
                    print e, "at ", (row + i), ", ", (col + i)
                    print "I'm surprised there's any out of range?"
                
    reds = []
    greens = []
    blues = []
    for [r, g, b] in nearby:
        reds.append(r)
        greens.append(g)
        blues.append(b)
    
    red = sum(reds)/len(reds)
    green = sum(greens)/len(greens)
    blue = sum(blues)/len(blues)
            
    return [red, green, blue]

                
def make_two_dim_list(pixels, width, height):
    grid = []
    for i in range(width):
        row = []
        for j in range(height):
            row.append(pixels[j + i * height])
        grid.append(row)
    return grid
    
def open_file(file, type):
    try:
        f = open(file, type)
        return f
    except IOError as e:
        print "{0}: {1}".format(sys.argv[1], e.strerror)
        exit(1)
        
def groups_of_three(list):
    new = []
    for index in range(len(list)/3):
        newer = []
        for i in range(3):
            newer.append(list[i + index * 3])
        new.append(newer)
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
    
    
    
    
if __name__ == '__main__':
    main(sys.argv)