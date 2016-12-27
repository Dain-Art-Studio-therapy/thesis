
def open_file(argv):
   try:
      opened_f = open(argv[1], 'rb')
      return opened_f
   except IOError as e:
      print 'File does not exist, or cannot be opened for reading.'
      exit(1)
   except IndexError as e:
      print 'usage: python ray_caster.py <filename> [-eye x y z]'\
            '[-view min_x max_x min_y max_y width height]'\
            '[-light x y z r g b][-ambient r g b]'
      exit(1)


#def obtain_single_sphere(file_line, i):
 #  split_line = file_line.split()
   #length_test = sphere_length_test(split_line, i)
  # if len(split_line) == 11:
   #   single_s_list = []
    #  for value in split_line:
     #    new_value = convert_float(value)
      #   single_s_list.append(new_value)
    #  return single_s_list

def obtain_sphere(argv):
   f = open_file(argv)
   line_index = 0
   result = []
   for line in f:
      split_line = line.split()
      single_sphere = []
      line_index += 1
      if len(split_line) == 11:
         try:
            for value in split_line:
               converted = float(value)
               single_sphere.append(converted)
         except:
            print 'malformed sphere on line',line_index,'...skipping'
      else:
         print 'malformed sphere on line',line_index,'...skipping'
      result.append(single_sphere)
   f.close()
   return result
   
#def obtain_single_sphere(file_line, i):
  # split_line = file_line.split()
  # try: 
    #  if len(split_line) == 11:
     #    single_s_list = []
     #    for value in split_line:
    #        new_value = convert_float(value)
   #         single_s_list.append(new_value)
  #    return single_s_list
 #  except TypeError as e:
#      print 'malformed sphere on line',i+1,'...skipping'
      
#def float_sphere_list(input_list):
 #  float_list = []
  # for value in input_list:
   #   new_value = convert_float(value)
    #  float_list.append(new_value)
   #return float_list

def find_flag(input_argu, flag):
   for i in range(len(input_argu)):
      if input_argu[i] == flag:
         return i
   return False

def obtain_eye_point(input_argu):
   DEFAULT_EYE = [0.0, 0.0, -14.0]
   FLAGS = ['-view','-light','-ambient']
   flag_index = find_flag(input_argu, '-eye')
   if flag_index is not False:
      eye_point = []
      start_range = flag_index+1
      end_range = flag_index+4
      for i in range(start_range, end_range):
         if len(input_argu) >= end_range:
            if input_argu[i] not in FLAGS:
               try:
                  float_value = float(input_argu[i])
                  eye_point.append(float_value)
               except:
                  eye_point.append(DEFAULT_EYE[i-start_end])
            else:
               return DEFAULT_EYE
         else:
            return DEFAULT_EYE
      return eye_point
   else:
      return DEFAULT_EYE

def obtain_view(input_argu):
   DEFAULT_VIEW = [-10, 10, -7.5, 7.5, 1024, 768]
   FLAGS = ['-eye','-light','-ambient']
   flag_index = find_flag(input_argu, '-view')
   if flag_index is not False:
      view = []
      start_range = flag_index+1
      end_range = flag_index+7
      for i in range(start_range, end_range):
         if len(input_argu) >= end_range:
            if input_argu[i] not in FLAGS:
               try:
                  float_value= float(input_argu[i])
                  view.append(float_value)
               except:
                  view.append(DEFAULT_VIEW[i-start_range])
            else:
               return DEFAULT_VIEW
         else:
            return DEFAULT_VIEW
      return view
   else:
      return DEFAULT_VIEW

def obtain_light_object(input_argu):
   DEFAULT_LIGHT = [-100.0, 100.0, -100.0, 1.5, 1.5, 1.5]
   FLAGS = ['-eye','-view','-ambient']
   flag_index = find_flag(input_argu, '-light')
   if flag_index is not False:
      light_object = []
      start_range = flag_index+1
      end_range = flag_index+7
      for i in range(start_range, end_range):
         if len(input_argu) >= end_range:
            if input_argu[i] not in FLAGS:
               try:
                  float_value= float(input_argu[i])
                  light_object.append(float_value)
               except:
                  light_object.append(DEFAULT_LIGHT[i-start_range])
            else:
               return DEFAULT_LIGHT
         else:
            return DEFAULT_LIGHT
      return light_object
   else:
      return DEFAULT_LIGHT


def obtain_ambient_color(input_argu):
   DEFAULT_AMBIENT = [1.0, 1.0, 1.0]
   FLAGS = ['-eye','-view','-light']
   flag_index = find_flag(input_argu, '-ambient')
   if flag_index is not False:
      ambient_color = []
      start_range = flag_index+1
      end_range = flag_index+4
      for i in range(start_range, end_range):
         if len(input_argu) >= end_range:
            if input_argu[i] not in FLAGS:
               try:
                  float_value= float(input_argu[i])
                  ambient_color.append(float_value)
               except:
                  ambient_color.append(DEFAULT_AMBIENT[i-start_range])
            else:
               return DEFAULT_AMBIENT
         else:
            return DEFAULT_AMBIENT
      return ambient_color
   else:
      return DEFAULT_AMBIENT


