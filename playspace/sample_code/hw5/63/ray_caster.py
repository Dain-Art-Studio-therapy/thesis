import sys
from cast import *
from commandline import *

def float_default(string, standard):
        try:
                return float(string)
        except:
                return standard

def open_file(name, mode):
        try:
                return open(name, mode)
        except:
                print >> sys.stderr, '{0}:{1}'.format(name, "File wont open")
                exit(1)



def main(argv):
        with open_file(argv[1], 'rb') as f:
                sphere_list = []
                line = f.readlines()
                for v in line:
                        g = v.split()
                        if len(g) == 11:
                                try:
                                        point = Point(float(g[0]), float(g[1]), float(g[2]))
                                        radius = float(g[3])
                                        color = Color(float(g[4]), float(g[5]), float(g[6]))
                                        finish = Finish(float(g[7]), float(g[8]), float(g[9]), float(g[10]))
                                        sphere_list.append(Sphere(point, radius, color, finish))
                                except:
                                        print >> sys.stderr, "sphere had an incorrect value"
                return sphere_list
sphere_list = main(sys.argv)
view = view_flag(sys.argv)
eye_point = eye_flag(sys.argv)
color = ambient_flag(sys.argv)
light = light_flag(sys.argv)
min_x = view[0]
max_x = view[1]
min_y = view[2]
max_y = view[3]
width = view[4]
height = view[5]


#min_x = -10
#max_x = 10
#min_y = -7.5
#max_y = 7.5
#width = 1024
#height = 768
#eye_point = Point(0.0, 0.0, -14.0)
#color = Color(1.0, 1.0, 1.0)
#light = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))

cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light)


if __name__=='__main__':
        main(sys.argv)


