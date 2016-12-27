import sys
import data
import utility

def main(file):
    if len(sys.argv) < 2:
        print "Not enough arguments on cmdline. Expected: input file \
        (text file of values to make spheres) and (optional) flags for \
        position of the eye, view dimensions, point light position and color, \
        and ambient light color (flags in any order)."
        exit(1)
        
    spheres = extract_spheres(file)
    eye = check_for_eye(sys.argv)
    view_list = check_for_view(sys.argv)
    light = check_for_light(sys.argv)
    ambient = check_for_ambient(sys.argv)
    
    return [spheres, eye, view_list, light, ambient]
    
def check_for_eye(list):
    x = 0
    y = 0
    z = -14
    
    for i in range(len(list)):
        if list[i] == "-eye":
            try:
                x = float(list[i + 1])
                y = float(list[i + 2])
                z = float(list[i + 3])
            except:
                x = 0
                y = 0
                z = -14        
    return data.Point(x, y, z)
            
def check_for_view(list):
    min_x = -10
    max_x = 10
    min_y = -7.5
    max_y = 7.5
    width = 1024
    height = 768
    
    for i in range(len(list)):
        if list[i] == "-view":
            try:
                min_x = float(list[i + 1])
                max_x = float(list[i + 2])
                min_y = float(list[i + 3])
                max_y = float(list[i + 4])
                width = int(list[i + 5])
                height = int(list[i + 6])
            except:
                min_x = -10
                max_x = 10
                min_y = -7.5
                max_y = 7.5
                width = 1024
                height = 768  
    return [min_x, max_x, min_y, max_y, width, height]
        
def check_for_light(list):
    x = -100
    y = 100
    z = -100
    r = 1.5
    g = 1.5
    b = 1.5
    
    for i in range(len(list)):
        if list[i] == "-light":
            try:
                x = float(list[i + 1])
                y = float(list[i + 2])
                z = float(list[i + 3])
                r = float(list[i + 4])
                g = float(list[i + 5])
                b = float(list[i + 6])
            except:
                x = -100
                y = 100
                z = -100
                r = 1.5
                g = 1.5
                b = 1.5
    return data.Light(data.Point(x, y, z), data.Color(r, g, b))
            
def check_for_ambient(list):
    r = 1.0
    g = 1.0
    b = 1.0
    
    for i in range(len(list)):
        if list[i] == "-ambient":
            try:
                r = float(list[i + 1])
                g = float(list[i + 2])
                b = float(list[i + 3])
            except:
                r = 1.0
                g = 1.0
                b = 1.0
    return data.Color(r, g, b)
    
    
def extract_spheres(file):
    with utility.open_file(file, 'rb') as f:
        
        line_count = 0
        sphere_list = []
        for line in f:
            line_count += 1
            raw_arguments = line.split()
            if len(raw_arguments) != 11:
                print "Sphere on line ", line_count, " is malformed\
                (incorrect number of arguments) ... skipping"
            else:
                arguments = []
                try:
                    for argument in raw_arguments:
                        arguments.append(float(argument))
                        
                    sphere = data.Sphere(data.Point(arguments[0], 
                    arguments[1], arguments[2]), arguments[3], 
                    data.Color(arguments[4], arguments[5], arguments[6]), 
                    data.Finish(arguments[7], arguments[8], arguments[9], 
                    arguments[10]))
                    
                    sphere_list.append(sphere)
                    
                except:
                    print "Sphere on line ", line_count, "is malformed \
                    (incorrect argument type)... skipping"
            

        return sphere_list