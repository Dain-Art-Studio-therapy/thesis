import commandline
import sys
import cast

def main(argv):
    cmd = commandline.main(argv)

    eye_point = cmd[0]
    min_x = cmd[1]
    max_x = cmd[2]
    min_y = cmd[3]
    max_y = cmd[4]
    width = cmd[5]
    height = cmd[6]
    ambient = cmd[7]
    light = cmd[8]
    sphere_list = cmd[9]
    fout = cmd[10]
    fout.write("P3\n")
    fout.write(str(width) + "\n")
    fout.write(str(height) + "\n")

    cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list,ambient, light, fout)


if __name__ == "__main__":
    main(sys.argv)