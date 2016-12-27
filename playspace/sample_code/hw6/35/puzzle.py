import sys
from puzzle_utilities import *

def main():
    with open_file(sys.argv[1], "rb") as pic:
        #read through header
        header_1 = pic.readline().split()
        header_2 = pic.readline().split()
        header_3 = pic.readline().split()
        
        colors = []
        for line in pic:
            colors.append(line.split())
        
        raw_pixels = groups_of_three(colors)
        
        pixels = make_integers(raw_pixels)
        
        fixed = fix_red(pixels)
        
        print_to_file(header_1, header_2, header_3, fixed)

def make_integers(lists):
    list_of_lists = []
    for list in lists:
        new_list = []
        for [e] in list:
            new_list.append(int(e))
        list_of_lists.append(new_list)
    return list_of_lists
    
def fix_red(pixels):
    fixed = []
    for [r, g, b] in pixels:
        newr = r*10
        if newr > 255:
            newr = 255
        pixel = [newr, newr, newr]
        fixed.append(pixel)
    return fixed
    
def print_to_file(h1, h2, h3, pixels):
    with open_file("hidden.ppm", "w") as hidden:
        print >> hidden, ''.join(h1)
        print >> hidden, ' '.join(h2)
        print >> hidden, ''.join(h3)
        for [r, g, b] in pixels:
            print >> hidden, r
            print >> hidden, g
            print >> hidden, b
            
if __name__ == '__main__':
    main()