from sys import *
import cast
from data import *

def open_file(argv):
    if len(argv) < 2:
        m1 = 'usage: python ray_caster.py <filename> [-eye x y z]'
        m2 = ' [-view min_x max_x min_y max_y width height]'
        m3 = ' [-light x y z r g b] [-ambient r g b]'
        print >> stderr, m1+m2+m3
        exit(1)
    try:
        return open(argv[1], 'rb')
        
    except IOError as e:
        print >> stderr, '{0} : {1}'.format(argv[1], e.strerror)
        exit(1)          


def find_eye(argv):
    flag = 0
    for i in range(2, len(argv)):
        if argv[i] == '-eye':
           flag = i

    if len(argv)-1 < flag+3 or flag == 0:
            return Point(0.0, 0.0, -14.0)

    excepts = 0
    for j in range(flag+1, flag+4):
        try:
            float(argv[j])
        except:
            excepts += 1

    if excepts != 0:
        return Point(0.0, 0.0, -14.0)
    else:
        valx = float(argv[flag+1])
        valy = float(argv[flag+2])
        valz = float(argv[flag+3])
        return Point(valx, valy, valz)
            

def find_view(argv):
    flag = 0
    for i in range(2, len(argv)):
        if argv[i] == '-view':
           flag = i

    if len(argv)-1 < flag + 6 or flag == 0:
        return [-10.0, 10.0, -7.5, 7.5, 1024, 768]

    excepts = 0
    for j in range(flag+1, flag+7):
        try:
            float(argv[j])
        except:
            excepts += 1

    if excepts != 0:
        return [-10.0, 10.0, -7.5, 7.5, 1024, 768]
    else:
        min_x = float(argv[flag+1])
        max_x = float(argv[flag+2])
        min_y = float(argv[flag+3])
        max_y = float(argv[flag+4])
        width = float(argv[flag+5])
        height = float(argv[flag+6])
        return [min_x, max_x, min_y, max_y, width, height]



def find_light(argv):
    flag = 0
    for i in range(2, len(argv)):
        if argv[i] == '-light':
           flag = i

    if len(argv)-1 < flag+6 or flag == 0:
        return Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))

    excepts = 0
    for j in range(flag+1, flag+7):
        try:
            float(argv[j])
        except:
            excepts += 1
    if excepts != 0:
        return Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5)) 
    else:
        x = float(argv[flag+1])
        y = float(argv[flag+2])
        z = float(argv[flag+3])
        r = float(argv[flag+4])
        g = float(argv[flag+5])
        b = float(argv[flag+6])
        point = Point(x, y, z)
        color = Color(r, g, b)
        return Light(point, color)



def find_ambient(argv):
    flag = 0
    for i in range(2, len(argv)):
        if argv[i] == '-ambient':
           flag = i

    if len(argv)-1 < flag+3 or flag == 0:
        return Color(1.0, 1.0, 1.0)
    
    excepts = 0
    for j in range(flag+1, flag+4):
        try:
            float(argv[j])
        except:
            excepts += 1

    if excepts != 0:
        return Color(1.0, 1.0, 1.0)
    else:
        r = float(argv[flag+1])
        g = float(argv[flag+2])
        b = float(argv[flag+3])
        return Color(r, g, b)



def get_spheres(sphere_file):
        sphere_list = []
        total_exc = 0

        for i, line in enumerate(sphere_file):
            val = line.split()
            s_err = 'malformed sphere on line {0} ... skipping'.format(i+1)
            ins = []
            excepts = 0
            for num in val:
                try:
                    var = float(num)
                    ins.append(var)
                except:
                    excepts += 1

            if len(val) != 11 or excepts != 0:
                total_exc += 1
                print >> stderr, s_err  
            else: 
                x = ins[0]
                y = ins[1]
                z = ins[2]
                center = Point(x, y, z)
                radius = ins[3]
                r = ins[4]
                g = ins[5]
                b = ins[6]
                color = Color(r, g, b)
                f1 = ins[7]
                f2 = ins[8]
                f3 = ins[9]
                f4 = ins[10]
                finish = Finish(f1, f2, f3, f4)
                newsphere = Sphere(center, radius, color, finish)
                sphere_list.append(newsphere) 
        if total_exc != 0:
            exit(1)
        sphere_file.close()
        return sphere_list

    
def open_image_file(name, mode):
    try:
        return open(name, mode)
    except IOError as e:
        print >> stderr, '{0} : {1}'.format(name, e.stderr)
        exit(1)
