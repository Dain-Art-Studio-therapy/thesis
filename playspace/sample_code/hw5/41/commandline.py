# Name: Audrey Chan
# Instructor: Aaron Keen
# Section: 09

# Description: contains implementations of command-line processing functions

import sys
import data
import cast

def main(argv):
    if len(argv) < 2:
        print "usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]"
        exit(1)
    with open_file(argv[1], 'rb') as f:
        return process_file(f)

def open_file(name, mode):
    try:
        return open(name, mode)
    except:
        print "error:", name, "is not a valid file - could not be opened"
        exit(1)
    
def process_file(f):
    i = 0
    sph_list = []

    for line in f:

        if len(line.split()) != 11:
            print "malformed sphere on line", i + 1, "... skipping"

        else:
            try:
                sph = []
             
                for num in line.split():
                    sph.append(float(num))
                
                sphere = data.Sphere(data.Point(sph[0], sph[1], sph[2]), sph[3], data.Color(sph[4], sph[5], sph[6]), data.Finish(sph[7], sph[8], sph[9], sph[10]))
                sph_list.append(sphere)
            
            except:
                print "malformed sphere on line", i + 1, "... skipping"
        i += 1
    return sph_list

#main(sys.argv)
