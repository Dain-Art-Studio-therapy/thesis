import sys
import math
import string

def main(argv):
    try:
        f = open(argv[1], 'r')
        grouper(argv)
    except:
        print "usage: python puzzle.py <filename>"

def grouper(argv):
    long_line = []
    new_long = []
    new_in_groups = []
    f = open(argv[1], 'r')
    for line in f:
        indvl = line.split()
        for item in indvl:
            long_line.append(item)
    long_line.remove(long_line[0])
    for string in long_line:
        new_long.append(int(string))
    new_in_groups = three_group(new_long)
    header = [new_long[0],new_long[1],new_long[2]]
    writer(new_in_groups,header)

def three_group(list):
    list_create = []
    for e in range(3, len(list), 3):
         g = list[e]*10
         if g>255:
             g = 255
         list_create.append([g,g,g])
    return list_create

def writer(list1,list2):
    with open('hidden.ppm', 'w') as f:
        print >> f, 'P3'
        print >> f, list2[0],list2[1]
        print >> f, list2[2]
        for color_list in list1:
            print >> f, color_list[0], color_list[1],color_list[2]

if __name__ == "__main__":
   main(sys.argv)
