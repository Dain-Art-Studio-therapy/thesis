import sys

def main(argv):
    try:
       value = int(argv[2])
    except: 
        value = 4
    image = r_w_file(argv[1],"r")
    blur_image = r_w_file("blurred.ppm","w")
    plist = pixel_list(image)
    groups = groups_of_3(plist)
    two_list = twoD_list(int(plist[1]),int(plist[2]),groups)
    final_list= surrounding(two_list,int(plist[1]),int(plist[2]),value)
    output(final_list, int(plist[1]), int(plist[2]),blur_image)
    
    image.close()
    blur_image.close()
    
def r_w_file(file_name, mode):
    try:
        return open(file_name,mode)
    except:
        print "Can't Open File"
        
def pixel_list(image):
    plist = [ ]
    
    for line in image:
        pix = line.split()
        for e in pix:
            plist.append(e)
            
    return plist

def groups_of_3(plist):
    groups = [plist[i:i+3] for i in range(4,len(plist),3) ]
    
    return groups

def twoD_list(width,height,groups):
    two_list = [ ]
    
    for y in range(height):
        row_list = [ ]
        
        for x in range(width):
            row_list.append(groups[ x + (y * width) ] )
        two_list.append(row_list)
        
    return two_list

def get_avg(lower_row,upper_row,left_col,right_col,main_list,value):
    r = 0
    b = 0
    g = 0
    row_range = range(lower_row,upper_row)
    col_range = range(left_col,right_col )
    total_pix = ((2 * value) +1) **2
    for row in row_range:
        for col in col_range:
            r += int(main_list[row][col][0])
            g += int(main_list[row][col][1])
            b += int(main_list[row][col][2])
            
    red = r / total_pix
    green = g / total_pix
    blue = b / total_pix
    
    return [red,green,blue] 
                
def surrounding(main_list,width,height,value): 
    
    for row in range(len(main_list)):
        for col in range(len(main_list[row])):
            
            
            lower_row = row - value
            upper_row = row + value
            left_col  = col - value
            right_col = col + value
            
            if lower_row<0:
                 lower_row = 0
            if upper_row > height:
                 upper_row = height
            if left_col< 0:
                 left_col = 0
            if  right_col > width:
                 right_col = width
           
            main_list[row][col]  = get_avg(lower_row,upper_row,\
                                   left_col,right_col,main_list,value)         
            
    return main_list
            
            
                      
            
                       
            

def output (main_list,width,height,blur):
    #Header
    blur.write("P3" + "\n")
    blur.write(str(width) + " " + str(height) + "\n")
    blur.write("255" + "\n")

    for row in main_list:
        for pix in row:
            r = pix[0]
            g = pix[1]    
            b = pix[2]
            blur.write(str(r) + " " + str(g) + " "+ str(b) + "\n")
        
        
    


if __name__ == "__main__":
    main(sys.argv)
            
            
            
    
        

