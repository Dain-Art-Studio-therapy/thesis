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

def pixel_list(list):
    #returns a list of pixels grouped by threes
    pixels = []
    for p in range(4,len(list),3):
        r = int(list[p])
        g = int(list[p+1])
        b = int(list[p+2])
        pixels.append((r,g,b))
    return pixels

def pixel_list_rows(list,width):
    #returns a list of grouped pixels that're grouped by row.
    rows = []
    for n in range(0,len(list),width):
        rows.append(list[n:n+width])
    return rows

def check_arg(arg):
    #Will check the argument and return the correct reach.
    if len(arg)>3 or len(arg)<2:
        print 'Usage: filename neighbor_reach'
        exit()
    if len(arg)==2:
        return 4
    if len(arg)==3:
        try:
            return int(arg[2])
        except:
            print 'neighbor_reach needs to be an integer.'
            exit()

def print_header(pixels):
    #outputs print statements to the file
    sys.stdout = open("blurred.ppm",'w')
    #the header
    print "P3"
    print pixels[1],pixels[2]
    print pixels[3]

def read_pixels(file):
    #returns the image
    with file as f:
        image = f.read().split()
    return image

def blur_pixels(row_list,reach,height,width):
    #loops through each pixel
    for row in range(0, height):
        for col in range(0,width):
            #sets the resulting rgb and current rgb to 0 for the time being.
            rc = 0
            gc = 0
            bc = 0
            r = 0
            g = 0
            b = 0
            count = 0
            #loops through the box from -reach to reach and adds values to rgb
            for y in range(-reach,reach+1):
                for x in range(-reach,reach+1):
                    # if it's in bounds
                    if row+y>=0 and row+y<height and col+x>=0 and col+x<width:
                        #the values of the rgb of the surrounding pixels
                        rc = row_list[row+y][col+x][0]
                        gc = row_list[row+y][col+x][1]
                        bc = row_list[row+y][col+x][2]
                        #make the sum of every relevant pixel
                        r += rc
                        g += gc
                        b += bc
                        count +=1
             #average all the values
            r = r/count
            g = g/count
            b = b/count
            #print the final colors    
            print r,g,b
        
def main(arg):
    check_arg(arg)
    rfile = open_file(arg[1])
    reach = check_arg(arg)
    pixels = read_pixels(rfile)
    print_header(pixels)
    pixellist = pixel_list(pixels) #the list of grouped pixels
    rows = pixel_list_rows(pixellist,int(pixels[1])) #pixels grouped by row
    blur_pixels(rows,reach,int(pixels[2]),int(pixels[1]))    
        
if __name__ == "__main__":
   main(sys.argv)
