import sys
import groups
import math

#Main
def main(argv):
   output_file = open('hidden.ppm','r+b')
   ppm = "P3\n500 375\n255\n" 
   output_file.write(ppm)
   user_input = commandline(argv)
   input_file = attempt_to_open(user_input)
   process_file(input_file,output_file)
   
#Takes file string lines and returns a pixel   
def process_file(input_file,output_file):
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
            try:
               
               incomplete_pixel.extend(pixel)
               test = incomplete_pixel[2] * 2                  
               print_pixel(incomplete_pixel,output_file)
               incomplete_pixel = []
               x_counter += 1
               if x_counter == 500:
                  x_counter = 0
                  y_counter += 1
               if y_counter == 375:
                  y_counter = 0
            except:
               pass           
   input_file.close()
   output_file.close()

#Writes the pixel
def print_pixel(incomplete_pixel,output_file):
   red = 10 * float(incomplete_pixel[0]) 
   new_pixel = int(too_high(red)),int(too_high(red)),int(too_high(red)),'\n'                    
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
   return new_list



def attempt_to_open(user_input):
   try:
      o = open(user_input[0],'rb')
      return o
   except:
      print "error: missing or unusable file"
      sys.exit()




if __name__ == '__main__':
   main(sys.argv)
