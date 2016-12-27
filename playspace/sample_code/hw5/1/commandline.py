import data


def get_sphere(line,line_num):
   l = line.split()
   try:
      return data.Sphere(data.Point(float(l[0]),float(l[1]),
                                    float(l[2])),
                                    float(l[3]),
                                    data.Color(float(l[4]),float(l[5]),
                                               float(l[6])),
                                    data.Finish(float(l[7]),float(l[8]),
                                                float(l[9]),float(l[10])))
   except:
      print ('malformed sphere on line ' + str(line_num) +
             '... skipping')

def get_sphere_list(file):
   sphere_list = []
   current_line = 1
   try:
      f = open(file,'rb')
      for line in f:
         sphere = get_sphere(line,current_line)
         if sphere != None:    
            sphere_list.append(sphere)
            current_line += 1
      f.close()
      return sphere_list
   except:
      print ('File could not be opened.\nusage: python ray_caster.py <filename>'+ 
             '[-eye x y z][-view min_x'+
             'max_x min_y max_y width height][-light x y z r g b][-ambient r g '+
             'b]')
      exit(0)
                           
def get_flag_index(argv,flag_str):
   for i in range(1,len(argv)):
      if argv[i] == flag_str:
         return i
   return None

def get_view(argv):
   view_values = [-10,10,-7.5,7.5,1024,768]
   flag_i = get_flag_index(argv,'-view')
   if flag_i != None:
      try:
         for x in range(1,7):
            view_values[x - 1] = float(argv[flag_i + x])
      except:
         print 'View arguments cannot be converted into numeric values.'
         view_values = [-10,10,-7.5,7.5,1024,768]
      return view_values
   else:
      return view_values
            
def get_eye(argv):
   eye_pos = [0.0,0.0,-14.0]
   eye_i = get_flag_index(argv,'-eye')
   if eye_i != None:
      try:
         for x in range(1,4):
            eye_pos[x - 1] = float(argv[eye_i + x])
      except:
         print 'Eye arguments cannot be converted into numeric values.'
         eye_pos = [0.0,0.0,-14.0]
      return data.Point(eye_pos[0],eye_pos[1],eye_pos[2])
   else:
      return data.Point(eye_pos[0],eye_pos[1],eye_pos[2])

def get_light(argv):
   light_values = [-100.0,100.0,-100.0,1.5,1.5,1.5]
   light_i = get_flag_index(argv,'-light')
   if light_i != None:
      try:
         for x in range(1,7):
            light_values[x - 1] = float(argv[light_i + x])
      except:
         print 'Light arguments cannot be converted into numeric values.'
         light_values = [-100.0,100.0,-100.0,1.5,1.5,1.5]
      return data.Light(data.Point(light_values[0],
                                   light_values[1],
                                   light_values[2]),
                        data.Color(light_values[3],
                                   light_values[4],
                                   light_values[5]))
   else:
      return data.Light(data.Point(light_values[0],
                                   light_values[1],
                                   light_values[2]),
                        data.Color(light_values[3],
                                   light_values[4],
                                   light_values[5]))

def get_ambient(argv):
   amb_values = [1.0,1.0,1.0]
   amb_i = get_flag_index(argv,'-ambient')
   if amb_i != None:
      try:
         for x in range(1,4):
            amb_values[x - 1] = float(argv[amb_i + x])
      except:
         print 'Ambient arguments cannot be converted into numeric values.'
         amb_values = [1.0,1.0,1.0]
      return data.Color(amb_values[0],amb_values[1],amb_values[2])
   else:
      return data.Color(amb_values[0],amb_values[1],amb_values[2])
