from math import sqrt


def fade_scale(x, y, argv):
    pixel_pt = Point(x, y)
    dist = dist_from_center(float(argv[2]), 
                            float(argv[3]), 
                            pixel_pt)
    scale = calc_scale(float(argv[4]), dist)
    return scale

	
def calc_scale(radius, distance):
    min_dark = .20
    scale = (radius - distance)/float(radius)
    if scale < min_dark:
        scale = min_dark
    return scale


def dist_from_center(row, col, pixel_pt):
    center_pt = Point(col, row)
    return sqrt(((pixel_pt.x - center_pt.x) ** 2) + 
            ((pixel_pt.y - center_pt.y) ** 2))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

