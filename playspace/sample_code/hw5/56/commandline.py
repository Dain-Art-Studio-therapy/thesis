import sys
from data import *
from ray_caster import *
import ray_caster

def arguments(argv):
    #returns a tuple of all settings, default if invalid input is supplied

    eye_point = Point(0.0, 0.0, -14.0)
    min_x = -10
    max_x = 10
    min_y = -7.5
    max_y = 7.5
    width = 1024
    height = 768
    light_point = Point(-100.0, 100.0, -100.0)
    light_color = Color(1.5, 1.5, 1.5)
    light = Light(light_point, light_color)
    ambient_light = Color(1.0, 1.0, 1.0)

    for i in range(len(argv)):
        if argv[i] == '-eye':

            try:
                eye_x = ray_caster.convert_to_float(argv[i+1])
                eye_y = ray_caster.convert_to_float(argv[i+2])
                eye_z = ray_caster.convert_to_float(argv[i+3])
                eye_point = Point(eye_x, eye_y, eye_z)

            except:
               print >> sys.stderr, 'Invalid eye point. ' \
                                    'Eye point set to default.'

        if argv[i] == '-view':
            try:
                min_x = ray_caster.convert_to_float(argv[i+1])
                max_x = ray_caster.convert_to_float(argv[i+2])
                min_y = ray_caster.convert_to_float(argv[i+3])
                max_y = ray_caster.convert_to_float(argv[i+4])
                width = int(argv[i+5])
                height = int(argv[i+6])
            except:
                print >> sys.stderr, 'Invalid view. View set to default.'

        if argv[i] == '-light':
            try:
                light_x = ray_caster.convert_to_float(argv[i+1])
                light_y = ray_caster.convert_to_float(argv[i+2])
                light_z = ray_caster.convert_to_float(argv[i+3])
                light_r = ray_caster.convert_to_float(argv[i+4])
                light_g = ray_caster.convert_to_float(argv[i+5])
                light_b = ray_caster.convert_to_float(argv[i+6])
                light_point = Point(light_x, light_y, light_z)
                light_color = Color(light_r, light_g, light_b)
                light = Light(light_point, light_color)
            except:
                print >> sys.stderr, 'Invalid light. Light set to default.'

        if argv[i] == '-ambient':
            try:
                ambient_r = ray_caster.convert_to_float(argv[i+1])
                ambient_g = ray_caster.convert_to_float(argv[i+2])
                ambient_b = ray_caster.convert_to_float(argv[i+3])
                ambient_light = Color(ambient_r, ambient_g, ambient_b)
            except:
                print >> sys.stderr, 'Invalid ambient light. ' \
                                     'Ambient light set to default.'


    settings = (min_x, max_x, min_y, max_y, width, height,
                    eye_point, light, ambient_light)
    return settings