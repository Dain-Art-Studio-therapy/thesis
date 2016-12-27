# x y z radius r g b ambient diffuse specular roughness
#1.0 1.0 0.0 2.0 1.0 0.0 1.0 0.2 0.4 0.5 0.05
#8.0 -10.0 110.0 100.0 0.2 0.2 0.6 0.4 0.8 0.0 0.05
import sys
import data
import cast
def open_file(name, mode):
   try:
      f = open(name,'r')
      return f
   except IndexError:
      print ("usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]")
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

def make_spheres(f):
   spheres=[]
   for line in f:
      sphere_values= str.split(line)
      print sphere_values
      try:
         point_sphere= data.Point(float(sphere_values[0]), float(sphere_values[1]), float(sphere_values[2]))
         radius_sphere= float(sphere_values[3])
         color_sphere= data.Color(float(sphere_values[4]), float(sphere_values[5]), float(sphere_values[6]))
         ambient_sphere= float(sphere_values[7])
         diffuse_sphere= float(sphere_values[8])
         specular_sphere= float(sphere_values[9])
         roughness_sphere= float(sphere_values[10])
         spheres.append(data.Sphere(point_sphere, radius_sphere, color_sphere, data.Finish(ambient_sphere, diffuse_sphere, specular_sphere, roughness_sphere)))
      except:
         print 'Error'
         #print("malformed sphere on line {0}".format(num))
   return spheres

def rays_other_values(arg):
   command_line= ['-eye', '-view', '-light', '-ambient']
   default_eye= (0.0, 0.0, -14.0)
   default_rectangle= (-10, 10, -7.5, 7.5, 1024, 768)
   default_light= (-100.0, 100.0, -100.0, 1.5, 1.5, 1.5)
   default_ambient= (1.0, 1.0, 1.0)
   set_eye= []
   set_view= []
   set_light= []
   set_ambient= []
   for i in range(len(arg)):
      if arg[i] in command_line:
         if arg[i] == command_line[0]:
            try:
               eye_indice= arg.index(command_line[0])
               x= float(arg[eye_indice +1])
               y= float(arg[eye_indice +2])
               z= float(arg[eye_indice +3])
               set_eye= (x, y, z)
            except:
               set_eye= default_eye
         if arg[i] == command_line[1]:
            try:
               view_indice= sys.arg.index(command_line[1])
               min_x= float(arg[view_indice +1])
               max_x= float(arg[view_indice +2])
               min_y= float(arg[view_indice +3])
               max_y= float(arg[view_indice +4])
               width= float(arg[view_indice +5])
               height= float(arg[view_indice +6])
               set_view= (min_x, max_x, min_y, max_y, width, height)
            except:
               set_view= default_rectangle
         if arg[i] == command_line[2]:
            try:
               light_indice= arg.index(command_line[2])
               x= float(arg[light_indice +1])
               y= float(arg[light_indice +2])
               z= float(arg[light_indice +3])
               r= float(arg[light_indice +4])
               g= float(arg[light_indice +5])
               b= float(arg[light_indice +6])
               set_light= (x, y, z, r, g, b)
            except:
               set_light= default_light
         if arg[i] == command_line[3]:
            try:
               ambient_indice= arg.index(command_line[3])
               r= float(arg[ambient_indice +1])
               g= float(arg[ambient_indice +2])
               b= float(arg[ambient_indice +3])
               set_ambient= (r, g, b)
            except:
               set_ambient= default_ambient
   if set_eye == []:
      set_eye= default_eye
   if set_view == []:
      set_view= default_rectangle
   if set_ambient == []:
      set_ambient = default_ambient
   if set_light == []:
      set_light = default_light
   light= data.Light(data.Point(set_light[0], set_light[1], set_light[2]), data.Color(set_light[3], set_light[4], set_light[5]))
   eye= data.Point(set_eye[0], set_eye[1], set_eye[2])
   ambient= data.Color(set_ambient[0], set_ambient[1], set_ambient[2])
   other_values= [eye, set_view, light, ambient]
   return other_values

#def length_arg(default, object):
   #for i in default:
      #while len(default) >= len(object):
         #object.append(default[i])
      #break
   #return object


#def check_length(command_line, default, arg, i):
   #list_length= 0
   #flagged_list= []
   #if arg[i] == command_line[1] or arg[i] == command_line[2]:
      #list_length= 6
   #else:
      #list_length= 3
   #i+=1
   #indice= 0
   #current_length= i
   #while i < current_length + list_length:
      #try:
         #flagged_list.append(float(arg[i]))
      #except:
         #if i == len(arg):
            #return (flagged_list, i)
            #break
         #elif arg[i] in command_line:
            #return (flagged_list, i)
            #break
         #else:
            #return_list.append(default[indice])
      #i+=1
      #indice+=1
   #return (flagged_list, i)
  #take file, split file to lines, list, convert to float(try, except - missing index? try- make sphere, except-conversion-not enough info), sphere, point=[0][1][2], append
