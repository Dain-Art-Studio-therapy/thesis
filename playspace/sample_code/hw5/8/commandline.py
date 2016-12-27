# Implementations of command-line processing functions 
# Value Order for Sphere(11) x y z radius r g b ambient diffuse specular roughness (all float vals). This is a Sphere object (Point, Radius, Color, Finish)
# Create sphere from all 11 numbers then add it to new_spheres 
 
import sys 
import data
from cast import *
 
def open_file(name,mode): 
    try: 
        return open(name,mode) 
    except IOError as e: 
        print >>sys.stderr, '{0}:{1}'.format(name,e.strerror) 
        exit(1) 


def float_default(n):
    for i, val in enumerate(n):
        try:
            n[i] = float(val)
        except ValueError:
            n[i] = val

 
def line_check(line): 
    n = line.split( )
    new_spheres = [] 
    float_default(n)
    if len(n) == 11: 

        center = data.Point(n[0],n[1],n[2])
        radius = n[3]
        color  = data.Color(n[4],n[5],n[6])
        finish = data.Finish(n[7],n[8],n[9],n[10])

        sphere = data.Sphere(center,radius,color,finish)
 
        new_spheres.append(sphere)
        
        return new_spheres
    else:
        print "malformed sphere on line [line] ... skipping."
 

def read_file(argv):

    with open_file(argv[1],'r') as f: 
        for line in f: 
            spherelist = line_check(line)

        View = view(argv)
        Eye = eye(argv)
        Ambient = ambient(argv)
        Light = light(argv)

        cast_all_rays(View[0],View[1],View[2],View[3],View[4],View[5],
                      Eye,spherelist,Ambient,Light) 
                      
 

 
# Additional Arguments
 
# -eye,  if present, next three arguments specify x,y,z coordinates of the position of eye_point for casting ray. If not present, defaults to  
# -eye = (0.0, 0.0, -14.0)
 
def eye(argv):
    if '-eye' in sys.argv:
        for i, e in enumerate(sys.argv):
            if e == '-eye':
               return data.Point(sys.argv[i+1], sys.argv[i+2], sys.argv[i+3])
        return data.Point(0.0, 0.0, -14.0)
    else:
        return data.Point(0.0, 0.0, -14.0)

# -view, if present, the next six arguments min/max_x, min/max_y, width, height specify the view rectangle. If not present, defaults to  
# -view = (-10, 10, -7.5, 7.5, 1024, 768) 

def view(argv):
    if '-view' in sys.argv:
        for i, e in enumerate(sys.argv):
            if e == '-view':
                return (sys.argv[i+1], sys.argv[i+2], sys.argv[i+3], sys.argv[i+4], 
                        sys.argv[i+5], sys.argv[i+6])
        return -10, 10, -7.5, 7.5, 1024, 768
    else:
        return -10, 10, -7.5, 7.5, 1024, 768
 
# -light, if present, next six arguments specify x,y,z of light's position and r,g,b of lights color. If not present, defaults to  
# -light = (-100.0, 100.0, -100.0, 1.5, 1.5, 1.5) 

def light(argv):
    if '-light' in sys.argv:
        for i, e in enumerate(sys.argv):
            if e == '-light':
                return data.Light((data.Point(sys.argv[i+1], sys.argv[i+2], sys.argv[i+3]),
                                   data.Color(sys.argv[i+4], sys.argv[i+5], sys.argv[i+6])))
        return data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
    else:
        return data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))

# -ambient, if present, next three arguments specify the r,g,b of the ambient light color. If not present, defaults to [white] 
# -ambient = (1.0, 1.0, 1.0) 

def ambient(argv):
    if '-ambient' in sys.argv:
        for i, e in enumerate(sys.argv):
            if e == '-ambient':
                return data.Color(sys.argv[i+1], sys.argv[i+2], sys.argv[i+3])
        return data.Color(1.0, 1.0, 1.0)
    else:
        return data.Color(1.0, 1.0, 1.0)




#if __name__=='__main__': 
#    if len(sys.argv) >= 2: 
#        read_file(sys.argv[1]) 
#    else: 
#        print "usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x #min_y max_y width height] [-light x y z r g b] [-ambient r g b]."
