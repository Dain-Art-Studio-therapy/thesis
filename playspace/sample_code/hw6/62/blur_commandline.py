from sys import *
import math

def checkargs(argv):
    if len(argv) < 2:
        print >> stderr, 'Need input file'
        exit(1)
    
    if len(argv) == 3:
        try:
            r = int(argv[2])
            if r < 0:
                raise ValueError
        except ValueError:
            print >> stderr, 'Reach must be a positive integer'
            exit(1)


def getReach(argv):
    if len(argv) == 3:
        return int(argv[2])
    else:
        return 4        


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


def gridPixels(list, width, height):
    newlist = []
    index = 0

    for i in range(height):
        newrow = []
        for j in range(width):
            pixel = list[index]
            newrow.append(pixel)
            index += 1
        newlist.append(newrow)
    return newlist



def print_colors(tuple, imagefile):
    print >> imagefile, tuple[0]
    print >> imagefile, tuple[1]
    print >> imagefile, tuple[2]


def getbounds(row, col, reach, width, height):
    startx = 0
    endx = 0
    starty = 0
    endy = 0

    #evaluate first col
    if (col - reach) < 0:
        startx = 0
    else:
        startx = col - reach

    #evaluate last col
    if (col + reach) > width-1:
        endx = width
    else:
        endx = col + reach + 1

    #evaluate first row
    if (row - reach) < 0:
        starty = 0
    else:
        starty = row - reach

    #evaluate last row
    if (row + reach) > height-1:
        endy = height
    else:
        endy = row + reach + 1
    
    return [startx, endx, starty, endy]


def blur_tuple(row, col, boundlist, gridlist):
    startx = boundlist[0]
    endx = boundlist[1]
    starty = boundlist[2]
    endy = boundlist[3]  

    av_red = 0
    av_green = 0
    av_blue = 0
    numprocessed = 0

    for y in range(starty, endy):
        for x in range(startx, endx):     
                pixel = gridlist[y][x]
                av_red += int(pixel[0])
                av_green += int(pixel[1])
                av_blue += int(pixel[2])        
                numprocessed += 1

    finalred = av_red / numprocessed
    finalgreen = av_green / numprocessed
    finalblue = av_blue / numprocessed   

    return (finalred, finalgreen, finalblue)



def solve_colors(reach, width, height, list, imagefile): 
    gridlist = gridPixels(list, width, height)
    blurlist = []

    for row in range(height):
        for col in range(width):
            bounds = getbounds(row, col, reach, width, height)
            blurlist.append(blur_tuple(row, col, bounds, gridlist))
   
    for tuple in blurlist:
        print_colors(tuple, imagefile)


def blur(inputfile, imagefile, width, height, reach):
    print >> imagefile, 'P3'
    print >> imagefile, width, height
    print >> imagefile, 255    
    
    line_str = inputfile.read()
    list = line_str.splitlines() 

    wid = int(width)
    hgt = int(height)
    solve_colors(reach, wid, hgt, groups_of_3(list), imagefile)
