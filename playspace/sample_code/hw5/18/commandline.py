from data import *


def find_eye(argv_list):
    default_point = Point(0.0, 0.0, -14.0)
    try:
        for i in range(len(argv_list)):
            if argv_list[i] == '-eye':
                return Point(float(argv_list[i + 1]),\
                             float(argv_list[i + 2]),\
                             float(argv_list[i + 3]))
    except IndexError:
        return default_point
    except ValueError:
        return default_point
    return default_point


# returns Light object
def find_light(argv_list):
    light_pt = Point(-100.0, 100.0, -100.0)
    light_color = Color(1.5, 1.5, 1.5)
    default_light = Light(light_pt, light_color)
    try:
        for i in range(len(argv_list)):
            if argv_list[i] == '-light':
                lightPoint = Point(float(argv_list[i + 1]),\
                                   float(argv_list[i + 2]),\
                                   float(argv_list[i + 3]))
                lightColor = Color(float(argv_list[i + 4]),\
                                   float(argv_list[i + 5]),\
                                   float(argv_list[i + 6]))
                return Light(lightPoint, lightColor)
    except ValueError:
        return default_light
    except IndexError:
        return default_light
    return default_light


# returns Color object
def find_ambient(argv_list):
    default_ambient = Color(1.0, 1.0, 1.0)
    try:
        for i in range(len(argv_list)):
            if argv_list[i] == '-ambient':
                return Color(float(argv_list[i + 1]), float(argv_list[i + 2]),\
                        float(argv_list[i + 3]))
    except ValueError:
        return default_ambient
    except IndexError:
        return default_ambient
    return default_ambient


# returns Tuple of all numbers
def find_view(argv_list):
    default_view = (-10, 10, -7.5, 7.5, 1024, 768)
    try:
        for i in range(len(argv_list)):
            if argv_list[i] == '-view':
                return (float(argv_list[i + 1]), float(argv_list[i + 2]),\
                        float(argv_list[i + 3]), float(argv_list[i + 4]),\
                        int(argv_list[i + 5]), int(argv_list[i + 6]))
    except ValueError:
        return default_view
    except IndexError:
        return default_view
    return default_view
