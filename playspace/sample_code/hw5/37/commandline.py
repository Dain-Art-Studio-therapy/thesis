import sys

#######NOTE TO INSTRUCTOR: I could have written this in different files, but 
#the way i did it allowed the arguments to only be gone through once, making the 
#program faster

def command_line(eye_default, default_view_tuple, default_light, default_ambient):
   eye_flag = 0
   view_flag = 0
   light_flag = 0
   ambient_flag = 0

   for arg_index in range(len(sys.argv)):
      if sys.argv[arg_index] == '-eye':
         eye_flag = 1
         try:
            arg_eye = Point(float(sys.argv[arg_index + 1]), 
               float(sys.argv[arg_index + 2]), float(sys.argv[arg_index + 3]))
         except:
            arg_eye = default_eye
      elif sys.argv[arg_index] == '-view':
         view_flag = 1
         try:
            arg_view_tuple = (float(sys.argv[arg_index + 1]), 
               float(sys.argv[arg_index + 2]), float(sys.argv[arg_index + 3]), 
               float(sys.argv[arg_index + 4]), float(sys.argv[arg_index + 5]), 
               float(sys.argv[arg_index + 6]))
         except:
            arg_view_tuple = default_view_tuple
      elif sys.argv[arg_index] == '-light':
         light_flag = 1
         try:
            arg_light = Light(Point(float(sys.argv[arg_index + 1]), 
               float(sys.argv[arg_index + 2]), float(sys.argv[arg_index + 3])), 
            Color(float(sys.argv[arg_index + 4]), 
               float(sys.argv[arg_index + 5]), float(sys.argv[arg_index + 6])))
         except:
            arg_light = default_light
      elif sys.argv[arg_index] == '-ambient':
         ambient_flag = 1
         try:
            arg_ambient = Color(float(sys.argv[arg_index + 1]), 
               float(sys.argv[arg_index + 2]), float(sys.argv[arg_index + 3]))
         except:
            arg_ambient = default_ambient

   if eye_flag == 1:
      new_eye = arg_eye
   elif eye_flag == 0:
      new_eye = eye_default

   if view_flag == 1:
      new_view_tuple = arg_view_tuple
   else:
      new_view_tuple = default_view_tuple

   if light_flag == 1:
      new_light = arg_light
   elif light_flag == 0:
      new_light = default_light

   if ambient_flag == 1:
      new_ambient = arg_ambient
   elif ambient_flag == 0:
      new_ambient = default_ambient

   return new_eye, new_view_tuple, new_light, new_ambient