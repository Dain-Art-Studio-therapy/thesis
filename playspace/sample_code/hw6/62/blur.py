from sys import *
from blur_commandline import *

def main(argv):
   checkargs(argv)
   input = open_file(argv)
   width_height_list = get_width_height(input)
   width = width_height_list[0]
   height = width_height_list[1]
   reach = getReach(argv)

   imagefile = open_image_file('blurred.ppm', 'wb')    
    
   blur(input, imagefile, width, height, reach)        
   
   

if  __name__ == '__main__':
     main(argv)


