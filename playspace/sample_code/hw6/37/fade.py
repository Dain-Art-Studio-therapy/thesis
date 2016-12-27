
import sys
import math

row = int(sys.argv[2])
col = int(sys.argv[3]) 
radius = int(sys.argv[4])




def open_file(name,mode): 
    try: 
        return open(name,mode) 
    except IOError as e: 
        print >>sys.stderr, '{0}:{1}'.format(name,e.strerror) 
        exit(1) 


def groups_of_3(nums):
    threes = []
    for i in range(0,len(nums),3):
        threes.append(nums[i:i+3])
    return threes


def process_file(f):
    line_after_header = []
    for line in f:
        line_after_header.append(line)
    return line_after_header

def process_header(f):
    head = [next(f) for x in xrange(3)]    
    return head


def read(File):

    faded = open('faded.ppm','w')

    header = process_header(File)
    for line in header:
        faded.write(line)

    width_height = header[1].split( )
    width = int(width_height[0])
    height = int(width_height[1])
   
    lines_after_header = process_file(File)
    intLines = [int(i) for i in lines_after_header]

    pixel_list = groups_of_3(intLines)
    pixel_grid = []
    for i in range(0,len(pixel_list),width):
        pixel_grid.append(pixel_list[i:i+width])

    for row_index in range(len(pixel_grid)):
        for pixel_index in range(len(pixel_grid[row_index])):
            pixel_x = pixel_index
            pixel_y = row_index

            distance = math.sqrt((col - pixel_x)**2 + (row - pixel_y)**2)
            scalar = max(0.2,((radius - distance)/radius))

            scale_r = int(pixel_grid[pixel_y][pixel_x][0] * scalar)
            scale_g = int(pixel_grid[pixel_y][pixel_x][1] * scalar)
            scale_b = int(pixel_grid[pixel_y][pixel_x][2] * scalar)

            faded.write(str(scale_r) + ' ' + str(scale_g) + ' ' + str(scale_b) + '\n')
        
    faded.close()





def main(inFile):
    with open_file(inFile,'r') as f:

        read(f)
       






if __name__=='__main__':
    main(sys.argv[1])

