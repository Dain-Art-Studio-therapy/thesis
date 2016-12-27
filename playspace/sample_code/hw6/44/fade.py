import sys
import math
import point

def main():

   try:
      input = open(sys.argv[1], 'r')
   except:
      print "usage: python fade.py <filename> <row> <col> <radius>"
      exit()

   process_fade()
   
def groups_of_3(list):

   # Groups pixel values
   n = 0
   new_list = []

   while n < len(list):
      new_list.append(list[n:n+3])
      n += 3
   return new_list

def distance(p1, p2):

   # Calculates distance between two points
   distance = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
   return distance

def process_fade():

   output = open("faded.ppm", 'w')
   input = open(sys.argv[1], 'r')
   
   header_line = 0
   pix_list = []

   # Regroups pixel values
   for line in input:
      if header_line < 3:
         output.write(line,) 

         # Gets height/width and assigns to variables
         if header_line == 1:
            h_w = line.split()
            img_width = int(h_w[0])    
            img_height = int(h_w[1])          

         header_line += 1

      else:
         all_lines = line.split()
         for values in all_lines: 
            pix_list.append(values)

   grouped_values = groups_of_3(pix_list)

   # Converts each pixel
   width = -1
   height = 0
   radius = float(sys.argv[4])
   for pixel in grouped_values:
      if width < img_width:
         width += 1
      if width == img_width:
         height +=1
         width = 0
      pixel_point = point.Point(width, height)

      specified_point = point.Point(float(sys.argv[3]), 
                                    float(sys.argv[2]))
      pixel_dist = float(distance(specified_point, pixel_point))
      pixel_scale = float(radius - pixel_dist)/radius
 
      if pixel_scale < 0.2:
         pixel_scale = 0.2

      r = int(pixel[0]) * pixel_scale
      g = int(pixel[1]) * pixel_scale
      b = int(pixel[2]) * pixel_scale

      output.write(str(int(r)) + ' ' +
                   str(int(g)) + ' ' +
                   str(int(b)) + '\n') 
  
  
if __name__ == "__main__":
   main()
           
