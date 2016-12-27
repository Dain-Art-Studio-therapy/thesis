import sys

OUTFILE = "hidden.ppm"
INFILE_IDX = 1

def cmd_processing(argv):
   if len(argv) != 2:
      print "Arguments not properly formatted"
      print "> puzzle.py <filename>"
   else:
      return argv[INFILE_IDX]

def main(argv):
   input_filename = cmd_processing(argv)
   output_filename = OUTFILE
   i_d = image_to_list(input_filename) #input_data
   width,height,color_max,pixels = i_d[1],i_d[2],i_d[3],i_d[4:] 
   pixels = group_pixels(pixels)
   processed_pixels = process_pixels(pixels,color_max)
   write_image(output_filename,processed_pixels,width,height,color_max)

def image_to_list(filename):
   try:
      ls = []
      with open(filename,'rb') as f:
         ls = f.read().split()
      return ls
   except IOError as e:
      print >> stderror, e
      sys.exit(1)

def group_pixels(nums):
   ls = []
   for i in range(len(nums)):
      if i%3 == 0:
         ls.append([nums[i]])
      else:
         ls[i/3].append(nums[i])
   return ls

def process_pixels(ls,max):
   output_pixels = ls
   for i in range(len(ls)):
      output_pixels[i] = process_pixel(ls[i],max)
   return output_pixels

def process_pixel(pixel,max):
   #Pixel should be in this format ['r','g','b']
   try:
      red = str(min_int(int(pixel[0])*10,int(max))) 
      #Convert 'r' to int, *10, take min of that and color_max
      #and then convert back to string
   except ValueError as e:
      print >> stderror, e
      sys.exit(1)
   return [red, red, red]

def min_int(value,max):
   if value > max:
      return max
   else:
      return value

def write_image(filename,pixels,width,height,max):
   with open(filename, 'wb') as f:
      f.write('{0}\n'.format('P3'))
      f.write('{0} {1}\n'.format(width,height))
      f.write('{0}\n'.format(max))
      for i in range(len(pixels)):
         for j in range(len(pixels[i])):
            f.write('{0} '.format(pixels[i][j]))
   return None



if __name__ == '__main__':
   main(sys.argv)
