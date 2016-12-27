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

def get_image_dimensions(line):
    lin = line.split()
    width_image = int(lin[0])
    height_image = int(lin[1])
    return (width_image, height_image)

def setup_file(filename, width_image, height_image):
    output = open(filename, 'w')
    output.write("P3\n")
    output.write(str(width_image)+" " + str(height_image) + "\n")
    output.write("255\n")
    return output
   
def construct_pixel_array(width_image, height_image):
    return [[0 for y in range(0,height_image)] for x in range(width_image)]
   
def populate_pixel_array(pixel_array, width_image, height_image, l):
    for i in range(0,len(l)):
        y = int(floor(i/float(width_image)))
        x = int(i % width_image)
        pixel_array[x][y] = l[i]
    return pixel_array
    
def print_pts(ravg,gavg,bavg,output):
    output.write(str(int(ravg))+ " "+str(int(gavg))+ " " +str(int(bavg))+"\n")

def average(sum_items, number_items):
     return sum_items/number_items

def isvalidpt(x,y,width_image,height_image):
   flag1 = False
   flag2 = False
   if (x > 0 and x < width_image):
      flag1 = True
   if (y > 0 and y < height_image):
      flag2 = True
   return flag1 and flag2

def avg_points(i,j,pixel_array,height_image,width_image,blur):
    redsum = 0
    greensum = 0
    bluesum = 0
    pixelct = 0
    for k in range(i-blur,i+blur+1):
        for l in range(j-blur,j+blur+1):
            if (isvalidpt(l,k,width_image,height_image)):
                redsum += pixel_array[l][k][0]
                greensum += pixel_array[l][k][1]
                bluesum += pixel_array[l][k][2]
                pixelct += 1
    ravg = average(redsum, pixelct)
    gavg = average(greensum, pixelct)
    bavg = average(bluesum, pixelct)
    return (ravg,gavg,bavg)

def test_args(argv):
    try:
        filename = sys.argv[1]
    except:
        sys.stderr.write('Invalid file name specified. Exiting.\n')
        sys.stderr.write('Proper syntax is: python blur.py <filename> \
[blur factor]\n')
        exit()
    try:
        blur_factor = int(sys.argv[2])
    except:
        blur_factor = 4
    return (filename, blur_factor)
   
def main(argv):
    args = test_args(argv)
    file_to_open = args[0]
    blur = args[1]
    try:
       with open(file_to_open, 'r') as f:
           l = []
           i = 0
           for line in f:
               i+=1
               if i == 2:
                  dimensions = get_image_dimensions(line)
                  width_image = dimensions[0]
                  height_image = dimensions[1]
               if i >= 4:
                  lin = line.split()
                  for w in lin:
                      l.append(float(w))
    except:
        sys.stderr.write('Error parsing file. Verify validity of file \
syntax.\n')
        exit()
    l = groups_of_3(l)
    
    output = setup_file('blurred.ppm', width_image, height_image)
    pixel_array = construct_pixel_array(width_image,height_image)
    pixel_array = populate_pixel_array(pixel_array,width_image,height_image,l)
        
    for i in range(0,height_image):
        for j in range(0,width_image):
            averages=avg_points(i,j,pixel_array,height_image,width_image,blur)
            print_pts(averages[0],averages[1],averages[2],output)
            
main(sys.argv)
