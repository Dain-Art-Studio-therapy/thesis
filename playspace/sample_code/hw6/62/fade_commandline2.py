from sys import *
import math

def checkargs(argv):
    if len(argv) < 5:
        print >> stderr, 'Need input file, row, column, and radius'
        exit(1)

    try:
        int(argv[2])
        int(argv[3])
        int(argv[4])
    except ValueError:
        print >> stderr, 'Row, column, and radius must be integers'
        exit(1)


def open_file(argv):
    try:
        return open(argv[1], 'rb')       
    except IOError as e:
        print >> stderr, '{0} : {1}'.format(argv[1], e.strerror)
        exit(1) 


def open_image_file(name, mode):
    try:
        return open(name, mode)
    except IOError as e:
        print >> stderr, '{0} : {1}'.format(name, e.stderr)
        exit(1)



def get_width_height(openfile):
   openfile.readline()
   list = openfile.readline().split()  
   openfile.readline()
   return list  
   


def groups_of_3(list):
    if list == []:
        return []

    newlist = []
    first = 0
    last = len(list)

    while first + 3 <= last:
        newgroup = []
        for i in range(first, first + 3):
            newgroup.append(list[i])
        newlist.append(newgroup)
        first += 3

    if first <= last - 1:
        lastgroup = []
        for num in range(first, last):
            lastgroup.append(list[num])
        newlist.append(lastgroup)

    return newlist


def print_colors(tuple, imagefile):
    print >> imagefile, tuple[0]
    print >> imagefile, tuple[1]
    print >> imagefile, tuple[2]


def getDistance(row, col, p_row, p_col):
    return math.sqrt((row - p_row)**2 + (col - p_col)**2)


def fade_tuple(distance, radius, tuple):
    component = max((radius - distance)/(radius), .20)
    red = int(tuple[0])*component
    green = int(tuple[1])*component
    blue = int(tuple[2])*component
    return (red, green, blue)



def solve_colors(radius, row, col, width, height, list, imagefile): 

    y_val = 0
    x_val = 0

    for tuple in list:
        distance = getDistance(row, col, y_val, x_val)
        newtuple = fade_tuple(distance, radius, tuple)
        print_colors(newtuple, imagefile)
        x_val += 1
        if (x_val == width):
            x_val = 0
            y_val += 1


def fade(inputfile, imagefile, width, height, row, col, radius):
    print >> imagefile, 'P3'
    print >> imagefile, width, height
    print >> imagefile, 255    
    
    line_str = inputfile.read()
    list = line_str.split() 

    wid = int(width)
    hgt = int(height)
    solve_colors(radius, row, col, wid, hgt, groups_of_3(list), imagefile)
   
