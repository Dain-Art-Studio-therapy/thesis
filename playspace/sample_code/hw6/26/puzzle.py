import sys
import math

# from puzzle_funcs import *

def open_file(name, mode):
        try:
                return open(name, mode)
        except:
                print >> sys.stderr, '{0}:{1}'.format(name, "File wont open")
                exit(1)

def format_color(X):
        r = X * 10
        if r > 255:
                r = 255
        return r

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
        with open_file('decode.ppm', "w") as H:
                print >> H, 'P3'
                print >> H, y[0], y[1]
                print >> H, 255
                for i in (list):
                        print >> H, format_color(i[0]), format_color(i[0]), format_color(i[0])

def main(argv):
        with open_file(argv[1], 'rb') as f:
                X = list_transformer(f)
                Y = color_list(X)
        return Y

wh = find_width_height(sys.argv)
final_list = main(sys.argv)

decode_image(final_list, wh)


if __name__=='__main__':
        main(sys.argv)


