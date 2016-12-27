import sys
from data import *

def eye(argv):
    for i in range(len(argv)):
        if argv[i] == '-eye':
            return eye_pt(argv[i])
        else:
            return Point(0.0,0.0,-14.0)

def view(argv):
    for i in range(len(argv)):
        if argv[i] == '-view':
            return window(argv[i])
        else:
            min_x = -10
            max_x = 10
            min_y = -7.5
            max_y = 7.5
            width = 128
            height = 96
            window = [min_x,max_x,min_y,max_y,width,height]
            return window

def light(argv):
    for i in range(len(argv)):
        if argv[i] == '-light':
            return lighting(argv[i])
        else:
            pt = Point(-100.0,100.0,-100.0)
            clr = Color(1.5,1.5,1.5)
            return Light(pt,clr)

def ambient(argv):
    for i in range(len(argv)):
        if argv[i] == '-ambient':
            return amb_clr(argv[i])
        else:
            return Color(1.0,1.0,1.0)

def eye_pt(list):
    x,y,z = float(argv[i+1]),float(argv[i+2]),float(argv[i+3])
    return Point(x,y,z)

def window(list):
    min_x = float(argv[i+1])
    max_x = float(argv[i+2])
    min_y = float(argv[i+3])
    max_y = float(argv[i+4])
    width = float(argv[i+5])
    height = float(argv[i+6])
    viewing = [min_x,max_x,min_y,max_y,width,height]
    return viewing

def lighting(list):
    pt.x,pt.y,pt.z  = float(argv[i+1]),float(argv[i+2]),float(argv[i+3])
    light.pt = Point(pt.x,pt.y,pt.z)
    clr.r,clr.g,clr.b = float(argv[i+4]),float(argv[i+5]),float(argv[i+6])
    light.clr = Color(clr.r,clr.b,clr.g)
    return Light(light.pt,light.clr)

def amb_clr(list):
    clr.r,clr.g,clr.b = float(argv[i+1]),float(argv[i+2]),float(argv[i+3])
    return Color(clr.r,clr.g,clr.b)
