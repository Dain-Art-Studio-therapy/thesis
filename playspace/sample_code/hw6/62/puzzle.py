from sys import *
from puzzle_commandline import *

def main(argv):
   puzzle = open_file(argv)
   width_height_list = get_width_height(puzzle)
   width = width_height_list[0]
   height = width_height_list[1]

   imagefile = open_image_file('hidden.ppm', 'wb')    
    
   decode(puzzle, imagefile, width, height)        
   
   
if  __name__ == '__main__':
     main(argv)

