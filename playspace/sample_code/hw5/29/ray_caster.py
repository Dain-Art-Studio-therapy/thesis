import sys
from data import *
from cast import *
from commandline import *

def main(argv):
    if len(argv) == 1:
        print 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
        exit(1)
    with open_file(argv[1],'rb') as s:
        sphere_list = process_file(s)
    eye_pt = eye(argv)
    win = view(argv)
    l = light(argv)
    amb_clr = ambient(argv)    
    return cast_all_rays(win[0],win[1],win[2],win[3],win[4],win[5],eye_pt,sphere_list,amb_clr,l)

def open_file(name,mode):
    try:
        return open(name,mode)
    except IOError as e:
        print 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
        exit(1)

def process_file(s):
    spheres = []
    line_num = 0
    for line in s: 
        info = line.split()
        if len(info) == 11:
            sph = init_sphere(info)
            spheres.append(sph)
        else:
            print 'Malformed sphere on line ',line_num
        line_num += 1
    return spheres

def init_sphere(line): 
    pt = Point(float(line[0]),float(line[1]),float(line[2]))
    rad = float(line[3])
    clr = Color(float(line[4]),float(line[5]),float(line[6]))
    fin = Finish(float(line[7]),float(line[8]),float(line[9]),float(line[10]))
    return Sphere(pt,rad,clr,fin)

if __name__ == '__main__':
    main(sys.argv)
