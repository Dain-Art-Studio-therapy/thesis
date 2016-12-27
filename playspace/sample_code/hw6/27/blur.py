import sys
import math

def groups_of_3(list):
   length = len(list)
   ans = []
   point = 0
   odds = length % 3
   cycles = length / 3
   while point < (length - 3):
      ans.append([ list[point], list[point + 1], list[point + 2] ])
      point += 3
   if odds == 0:
      ans.append([list[point], list[point + 1], list[point + 2]])
   if odds == 1:
      ans.append([ list[point] ])
   if odds == 2:
      ans.append([list[point],list[point + 1]])
   return ans

def main(argv):
   temp = sys.stdout
   sys.stdout = open('blurred.ppm','w')
   try:
      blur_factor = int(argv[2])
   except:
      blur_factor = 4

   infile = open(argv[1],"r")
   lines = infile.readlines()
   file_info = lines[0:2]
   file_pixels = lines [3:]
   print file_info[0][:-1]
   print file_info[1][:-1]
   size = file_info[1].split()
   size_width = int(size[0])
   size_height = int(size[1])

   without_n = []
   print 255
   for pixel in file_pixels:
      without_n.append(int(pixel[:-1]))
   grouped = groups_of_3(without_n)
   pixel_index = 0
   area_blur = float(2*blur_factor + 1)
   parts_width = int(math.ceil(size_width / area_blur))
   if_side_width = size_width % area_blur
  
   if if_side_width == 0:
      side_width = area_blur
   else:
      side_width = if_side_width

   parts_height = int(math.ceil(size_height / area_blur))
   if_side_height = size_height % area_blur
 
   if if_side_height == 0:
      side_height = area_blur
   else:
      side_height = if_side_height
   array_avg = []
   for y_section_num in range(parts_height):
      index_in_row = []
      for x_section_num in range(parts_width):
         red_total = 0
         green_total = 0
         blue_total = 0      
         index_in_block = []

         if x_section_num == range(parts_width)[-1] and y_section_num == range(parts_height)[-1]:
            area_block = side_height * side_width
            for y in range(int(side_height)):
               for x in range(int(side_width)):
                  index = int((y_section_num * area_blur * size_width) + (y * size_width) + (x_section_num * area_blur) + x)
                  index_in_block.append(index)
     
         else:
            if x_section_num == range(parts_width)[-1]:
               area_block = area_blur * side_width
               for y in range(int(area_blur)): 
                  for x in range(int(side_width)):
                     index = int((y_section_num * area_blur * size_width) + (y * size_width) + (x_section_num * area_blur) + x)
                     index_in_block.append(index)
             
            else:
               if y_section_num == range(parts_height)[-1]:
                  area_block = area_blur * side_height
                  for y in range(int(side_height)): 
                     for x in range(int(area_blur)):
                        index = int((y_section_num * area_blur * size_width) + (y * size_width) + (x_section_num * area_blur) + x)
                        index_in_block.append(index)
      
               else:                  
                  area_block = area_blur ** 2
                  for y in range(int(area_blur)):            
                     for x in range(int(area_blur)):
                        index = int((y_section_num * area_blur * size_width) + (y * size_width) + (x_section_num * area_blur) + x)
                        index_in_block.append(index)
 
   
    
         for block_index in index_in_block:
            color_pixel = grouped[block_index]
            red_total += color_pixel[0]
            green_total += color_pixel[1]
            blue_total += color_pixel[2]

         red_avg = red_total / area_block
         green_avg = green_total / area_block
         blue_avg = blue_total / area_block
         avg_pixel = [red_avg,green_avg,blue_avg]

         index_in_row.append(avg_pixel)
      array_avg.append(index_in_row)
   for pixel_index in range(len(grouped)):
      y_group = int(pixel_index // (size_width * area_blur))
      x_index = int(pixel_index % size_width)
      x_group = int( x_index // area_blur)
      print int(array_avg[y_group][x_group][0])
      print int(array_avg[y_group][x_group][1])
      print int(array_avg[y_group][x_group][2])
             
   sys.stdout.close()
   sys.stdout = temp


if __name__ == "__main__":
   main(sys.argv)   

