#Contains implementations of command-line processing functions
import sys
import ray_caster
import data

def open_file(name, mode):
   
   try:
      return open(name, mode)
   
   except IOError as e:
      print >> sys.stderr, '{0}: {1}'.format(name, e.strerror)
      exit(1)
   
def set_components(index, list, variable_list):
   flag_list = ["-eye", "-view", "-light", "-ambient"]
   if list[index] == "-eye":
      for j in range(index, len(list)):
         if list[j] not in flag_list:
            if j == index + 1:
               variable_list[0].x = float(list[j])
            elif j == index + 2:
               variable_list[0].y = float(list[j])
            elif j == index + 3:
               variable[0].z = float(list[j])
   elif list[index] == "-view":
      for j in range(index, len(list)):
         if list[j] not in flag_list:
            if j == index + 1:
               variable_list[1] = float(list[j])
            elif j == index + 2:
               variable_list[2]= float(list[j])
            elif j == index + 3:
               variable_list[3] = float(list[j])
            elif j == index + 4:
               variable_list[4] = float(list[j])
            elif j == index + 5:
               variable_list[5] = float(list[j])
            elif j == index + 6:
               variable_list[6] = float(list[j])
   elif list[index] == "-light":
      for j in range(index, len(list)):
         if list[j] not in flag_list:
            if j == index + 1:
               variable_list[7].pt.x = float(list[j])
            elif j == index + 2:
               variable_list[7].pt.y = float(list[j])
            elif j == index + 3:
               variable_list[7].pt.z = float(list[j])
            elif j == index + 4:
               variable_list[7].color.r = float(list[j])
            elif j == index + 5:
               variable_list[7].color.g = float(list[j])
            elif j == index + 6:
               variable_list[7].color.b = float(list[j])
   elif list[index] == "-ambient":
      for j in range(len(list)):
         if list[j] not in flag_list:
            if j == index + 1:
               variable_list[8].r = float(list[j])
            elif j == index + 2:
               variable_list[8].g = float(list[j])
            elif j == index + 3:
               variable_list[8].b = float(list[j])
   
if __name__ == '__main__':
   main(sys.argv)
