# Name: Allison Lee
# Instructor: Aaron Keen
# Section: 09
import sys
import fadepoint
import math

def open_file(arg):
    try:
        return open(arg,'r')
    except:
        print 'Unable to read file.'
        exit()

def scale_array(arg,width,height):
    #return a list that has the scale of each pixel in corresponding location
    radius = float(arg[4])
    x = int(arg[3])
    y = int(arg[2])
    scalearray = []
    row = 0
    while row < height:
        col = 0
        while col < width:
            currentpoint = fadepoint.Point(col,row)
            fadedpoint = fadepoint.Point(x,y)
            distance = fadepoint.distance(fadedpoint,currentpoint)
            scale = float((radius-distance)/radius)
            if scale<0.2:
                scale = 0.2
            scalearray.append(scale)
            col+=1
        row+=1
    return scalearray

def print_pixels(list,arg):
    #edits the value of each pixel and prints it grouped in threes
    radius = float(arg[4])
    width = float(list[1])
    height = float(list[2])
    scalearray = scale_array(arg,width,height)
    i = 0
    for p in range(4,len(list),3):
        scale = scalearray[i]
        r = int(int(list[p])*scale)
        g = int(int(list[p+1])*scale)
        b = int(int(list[p+2])*scale)
        i+=1
        print r,g,b

def check_arg(arg):
    if len(arg)>5 or len(arg)<5:
        print 'Usage: filename row col radius'
        exit()
    else:
        try:
            int(arg[2])
            int(arg[3])
            int(arg[4])
        except:
            print 'row, col, and radius need to be integers.'
            exit()
def pixel_list(file):
    with file as f:
        pixels = f.read().split()
    return pixels

def print_header(pixels):
    #prints the header
    sys.stdout = open("faded.ppm",'w')
    print "P3"
    print pixels[1],pixels[2]
    print pixels[3]    
            
def main(arg):
    check_arg(arg)
    rfile = open_file(arg[1])
    pixels = pixel_list(rfile)
    print_header(pixels)
    print_pixels(pixels,arg)
        
if __name__ == "__main__":
   main(sys.argv)
