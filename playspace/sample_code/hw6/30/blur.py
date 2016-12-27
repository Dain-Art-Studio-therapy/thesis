import sys
import math

def open_infile(f):
   try:
      return open(f,'rb')
   except:
      print ('File cannot be opened.\nuasge: python blur.py <filename>' +
             ' [optional: blur factor]')
      exit(1)

def groups_of_3(list):
   new_list = []
   for i in range(0,len(list),3):
      new_list.append(list[i:i+3])
   return new_list

def write_header(input_file,outfile):
   infile = open_infile(input_file)
   header = [next(infile) for x in xrange(3)]
   for line in header:
      outfile.write(line + '\n')
   infile.close()

def get_height_width(input_file):
   infile = open_infile(input_file)
   for i, line in enumerate(infile):
      if i == 1:
         split = line.split()
         return (int(split[0]),int(split[1]))
      elif i > 1:
         break
   infile.close()

def get_distance(pos1,pos2):
   distance = math.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2)
   return distance

def get_scale_val(radius,pos1,pos2):
   distance = get_distance(pos1,pos2)
   scale = (radius - distance)/radius
   return max(scale,0.2)

def get_row_col(idx,width):
   row = idx / width
   col = idx % width
   return (row,col)

def get_index(row,col,width):
   idx = row*width + col
   return idx

def get_upleft_corner(pos,blur_factor):
   def corner_check(idx):      
      if pos[idx] - blur_factor >= 0:
         return pos[idx] - blur_factor
      else:
         return 0
   row = corner_check(0)
   col = corner_check(1)
   return (row,col)

def get_downright_corner(pos,blur_factor,width,height):
   def corner_check(idx,w_or_h):
      if pos[idx] + blur_factor <= w_or_h - 1:
         return pos[idx] + blur_factor
      else:
         return w_or_h - 1
   row = corner_check(0,height)
   col = corner_check(1,width)
   return (row,col)

def average_list(l):
   l_sum = 0
   for e in l:
      l_sum += e
   return l_sum / len(l)

def get_comp_averages(upleft,downright,pix_list,width):
   r_list = []
   g_list = []
   b_list = []
   for row in range(upleft[0],downright[0]+1):
      for col in range(upleft[1],downright[1]+1):
         idx = get_index(row,col,width)
         pix = pix_list[idx]
         r_list.append(pix[0])
         g_list.append(pix[1])
         b_list.append(pix[2])
   r = average_list(r_list)
   g = average_list(g_list)
   b = average_list(b_list)
   return [r,g,b] 

def get_input_pixels(input_file):
   pixels = []
   infile = open_infile(input_file)
   for i in xrange(3):
      infile.next()
   for line in infile:
      split = line.split()
      for e in split:
         pixels.append(int(e))
   infile.close()
   return groups_of_3(pixels)

def write_pixels(input_file,outfile,width,height,blur_factor):
   grouped_pixels = get_input_pixels(input_file)
   for i, e in enumerate(grouped_pixels):
      pix_pos = get_row_col(i,width)
      upleft = get_upleft_corner(pix_pos,blur_factor)
      downright = get_downright_corner(pix_pos,blur_factor,
                                       width,height)
      c_av = get_comp_averages(upleft,downright,grouped_pixels,width)
      col = str(c_av[0]) + ' ' + str(c_av[1]) + ' ' + str(c_av[2]) + ' '
      outfile.write(col)

def get_blur_factor(argv):
   blur_factor = 4
   if len(argv) == 3:
      blur_factor = int(argv[2])
   return blur_factor

def main(argv):
   outfile = open('blurred.ppm','w')
   blur_factor = get_blur_factor(argv)
   width = get_height_width(argv[1])[0]
   height = get_height_width(argv[1])[1]
   write_header(argv[1],outfile)
   write_pixels(argv[1],outfile,width,height,blur_factor)
   outfile.close()

if __name__ == "__main__":
   main(sys.argv)
