import sys
import math

RED = 0
GREEN = 1
BLUE = 2



#In process_file, you want to read the heading, write it to the output file, process the pixels by groups of three. 
def process_file(input_file, output_file):
   file_list = input_file.readlines()
   new_file_list = []
   for e in file_list:
      new = e.strip('\n')
      new_file_list.append(new)
   header = new_file_list[:3]
   print >> output_file, header[0]
   print >> output_file, header[1]
   print >> output_file, header[2]
   pixel_list = groups_of_3(file_list[3:len(file_list)+1])
   for pixel in pixel_list:
      new_pixel = process_pixel(pixel)
      print >> output_file, new_pixel[0], new_pixel[1], new_pixel[2]

def string_to_pixel_list(line_string, extras):
   line_list = line_string.split()
   for i in range(len(extras)):
      line_list.insert(i, extras[i])
   pixel_list = groups.groups_of_3(line_list)
   return pixel_list

def open_file(argv, mode):
   try:
      f = open(argv, mode)
      return f
   except:
   	  print >> sys.stderr, "Cannot open file provided."
   	  exit(1)

def process_pixel(pixel): 
   red = min(int(pixel[RED])*10, 255)
   green = red
   blue = red
   processed_pixel = [red, green, blue]
   return processed_pixel

def groups_of_3(list):
    return_list = []
    for i in range(int(math.ceil(len(list)/3.0))):       
        if len(list) <= (3*i+1):
            subgroup = [list[3*i]]
        elif len(list) <= (3*i+2):
            subgroup = [list[3*i], list[3*i+1]]
        else:
            subgroup =[list[3*i], list[3*i+1], list[3*i+2]] 
        return_list.append(subgroup)
    return return_list

def main():
   input_file = open_file(sys.argv[1], 'rb')
   output_file = open_file('hidden.ppm', 'w')
   process_file(input_file, output_file)   
   input_file.close()
   output_file.close()
if __name__ ==  '__main__':
   main()


