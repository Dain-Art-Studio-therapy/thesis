import sys
import data
import vector_math
import cast
import collisions

#Takes in command line data and returns it as a list
def command(argv):
   new_list = []
   for (a,b) in enumerate(argv):
      new_list.append(commandline_eye(argv))

      # COMMANDLINE: -VIEW
      if '-view' in argv:
         view_point_index = argv.index( '-view' )
         try:
            min_x = float(argv[view_point_index + 1])
            max_x = float(argv[view_point_index + 2])
            min_y = float(argv[view_point_index + 3])
            max_y = float(argv[view_point_index + 4])
            width = int(argv[view_point_index + 5])
            height = int(argv[view_point_index + 6])
            new_list.append(min_x)
            new_list.append(max_x)
            new_list.append(min_y)
            new_list.append(max_y)
            new_list.append(height)
            new_list.append(width)
         except:
            min_x = -10
            max_x = 10
            min_y = -7.5
            max_y = 7.5
            width = 1024
            height = 768
            new_list.append(min_x)
            new_list.append(max_x)
            new_list.append(min_y)
            new_list.append(max_y)
            new_list.append(height)
            new_list.append(width)
      else:
         min_x = -10
         max_x = 10
         min_y = -7.5
         max_y = 7.5
         width = 1024
         height = 768
         new_list.append(min_x)
         new_list.append(max_x)
         new_list.append(min_y)
         new_list.append(max_y)
         new_list.append(height)
         new_list.append(width)
     
      new_list.append(commandline_light(argv))
      new_list.append(commandline_ambient(argv))
      new_list.append(argv[1])
   return new_list



#COMMANDLINE -AMBIENT
def commandline_ambient(argv):
   if '-ambient' in argv:
      ambient_index = argv.index( '-ambient' )
      try:
         color = data.Finish(data.Color(float(argv[ambient_index + 1]), float(argv[ambient_index + 2]), float(argv[ambient_index + 3])), 1.0, 1.0, 1.0)
         return color
      except:
         color = data.Finish(data.Color(1.0, 1.0, 1.0), 1.0, 1.0, 1.0)
         return color
   else:
      color = data.Finish(data.Color(1.0, 1.0, 1.0), 1.0, 1.0, 1.0)
      return color


#COMMANDLINE -EYE
def commandline_eye(argv):
   if '-eye' in argv:
      eye_point_index = argv.index( '-eye' )
      try:
         eye_point = data.Point(float(argv[eye_point_index + 1]),float(argv[eye_point_index + 2]),float(argv[eye_point_index + 3]))
         return eye_point
      except:
         eye_point = data.Point(0.0,0.0,-14.0)
         return eye_point
   else: 
      eye_point = data.Point(0.0,0.0,-14.0)
      return eye_point


#COMMANDLINE -LIGHT
def commandline_light(argv):
   if '-light' in argv:
      light_index = argv.index( '-light' )
      try:
         light = data.Light(data.Point(float(argv[light_index + 1]), float(argv[light_index + 2]), float(argv[light_index + 3])), data.Color(float(argv[light_index + 4]), float(argv[light_index + 5]), float(argv[light_index + 6])))
         return light
      except:
         light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
         return light
   else:
      light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))
      return light




          
    



