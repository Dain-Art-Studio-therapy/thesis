def get_file_name(args, failure_message):
   # Check to make sure enough args are supplied
   if len(args) < 2:
      print failure_message
      sys.exit(1)

   return args[1]
