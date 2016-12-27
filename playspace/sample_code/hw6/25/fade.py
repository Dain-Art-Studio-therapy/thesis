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
    new_in_groups1 = calc(new_in_groups,new_long,argv)
    header = [new_long[0],new_long[1],new_long[2]]
    writer(new_in_groups1,header)

def three_group(list):
    list_create = []
    nested_new = []
    nested_new_total = []
    for e in range(3, len(list), 3):
         list_create.append([list[e],list[e+1],list[e+2]])

    for i in range(0,len(list_create),list[0]):
        nested_new.append(list_create[i:i+list[0]])
    return nested_new
def calc(list,list2,argv):
    distance = 0
    scalar = 0
    new = []
    for y_loc in range(0,len(list)):
        for x_loc in range(0,list2[0]):
          distance =math.sqrt((int(argv[2])-y_loc)**2 +(int(argv[3])-x_loc)**2)
          scalar = ((int(argv[4])-distance)/int(argv[4]))
          if scalar < .2:
              scalar = .2
          r=(int(list[y_loc][x_loc][0]*scalar))
          g =(int(list[y_loc][x_loc][1]*scalar))
          b=(int(list[y_loc][x_loc][2]*scalar))
          new.append([r,g,b])
    return new
                               

def writer(list1,list2):
    with open('faded.ppm', 'w') as f:
        print >> f, 'P3'
        print >> f, list2[0],list2[1]
        print >> f, list2[2]
        for color_list in list1:
            print >> f, color_list[0], color_list[1],color_list[2]

if __name__ == "__main__":
   main(sys.argv)
