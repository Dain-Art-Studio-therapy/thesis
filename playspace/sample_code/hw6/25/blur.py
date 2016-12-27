import sys
import math
import string

def main(argv):
    try:
        f = open(argv[1], 'r')
        grouper(argv)
    except:
        print "usage: python puzzle.py <filename>"

def arg_checker(argv):
    try:
        g = int(argv[2])
        return g
    except:
        g = 4
        return g
        
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
    
    for e in range(3, len(list), 3):
         list_create.append([list[e],list[e+1],list[e+2]])
    for i in range(0,len(list_create),list[0]):
        nested_new.append(list_create[i:i+list[0]])
    return nested_new

def calc(list,list2,argv):
    tmp = []
    final = []
    arg = arg_checker(argv)
    for y_loc in range(0,len(list)):
        for x_loc in range(0,list2[0]):
          pos_x_loc = arg + x_loc
          pos_y_loc = arg + y_loc
          neg_x_loc = x_loc - arg
          neg_y_loc = y_loc - arg
          if pos_x_loc >= list2[0]:
             pos_x_loc = list2[0]-1
          if pos_y_loc >= list2[1]:
             pos_y_loc = list2[1]-1
          if neg_x_loc <= 0:
             neg_x_loc = 0
          if neg_y_loc <= 0:
             neg_y_loc = 0
          for y_avg in range(neg_y_loc,pos_y_loc+1):
             for x_avg in range(neg_x_loc,pos_x_loc+1):
                color = list[y_avg][x_avg]
                tmp.append(color)
          final.append(tmp)
          tmp = []
    return average(final)

def average(list1):
   red_total = 0
   green_total = 0
   blue_total = 0
   new = []
   for row in list1:
      for x_pos in row:
         red_total +=x_pos[0]
         green_total +=x_pos[1]
         blue_total +=x_pos[2]
      red_average = red_total/len(row)
      green_average = green_total/len(row)
      blue_average = blue_total/len(row)
      average_list = [red_average,green_average,blue_average]
      red_total = 0
      green_total = 0
      blue_total = 0
      new.append(average_list)
   return new

def writer(list1,list2):
    with open('blurred.ppm', 'w') as f:
        print >> f, 'P3'
        print >> f, list2[0],list2[1]
        print >> f, list2[2]
        for color_list in list1:
            print >> f, color_list[0], color_list[1],color_list[2]

if __name__ == "__main__":
   main(sys.argv)
