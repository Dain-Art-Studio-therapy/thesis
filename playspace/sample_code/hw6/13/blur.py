import sys
import blur_commandline
import groups

def make_list(file):
   list = []
   for line in file:
      nums = line.split()
      for i in range(len(nums)):
         list.append(nums[i])
   return list

def find_p_width_height_c(list):
   variables = []
   for i in range(4):
      variables.append(list[0])
      list.remove(list[0])
   return variables

def make_grid(list, width):
   grid = []
   row = []
   for i in range(len(list)):
      if (i + 1)%width != 0:
         row.append(list[i])
      else:
         row.append(list[i])
         grid.append(row)
         row = []

   return grid

def calculate_new_color(pixels):
   red_sum = 0
   green_sum = 0
   blue_sum = 0
   for i in range(len(pixels)):
      red_sum += int(pixels[i][0])
      green_sum += int(pixels[i][1])
      blue_sum += int(pixels[i][2])
   red = red_sum/len(pixels)
   green = green_sum/len(pixels)
   blue = blue_sum/len(pixels)
   pixel = [red, green, blue]
   return pixel
   
def blur(grid, blur_factor):
   fin_grid = []
   list = []
   for i in range(len(grid)):
      for j in range(len(grid[i])):
         for k in range(-blur_factor, blur_factor + 1):
            if (i + k) >= 0 and (i + k) < len(grid):
               for l in range(-blur_factor, blur_factor + 1):
                  if (j + l) >= 0 and (j + l) < len(grid[i + k]):
                     list.append(grid[i + k][j + l])
                  else:
                     pass
            else:
               pass
         fin_grid.append(calculate_new_color(list))
         list = []
   fin_list = grid_to_list(fin_grid)
   return fin_list
   
def grid_to_list(grid):
   list = []
   for i in range(len(grid)):
      list.append(grid[i])
   return list

def printing(list, file):
   for i in range(len(list)):
      file.write("%d %d %d " % (int(list[i][0]), int(list[i][1]), int(list[i][2])))
   
def main(argv):
   if len(argv) >= 2:
      if len(argv) == 3:
         blur_factor = int(argv[2])
      else:
         blur_factor = 4
      with blur_commandline.open_file(argv[1], 'rb') as f:
         fin_list = make_list(f)
      variables = find_p_width_height_c(fin_list)
      fin_list = groups.groups_of_3(fin_list)
      grid = make_grid(fin_list, int(variables[1]))
      fin_list = blur(grid, blur_factor)
      
      with blur_commandline.open_file("blurred.ppm", 'wb') as f:
         f.write("%s\n%d %d\n%d\n" %(variables[0], int(variables[1]),
            int(variables[2]), int(variables[3])))
         printing(fin_list, f)

   else:
      print >> sys.stderr, "Does not have at least 2 arguments"


if __name__ == '__main__':
   main(sys.argv)
