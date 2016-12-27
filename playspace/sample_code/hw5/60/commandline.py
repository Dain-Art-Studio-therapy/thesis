import sys
import data
import vector_math
import collisions
import cast


usage_error = "usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]"

ARG_LENS = {"-eye": 4, "-view": 7, "-light": 7, "-ambient": 4, "-debug": 1, "-scale": 2}
# added -scale flag for convenience when only changing resolution

def find_cast_args(defaults, argv):
   
   result_dict = defaults.copy()
   
   arg_groups = group_args(argv)

   for group in arg_groups:
      if group[0] == "-eye":
         result_dict["eye_point"] = data.Point(group[1], group[2], group[3])
      elif group[0] == "-view":
         result_dict["min_x"] = group[1]
         result_dict["max_x"] = group[2]
         result_dict["min_y"] = group[3]
         result_dict["max_y"] = group[4]
         result_dict["width"] = group[5]
         result_dict["height"] = group[6]
      elif group[0] == "-light":
         result_dict["light"] = data.Light(data.Point(group[1], group[2], group[3]),
            data.Color(group[4], group[5], group[6]))
      elif group[0] == "-ambient":
         result_dict["ambient_color"] = data.Color(group[1], group[2], group[3])
      elif group[0] == "-scale":
         result_dict["width"] *= group[1]
         result_dict["height"] *= group[1]
   return result_dict


def group_args(argv):
   groups = []   
   try:
      for i in range(2, len(argv)):
         check_arg(argv[i])
         resgroup = []
         if argv[i] in ARG_LENS.keys():
            resgroup = argv[i: i + ARG_LENS[argv[i]]]
            resgroup = strs_to_floats(resgroup, argv[i])
            groups.append(resgroup)
      return groups
   except IOError as e:
      print >> sys.stderr, e
      exit(1)
   except Exception:
      print usage_error
      exit(1)
         
def check_arg(arg):
   try:
      float(arg)
   except:
      if arg not in ARG_LENS.keys():
         raise RuntimeError(usage_error)



def strs_to_floats(group, arg):
   result = [arg]
   for i in range(1, ARG_LENS[arg]):
      result.append(float(group[i]))
   return result
