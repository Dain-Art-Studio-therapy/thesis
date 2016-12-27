import sys
#import blur_pixel

def main():
   my_file= open("blurred.ppm", "w")
   if len(sys.argv) >= 1:
      tf= can_open(sys.argv[1], 'r')
      file_list= make_pixel_list(tf)
      pixel_values= file_list[0]#grab this function from earlier part
      pixel_grouped= groups_of_3(pixel_values)
      header_list= file_list[1]
      header_maker(my_file, header_list)#not sure this function works well
      try:
         neighbor= sys.argv[2]
      except:
         neighbor= 4
      i = 0
      for y in range(0, header_list[2]):
         for x in range(0, header_list[1]):
            surround_list= surround_pixels(neighbor, x, y, pixel_grouped, i, header_list[1], header_list[2])
            my_pixel= color_pixel(surround_list)
            my_file.write(my_pixel)
            i +=1
   else:
      print "No file was indicated"
      sys.exit()

def surround_pixels(neighbor, center_x, center_y, pixel_list, index, image_width, image_height):#you can also take the center pixel
   surround_list= []
   min_x= center_x - neighbor
   min_y= center_y - neighbor
   max_x= center_x + neighbor
   max_y= center_y + neighbor
   while min_x < 0:
      min_x += 1
   while min_y < 0:
      min_y += 1
   while max_x > image_width:
      max_x += -1
   while max_y > image_height:
      max_y += -1
   for height in range(min_y, max_y):
      for width in range(min_x, max_x):
         surround_list.append(pixel_list[index])#may be starting from center?
         index +=1
      index = index + image_width - (max_x - min_x)
   return surround_list

def color_pixel(surround):
   #[r, g, b]
   total_r = 0
   total_g = 0
   total_b = 0
   for i in surround:
      total_r += i[0]
      total_g += i[1]
      total_b += i[2]
   surround_count= len(surround)
   r_avg= str(total_r/surround_count)
   g_avg= str(total_g/surround_count)
   b_avg= str(total_b/surround_count)
   #color= [r_avg, g_avg, b_avg]#you can possibly already set this up as a str
   color= r_avg + " " + g_avg + " " + b_avg + "\n"
   return color

def header_maker(input_file, header_list):
      input_file.write((header_list[0]) + "\n")
      input_file.write(str(str(header_list[1]) + " " + str(header_list[2])) + "\n")
      input_file.write(str(header_list[3]) + "\n")

def make_pixel_list(f):
   list= []
   for line in f:
      pixel_in_list = line.split()
      for i in range(len(pixel_in_list)):
         try:
            list.append(int(pixel_in_list[i]))
         except ValueError:
            list.append(pixel_in_list[i])
   pixel_list= list[4:]
   headerlist= list[:4]
   image_list= [pixel_list, headerlist]
   return image_list

def groups_of_3(values):
   if values == []:
      return None
   list = []
   for l in range(0, len(values), 3):
      list.append(values[l: l+3])
   return list

def can_open(name, mode):
   try:
      f= open(name, 'r')
      return f
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)


if __name__ == "__main__":
   main()

