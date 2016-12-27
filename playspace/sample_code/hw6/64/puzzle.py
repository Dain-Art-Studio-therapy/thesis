import sys

def main():
    pixel_list_1 = list_of_pixels()
    grouped_pixel_list = groups_of_3(pixel_list_1)
    output_file(grouped_pixel_list)
    
        
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

def groups_of_3(l1):
    l2 = [l1[i:i+3] for i in range(0,len(l1),3)]
    return l2

def output_file (l1):
    ppmfile = open('hidden.ppm','w')
    ppmfile.write('P3\n')
    ppmfile.write(str(l1[0][0])+ ' ' + str(l1[0][1]) + '\n')
    ppmfile.write('255\n')
    for i in range(1,len(l1)):
        red = l1[i][0] * 10
        green = red
        blue =  red
        if red > 255:
            red = 255
        ppmfile.write(str(red) + ' ' + str(green) + ' ' + str(blue) + '\n')

if __name__ == '__main__':
    main()

    
