#open file_object that will call cast all rays
import sys
import cast
import data
import commandline

#CHANGE BACK TO IMAGE.PPM


def main(argv):
    with open_file(argv[1], 'r+') as file_object:
        splits = split_list(file_object)
        floats = float_list(splits)
        new_spheres = make_sphere(floats)
        #print_it(new_spheres)
        flags = commandline.find_flags(argv) #[eye, view, light, ambient]
        eye_point = flags[0]
        view = flags[1]
        min_x = flags[1][0]
        max_x = view[1]
        min_y = view[2]
        max_y = view[3]
        width = view[4]
        height = view[5]
        light = flags[2]
        color = flags[3]

    with open_file('image.ppm', 'w') as file_object:
        cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, new_spheres, color, light, file_object) #will eventually come from cmdline processing



def open_file(name, mode):
    try:
        return open(name, mode)

    except IOError as e:
        print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
        exit(1)


def make_floats(n):
    try:
        return float(n)
    except TypeError:
        print 0


def split_list(f): #returns list with split values
    new_list = []
    count = 1
    for line in f:
        count = count + 1
        values = line.split()
        if len(values) == 11:
            new_list.append(values)
        else:
            print 'Malformed sphere on line ' + str(count) + ' skipping...'
    return new_list


def float_list(value_list): #returns list of lists containing converted float values
    new_list = []
    for value in value_list:
        n = [make_floats(v) for v in value] #list containing all converted float values
        new_list.append(n)
    return new_list


def print_it(new_list):
    for n in new_list:
        print n


def make_sphere(list): #takes list of lists, returns list of spheres
    sphere_list = []
    for i in range(len(list)):
        center = data.Point(list[i][0], list[i][1], list[i][2])
        radius = list[i][3]
        color = data.Color(list[i][4], list[i][5], list[i][6])
        ambient = list[i][7]
        diffuse = list[i][8]
        specular = list[i][9]
        roughness = list[i][10]
        finish = data.Finish(ambient, diffuse, specular, roughness)
        s = data.Sphere(center, radius, color, finish)
        sphere_list.append(s)
    return sphere_list



if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
    else:
        print 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]'
