import sys
import math

def groups_of_num(list, num):
    return [list[e:e+num] for e in range(0, len(list), num)]

def open_file():
     try:
        inputfile = open(sys.argv[1], "r")
        return inputfile
     except:
        print "Error: File does not work"
        exit()
        
def altering_file():
    input_number = inputfile.read()
    nums_per_line = input_number.replace('\n', ' ')
    values = nums_per_line.split()
    return values
    
def main():
    inputfile = open_file()
    
    try:
        reach =  int(sys.argv[2])
        return reach
    except:
        reach = 4
        return reach
        
    values = altering_file()
    pixel_list = groups_of_num(values[4:], 3)
    pixels = groups_of_num(pixel_list, int(values[1]))
    
    file =  open("blurred.ppm", "w")
    file.write("P3\n")
    file.write(values[1] + " " + values[2] + "\n")
    file.write(values[3] + "\n")
    
    for row in range(int(values[2])):
        for col in range(int(values[1])):
            r = 0
            g = 0
            b = 0
            total = 0
            for j in range(row - reach, row+reach+1):
                for i in range(col - reach, col + reach +1):
                    if i >=0 and i <= int(values[1])-1 and j >= 0 and j <= int(values[2])-1:
                        r +=int(pixels[j][i][0])
                        g += int(pixels[j][i][1])
                        b += int(pixels[j][i][2])
                        total += 1
            r = (r/total)
            g = (g/total)
            b = (b/total)
            file.write(str(r) + ' ' + str(g) + ' ' + str(b) + '/n')
if __name__ == "__main__":
    main()
