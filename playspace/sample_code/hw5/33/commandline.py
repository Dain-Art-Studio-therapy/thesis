import sys
import data

#open file
try:
    fi_le = open(sys.argv[1],'rb')
except:
    print 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
    exit(1)

#find eye_point
def find_eye_point():
    if '-eye' in sys.argv:
        i = sys.argv.index('-eye')
        eye_point = data.Point(float(sys.argv[i+1]), float(sys.argv[i+2]), float(sys.argv[i+3]))
        return eye_point
    else:
        eye_point = data.Point(0.0, 0.0, -14.0)
        return eye_point
    
        
#find list of mins/maxs/dimensions
def find_dimensions():
    if '-view' in sys.argv:
        j = sys.argv.index('-view')
        min_x = float(sys.argv[j+1])
        max_x = float(sys.argv[j+2])
        min_y = float(sys.argv[j+3])
        max_y = float(sys.argv[j+4])
        width = int(sys.argv[j+5])
        height = int(sys.argv[j+6])
        dimensions = [min_x, max_x, min_y, max_y, width, height]
        return dimensions
    else:
        min_x = -10
        max_x = 10
        min_y = -7.5
        max_y = 7.5
        width = 1024
        height = 768
        dimensions = [min_x, max_x, min_y, max_y, width, height]
        return dimensions
     
#find light
def find_light():
    if '-light' in sys.argv:
        k = sys.argv.index('-light')
        light_point = data.Point(float(sys.argv[k+1]), float(sys.argv[k+2]), float(sys.argv[k+3]))
        light_color = data.Color(float(sys.argv[k+4]), float(sys.argv[k+5]), float(sys.argv[k+6]))
        light = data.Light(light_point, light_color)
        return light
    else:
        light_point = data.Point(-100.0, 100.0, -100.0)
        light_color = data.Color(1.5,1.5,1.5)
        light = data.Light(light_point, light_color)
        return light
    

#find ambient
def find_ambient():
    if '-ambient' in sys.argv:
        m = sys.argv.index('-ambient')
        ambient = data.Color(sys.argv[m+1],sys.argv[m+2],sys.argv[m+3])
        return ambient
    else:
        ambient = data.Color(1.0, 1.0, 1.0)
        return ambient
    
#close file    
fi_le.close()
