import sys
from math import *

def groups_of_3(l):
   final_list_length = len(l) % 3
   new_list = []
   x = 0
   while x < (len(l) - final_list_length):
      new_list.append([l[x], l[x+1], l[x+2]])
      x += 3
   if (final_list_length == 2):
      new_list.append([l[len(l)-final_list_length], l[len(l)-1]])
   if (final_list_length == 1):
      new_list.append([l[len(l)-1]])
   return new_list

def calculate_scale_factor(r,x,y,x2,y2):
    return (r - distance_form(x,y,x2,y2))/r

def limit_scale_factor(scale_factor):
    if (scale_factor < 0.2):
        scale_factor = 0.2
    return scale_factor

def print_pts(r,g,b,output):
    output.write(str(int(r))+ " "+str(int(g))+ " " +str(int(b))+"\n")

def fade_point_from_radius(i,l,width_image,height_image,r,x,y):
    number_in_list_file = i
    y2 = floor(number_in_list_file / width_image)
    x2 = number_in_list_file % width_image
    scale_factor = calculate_scale_factor(r,x,y,x2,y2)
    scale_factor = limit_scale_factor(scale_factor)
    l[i][0] = l[i][0] * scale_factor
    l[i][1] = l[i][1] * scale_factor
    l[i][2] = l[i][2] * scale_factor
    return (l[i][0], l[i][1], l[i][2])

def distance_form(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def setup_file(filename, width_image, height_image):
    output = open(filename, 'w')
    output.write("P3\n")
    output.write(str(width_image)+" " + str(height_image) + "\n")
    output.write("255\n")
    return output

def test_args(argv):
   try:
       try:
           file_to_open = argv[1]
       except:
           sys.stderr.write('Invalid file name specified. Exiting.\n')
       try:
           y = int(sys.argv[2])
       except:
           sys.stderr.write('Invalid row specified. Exiting.\n')
       try:
           x = int(sys.argv[3])
       except:
           sys.stderr.write('Invalid column specified. Exiting.\n')
       try:
           r = int(sys.argv[4])
       except:
           sys.stderr.write('Invalid radius specified. Exiting.\n')
       return (file_to_open,y,x,r)
   except:
       sys.stderr.write('Proper syntax is: python fade.py \
<filename> <row> <col> <radius>\n')
       exit()
        
   
def main(argv):
    args = test_args(argv)
    file_to_open = args[0]
    y = args[1]
    x = args[2]
    r = args[3]
    try:
       with open(file_to_open, 'r') as f:
           l = []
           i = 0
           for line in f:
               i+=1
               if i == 2:
                  lin = line.split()
                  width_image = int(lin[0])
                  height_image = int(lin[1])
               if i >= 4:
                  lin = line.split()
                  for w in lin:
                      l.append(float(w))                  
    except:
        sys.stderr.write('Error parsing file. Verify validity of file \
syntax.\n')
        exit()
    l = groups_of_3(l)

    output = setup_file('faded.ppm', width_image, height_image)
    for i in range(0,len(l)):
        point = fade_point_from_radius(i,l,width_image,height_image,r,x,y)
        print_pts(point[0],point[1],point[2],output)



main(sys.argv)
