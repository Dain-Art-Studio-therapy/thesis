import sys

def main(argv):
   try:
      input = open(argv[1], 'r')
   except:
      print 'failed to open file'
      sys.exit()
   myFile = open('hidden.ppm', 'w')
   waste = 0
   final = []
   for line in input:
      tem = line.split()
      waste = waste + 1
      if (waste == 2):
         print >> myFile, tem[0], tem[1]
      elif (waste < 4):
         print >> myFile, tem[0]
      else:
         for e in tem:
            final.append(int(e))
   pixels = puzzle_groups_of_3(final)
   for e in pixels:
      reveal = puzzle_reveal(e)
      print >>myFile, reveal[0][0], reveal[0][1], reveal[0][2]


def puzzle_groups_of_3(list):
   if (list == []):
      return None
   new = []
   for e in range(0, len(list)):
      if (list[(3 * e):(3 * e + 3)] != []):
         new.append(list[3 * e : 3 * e + 3])
   return new
 
def puzzle_reveal(list):
   new = []
   red = 0
   for e in range(0, 3):
      if (e == 0):
         red = (list[e]) * 10
         if (red > 255):
            red = 255
   green = red
   blue = red
   new.append([red, green, blue])
   return new


if __name__ == "__main__":
   main(sys.argv)     
