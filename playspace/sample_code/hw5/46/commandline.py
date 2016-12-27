from data import *


def process_eye_flag(argv, cm, default):
    try:
        inputs = [argv[cm + 1], argv[cm + 2], argv[cm + 3]]
        eye = verify_flag_float(inputs, default)
        return eye
    except:
        return default


def process_view_flag(argv, cm, default):
    try:
        inputs = [argv[cm + 1], argv[cm + 2], argv[cm + 3], 
                  argv[cm + 4], argv[cm + 5], argv[cm + 6]]
        view = verify_flag_float(inputs, default)
        return view
    except:
        return default    


def process_light_flag(argv, cm, default):
    try:
        inputs = [argv[cm + 1], argv[cm + 2], argv[cm + 3], 
                  argv[cm + 4], argv[cm + 5], argv[cm + 6]]
        light = verify_flag_float(inputs, default)
        return light
    except:
        return default


def process_ambient_flag(argv, cm, default):#ambient light color
    try:
        inputs = [argv[cm + 1], argv[cm + 2], argv[cm + 3]]
        color = verify_flag_float(inputs, default)
        return color
    except:
        return default

#-------------------------------helper function-------------------------------

def verify_flag_float(inputs, default):
    new_inputs = []
    for num in range(len(inputs)):
        try:
            float(inputs[num])
        except:
            inputs[num] = default[num]
        new_inputs.append(float(inputs[num]))
    return new_inputs

