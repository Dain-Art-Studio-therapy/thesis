import sys
import cast
import commandline
import data

def main():
    try:
        newfiles = open(sys.argv[1], 'r')
    except:
        print 'python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
        exit()
        
    sphere_list = []
    lines = 0
    
    for line in newfiles:
        lines += 1
        try:
            s = [float(values) for values in line.split()]
            center = data.Point(s[0],s[1],s[2])
            finish = data.Finish(s[7],s[8],s[9],s[10])
            sphere = data.Sphere(center,s[3],data.Color(s[4],s[5],s[6]),finish)
            
            sphere_list.append(sphere)
        except:
            print 'Malformed sphere on line ' + str(lines) + ' ... skipping'

    eyePoint = commandline.eye()
    viewPoint = commandline.view()
    lightPoint = commandline.light()
    ambientPoint = commandline.ambient()

    file = open('image.ppm', 'w')
    file.write('P3\n')
    file.write(str(viewPoint[4]) + ' ' +  str(viewPoint[5]) + '\n')
    file.write('255\n')

    a = viewPoint[0]
    b = viewPoint[1]
    c = viewPoint[2]
    d = viewPoint[3]
    e = viewPoint[4]
    f = viewPoint[5]
    g = data.Point(eyePoint[0],eyePoint[1],eyePoint[2])
    h = sphere_list
    i = data.Color(ambientPoint[0],ambientPoint[1],ambientPoint[2])
    pointer1 = data.Point(lightPoint[0],lightPoint[1],lightPoint[2])
    j = data.Light(pointer1,data.Color(lightPoint[3],lightPoint[4],lightPoint[5]))
    cast.cast_all_rays(a,b,c,d,e,f,g,h,i,j,file)
    
if __name__ == "__main__":
    main()
