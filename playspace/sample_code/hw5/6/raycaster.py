import commandline
import cast
import sys

def main():
    parameters = commandline.main(sys.argv[1])
    
    sphere_list = parameters[0]
    eye_point = parameters[1]
    min_x = parameters[2][0]
    max_x = parameters[2][1]
    min_y = parameters[2][2]
    max_y = parameters[2][3]
    width = parameters[2][4]
    height = parameters[2][5]
    light = parameters[3]
    ambient = parameters[4]
        
    cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, 
    eye_point, sphere_list, ambient, light)
    
if __name__ == '__main__':
    main()