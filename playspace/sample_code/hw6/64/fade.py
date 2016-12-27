import sys
import math
# fade.py input_file.ppm row(y-coordinate) col(x-coordinate) radius
# read pixel, process pixel, output pixel
# output image to a file called faded.ppm
# all column for row 0 prints first

def main():
    try:
        row_pt = sys.argv[2]
        col_pt = sys.argv[3]
        radius = sys.argv[4]
    except:
        print 'Check values and re-enter!'
        exit(1)
    
    all_pixel_list = list_of_pixels()
    grouped_list = groups_of_3 (all_pixel_list)


    
    width = int(grouped_list[0][0])
    height = int(grouped_list[0][1])
    
    grouped_by_width = groups_by_width(grouped_list, width)

    output_file_ppm(width, height)
    
    for row_pix in range(len(grouped_by_width)):
        for col_pix in range(len(grouped_by_width[row_pix])):
            pixel = grouped_by_width[row_pix][col_pix]
            distance = distance_pixel(int(row_pt), int(col_pt), int(row_pix), int(col_pix))
            scale_value = process_pixel_val(int(radius), float(distance))
            print_new_pixel(float(scale_value), pixel)   
        
        
def list_of_pixels():
    try:
        input_file = open(sys.argv[1],'rb')
    except:
        print 'File cannot be opened!'
        exit(1)
    all_list = [ ] # creat empty list
    for line in input_file: #for each line
        s = line.split() #make list by splitting each line
        for num in s:
            all_list.append(num) #append all values in line
    del all_list[0]
    test = len(all_list)
    return all_list

def groups_of_3 (l1):
    l2 = [l1[i:i+3] for i in range(0,len(l1),3)]
    return l2


def groups_by_width (l1,num):
    l2 = [l1[i:i+num] for i in range(0,len(l1),num)]
    return l2
    

def distance_pixel(row_pt, col_pt, row_pix, col_pix):
    return math.sqrt((row_pt - row_pix) ** 2 + (col_pt - col_pix) ** 2)

def process_pixel_val(radius, distance):
    scale_value = (radius - distance) / radius
    if scale_value >= 0.2:
        return scale_value
    else:
        return 0.2
    
def output_file_ppm(width,height):
    ppmfile = open('faded.ppm','w')
    ppmfile.write('P3\n')
    ppmfile.write(str(width) + ' ' + str(height) + '\n')
    ppmfile.write('255\n')

def print_new_pixel(scale_value, l1):
    ppmfile = open('faded.ppm','w')
    red = int(l1[0]) * scale_value
    green = int(l1[1]) * scale_value
    blue = int(l1[2]) * scale_value
    ppmfile.write(str(red) + ' ' + str(green) + ' ' + str(blue) + '\n')

if __name__ == '__main__':
    main()
