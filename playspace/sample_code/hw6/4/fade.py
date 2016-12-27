# Name: Audrey Chan
# Instructor: Aaron Keen
# Section: 09

# Description: program will output the faded image to a file named faded.ppm

import sys
import math

def main(argv):
    try:
        in_image = argv[1]
        row = int(argv[2])
        col = int(argv[3])
        radius = int(argv[4])

        with open(in_image, 'rb') as f:
            process_file(f, row, col, radius)
    except:
        print "invalid commandline entry: file not valid or non-integer inputs"


def distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def scale_pixel(dist, radius, r, g, b):
	sc = (float(radius - dist)) / float(radius)
	return max(0.2, sc)*r, max(0.2, sc)*g, max(0.2, sc)*b


def pixel_array(ppm):
    # Description: takes in a ppm file and converts it into an array            
    # of pixels                                                                 
	pix = []
	ppm_lines = ppm.readlines()
	
	for l in range(3, len(ppm_lines), 3):
		pix.append(ppm_lines[l:l+3])
		
	return pix, ppm_lines

	
def process_file(f, destX, destY, radius):
	faded = open('faded.ppm', 'w')
	pix_arr, ppm_lines = pixel_array(f)
		
	faded.writelines(ppm_lines[0:3])
    
	f_row = int(ppm_lines[1].split()[0])
	f_col = int(ppm_lines[1].split()[1])

	row = 0
	col = 0

	for color in pix_arr:
		r, g, b = scale_pixel(distance(row, col, destX,destY),
                                      radius,
                                      min(255, int(color[0])), 
                                      min(255, int(color[1])), 
                                      min(255, int(color[2])))
		print >> faded, int(r), int(g), int(b),
		
		if row + 1 < f_row:
			row += 1
		else:
			row = 0
			col += 1
        
	faded.close()


main(sys.argv)
