import sys
from math import sqrt

def main():
   my_file= open("faded.ppm", "w")
   if len(sys.argv) >= 1:
      tf= can_open(sys.argv[1], 'r')
      file_list= make_pixel_list(tf)
      pixel_values= file_list[0]
      pixel_grouped= groups_of_3(pixel_values)
      header_list= file_list[1]
      #print pixel_grouped[0]
      #print header_list
      my_file.write((header_list[0]) + "\n")
      my_file.write(str(str(header_list[1]) + " " + str(header_list[2])) + "\n")
      my_file.write(str(header_list[3]) + "\n")
      try:
         radius= int(sys.argv[4])
         y_row= int(sys.argv[2])
         x_col= int(sys.argv[3])
      except:
         print "insufficient argument" #try to make this a little more detailed
      #x= 0 #[['114'], ['101'], ['82']]
      #y= 0#image file goes from left to right
      #for i in range(0 ,len(pixel_grouped)):
      i= 0
      for y in range(0, header_list[2]):
         for x in range(0, header_list[1]):
            distance= dist(x_col, y_row, x, y)
            scale_value= (radius - distance)/radius
            sv= max(scale_value, 0.2)
            #print sv
            #print pixel_grouped[i][0]
            red_value= str(int(pixel_grouped[i][0] * sv))
            green_value= str(int(pixel_grouped[i][1] * sv))
            blue_value= str(int(pixel_grouped[i][2] * sv))
            my_pixel= red_value + " " + green_value + " " + blue_value + "\n"
            my_file.write(my_pixel)
            #x +=1
            i += 1
         #x= 0
         #y += 1
   else:
      print "No file was indicated"
      sys.exit()

def remove_extra_list(lists):
   list= []
   for i in lists:
      list.append(i)
   return list

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

def dist(x1, y1, x2, y2):
   distance= sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
   return distance

def can_open(name, mode):
   try:
      f= open(name, 'r')
      return f
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

if __name__ == "__main__":
   main()
