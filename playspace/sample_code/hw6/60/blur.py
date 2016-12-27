import sys
from blur_groups import *

def main(argv):
    if len(argv) == 1:
        print >> sys.stderr, 'Missing image file and blur(Optional)'
        exit(1)

    with open_file(argv[1],'rb') as image:
        grids = process_file(image)

    blur = 4
    if len(argv) == 3:
        blur = float(argv[2])

    return update_pix(grids,blur)

def open_file(name,mode):
    try:
        return open(name,mode)
    except IOError as e:
        if name.isdigit():
            print >> sys.stderr, 'Missing image file'
        else:
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
    
    return image_grid(groups)

def update_pix(pixel_list,blur):
    header = pixel_list[0][0]
    pixels = pixel_list[1] 

    WIDTH = int(header[0])
    HEIGHT = int(header[1])
    COLOR = header[2]

    output = open_file('blurred.ppm','w')
    output.write('P3 '+str(WIDTH)+' '+str(HEIGHT)+' '+COLOR+' ')

    for y in range(HEIGHT):
        for x in range(WIDTH):
            clr = avg_clr(x,y,pixels,blur,WIDTH,HEIGHT)
            output.write(str(clr[0])+' '+str(clr[1])+' '+str(clr[2])+' ')

    output.close
    return output

def avg_clr(x,y,pixel_list,reach,width,height):
    r = 0
    g = 0
    b = 0

    pixel_count = 0
    for dy in range(-reach,reach+1):
        for dx in range(-reach,reach+1):
            px = x + dx
            py = y + dy
            if  0 <= px < width and 0 <= py < height:
                pixel_count += 1
                r += float(pixel_list[py][px][0])
                g += float(pixel_list[py][px][1])
                b += float(pixel_list[py][px][2])           

    return [(r/pixel_count),(g/pixel_count),(b/pixel_count)]        

def image_grid(groups):
    pixels = []
    header = groups[0:1]
    for i in range(len(groups)):
        if i != 0:
            pixels.append(groups[i])

    WIDTH = int(header[0][0])
    grids = grid(pixels,WIDTH)

    return [header,grids]

if __name__ == '__main__':
    main(sys.argv)
