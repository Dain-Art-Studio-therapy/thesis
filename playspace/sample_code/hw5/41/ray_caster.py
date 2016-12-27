# Name: Audrey Chan
# Instructor: Aaron Keen
# Section: 09

# Description: contains a main function and supporting I/O functions
#              that implement the required functionality of the assignment

import cast
import commandline
import sys
import data

def main(argv):
    sph_list = commandline.main(argv)
    flist = check_flags(argv)
    # flist contains [eye, view, light, ambient]

    cast.cast_all_rays(flist[1][0], flist[1][1], flist[1][2], flist[1][3], flist[1][4], flist[1][5], flist[0], sph_list, flist[3], flist[2])
#    cast.cast_all_rays(-10.0, 10.0, -7.5, 7.5, 1024, 768, data.Point(0.0, 0.0, -14.0), sph_list, data.Color(1.0, 1.0, 1.0), data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5)))

def check_flags(argv):
    flags = ['-eye', '-view', '-light', '-ambient']
    pos = 2

    eye = data.Point(0.0, 0.0, -14.0)
    view = [-10, 10, -7.5, 7.5, 1024, 768]
    light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
    ambient = data.Color(1.0, 1.0, 1.0)    
    
    while pos < len(argv):

        if argv[pos] == '-eye':
            try:
                eye = data.Point(float(argv[pos + 1]), float(argv[pos + 2]), float(argv[pos + 3]))
            except:
                pass

        elif argv[pos] == '-view':
            try:
                view = [float(argv[pos + 1]), float(argv[pos + 2]), float(argv[pos + 3]), float(argv[pos + 4]), float(argv[pos + 5]), float(argv[pos + 6])]
            except:
                pass
        
        elif argv[pos] == '-light':
            try:
                light = data.Light(data.Point(float(argv[pos + 1]), float(argv[pos + 2]), float(argv[pos + 3])), data.Color(float(argv[pos + 4]), float(argv[pos + 5]), float(argv[pos + 6])))
            except:
                pass

        elif argv[pos] == '-ambient':
            try:
                ambient = data.Color(float(argv[pos + 1]), float(argv[pos + 2]), float(argv[pos + 3]))
            except:
                pass

        pos += 1
    return [eye, view, light, ambient]

main(sys.argv)
