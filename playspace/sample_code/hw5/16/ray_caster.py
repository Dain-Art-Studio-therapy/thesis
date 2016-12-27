from data import *
from cast import *
from commandline import *

def get_sphere_object(nums):

    return Sphere(
        Point(nums[0], nums[1], nums[2]),
        nums[3],
        Color(nums[4], nums[5], nums[6]),
        Finish(nums[7], nums[8], nums[9], nums[10])
        )


def import_sphere_data(f):

    sphere_list = []

    with open(str(f), 'rb') as f:
        lines = f.readlines()        
        for i in range(len(lines)):
            strings = lines[i].split()
            if len(strings) != 11:
                print 'malformed sphere on line %d ... skipping' % (i+1)
            else:
                try:
                    nums = map(float, strings)
                    sphere = get_sphere_object(nums)
                    sphere_list.append(sphere)
                except:
                    print 'malformed sphere on line %d ... skipping' % (i+1)

    return sphere_list


def print_to_file(color_list, width, height):

    with open('image.ppm', 'wb') as f:
        f.write('P3\n{0} {1}\n255\n'.format(width, height))
        for triple in color_list:
            f.write('{0} {1} {2}\n'.format(triple[0], triple[1], triple[2]))
    

def main(argv):

    file_name = get_file_name(argv)
    sphere_list = import_sphere_data(file_name)
    eye_point = get_eye(argv)
    light = get_light(argv)
    ambience = get_ambient(argv)
    view = get_view(argv)    
    min_x = view[0]
    max_x = view[1]
    min_y = view[2]
    max_y = view[3]
    width = view[4]
    height = view[5]

    color_list = cast_all_rays(
                min_x, max_x, min_y, max_y, 
                width, height, eye_point, sphere_list, 
                ambience, light
                )

    print_to_file(color_list, width, height)
    

if __name__ == '__main__':
    main(argv)
