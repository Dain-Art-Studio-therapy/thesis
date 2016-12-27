import ray_caster
import data
import sys
import cast

def process_cmdline(sphere_list):
   # combines all previous functions and returns a list with commandline arguments
   view_stuff = view()
   eye_stuff = eye()
   ambient_stuff = ambient()
   light_stuff = light()
   cmdline_return = cast.cast_all_rays(view_stuff[0], view_stuff[1], view_stuff[2], view_stuff[3], \
   	  view_stuff[4], view_stuff[5], \
   	  eye_stuff, sphere_list, \
        ambient_stuff, light_stuff)
   return cmdline_return
   

def eye():
   eye_args = find_args('-eye', 3)
   return data.Point(eye_args[0], eye_args[1], eye_args[2])

def view():
	return find_args('-view', 6)

def light():
   l_args = find_args('-light', 6)
   return data.Light(data.Point(l_args[0], l_args[1], l_args[2]), \
   	data.Color(l_args[3], l_args[4], l_args[5]))

def ambient():
	amb_args = find_args('-ambient', 3)
	return data.Color(amb_args[0], amb_args[1], amb_args[2])

def find_args(flag, num_args):
   if in_cmdline(flag):
      index = sys.argv.index(flag)
      arguments = []
      for arg in range(1, int(num_args) + 1):
         arguments.append(float(sys.argv[index + arg]))
      return arguments
   else:
      return default_args(flag)

def in_cmdline(flag):
   return flag in sys.argv

def default_args(flag):
   if 'eye' in flag:
   	  return [0.0, 0.0, -14.0]
   elif 'view' in flag:
   	  return [-10, 10, -7.5, 7.5, 1024, 768]
   elif 'light' in flag:
   	  return [-100.0, 100.0, -100.0, 1.5, 1.5, 1.5]
   elif 'ambient' in flag:
   	  return [1.0, 1.0, 1.0]
   else:
   	  return None


  
