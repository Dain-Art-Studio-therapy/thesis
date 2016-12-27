# blur_commandline
import sys

def get_file_info(args, failure_message, def_rad):
   # Check to make sure enough args are supplied
   if len(args) < 2:
      print failure_message
      sys.exit(1)
   
   # Start converted args array
   # Get optional if possible
   new_args = [args[1]]

   try:
      new_args.append(int(args[2]))
   except:
      new_args.append(def_rad)
   
   
   return new_args
