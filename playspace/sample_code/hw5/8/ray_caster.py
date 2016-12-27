#a main function and I/O functions


# call read_file to get list of spheres
# cast all rays into the list of spheres
# output the pixel values to a file: image.ppm


from collisions import *
from cast import *
from commandline import *
import sys
import math
import data
import vector_math



    

image = open('image.ppm','w')
image.write('P3')
image.write(str(view(sys.argv)[4]) + ' ' + str(view(sys.argv)[5]))
image.write('255')
image.write(read_file(sys.argv))
image.close()


if __name__=='__main__': 
    if len(sys.argv) >= 2: 
        read_file(sys.argv[1]) 
    else: 
        print "usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]."
