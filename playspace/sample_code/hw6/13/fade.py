#Contains Main Function
import sys
import fade_commandline
import groups
import math

def make_list(file):
   fin_list = []
   last_list = []
   with fade_commandline.open_file(file, 'rb') as f:
      for line in f:
         list = line.split()
         for i in range(len(list)):
            fin_list.append(list[i])
   last_list.append([fin_list[0], fin_list[1], fin_list[2], fin_list[3]])
   for j in range(4):
      fin_list.remove(fin_list[0])
   last_list += groups.groups_of_3(fin_list)
   return last_list

def trial_print(list, row, col, radius, width, f):
   a_list = list
   for i in range(0, len(a_list)):
      if i == 0:
         pass
      else:
         distance = math.sqrt((col - ((i - 1)%width))**2 + (row -
            ((i - 1)/width))**2)
         scale = (radius - distance)/radius
         if scale < 0.2:
            scale = 0.2
         f.write("%d " %(int(int(a_list[i][0]) * scale)))
         f.write("%d " %(int(int(a_list[i][1]) * scale)))
         f.write("%d " %(int(int(a_list[i][2]) * scale)))

def main(argv):
   if len(argv) == 5:
      variables = fade_commandline.set_pos_rad(argv)
      list = make_list(argv[1])
      p_width_height = fade_commandline.set_width_height(list)
      
      with fade_commandline.open_file("faded.ppm", 'wb') as f:
         f.write("%s\n%d %d\n255\n" % (p_width_height[0], int(p_width_height[1]
            ), int(p_width_height[2])))
         trial_print(list, int(variables[0]), int(variables[1])
            , float(variables[2]), int(p_width_height[1]), f)

   else:
      print >> sys.stderr, "Does not have five arguments"
      exit(1)


if __name__ == '__main__':
   main(sys.argv)

