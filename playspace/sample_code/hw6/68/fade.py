import sys
import math

class Pixel:
   def __init__(self, x, y, color):
      self.x = x
      self.y = y
      self.color = color

def groups_of_certain(list, length):
   list_of_groups = []

   for index in range(len(list)/length +1):
      group = list[(index * length):((index + 1) * length)]
      if group != []:
         list_of_groups.append(group)
   return list_of_groups


def main(argv):
   try:
      in_file = argv[1]
      open(in_file)
   except:
      print 'no input image'
      sys.exit()
   try:
      row = int(argv[2])
      col = int(argv[3])
   except:
      print 'row and column not valid'
      sys.exit() 

   try:
      radius = int(argv[4])
   except:
      print 'radius not valid'
      sys.exit()
   with open('faded.ppm', 'w+')as out_pic:
      with open(in_file, 'r')as in_pic:

         big_ass_list = in_pic.readlines()

         #print big_ass_list[1]
         width_and_height = big_ass_list[1].split()
         #print width_and_height
         width = int(width_and_height[0])
         height = int(width_and_height[1])
         #print big_ass_list[3:]

         out_pic.write('P3''\n')
         out_pic.write(str(width)+" "+str(height)+'\n')
         out_pic.write('255''\n')

         just_numbers = []
         for line in big_ass_list[3:]:
            just_numbers.append(int(line))
         in_three_tuples = groups_of_certain(just_numbers, 3)


         pixel_matrix = (groups_of_certain(in_three_tuples, width))
         for y in range(height):
            for x in range(width):
               pixel = Pixel(x, y, pixel_matrix[y][x])
               #print pixel.x, pixel.y

               a = pixel.x - col
               b = pixel.y - row
               distance = math.sqrt((float(a)**2) + (float(b)**2))
               #print distance

               raw_scalar = (((radius) - distance) / (radius))
               if raw_scalar <= 0.2:
                  out_pic.write(str(int(pixel.color[0] * .2))+" "+str(int(pixel.color[1] * .2))+" "+str(int(pixel.color[1] * .2))+'\n')
               else:
                  out_pic.write(str(int(pixel.color[0] * raw_scalar))+" "+str(int(pixel.color[1] * raw_scalar))+" "+str(int(pixel.color[1] * raw_scalar))+'\n')


if __name__ == '__main__':
   main(sys.argv)