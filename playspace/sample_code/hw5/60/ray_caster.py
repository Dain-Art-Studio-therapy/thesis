import sys
import commandline
import cast
import collisions
import vector_math
import data

defaults = {"min_x": -10, "max_x": 10, "min_y": -7.5, "max_y":7.5,
            "width": 1024, "height": 768, "eye_point": data.Point(0, 0, -14),
            "ambient_color": data.Color(1, 1, 1),
            "light": data.Light(data.Point(-100, 100, -100),
            data.Color(1.5, 1.5, 1.5)), "outfile": "image.ppm"}



def main(argv):
   sphere_list = get_sphere_list(argv)
   
   arg_dict = commandline.find_cast_args(defaults, argv)

   if "-debug" not in argv:
      cast.cast_all_rays(arg_dict["min_x"], arg_dict["max_x"], arg_dict["min_y"],
            arg_dict["max_y"], int(arg_dict["width"]), int(arg_dict["height"]),
            arg_dict["eye_point"], sphere_list, arg_dict["ambient_color"], 
            arg_dict["light"], arg_dict["outfile"])

      
def get_sphere_list(argv):
   sphere_list = []
   try:
      if len(argv) == 1:
         raise RuntimeError
      filename = argv[1]
      file = open(filename, "rb")
   except IOError:
      print >> sys.stderr, "Input File could not be opened"
      exit(1)
   except RuntimeError:
      print >> sys.stderr, commandline.usage_error
      exit(1)

   line_num = 0
   for line in file:
      line_num += 1
      try:
         sphere_list.append(process_line(line))
      except:
         print >> sys.stderr, "Malformed Sphere on Line %d ... skipping" % line_num
   
   file.close()
   return sphere_list      



def process_line(line):
   val_list = line.strip().split()
   float_list = []
   if len(val_list) != 11:
      raise RuntimeError("The input line is not properly formatted")
   for i in range(len(val_list)):
      float_list.append(float(val_list[i]))
   return data.Sphere(data.Point(float_list[0], float_list[1], float_list[2]),
      float_list[3], data.Color(float_list[4], float_list[5], float_list[6]),
      data.Finish(float_list[7], float_list[8], float_list[9], float_list[10]))


      
if __name__ == "__main__":
   main(sys.argv)
