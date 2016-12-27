import sys
import math

def main(argv):
    
    image = r_w_file(argv[1],"r")
    faded_image = r_w_file("faded.ppm","w")
    plist = pixel_list(image)
    groups = group_pixels_3(plist)
    main_list = twoD_list(int(plist[2]),int(plist[1]),groups)
    output(main_list,faded_image, plist,argv)

    
    image.close()
    faded_image.close()
    
    
def r_w_file(file_name, mode):
    try:
        return open (file_name,mode)
    except:
        print "Can't Open File"
        
        
# Creates List of ALL pixels        
def pixel_list(image):
    pixel_list= []
    
    for line in image:
        pix = line.split()
        for e in pix:
                
           pixel_list.append(e)
            
    return pixel_list

#Groups Pixels
def group_pixels_3(pixel_list):
    group = [pixel_list[i:i+3] for i in range(4,len(pixel_list),3)]
    
    return group


#Finds Scale Constant
def scale(radius,distance):
    
   scale =  (float(radius) - distance)/float(radius)
   if scale < .2:
      scale = .2
   #print scale
   return scale

def distance(row_p,col_p,row_given,col_given):
   dist = math.sqrt( (((row_p - int(row_given))  ** 2) +
          ((col_p - int(col_given) ) ** 2 ) ))
   #print "dist:", dist
   return dist


    

    
def twoD_list(height,width,groups): # making 2D List
    
    main_list = [ ]
    for y in range(height):
        row_list = [ ]  
        for x in range(width):                        
                                        
            row_list.append(groups[x+ (y * width) ]) #new rows
            
            
            row = y 
            col = x
            
            #print "COL:", col
            #print "ROW:", row 
        main_list.append(row_list)  

            
    #print len(main_list)
    return main_list

def output(main_list,faded_image,plist,argv):
    #Header
    faded_image.write(plist[0] + "\n")
    faded_image.write(plist[1] + " " + plist[2] + "\n")
    faded_image.write(plist[3] + "\n")
    
    #print len(main_list)
    for y in range(len(main_list)):
        #print len(main_list[y])
        for x in range(len(main_list[y])):
            row = y
            col = x
            dist = distance(row,col,argv[2],argv[3])
            constant = float(scale(argv[4],dist))
           
            #print "row:", y
            #print "col:", x
            
            red   = int( int(main_list[y][x][0] )   * constant )
            green = int( int(main_list[y][x][1] )   * constant )
            blue  = int( int(main_list[y][x][2] )   * constant )
           # print str(main_list[y][x][0]) + "" + "Constant:" + str(constant)
            
            faded_image.write((str(red) + " " + str(green) + " "+ 
                              str(blue) + "\n"))
            
    


if __name__ == "__main__":
    main(sys.argv)
