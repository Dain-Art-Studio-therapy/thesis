# Name: Allison Lee
# Instructor: Aaron Keen
# Section: 09
import sys

def open_file(arg):
    try:
        return open(arg,'r')
    except:
        print 'Unable to read file.'
        exit()

def groups_of_3(list):
    for n in range(4,len(list),3):
        c = int(list[n])*10
        if c>255:
            print 255,255,255
        else:
            print c,c,c

def check_arg(arg):
    if len(arg)>2 or len(arg)<2:
        print 'Please provide the filename.'
        exit()
        
def make_pixel_list(file):
    with file as f:
        pixels = f.read().split()
    return pixels

def print_pixels(pixels):
    sys.stdout = open("hidden.ppm",'w')
    #prints header
    print "P3"
    print pixels[1],pixels[2]
    print pixels[3]
    groups_of_3(pixels)    
            
def main(arg):
    check_arg(arg)
    rfile = open_file(arg[1])
    pixels = make_pixel_list(rfile)
    print_pixels(pixels)
        
if __name__ == "__main__":
   main(sys.argv)
