import sys
import data

def cmd_args(min_x, max_x, min_y, max_y, width, height, eye, light, ambient):
    arg_list = [min_x, max_x, min_y, max_y, width, height, eye, light, ambient]

    if len(sys.argv) < 2: 
        print 'no sphere file' 
        exit()
    changes = []
    for arg in xrange(len(sys.argv)):  
        if sys.argv[arg] == '-view': 
            try:
                minx = float(sys.argv[arg+1]) 
                maxx = float(sys.arg[arg+2])
                miny = float(sys.arg[arg+3])
                maxy = float(sys.arg[arg+4])
                width1 = int(sys.arg[arg+5])
                height1 = int(sys.arg[arg+6])
                changes.append(('-view',[minx, maxx, miny, maxy, width1, height1])) 
            except:
                print 'invalid view; default values used'

        if sys.argv[arg] == '-eye':
            try: 
                neweye = data.Point(float(sys.argv[arg+1]), float(sys.argv[arg+2]), float(sys.argv[arg+3]))
                changes.append(('-eye', neweye)) 
            except:
                print 'invalid eye; default values used'

        if sys.argv[arg] == '-light':
            try:
                newlight = data.Light(data.Point(float(sys.argv[arg+1]), float(sys.argv[arg+2]), float(sys.argv[arg+3])), data.Color(float(sys.argv[arg+4]), float(sys.argv[arg+5]), float(sys.argv[arg+6]))) 
                changes.append(('-light', newlight)) 
            except: 
                print 'invalid light; default values used'
               
        if sys.argv[arg] == '-ambient':
            try:
                newambient = data.Color(float(sys.argv[arg+1]), float(sys.argv[arg+2]), float(sys.argv[arg+3]))
                changes.append(('-ambient', newambient))
            except:
                print 'invalid ambient; default values used'

    return changes
