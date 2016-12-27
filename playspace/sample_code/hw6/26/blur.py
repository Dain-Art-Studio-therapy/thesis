import sys
from math import *

def range_flag(argv):
        try:
                return int(argv[2])
        except:
                return 4

def open_file(name, mode):
        try:
                return open(name, mode)
        except:
                print >> sys.stderr, '{0}:{1}'.format(name, "File wont open")
                exit(1)

def find_width_height(argv):
        list = []
        with open_file(argv[1], 'rb') as f:
                lines = f.readlines()[1:2]
                for line in lines:
                        nums = line.split()
                        for e in nums:
                                list.append(int(e))
                return list

def list_transformer(f):
        pixel_list = []
        counter = 0
        lines = f.readlines()[3:]
        for line in lines:
                counter += 1
                nums = line.split()
                for e in nums:
                        pixel_list.append(int(e))
        return pixel_list

def color_list(pixel_list):
        set_of_three = []
        for i in range(0, len(pixel_list), 3):
                if i + 2 < len(pixel_list):
                        set_of_three.append([pixel_list[i], pixel_list[i + 1],  pixel_list[i + 2]])
        return set_of_three

def w_h_list(list):
        XY = find_width_height(sys.argv)
        w_h_list = []
        q = 0
        for x in range(0, XY[1]):
                r_list = []
                for y in range(0, XY[0]):
                        zz = list[q]
                        r_list.append(zz)
                        q += 1
		w_h_list.append(r_list)
        return w_h_list

def scribble(list):
        RV = range_flag(sys.argv)
        XY = find_width_height(sys.argv)
        new_list = []
        for i in range(len(list)):
                for j in range(len(list[i])):
                        if i-RV < 0:
                                start = 0
                        else:
                                start = i-RV
                        if i+RV > XY[1]-1:
                                end = XY[1]
                        else:
                                end = i+RV+1
                        if j-RV < 0:
                                starts = 0
                        else:
                                starts = j-RV
                        if j+RV > XY[0]-1:
                                ends = XY[0]
                        else:
                                ends = j+RV+1
                        Reds = []
                        Blues = []
                        Greens = []
                        for x in range(start, end):
                                for y in range(starts, ends):
                                        Reds.append(list[x][y][0])
                                        Blues.append(list[x][y][1])
                                        Greens.append(list[x][y][2])
                        Red = sum([float(r) for r in Reds]) / len(Reds)
                        Blue = sum([float(g) for g in Greens]) / len(Greens)
                        Green = sum([float(b) for b in Blues]) / len(Blues)
                        new_list.append([Red, Green, Blue])
        return new_list

def decode_image(list, y):
        with open_file('blurred.ppm', "w") as H:
                print >> H, 'P3'
                print >> H, y[0], y[1]
                print >> H, 255
                for i in (list):
                        print >> H, int(i[0]), int(i[1]), int(i[2])
def main(argv):
        y = find_width_height(argv)
        with open_file(argv[1], 'rb') as f:
                X = list_transformer(f)
                Y = color_list(X)
                Z = w_h_list(Y)
                D = scribble(Z)
        return D


wh = find_width_height(sys.argv)
final_list = main(sys.argv)

decode_image(final_list, wh)


if __name__=='__main__':
        main(sys.argv)

