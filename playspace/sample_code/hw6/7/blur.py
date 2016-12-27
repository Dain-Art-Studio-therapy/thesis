import sys
import math

OUTFILE = "blurred.ppm"
INFILE_IDX = 1
BLUR_IDX = 2

def cmd_processing(argv):
   if not(2 <= len(argv) <= 3):
      print "Arguments not properly formatted"
      print "> blur.py <filename> [blur]"
   else:
      try:
         if len(argv) == 3:
            ls = [argv[INFILE_IDX],int(argv[BLUR_IDX])]
         else:
            ls = [argv[INFILE_IDX],4]
      except ValueError as e:
         print >> stderror, e
         sys.exit(1)
      return ls

def main(argv):
   input_filename,blur_factor = cmd_processing(argv)
   output_filename = OUTFILE
   i_d = image_to_list(input_filename) #input_data
   width,height,color_max,pixels = i_d[1],i_d[2],i_d[3],i_d[4:] 
   pixels = group_pixels(pixels,3) #Join together colors for pixels
   pixels = group_pixels(pixels,int(width)) #Make grid of pixels ls[y][x]
   processed_pixels = process_pixels(pixels,color_max,blur_factor,width,height)
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

def process_pixels(pixels,max,blur,w,h):
   output_pixels = [] 
   for i in range(len(pixels)):
      row = []
      for j in range(len(pixels[i])):
         sub_pixels = sub_divide(pixels,blur,i,j)
         row.append(process_pixel(sub_pixels,max))
      output_pixels.append(row)
   return output_pixels #return image set of pixels

def sub_divide(pixels,dist,row_pos,col_pos):
   width = len(pixels[0]) #find width
   height = len(pixels)   #find height
   left_limit = bigger_of_2(col_pos - dist,0) 
   right_limit = smaller_of_2(col_pos + dist, width-1)
   upper_limit = bigger_of_2(row_pos - dist, 0)
   lower_limit = smaller_of_2(row_pos + dist, height-1)
   sub_pixels = pixels[upper_limit : lower_limit+1] 
   for i in range(len(sub_pixels)):
      sub_pixels[i] = sub_pixels[i][left_limit : right_limit+1] 
   return sub_pixels 

def process_pixel(sub_pixels,max):
   #Pixel should be in this format ['r','g','b']
   r_total = 0 
   g_total = 0
   b_total = 0 
   num = 0 
   try:
      for i in range(len(sub_pixels)): 
         for j in range(len(sub_pixels[i])): 
            r_total += int(sub_pixels[i][j][0])
            g_total += int(sub_pixels[i][j][1]) 
            b_total += int(sub_pixels[i][j][2])
            num += 1
   except ValueError as e:
      print >> stderror, e
      sys.exit(1)
   new_pixel = [str(smaller_of_2(int(r_total/num),max)), 
                str(smaller_of_2(int(g_total/num),max)), 
                str(smaller_of_2(int(b_total/num),max))]
   return new_pixel 

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
