import sys
import data
import cast
import commandline


command_result = commandline.spheres(sys.argv[1])
sphere_list = command_result[0]
failed = command_result[1]

arg_list = []
for i in range(2,len(sys.argv)):
   value = sys.argv[i]
   arg_list.append(value)

truth = []   
   
if "[-eye" in arg_list:
   truth.append(True)
else:
   truth.append(False)

if "[-view" in arg_list:
   truth.append(True)
else:
   truth.append(False)

if "[-light" in arg_list:
   truth.append(True)
else:
   truth.append(False)

if "[-ambient" in arg_list:
   truth.append(True)
else:
   truth.append(False)
   
if truth[0]:
   location = arg_list.index("[-eye")
   x = float(arg_list[location+1])
   y = float(arg_list[location+2])
   z = float(arg_list[location+3][:-1])
   eye = data.Point(x,y,z)
else:
   eye = data.Point(0.0,0.0,-14.0)

if truth[1]:
   location = arg_list.index("[-view")
   min_x = float(arg_list[location+1])
   max_x = float(arg_list[location+2])
   min_y = float(arg_list[location+3])
   max_y = float(arg_list[location+4])
   width = float(arg_list[location+5])
   height = float(sys.argv[location+6][:-1])
else:
   min_x = -10
   max_x = 10
   min_y = -7.5
   max_y = 7.5
   width = 1024
   height = 768

if truth[2]:
   location = arg_list.index("[-light")
   x = float(arg_list[location+1])
   y = float(arg_list[location+2])
   z = float(arg_list[location+3])
   r = float(arg_list[location+4])
   g = float(arg_list[location+5])
   b = float(arg_list[location+6][:-1])
   point_light = data.Point(x,y,z)
   color_light = data.Color(r,g,b)
   light = data.Light(point_light,color_light)
else:   
   point_light = data.Point(-100,100,-100)
   color_light = data.Color(1.5,1.5,1.5)
   light = data.Light(point_light,color_light)

if truth[3]:
   location = arg_list.index("[-ambient")
   r = float(arg_list[location+1])
   g = float(arg_list[location+2])
   b = float(arg_list[location+3][:-1])
   ambient = data.Color(r,g,b)
else:
   ambient = data.Color(1.0,1.0,1.0)


temp = sys.stdout
sys.stdout = open('image.ppm','w')

cast.cast_all_rays(min_x,max_x,min_y,max_y,width,height,eye,sphere_list,ambient,light)

sys.stdout.close()
sys.stdout = temp

for x in failed:
   print "malformed sphere on line", x


