import sys

def main(args):
   image_file = open_file(args, 'r')
   output = open_file(["","hidden.ppm"], 'w')
  
   colors = []

   count = 0
   output.write(image_file.readline())
   output.write(image_file.readline())
   output.write(image_file.readline())

   for line in image_file:
      line = line.split()
      for x in line:
         if count % 3 == 0: 
            print_color(output, x)
         count += 1 

def open_file(args, r):      
   try:
      file = open(args[1], r)
   except:
      print "ERROR-- Did not include argument"
   return file

def print_color(output, x):
   r_value = float(x) * 10
   output.write("%d %d %d \n" % (r_value,r_value,r_value))

if __name__ == "__main__":
   main(sys.argv)
