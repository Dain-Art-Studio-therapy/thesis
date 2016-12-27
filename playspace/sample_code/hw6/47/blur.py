import sys
import groups
import math

#Main
def main(argv):
   output_file = open('blurred.ppm','r+b')
   ppm = "P3\n493 401\n255\n" 
   output_file.write(ppm)
   user_input = commandline(argv)
   input_file = attempt_to_open(user_input)
   neighbor_reach = int(user_input[1])

   pixel_list = process_file(input_file,output_file,neighbor_reach)
   print_pixel(output_file,pixel_list,neighbor_reach)
   input_file.close()
   output_file.close()
   
#Takes file string lines and returns a pixel_list with x,y coordinates   
def process_file(input_file,output_file,neighbor_reach):

   header_counter = 0
   incomplete_pixel = []
   pixel_list = []
   for line in input_file:
      if header_counter != 3:
         header_counter += 1
      else:
         list_of_lists_of_pixel_values = groups.groups_of_3(line.split())
       
         for pixel in list_of_lists_of_pixel_values:
   
            try:

               incomplete_pixel.extend(pixel)
          
               test = incomplete_pixel[2] * 2
                               
               pixel_list.append(incomplete_pixel)                  
                          
               incomplete_pixel = []
               
            except:
               pass 
   return pixel_list          
   
#Writes the pixel
def print_pixel(output_file,pixel_list,neighbor_reach):

   for pixel in range(0,len(pixel_list)):
      
      average_red = 0
      average_blue = 0
      average_green = 0
      for i in range((-1 * neighbor_reach),neighbor_reach + 1):
         for j in range((-1 * neighbor_reach),neighbor_reach + 1):
            try:
               average_red += int(pixel_list[pixel+(j*493)+i][0])   
               average_blue += int(pixel_list[pixel+(j*493)+i][1]) 
               average_green += int(pixel_list[pixel+(j*493)+i][2]) 
            except:
               pass
      
      final_red = average_red/(((2* neighbor_reach) + 1) * ((2* neighbor_reach) + 1))
    
      final_blue = average_blue/(((2* neighbor_reach) + 1) * ((2* neighbor_reach) + 1))
      final_green = average_green/(((2* neighbor_reach) + 1) * ((2* neighbor_reach) + 1))  
      new_pixel = int(too_high(final_red)),int(too_high(final_blue)),int(too_high(final_green)),'\n'                    
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
      new_list.append(argv[2])
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
