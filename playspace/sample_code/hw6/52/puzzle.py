import sys

def groups_of_3(list):
    #splits the list of pixels into groups of three
    return [list[e:e+3] for e in range(0,len(list),3)]

def open_file():
    try:
        # opens and returns input file
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

    # header
    file = open('hidden.ppm', 'w')
    file.write('P3\n')
    file.write(values[1] + ' ' + values[2] + '\n')
    file.write(values[3] + '\n')
    
    for e in pixel_list:
        e[0] = min(int(e[0]) * 10, 225)
        first = str(e[0])
        file.write(first + ' ' + first + ' ' + first + '\n')
        
if __name__ == '__main__':
    main()
        

       
    
