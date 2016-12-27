import sys 

def main(args):
   #arguments = [input_file, neighbor reach (optional)] 
   arguments = get_arguments(args)
    
   input = open_file(args, 'r')
   output = open_file(["","blurred.ppm"], 'w')

   header = input.readline()
   output.write(header)
   view = input.readline()
   output.write(view)
   output.write(input.readline())

   #view = [width, height]
   view = view.split()
   view = [float(view[0]), float(view[1])]
   pixel_array = read_input(view, arguments, input, output)
   to_output(pixel_array, output, arguments)
         
def to_output(pixel_array, output, arguments):
   height = len(pixel_array)
   width = len(pixel_array[0])
   for i in range(len(pixel_array)):
      for j in range(len(pixel_array[i])):
         reach_array = get_reach_array(pixel_array, j, i, int(arguments[2]))
         r_g_b_averages = get_r_g_b_averages(reach_array)
         print_to_output(r_g_b_averages,output,input)
         #output.write("%d %d %d \n" % (pixel_array[i][j][0],pixel_array[i][j][1],pixel_array[i][j][2]))
     
def print_to_output(averages,output, input):
   output.write("%d %d %d \n" % (averages[0], averages[1], averages[2]))

def get_r_g_b_averages(reach_array):
   r = 0
   b = 0
   g = 0
   width = len(reach_array[0])
   height = len(reach_array)
   total = width * height
   for i in range(height):
      for j in range(len(reach_array[i])):
         r += reach_array[i][j][0]   
         g += reach_array[i][j][1]
         b += reach_array[i][j][2]
   
   if not total == 0:
      r = int(r / total)
      g = int(g / total)
      b = int(b / total)
   else: 
      r = 0
      g = 0 
      b = 0
   return [r,g,b]

def get_reach_array(pixel_array, x,y, reach):
   width = len(pixel_array[y])
   height = len(pixel_array)
   leftX = max(x - reach, 0)
   rightX = min(x + reach, width)
   bottomY = max(y - reach, 0)
   topY = min(y + reach, height)
   
   result = [[]]
   w = leftX 
   h = 0
   for i in range(bottomY, topY):
      for j in range(leftX, rightX): 
         if w >= rightX:
            w = leftX
            h += 1
            result.append([pixel_array[i][j]])
         else: 
            w += 1
            pix = pixel_array[i][j]
            result[h].append(pix)
   return result    
 
def read_input(view, arguments, input, output):
   wCount = 0
   hCount = 0
   count = 0
   threes = []
   result = [[]]
   for line in input:
      line = line.split()
      for x in line:
         if count < 3:
            count += 1
            threes.append(float(x))
         else:
            count = 1
            if (wCount >= view[0] and hCount < view[1]):
               wCount = 1
               hCount += 1
               result.append([])
               result[hCount].append(threes)
               threes = [float(x)]
            else:
               wCount+= 1
               result[hCount].append(threes)
               threes = [float(x)]  
   result[hCount].append(threes)
   return result 

def get_arguments(args):
   arguments = []
   try:
      if (len(args) == 3):
         arguments.append(args[0])
         arguments.append(args[1])
         arguments.append(args[2])
      else: 
         arguments.append(args[0])
         arguments.append(args[1])
         arguments.append(4)
   except:
      print "Wrong number of arguments"
   return arguments

def open_file(args, r):
   try:
      return open(args[1], r)
   except:
      print "ERROR-- Did not include argument"
      return None

if __name__ == "__main__":
   main(sys.argv)
