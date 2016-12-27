from cast import *
from commandline import *
import sys

def main(argv):
    sphere_list = analyze_file(argv)
    l = parse_args(argv)
    eye_point = l[0]
    min_x = l[1]
    max_x = l[2]
    min_y = l[3]
    max_y = l[4]
    width = l[5]
    height = l[6]
    light = l[7]
    ambient = l[8]
    cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye_point,sphere_list,
ambient,light)

main(sys.argv)    
