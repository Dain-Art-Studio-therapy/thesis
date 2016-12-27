# blur.py (int value -->"neighbor reach")
# if second not present, neighbor reach = 4

def main():
    pixel_list = list_of_pixels()
    grouped_list = groups_of_3 (all_pixel_list)

    neighbor_reach = sys.argv[1]
    width = grouped_list[0][0]
    height = grouped_list[0][1]

    grouped_by_width = groups_by_width(grouped_list, width)

    output_file_ppm()

    for row_pix in range(len(grouped_by_width)):
        for col_pix in range(len(grouped_by_width[row])):
            pixel = grouped_by_width[row_pix][col_pix]
            neighbor_list = neighboring_pixels(row_pix, col_pix, grouped_by_width, neighbor_reach)
            color_list = find_avg_color(neighbor_list)
            print_new_pixel(color_list)
        
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

def groups_by_width(l1,width):
    l2 =[l1[i:i+width] for i in range(1,len(l1),width)]

def neighboring_pixels(row_pix, col_pix, pixel_list, neighbor_reach):
    list_of_neighbors = []
    for val in range(1, neighbor_reach):
        for val2 in range(1, neighbor_reach):
            try:
                pixel1 = pixel_list[row_pix + val][col_pix + val2]
                list_of_neighbors.append(pixel1)
            except:
                None
            try:
                pixel2 = pixel_list[row_pix - val][col_pix + val2]
                list_of_neighbors.append(pixel2)
            except:
                None
            try:
                pixel3 = pixel_list[row_pix + val][col_pix - val2]
                list_of_neighbors.append(pixel3)
            except:
                None
            try:
                pixel4 = pixel_list[row_pix - val][col_pix - val2]
                list_of_neighbors.append(pixel4)
            except:
                None
    return list_of_neighbors

def find_avg_color(l1):
    red_sum = 0
    green_sum = 0
    blue_sum = 0
    total = len(l1)
    for i in range(len(l1)):
        red = l1[0]
        green = l1[1]
        blue = l1[2]
        red_sum += red
        green_sum += green
        blue_sum += blue
    avg_red = red_sum / total
    avg_green = green_sum / total
    avg_blue = blue_sum / total
    return [avg_red, avg_green, avg_blue]
           
def output_file_ppm(width,height):
    ppmfile = open('blurred.ppm','w')
    ppmfile.write('P3\n')
    ppmfile.write(str(width) + ' ' + str(height) + '\n')
    ppmfile.write('255\n')

def print_new_pixel(scale_value, l1):
    ppmfile = open('blurred.ppm','w')
    red = l1[0]
    green = l1[1]
    blue = l1[2]
    ppmfile.write(str(red) + ' ' + str(green) + ' ' + str(blue) + '\n')
