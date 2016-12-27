import sys
import data
import cast
import commandline

def ray_caster():
    eye = data.Point(0.0, 0.0, -14.0) 
    light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
    ambient = data.Color(1.0, 1.0, 1.0) 
    min_x = -10.0
    max_x = 10.0
    min_y = -7.5
    max_y = 7.5
    width = 400
    height = 300
    changes = commandline.cmd_args(min_x, max_x, min_y, max_y, width, height, eye, light, ambient)
    print changes 
    for change, val in changes: 
        if change == '-view':
            min_x = val[0]
            max_x = val[1]
            min_y = val[2]
            max_y = val[3]
            width = val[4]
            height = val[5]   
        if change == '-light':
            light = val
        if change == '-ambient':
            ambient = val 
        if change == '-eye':
            eye = val
       
    sphere_list = make_sphere_list()
    out_file = open('image.ppm', 'w')
    out_file
    out_file.write('P3\n')
    out_file.write(str(width) + ' ' + str(height) + '\n') 
    out_file.write('255\n')  
    rows = cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye, sphere_list, ambient, light)
    for row in rows: 
        for color in row:
            out_file.write(str(color[0]) + ' ' + str(color[1]) + ' ' + str(color[2]) + '\n')
            
def make_sphere_list():
    try:
        file_name = sys.argv[1] 
        fh = open(file_name, 'r')
    except:
         print 'invalid file' 
         exit() 
    sphere_list = []
    for line in fh:
        values = line.split()
        if len(values) == 11: 
            try:  
                point = data.Point(float(values[0]), float(values[1]), float(values[2])) 
                radius = float(values[3]) 
                color = data.Color(float(values[4]), float(values[5]), float(values[6]))
                finish = data.Finish(float(values[7]), float(values[8]), float(values[9]), float(values[10])) 
                sphere = data.Sphere(point, radius, color, finish) 
                sphere_list.append(sphere)     
            except:
                print 'invalid sphere values'  
        else:
            print 'wrong amount of sphere values' 
    fh.close()
    return sphere_list 

if __name__ == '__main__': 
    ray_caster()
    
