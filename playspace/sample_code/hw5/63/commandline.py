from data import *

def float_default(string, standard):
        try:
                return float(string)
        except:
                return standard

def eye_flag(argv):
        try:
                for i in range(len(argv)):
                        if argv[i] == '-eye':
                                x = float(argv[i+1])
                                y = float(argv[i+2])
                                z = float(argv[i+3])
                return Point(x, y, z)
        except:
                return Point(0.0, 0.0, -14.0)

def view_flag(argv):
        try:
                for i in range(len(argv)):
                        if argv[i] == '-view':
                                min_x = float(argv[i+1])
                                max_x = float(argv[i+2])
                                min_y = float(argv[i+3])
                                max_y = float(argv[i+4])
                                width = int(argv[i+5])
                                height = int(argv[i+6])
                return min_x, max_x, min_y, max_y, width, height
        except:
                return -10.0, 10.0, -7.5, 7.5, 1024, 768


def light_flag(argv):
        try:
                for i in range(len(argv)):
                        if argv[i] == '-light':
                                x = float(argv[i+1])
                                y = float(argv[i+2])
                                z = float(argv[i+3])
                                r = float(argv[i+4])
                                g = float(argv[i+5])
                                b = float(argv[i+6])
                return Light(Point(x, y, z), Color(r, g, b))
        except:
                return Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))

def ambient_flag(argv):
        try:
                for i in range(len(argv)):
                        if argv[i] == '-ambient':
                                r = float(argv[i+1])
                                g = float(argv[i+2])
                                b = float(argv[i+3])
                return Color(r, g, b)
        except:
                return Color(1.0, 1.0, 1.0)
