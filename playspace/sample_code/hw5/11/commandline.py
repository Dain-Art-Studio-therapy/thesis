import sys
from data import * 

def parse_args(argv):
    eye_set = False
    view_set = False
    light_set = False
    ambient_set = False

    for i in range(0,len(argv)):
        try:
            if argv[i] == '-eye':
                eye = Point(float(argv[i+1]),float(argv[i+2]),float(argv[i+3]))
                eye_set = True
        except:
            sys.stderr.write('Invalid eye values specified.\
 Using default values.\n')

        try:
            if argv[i] == '-view':   
                min_x = float(argv[i+1])
                max_x = float(argv[i+2])
                min_y = float(argv[i+3])
                max_y = float(argv[i+4])
                width = int(argv[i+5])
                height = int(argv[i+6])
                view_set = True
        except:
            sys.stderr.write('Invalid view values specified.\
 Using default values.\n')

        try:
            if argv[i] == '-light': 
                x = float(argv[i+1])
                y = float(argv[i+2])
                z = float(argv[i+3])
                r = float(argv[i+4])
                g = float(argv[i+5])
                b = float(argv[i+6])
                light = Light(Point(x,y,z),Color(r,g,b))
                light_set = True
        except:
            sys.stderr.write('Invalid light values specified.\
 Using default values.\n')

        try:
            if argv[i] == '-ambient':    
                r = float(argv[i+1])
                g = float(argv[i+2])
                b = float(argv[i+3])
                ambient = Color(r,g,b)
                ambient_set = True
        except:
            sys.stderr.write('Invalid ambient values specified.\
 Using default values.\n')

    if not(eye_set):
        eye = Point(0.0,0.0,-14.0)
    if not(view_set):
        min_x = -10
        max_x = 10
        min_y = -7.5
        max_y = 7.5
        width = 1024
        height = 768
    if not(light_set):
        light = Light(Point(-100.0,100.0,-100.0), Color(1.5,1.5,1.5))
    if not(ambient_set):
        ambient = Color(1.0,1.0,1.0)

    return (eye, min_x, max_x, min_y, max_y, width, height, light, ambient)

def analyze_file(argv):
    l = []
    linenum = 1
    try:
        with open(argv[1],'rb') as f:
            for line in f:
                sphere = parse_line(line,linenum)
                if sphere != None:
                    l.append(sphere)
                linenum += 1
    except IndexError:
        sys.stderr.write('usage: python ray_caster.py <filename> [-eye x y z]\
 [-view min_x max_x min_y max_y width height] [-light x y z r g b]\
 [-ambient r g b]\n')
        exit()
    except:
        sys.stderr.write('Invalid file specified.File could not be read.\n')
        exit()   
    return l

def parse_line(line,linenum):
    try:
        sp = line.split(" ")
        if len(sp) != 11:
            raise Exception()
        sp = convert_list_float(sp)
        return Sphere(Point(sp[0],sp[1],sp[2]),sp[3],
Color(sp[4],sp[5],sp[6]),Finish(sp[7],sp[8],sp[9],sp[10]))
    except:
        sys.stderr.write('Invalid sphere on line %i...skipping.\n' % linenum)
        return None
     
def convert_list_float(sp):
    l = []
    try:
        for i in sp:
            l.append(float(i))
    except:
        raise Exception()
    return l


