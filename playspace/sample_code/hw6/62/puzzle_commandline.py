from sys import *

def open_file(argv):
    if len(argv) < 2:
        print >> stderr, 'Need input file'
        exit(1)

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


def solve_colors(list, imagefile):
    for tuple in list:
        red = min(float(tuple[0])*10, 255)
        green = red
        blue = red
        newtuple = (red, green, blue)
        print_colors(newtuple, imagefile)



def decode(inputfile, imagefile, width, height):
    print >> imagefile, 'P3'
    print >> imagefile, width, height
    print >> imagefile, 255

    line_str = inputfile.read()
    list = line_str.split()    
    
    
    solve_colors(groups_of_3(list), imagefile)
    inputfile.close()
    imagefile.close()
     
