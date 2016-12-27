#Core Functionality of Processing ppm image file
import sys
import puzzle_commandline
import groups
import puzzle_data

def make_list(file):
   list = []
   for line in file:
      components = line.split()
      for i in range(len(components)):
         list.append(components[i])
   return list

def obtain_colors(list):
   fin_list = groups.groups_of_3(list)
   return fin_list

def final_colors(list):
   for i in range(len(list)):
      red = int(list[i][0]) * 10
      list[i][0] = red
      list[i][1] = red
      list[i][2] = red
   return list

def print_colors(list, file):
   for i in range(len(list)):
      file.write("%d %d %d " % (min(list[i][0], 255), min(list[i][1], 255), 
         min(list[i][2], 255)))

def get_width_height(list):
   variable = []
   for i in range(4):
      variable.append(list[0])
      list.remove(list[0])
   return variable

def main(argv):
   if len(argv) == 2:
      color = []
      with puzzle_commandline.open_file(argv[1], 'rb') as f:
         fin_list = make_list(f)
         variables = get_width_height(fin_list)
         colors = obtain_colors(fin_list)
      with puzzle_commandline.open_file("hidden.ppm", 'wb') as f:
         f.write("%s\n%d %d\n%d\n" %(variables[0], int(variables[1]),
            int(variables[2]), int(variables[3])))
         print_colors(final_colors(colors), f)
         
   else:
      print >> sys.stderr, "Does not have two arguments"
      exit(1)

if __name__ == '__main__':
   main(sys.argv)





