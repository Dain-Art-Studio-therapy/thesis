import sys
import linecache
import math

def decoder(infile,outfile,whtup,locy,locx,r):

    p = []  #the blank pixel
    linenum = 0
    x = 0
    y = 0
    width = int(whtup[0])
    height = int(whtup[1])
    
    for l in infile:
        
        #print the header using information from the base file. Should never be more than 3 lines.
        if linenum < 3:
            outfile.write(l)
            
        else: #primary logic from here
            s = str.split(l)

            for v in s:

                val = int(v) #working with int color values

                p.append(val)

                if len(p) == 3: #an entire pixel is stored in p, time to process and clear it
                    fade_pixel(p,outfile,x,y,locx,locy,r)
                    p = [] 

                    x += 1
                    if x >= width: #adjust x/y position for location calculation
                        x = 0
                        y += 1           
        linenum += 1

def fade_pixel(pixlist,outfile,x,y,locx,locy,rad): #modifies pixel according to assignment specification

    scale = (rad - distance_point(x,y,locx,locy))/rad
    if scale < .2:
        scale = .2

    r = pixlist[0]*scale
    g = pixlist[1]*scale
    b = pixlist[2]*scale
    
    r = str(int(r))
    g = str(int(g))
    b = str(int(b))
    
    outfile.write(r)
    outfile.write('\n')  
    outfile.write(g)
    outfile.write('\n')
    outfile.write(b)
    outfile.write('\n')
    

def length_width(argv):
    l = str.split(linecache.getline(argv[1],2)) #retrieves and splits line containing l/w in standard PPM
    print l
    return l
                
def distance_point(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def main(argv):
    #argv expects an image file in the ppm form
    #this ultimately outputs to a file named 'faded.ppm'
    #this has no checks against improper commands
    #expects: filname row col radius
    fileout = sys.stdout
    try:
        infile = open(argv[1],"r")
        outfile = open("faded.ppm","w")
    except IOError as e:
        print >> sys.stderr, e
        sys.exit()
    
    try:
        decoder(infile,outfile,length_width(argv),int(argv[2]),int(argv[3]),int(argv[4]))
    except:
        print >> sys.stderr, 'There was an error prrocessing the image'
        sys.exit()
        
    outfile = sys.stdout
    infile.close()
    outfile.close()

if __name__ == "__main__":
    main(sys.argv)
