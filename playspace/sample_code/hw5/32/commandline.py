# Command line processing
import sys
import copy

def get_file_name(args):
   # Check to make sure enough args are supplied
   if len(args) < 2:
      print 'usage: python ray_caster.py <filename> [-eye x y z] \
[-view min_x max_x min_y max_y width height] \
[-light x y z r g b] [-ambient r g b]'
      sys.exit(1)

   return args[1]

# flags = [(flag, [default vals]), ...]
# ex      [ ('-eye', [0.0, 0.0, -14.0] ) , ...]
def process_optional_args(args, flags):

   # this will hold arrays of flag values, starting with default
   processed_args = list([vals for (flag, vals) in flags])
   
   # Check length of args
   if len(args) < 3:
      return processed_args

   # Iterate through flags and args and see which ones match
   for (i, (flag, def_vals)) in enumerate(flags):
      for (j, arg) in enumerate(args):
         if arg == flag:
            converted_vals = process_args(args[(j+1)::], def_vals, [f for (f, v) in flags])
            # Put flag_vals into appropriate slot
            processed_args[i] = converted_vals
   return processed_args 

#flag_strs = ['-eye', '-view', ...]
def process_args(vals, def_vals, flag_strs):
   use_def_vals = False
   converted_vals = []

   # Check if enough args are present
   if len(def_vals) > len(vals):
      use_def_vals = True

   # Iterate through see if convert is possible
   def_val_len = len(def_vals)
   i = 0
   while use_def_vals == False and i < def_val_len:
      val = vals[i]
      try:
         f = float(val)
         converted_vals.append(f)
      except:
         # If a flag is found as an argument, assume the user left out an arg
         for flag in flag_strs:
            if val == flag:
               use_def_vals == True
               break
         converted_vals.append(def_vals[i])
      i += 1

   # Decide which vals to return
   if use_def_vals == True:
#      return copy.deepcopy(def_vals)
      return def_vals
   else:
      return converted_vals






