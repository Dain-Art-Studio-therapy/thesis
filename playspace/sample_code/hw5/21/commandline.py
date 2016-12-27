from sys import *
import data
from cast import *

def float_default(string):
    try:
        return float(string)
    except:
        return string

def eye():
    if '-eye' in argv:
       try:
           index = argv.index('-eye')
           x = float_default(argv[index + 1])
           y = float_default(argv[index + 2])
           z = float_default(argv[index + 3])
           return (x,y,z)
           print 'eyetrue'
       except:
           return (0.0, 0.0, -14.0)
           print 'eyefalse'
    else:
        return (0.0, 0.0, -14.0)
        print 'elseeye'
    
def view():
    if '-view' in argv:
        try:
            index = argv.index('-view')
            min_x = float_default(argv[index + 1])
            max_x = float_default(argv[index + 2])
            min_y = float_default(argv[index + 3])
            max_y = float_default(argv[index + 4])
            width = float_default(argv[index + 5])
            height = float_default(argv[index + 6])
            return (min_x,max_x,min_y,max_y,width,height)
            print 'viewtrue'
        except:
            return (-10,10,-7.5,7.5,1024,768)
            print 'viewfalse'
    else:
        return (-10,10,-7.5,7.5,1024,768)
        print 'elseview'
    
def light():
    if '-light' in argv:
        try:
            index = argv.index('-light')
            x = float_default(argv[index + 1])
            y = float_default(argv[index + 2])
            z = float_default(argv[index + 3])
            r = float_default(argv[index + 4])
            g = float_default(argv[index + 5])
            b = float_default(argv[index + 6])
            return (x, y, z, r, g, b)
            print 'truelight'
        except:
            return (-100.0,100.0,-100.0,1.5,1.5,1.5)
            print 'falselight'
    else:
        return (-100.0,100.0,-100.0,1.5,1.5,1.5)
        print 'elselight'
        
            
    
def ambient():
    if '-ambient' in argv:
        try:
            index = argv.index('-ambient')
            r = float_default(argv[index + 1])
            g = float_default(argv[index + 2])
            b = float_default(argv[index + 3])
            return (r,g,b)
            print 'trueambient'
        except:
            return (1.0,1.0,1.0)
            print 'false ambient'
    else:
        return (1.0, 1.0, 1.0)
        print 'else ambiet'
