import sys
import groups
import math

#Main
def main(argv):
   output_file = open('faded.ppm','r+b')
   ppm = "P3\n493 401\n255\n" 
   output_file.write(ppm)
   user_input = commandline(argv)
   input_file = attempt_to_open(user_input)
   row = user_input[1]
   col = user_input[2]
   radius = user_input[3]
   process_file(input_file,output_file,row,col,radius)
   
#Takes file string lines and returns a pixel   
def process_file(input_file,output_file,row,col,radius):
   x_counter = 0
   y_counter = 0
   header_counter = 0
   incomplete_pixel = []
   for line in input_file:
      if header_counter != 3:
         header_counter += 1
      else:
         list_of_lists_of_pixel_values = groups.groups_of_3(line.split())
     
         for pixel in list_of_lists_of_pixel_values:
            x = x_counter
            y = y_counter   
            try:
               incomplete_pixel.extend(pixel)                  
               print_pixel(x,y,row,col,radius,incomplete_pixel,output_file)
               incomplete_pixel = []
               x_counter += 1
               if x_counter == 493:
                  x_counter = 0
                  y_counter += 1
               if y_counter == 401:
                  y_counter = 0
            except:
               pass           
   input_file.close()
   output_file.close()

#Writes the pixel
def print_pixel(x,y,row,col,radius,incomplete_pixel,output_file):
   scale = scale_fade(x,y,row,col,radius)
   if scale < 0.2:
      scale = 0.2
   red = float(incomplete_pixel[0]) * scale
   blue = float(incomplete_pixel[1]) * scale
   green = float(incomplete_pixel[2]) * scale
   new_pixel = int(too_high(red)),int(too_high(blue)),int(too_high(green)),'\n'                    
   output_pixel= ' '.join(map(str, new_pixel))
   output_file.write(output_pixel)

#Checks if pixel is over 255   
def too_high(num):
   if num > 255:
      return 255
   else:
      return num

#Takes commandline and returns a list of user_input
def commandline(argv):
   new_list = []
   for a,b in enumerate(argv):
      the_file = argv[1]
      new_list.append(the_file)
      row = argv[2]
      new_list.append(row)
      new_list.append(argv[3])
      new_list.append(argv[4])
   return new_list

#Returns the scale to be multiplied against the pixel value         
def scale_fade(x,y,row,col,radius):
   scale = ((int(radius) - distance(x,y,row,col))/int(radius))
   return scale

def attempt_to_open(user_input):
   try:
      o = open(user_input[0],'rb')
      return o
   except:
      print "error: missing or unusable file"
      sys.exit()

#Returns distance between choosen fade point and pixel   
def distance(x,y,row,col):
   distance = math.sqrt(((x - int(row))**2) + ((y - int(col))**2))
   return distance


if __name__ == '__main__':
   main(sys.argv)
