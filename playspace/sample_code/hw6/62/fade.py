from sys import *
from fade_commandline import *

def main(argv):
   checkargs(argv)
   input = open_file(argv)
   width_height_list = get_width_height(input)
   width = width_height_list[0]
   height = width_height_list[1]

   row = int(argv[2])
   col = int(argv[3])   
   radius = int(argv[4])

   imagefile = open_image_file('faded.ppm', 'wb')    
    
   fade(input, imagefile, width, height, row, col, radius)        
   
   

if  __name__ == '__main__':
     main(argv)

