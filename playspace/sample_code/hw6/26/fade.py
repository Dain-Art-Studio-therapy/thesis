import sys
from math import *

def row_flag(argv):
        try:
                for i in range(len(argv)):
                        x = float(argv[2])
                return x
        except:
                print >> stderr, "row was not correct format"
def col_flag(argv):
        try:
                for i in range(len(argv)):
                        x = float(argv[3])
                return x
        except:
                print >> stderr, "col was not correct format"

def radius_flag(argv):
        try:
                for i in range(len(argv)):
                        x = float(argv[4])
                return x
        except:
                print >> stderr, "radius was not correct format"

def open_file(name, mode):
        try:
                return open(name, mode)
        except:
                print >> sys.stderr, '{0}:{1}'.format(name, "File wont open")
                exit(1)

def list_transformer(f):
        pixel_list = []
        count = 0
        lines = f.readlines()[3:]
        for line in lines:
                count += 1
                nums = line.split()
                for e in nums:
                        pixel_list.append(int(e))
        return pixel_list

def color_list(pixel_list):
        set_of_three = []
        for i in range(0, len(pixel_list), 3):
                if i + 2 < len(pixel_list):
                        set_of_three.append([pixel_list[i],
                                             pixel_list[i + 1],
                                             pixel_list[i + 2]])
        return set_of_three

def list_combo(set_of_three, x, y):
        num = 0
        frsh = []
        work = set_of_three
        for row in range(int(y)):
                for col in range(int(x)):
                        pt = [row, col]
                        work[num].append(pt)
                        frsh.append(work[num])
                        num = num + 1
        return frsh

def find_distance(argv, X):
        distance = sqrt((row_flag(argv) - X[3][0]) ** 2 + (col_flag(argv) - X[3][1]) ** 2)
        return distance

def shader_finder(argv, X, distance):
        r = ((radius_flag(argv) - distance) / radius_flag(argv))
        if r < 0.2:
                r = 0.2
        return r * X
def scaled_list(list):
        next_list = []
        for i in list:
                n = find_distance(sys.argv, i)
                f = shader_finder(sys.argv, i[0], n)
                g = shader_finder(sys.argv, i[1], n)
                h = shader_finder(sys.argv, i[2], n)
                next_list.append([f, g, h])
        return next_list

def find_width_height(argv):
        list = []
        with open_file(argv[1], 'rb') as f:
                lines = f.readlines()[1:2]
                for line in lines:
                        nums = line.split()
                        for e in nums:
                                list.append(int(e))
                return list

def decode_image(list, y):
        with open_file('faded.ppm', "w") as H:
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
                Z = list_combo(Y, y[0], y[1])
                ZZ = scaled_list(Z)
        return ZZ


wh = find_width_height(sys.argv)
final_list = main(sys.argv)

decode_image(final_list, wh)


if __name__=='__main__':
        main(sys.argv)


