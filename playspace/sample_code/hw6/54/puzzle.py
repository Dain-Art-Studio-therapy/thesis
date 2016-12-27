# contains the main function
#    - takes in input file as only argument
import sys

def main(argv):
   try:
      with open(argv[1], 'rb') as f:
         pixel_list = file_to_list(f)
         color_lists = list_to_colors(pixel_list)
         solution = solve_puzzle(color_lists)
         output_file(argv, solution)
   except:
      print >> sys.stderr, "Valid file was not provided"


def find_dim(argv):
   try:
      with open(argv[1], 'rb') as f:
         line = f.readlines()[1]
         nums = line.split()
         dimensions = []
         for e in nums:
            dimensions.append(int(e))
         return dimensions
   except:
      print >> sys.stderr, "Valid file was not provided"


def file_to_list(f):
   pixel_list = []
   counter = 0
   f.next()
   f.next()
   f.next()
   for line in f:
      counter += 1
      nums = line.split()
      try:
         for e in nums:
            pixel_list.append(int(e))
      except:
         print >> sys.stderr, "Invalid integer on line {0}".format(counter)
   return pixel_list



def list_to_colors(pixels):
   color_lists = []
   for i in range(0, len(pixels), 3):
      if i + 2 < len(pixels):
         color_lists.append([pixels[i], pixels[i+1], pixels[i+2]])     
   return color_lists
      

def solve_puzzle(color_lists):
   solution = []
   for [r, g, b] in color_lists:
      new_red = min(r * 10, 255)
      green = new_red
      blue = new_red
      solution.append([new_red, green, blue])
   return solution

def output_file(argv, solution):
   dimensions = find_dim(argv)
   width = dimensions[0]
   length = dimensions[1]
   with open('hidden.ppm', 'wb') as f:
      print >> f, 'P3'
      print >> f, width, length
      print >> f, 255
      for [r, g, b] in solution:
         print >> f, r, g, b
        

if __name__ == '__main__':
   main(sys.argv)
      
