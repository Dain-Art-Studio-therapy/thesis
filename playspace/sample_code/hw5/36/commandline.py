import sys
import data

# -eye -view -light -ambient
# defaults eye(0.0, 0.0, -14.0) view(min_x -10, max_x 10, min_y -7.5, max_y 7.5, width 1024, height 768)
# default light((-100.0, 100.0, -100.0), (1.5, 1.5, 1.5)) ambient(1.0, 1.0, 1.0)
eye_point = data.Point(0.0, 0.0, -14.0)
min_x = -10
max_x = 10
min_y = -7.5
max_y = 7.5
width = 1024
height = 768
ambient = data.Color(1.0, 1.0, 1.0)
light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))


def argv_check(argv):
    # check cmdline flags
    if "-eye" in argv:
        try:
            e = argv.index('-eye')
            x = float(argv[e + 1])
            y = float(argv[e + 2])
            z = float(argv[e + 3])
            global eye_point
            eye_point = data.Point(x, y, z)
        except:
            pass

    if "-view" in argv:
        try:
            v = argv.index('-view')
            global min_x, max_x, min_y, max_y, width, height
            min_x = float(argv[v + 1])
            max_x = float(argv[v + 2])
            min_y = float(argv[v + 3])
            max_y = float(argv[v + 4])
            width = (argv[v + 5])
            height = (argv[v + 6])
        except:
            pass
    if "-light" in agrv:
        try:
            l = argv.index('-light')
            x = float(argv[l + 1])
            y = float(argv[l + 2])
            z = float(argv[l + 3])
            c1 = float(argv[l + 4])
            c2 = float(argv[l + 5])
            c3 = float(argv[l + 6])
            global light
            light = data.Light(data.Point(x, y, z), data.Color(c1, c2, c3))
            # find location of light in argv process argv to try and set light
        except:
            pass
    if "-ambient" in argv:
        try:
            a = argv.index('-ambient')
            c1 = float(argv[a + 1])
            c2 = float(argv[a + 2])
            c3 = float(argv[a + 3])
            global ambient
            ambient = data.Color(c1, c2, c3)
        except:
            pass
            # process argv to try setting ambient except to default

def open_file(name, mode):
    try:
        return open(name, mode)
    except:
        print >> sys.stderr, 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width' \
                             ' height] [-light x y z r g b] [-ambient r g b]'
        exit(1)


def read_file(line, num):
    try:
        sp = line.split()
        x = float(sp[0])
        y = float(sp[1])
        z = float(sp[2])
        radius = float(sp[4])
        r = float(sp[5])
        g = float(sp[6])
        b = float(sp[7])
        a = float(sp[8])
        diffuse = float(sp[9])
        specular = float(sp[10])
        roughness = float(sp[11])
        center = data.Point(x, y, z)
        color = data.Color(r, g, b)
        finish = data.Finish(a, diffuse, specular, roughness)
        sphere = data.Sphere(center, radius, color, finish)
        return sphere
    except:
        n = str(num)
        print >> sys.stderr, 'malformed sphere on line ', n, '... skipping'

def main(argv):
    fout = open('image.ppm', 'w')

    sphere_list = []
    num = 0
    if len(argv) < 2:
        print >> sys.stderr, 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width' \
                             ' height] [-light x y z r g b] [-ambient r g b]'
        exit(1)
    with open_file(argv[1], 'rb') as f:
        for line in f:
            num += 1
            sphere_list.append(read_file(line, num))
    return eye_point, min_x, max_x, min_y, max_y, width, height, ambient, light, sphere_list, fout


