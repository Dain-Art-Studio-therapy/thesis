import sys

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
   except:
      print 'no input image'
      sys.exit()
   try:
      blur = int(argv[2])
   except:
      blur = 4
   with open('blurred.ppm', 'w+')as out_pic:
      with open(in_file, 'rb')as in_pic:

         big_ass_list = in_pic.readlines()

         w_h = big_ass_list[1].split()
         width = int(w_h[0])
         height = int(w_h[1])

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
               accept_x = range(-blur, blur)
               accept_y = range(-blur, blur)

               list_of_neighbors = []
               for near_col in accept_y:
                  for near_row in accept_x:
                     try:
                        list_of_neighbors.append(Pixel((x + near_row), (y + near_row), pixel_matrix[(y + near_col)][(x + near_row)]))
                     except:
                        pass
               r_sum = 0
               g_sum = 0
               b_sum = 0

               for each_pixel in list_of_neighbors:
                  r_sum += each_pixel.color[0]
                  g_sum += each_pixel.color[1]
                  b_sum += each_pixel.color[2]

               length = len(list_of_neighbors)
               out_pic.write(str(r_sum/length)+" "+str(g_sum/length)+" "+str(b_sum/length)+'\n')


if __name__ == '__main__':
   main(sys.argv)