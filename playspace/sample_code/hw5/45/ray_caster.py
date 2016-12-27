# Name: Allison Lee
# Instructor: Aaron Keen
# Section: 09

import data
import vector_math
import cast
import collisions
import sys
import commandline

def main():
    errormessage = 'usage: python ray_caster.py <filename> [-eye x y z]'
    errormessage += '[-view min_x max_x min_y max_y width height]'
    errormessage += '[-light x y z r g b]'
    
    if len(sys.argv)==1:
        # If no filename is specified.
        print errormessage
        exit()
    else:
        #eye point
        eye_point = data.Point(0.0,0.0,-14.0)
        #view
        min_x = -10
        max_x = 10
        min_y = -7.5
        max_y = 7.5
        width = 1024
        height = 768
        #light
        light = data.Light(data.Point(-100.0,100.0,-100.0),
                           data.Color(1.5,1.5,1.5))
        #ambient color
        ambient = data.Color(1.0,1.0,1.0)
        sphere_list = []
        filename = sys.argv[1]
        
        if len(sys.argv)<4 and len(sys.argv)>2:
            print errormessage
            exit()
        else:
            for idx, option in enumerate(sys.argv):
                if option=='-eye':
                    try:
                        eargv1 = float(sys.argv[idx+1])
                        eargv2 = float(sys.argv[idx+2])
                        eargv3 = float(sys.argv[idx+3])
                        eye_point = data.Point(eargv1,eargv2,eargv3)                        
                    except:
                         print errormessage
                         exit()
                if option=='-view':
                    try:
                        vargv1 = float(sys.argv[idx+1])
                        vargv2 = float(sys.argv[idx+2])
                        vargv3 = float(sys.argv[idx+3])
                        vargv4 = float(sys.argv[idx+4])
                        vargv5 = int(sys.argv[idx+5])
                        vargv6 = int(sys.argv[idx+6])                        
                        min_x = vargv1
                        max_x = vargv2
                        min_y = vargv3
                        max_y = vargv4
                        width = vargv5
                        height = vargv6
                    except:
                        print errormessage
                        exit()
                if option=='-light':
                    try:
                        largv1 = float(sys.argv[idx+1])
                        largv2 = float(sys.argv[idx+2])
                        largv3 = float(sys.argv[idx+3])
                        largv4 = float(sys.argv[idx+4])
                        largv5 = float(sys.argv[idx+5])
                        largv6 = float(sys.argv[idx+6])
                        lightp = data.Point(largv1,largv2,largv3)
                        lightc = data.Color(largv4,largv5,largv6)
                        light = data.Light(lightp,lightc)
                    except:
                         print errormessage
                         exit()
                if option=='-ambient':
                    try:
                        aargv1 = float(sys.argv[idx+1])
                        aargv2 = float(sys.argv[idx+2])
                        aargv3 = float(sys.argv[idx+3])
                        ambient = data.Color(aargv1,aargv2,aargv3)                        
                    except:
                         print errormessage
                         exit()

        file = commandline.file_open(filename)
        if commandline.file_check(file):
            print 'Outputting .ppm file. Please wait.'
            sphere_list = commandline.output_spheres(filename)
            cast.cast_all_rays(min_x,max_x,min_y,max_y,width,height,
                              eye_point,sphere_list,ambient,light)
        else:
            print 'Failed.'

if __name__ == '__main__':
   main()
