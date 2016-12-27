import sys
import math

def main(args):
   #arguments = [file_name, row, col, radius]
   arguments = get_arguments(args)

   input = open_file(args, 'r')
   output = open_file(["","faded.ppm"], 'w')

   output.write(input.readline())
   view = input.readline()
   output.write(view)
   output.write(input.readline())

   #view = [width, height]
   view = view.split()
   view = [float(view[0]), float(view[1])]   

   read_input_to_output(view, arguments, input, output)

def read_input_to_output(view, arguments, input, output):
   wCount = 0
   hCount = 0
   count = 0
   threes = []
   for line in input:
      line = line.split()
      for x in line:
         if count < 3:
            count += 1
            threes.append(float(x))
         else:
            print_color(threes, wCount, hCount, arguments, output)
            threes = [float(x)]
            count = 1
            if (wCount >= view[0]):
               wCount = 1
               hCount += 1
            else:
               wCount+= 1

      
def get_arguments(args):
   arguments = []
   try: 
      arguments.append(args[0])
      arguments.append(args[1])
      arguments.append(args[2])
      arguments.append(args[3])
      arguments.append(args[4])
   except: 
      print "Wrong number of arguments"
   return arguments

def open_file(args, r):
   try:
      return open(args[1], r)
   except:
      print "ERROR-- Did not include argument"
      return None

def print_color(threes, wCount, hCount, arguments, output):
   scale = get_scale(wCount, hCount, arguments)
   if scale < .2: 
      scale = .2
   
   r = threes[0] * scale
   g = threes[1] * scale
   b = threes[2] * scale

   output.write("%d %d %d \n" % (r,g,b))

def get_scale(wCount, hCount, arguments):
   distance = math.sqrt((wCount - float(arguments[3]))**2 + (hCount - float(arguments[2]))**2)
   scale = (float(arguments[4]) - distance) / float(arguments[4])
   return scale

if __name__ == "__main__":
   main(sys.argv)
