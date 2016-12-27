import cast
import sys
import data
import commandline

#make sphere list
def make_sphere_list():

    #make sure file can be opened
    try:
        f = open(sys.argv[1],'rb')        
    except:
        print 'File cannot be opened!'
        exit(1)
        
        
    sphere_list = []

    line_num = 0
    #if sphere is good, append to list
    for line in f:        
        l = line.split(' ')
        line_num += 1
        if len(l) == 11:
            try:
                center = data.Point(float(l[0]),float(l[1]),float(l[2]))
                radius = float(l[3])
                color = data.Color(float(l[4]),float(l[5]),float(l[6]))
                finish = data.Finish(float(l[7]),float(l[8]),float(l[9]),float(l[10]))
                sphere = data.Sphere(center,radius,color,finish)
                sphere_list.append(sphere)
            except:
                print str('Malformed sphere on line ' + str(line_num) + '...skipping')
        else:
            print str('Malformed sphere on line ' + str(line_num) + '...skipping') 
            
    f.close()
    
    return sphere_list
      
        


def main():
    ppmfile = open('image.ppm','w')
    try:
        min_x = float(commandline.find_dimensions()[0])
        max_x = float(commandline.find_dimensions()[1])
        min_y = float(commandline.find_dimensions()[2])
        max_y = float(commandline.find_dimensions()[3])
        width = int(commandline.find_dimensions()[4])
        height = int(commandline.find_dimensions()[5])
        eye_point = commandline.find_eye_point()
        sphere_list = make_sphere_list()
        ambient = commandline.find_ambient()
        light = commandline.find_light()
    except:
        print 'Please check entered values'
        exit(1)

    list_of_colors = cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, light)
    ppmfile.write('P3\n')
    ppmfile.write(str(width)+ ' ' + str(height) + '\n')
    ppmfile.write('255\n')
    
    for i in list_of_colors:
        ppmfile.write(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + '\n') 
    

if __name__ == '__main__':
    main()
