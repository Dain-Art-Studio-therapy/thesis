import sys
import linecache
import math

def build_array(infile,outfile,whtup):

    p = []  #the blank pixel
    linenum = 0
    x = 0
    y = 0
    width = int(whtup[0])
    height = int(whtup[1])
    array = [[] for h in range(height)]
    curln = []
    #print array
    for l in infile:
        
        #print the header using information from the base file. Should never be more than 3 lines.
        if linenum < 3:
            outfile.write(l)
            
        else: #primary logic from here
            s = str.split(l)

            for v in s:

                val = int(v) #working with int color values

                p.append(val)

                if len(p) == 3: #add complete pixel to the full list
                    array[y].append(p)
                    p = [] 
                    
                    x += 1
                    if x >= width: #adjust x/y position for location calculation                       
                        x = 0
                        y += 1
                        
        linenum += 1
    #print len(array),len(array[0])
    return array

def blur_img(img_arr,outfile,reach,width,height): #modifies image according to assignment specification

    x = 0
    y = 0

    for line in img_arr:
        for p in range(int(width)):
            #print img_arr[x][y] 
            write_pixel(blur_pixel(img_arr,reach,x,y,width,height),outfile)
            x+=1
        x=0
        y+=1

def blur_pixel(img_arr,reach,curx,cury,width,height):
    #sets base average pixel values
    aver = 0
    aveg = 0
    aveb = 0
    avecnt = 0 #total pixels averaged

    curxreach = -1*reach
    curyreach = -1*reach

    for x in range((reach*2)+1):
        for y in range((reach*2)+1):
            if curx+curxreach >= 0 and (curx+curxreach) < width and cury+curyreach >= 0 and (cury+curyreach) < height:
                try:
                    avepix = img_arr[cury+curyreach][curx+curxreach]
                except:
                    sys.exit()
                
                aver += avepix[0]
                aveg += avepix[1]
                aveb += avepix[2]
                avecnt += 1

            curyreach += 1
        curxreach += 1
        curyreach = -1*reach

            
    return [aver/avecnt,aveg/avecnt,aveb/avecnt]
    
    
def write_pixel(p,outfile):
    outfile.write(str(p[0]))
    outfile.write('\n')  
    outfile.write(str(p[1]))
    outfile.write('\n')
    outfile.write(str(p[2]))
    outfile.write('\n')
    return
    

def width_height(argv):
    l = str.split(linecache.getline(argv[1],2)) #retrieves and splits line containing l/w in standard PPM
    print l
    return l

def main(argv):
    #argv expects an image file in the ppm form
    #this ultimately outputs to a file named 'blurred.ppm'
    #this has no checks against improper commands
    #expects: filname [reach]
    fileout = sys.stdout

    reach = 4 #default +/- reach value
    
    try:
        infile = open(argv[1],"r")
        outfile = open("blurred.ppm","w")
    except IOError as e:
        print >> sys.stderr, e
        sys.exit()

    if len(argv) == 3:
        if int(argv[2]) > 0:
            reach = int(argv[2])
    #try:
    wht = width_height(argv)
    base = build_array(infile,outfile,wht)
    blur_img(base,outfile,reach,int(wht[0]),int(wht[1]))
    #except:
        #print >> sys.stderr, 'There was an error prrocessing the image'
        #sys.exit()
    outfile = sys.stdout
    infile.close()
    outfile.close()

if __name__ == "__main__":
    main(sys.argv)
