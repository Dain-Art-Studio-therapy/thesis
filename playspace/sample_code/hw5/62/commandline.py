import data
import cast
import sys

def eye_flag(argv):
    eye_x = 0.0
    eye_y = 0.0
    eye_z = -14.0
    for args in range(2,len(argv)):
        if argv[args] == '-eye':
          try:
            float(argv[args+1])
            float(argv[args+2])
            float(argv[args+3])
            eye_x = float(argv[args+1])
            eye_y = float(argv[args+2])
            eye_z = float(argv[args+3])
          except:
            eye_x = 0.0
            eye_y = 0.0
            eye_z = -14.0
    return data.Point(eye_x,eye_y,eye_z)

     
def view_flag(argv):
    view_min_x = -10.0
    view_max_x = 10.0
    view_min_y = -7.5
    view_max_y = 7.5
    view_width = 1024
    view_height = 768
    for args in range(2,len(argv)):
        if argv[args] == '-view':
          try:
            view_min_x = float(argv[args+1])
            view_max_x = float(argv[args+2])
            view_min_y = float(argv[args+3])
            view_max_y = float(argv[args+4])
            view_width = int(argv[args+5])
            view_height =int(argv[args+6])
          except:
            view_min_x = -10.0
            view_max_x = 10.0
            view_min_y = -7.5
            view_max_y = 7.5
            view_width = 1024
            view_height = 768
    view_list = [view_min_x,view_max_x,
                 view_min_y,view_max_y,view_width,view_height]
    return view_list

            
                
def light_flag(argv):
    light_x = -100.0
    light_y = 100.0
    light_z = -100.0
    light_color_r = 1.5
    light_color_g = 1.5
    light_color_b = 1.5
    for args in range(2,len(argv)):
        if argv[args] == '-light':
          try:
            float(argv[args+1])
            float(argv[args+2])
            float(argv[args+3])
            float(argv[args+4])
            float(argv[args+5])
            float(argv[args+6])
            light_x = float(argv[args+1])
            light_y = float(argv[args+2])
            light_z = float(argv[args+3])
            light_color_r = float(argv[args+4])
            light_color_g = float(argv[args+5])
            light_color_b = float(argv[args+6])
          except:
            light_x = -100.0
            light_y = 100.0
            light_z = -100.0
            light_color_r = 1.5
            light_color_g = 1.5
            light_color_b = 1.5  
    return data.Light(data.Point(light_x,light_y,light_z),
                      data.Color(light_color_r,light_color_g,light_color_b))


def ambient_flag(argv):
    ambient_r = 1.0
    ambient_g = 1.0
    ambient_b = 1.0
    for args in range(2, len(argv)):
        if argv[args] == '-ambient':
          try:
            float(argv[args+1])
            float(argv[args+2])
            float(argv[args+3])
            ambient_r = float(argv[args+1])
            ambient_g = float(argv[args+2])
            ambient_b = float(argv[args+3])
          except:
            ambient_r = 1.0
            ambient_g = 1.0
            ambient_b = 1.0
    return data.Color(ambient_r,ambient_g,ambient_b)
        

if __name__ == "__main__":
    main(sys.argv)
