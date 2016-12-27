import sys

def decoder(infile, outfile):
    p = []  #the blank pixel
    linenum = 0
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
                    decode_pixel(p,outfile)
                    p = []
                    
        linenum += 1

def decode_pixel(pixlist,outfile): #modifies pixel according to assignment specification
    r = pixlist[0]*10
    if r > 255:
        r = 255
    r = str(r)  #write does not take int  
    outfile.write(r)
    outfile.write('\n')  
    outfile.write(r)
    outfile.write('\n')
    outfile.write(r)
    outfile.write('\n')
    
def main(argv):
    #argv expects an image file in the ppm form
    #this ultimately outputs to a file named 'hidden.ppm'
    fileout = sys.stdout
    try:
        infile = open(argv[1],"r")
        outfile = open("hidden.ppm","w")
    except IOError as e:
        print >> sys.stderr, e
        sys.exit()
    

    decoder(infile,outfile)

    outfile = sys.stdout
    infile.close()
    outfile.close()

if __name__ == "__main__":
    main(sys.argv)
