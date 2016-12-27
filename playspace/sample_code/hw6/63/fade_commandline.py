# fade_commandline
import sys

def get_file_info(args, failure_message, arg_count):
   # Check to make sure enough args are supplied
   if len(args) < arg_count + 1:
      print failure_message
      sys.exit(1)
   
   # Start converted args array
   new_args = [args[1]]
   
   for i in range(2, len(args)):
      try:
         new_args.append(int(args[i]))
      except Type:
         print 'Invalid argument: {0}... Should be an integer'.format(args[i])
         sys.exit(1)
   
   return new_args
