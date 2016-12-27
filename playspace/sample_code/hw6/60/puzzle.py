import sys
from puzzle_groups import groups_of_3

def main(argv):
    if len(argv) != 2:
        print >> sys.stderr, 'Image file missing'
        exit(1)

    with open_file(argv[1],'rb') as image:
        pixels = process_file(image)

    return update_pix(pixels)

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

def update_pix(pixel_list):
    output = open_file('hidden.ppm','w')
    header = pixel_list[0]
    output.write('P3 '+header[0]+' '+header[1]+' '+header[2]+' ')

    for i in range(1,len(pixel_list)):
        pixel = str(capValue(float(pixel_list[i][0])*10))
        output.write(pixel+' '+pixel+' '+pixel+' ')

    output.close
    return output

def capValue(int):
    if 0.0 <= int <= 255.0:
        return int
    else:
        return 255.0

if __name__ == '__main__':
    main(sys.argv)
