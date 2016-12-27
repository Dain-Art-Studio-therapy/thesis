import sys


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
   sys.stdout = open('hidden.ppm','w')

   infile = open(argv[1],"r")
   lines = infile.readlines()
   file_info = lines[0:2]
   file_pixels = lines [3:]
   print file_info[0][:-1]
   print file_info[1][:-1]

   without_n = []
   for pixel in file_pixels:
      without_n.append(int(pixel[:-1]))
   grouped = groups_of_3(without_n)
   print 255   
   for pixel in grouped:  
      new_value =  pixel[0]*10
      if new_value > 255:
         true_value = 255
      else:
         true_value = new_value
      print true_value
      print true_value 
      print true_value
  
   sys.stdout.close()
   sys.stdout = temp


if __name__ == "__main__":
   main(sys.argv)   

