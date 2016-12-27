import sys
import math

def groups_of_3(list):
    #splits the list of pixels into groups of three 
    return [list[e:e+3] for e in range(0, len(list), 3)]

def open_file():
    #opens and returns input file
    try:
        inputfile = open(sys.argv[1], 'r')
        return inputfile
    except:
        print 'Error: File does not work'
        exit()
        
def reading_file():
    # reads file and gives the different variables back
    input_file = open_file()
    input_file_values = input_file.read()
    nums_per_line = input_file_values.replace('\n', ' ')
    values = nums_per_line.split()
    return values

def main():
    values = reading_file()
    pixel_list = groups_of_3(values[4:])

    #header
    file = open('faded.ppm', 'w')
    file.write('P3\n')
    file.write(values[1] + ' ' + values[2] + '\n')
    file.write(values[3] + '\n')

    pixel_y = sys.argv[2]
    pixel_x = sys.argv[3]
    r = sys.argv[4]
    count = 0

    for y in range(int(values[2])):
        #goes through each y value 
        for x in range(int(values[1])):
            #goes through each x value within each y value
            d = abs(math.sqrt((int(pixel_x) - x) ** 2 + (int(pixel_y) - y) ** 2))
            scale = max(((int(r) - d) / float(r)), 0.2)
            
            pixel_list[count][0] = str(int(int(pixel_list[count][0]) * scale))
            pixel_list[count][1] = str(int(int(pixel_list[count][1]) * scale))
            pixel_list[count][2] = str(int(int(pixel_list[count][2]) * scale))
            
            first = pixel_list[count][0]
            second = pixel_list[count][1]
            third = pixel_list[count][2]
    
            file.write(first + ' '  + second + ' ' + third + '\n')
            count +=1

if __name__ == '__main__':
    main()
        
