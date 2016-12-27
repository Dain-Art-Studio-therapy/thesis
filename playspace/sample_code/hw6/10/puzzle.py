import sys

def main(argv):
   image = r_w_file(argv[1],"r")
   hidden_file = r_w_file("hidden.ppm","w")
   list_pixels = read_in_pix(image)
   groups = group_pixels_3(list_pixels)
   output = write_hidden(groups,list_pixels,hidden_file)
   image.close()
   hidden_file.close()
    
    

def r_w_file(file_name,mode):
    try:
        return open(file_name,mode)
    except:
        print "Can't Open File"
        
def read_in_pix(image):
    #Get List of Pixels
    pixel_list = [ ]
    for line in image:
        pix = line.split()
        for e in pix:
            #print e
            pixel_list.append(e)
    return pixel_list

def group_pixels_3(pixel_list):
    # Groups Pixels 
    group = [pixel_list[i:i+3] for i in range(4,len(pixel_list),3)]

    
    return group    

def write_hidden(groups,pixel_list,hidden_file):
    hidden_file.write (pixel_list[0] + "\n")
    hidden_file.write(pixel_list[1] + " " +pixel_list[2]+ "\n")
    hidden_file.write(pixel_list[3] + "\n")
    #counter = 0
    for pixel in groups:
       red = int(pixel[0]) * 10
       green = blue = red
       if red>255:
          red = 255
       if green > 255:
          green = 255
       if blue>255:
          blue = 255
       
       hidden_file.write(str(red) + " " + str(green) + " " + str(blue) + "\n")
                
if __name__ == "__main__":
    main(sys.argv)
        
                        
