import sys
import math

OUTFILE = "faded.ppm"
INFILE_IDX = 1
ROW_IDX = 2
COL_IDX = 3
RAD_IDX = 4

def cmd_processing(argv):
   if len(argv) != 5:
      print "Arguments not properly formatted"
      print "> fade.py <filename> <row> <column> <radius>"
   else:
      try:
         ls = [argv[INFILE_IDX],int(argv[ROW_IDX]),
               int(argv[COL_IDX]),int(argv[RAD_IDX])]
      except ValueError as e:
         print >> stderror, e
         sys.exit(1)
      return ls

def main(argv):
   input_filename,row,col,radius = cmd_processing(argv)
   output_filename = OUTFILE
   i_d = image_to_list(input_filename) #input_data
   width,height,color_max,pixels = i_d[1],i_d[2],i_d[3],i_d[4:] 
   pixels = group_pixels(pixels,3) #Join together colors for pixels
   pixels = group_pixels(pixels,int(width)) #Make grid of pixels
   processed_pixels = process_pixels(pixels,color_max,row,col,radius)
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

def group_pixels(nums,size):
   ls = []
   for i in range(len(nums)):
      if i%size == 0:
         ls.append([nums[i]])
      else:
         ls[i/size].append(nums[i])
   return ls

def process_pixels(ls,max,row,col,radius):
   output_pixels = ls
   for i in range(len(ls)):
      for j in range(len(ls[i])):
         output_pixels[i][j] = process_pixel(ls[i][j],max,i,j,row,col,radius)
   return output_pixels

def process_pixel(pixel,max,row_pos,col_pos,fade_row,fade_col,radius):
   #Pixel should be in this format ['r','g','b']
   new_pixel = pixel 
   try:
      d = distance(row_pos,col_pos,fade_row,fade_col)
      scalar = bigger_of_2((radius-d)/radius,0.2)
      for i in range(len(pixel)):
         new_pixel[i] = str(int(smaller_of_2(int(pixel[i])*scalar,int(max)))) 
      #Convert 'r/g/b' to int, *s, take min of that and color_max
      #and then convert back to string
   except ValueError as e:
      print >> stderror, e
      sys.exit(1)
   return new_pixel

def distance(i,j,x,y):
   return math.sqrt((i-x)**2 + (j-y)**2)

def smaller_of_2(value,max):
   if value > max:
      return max
   else:
      return value

def bigger_of_2(value,min):
   if value < min:
      return min
   else:
      return value

def write_image(filename,pixels,width,height,max):
   with open(filename, 'wb') as f:
      f.write('{0}\n'.format('P3'))
      f.write('{0} {1}\n'.format(width,height))
      f.write('{0}\n'.format(max))
      for i in range(len(pixels)):
         for j in range(len(pixels[i])):
            for k in range(len(pixels[i][j])):
               f.write('{0} '.format(pixels[i][j][k]))
   return None



if __name__ == '__main__':
   main(sys.argv)
