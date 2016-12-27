import sys
import math

def distance(f_x,t_x,f_y,t_y):
   dif_x = f_x - t_x
   dif_y = f_y - t_y
   sum = dif_x ** 2 + dif_y ** 2
   return math.sqrt(sum)

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
   sys.stdout = open('faded.ppm','w')

   infile = open(argv[1],"r")
   row = int(argv[2])
   col = int(argv[3])
   radius = int(argv[4])
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
   for pixel in grouped:        
      pixel_row = int(pixel_index / size_width) + 1
      pixel_column = pixel_index % size_width + 1
      dist = distance(pixel_column,col,pixel_row,row)
      scale = (radius - dist) / radius      
      if scale < .2:
         true_scale = .2
      else:
         true_scale = scale
      print int(pixel[0] * true_scale)
      print int(pixel[1] * true_scale)
      print int(pixel[2] * true_scale)
      pixel_index += 1

   sys.stdout.close()
   sys.stdout = temp


if __name__ == "__main__":
   main(sys.argv)   

