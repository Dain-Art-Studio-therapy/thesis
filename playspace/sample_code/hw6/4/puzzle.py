# Name: Audrey Chan
# Instructor: Aaron Keen
# Section: 09

# Description: processes an image's pixels and hides a real image 
# behind the red components of the pixels

import sys

def main(argv):
    try:
        with open(argv[1], 'rb') as f:
            process_file(f)
    except:
        print "invalid commandline entry: file could not be read"


def pixel_array(ppm):
    # Description: takes in a ppm file and converts it into an array
    #              of pixels
    pix = []
    ppm_lines = ppm.readlines()

    for l in range(3, len(ppm_lines), 3):
        pix.append(ppm_lines[l:l+3])

    return pix, ppm_lines
                


def process_file(input_file):
    # Description: reads pixels and decode puzzle images 
    #              into new .ppm file
    hidden = open('hidden.ppm', 'w')
    pix_arr, ppm_lines = pixel_array(input_file)

    hidden.writelines(ppm_lines[0:3])
    
    for color in pix_arr:
        r = min(255, int(color[0])*10)
        print >> hidden, r, r, r

    hidden.close()


main(sys.argv)
