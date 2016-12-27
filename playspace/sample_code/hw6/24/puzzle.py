import sys

def groups_of_3(values):
   if values == []:
      return None
   list = []
   for l in range(0, len(values), 3):
      list.append(values[l: l+3])
   return list

def make_pixel_list(f):
   list= []
   for line in f:
      pixels = line.split()
      list.append(pixels)
   newlist= list[3:]
   headerlist= list[:3]
   newerlist= [newlist, headerlist]
   return newerlist
#take header later on and put in
def main():
   my_file = open("hidden.ppm", "w")
   if len(sys.argv) >= 1:
      tf= can_open(sys.argv[1], 'r')
      file_list= make_pixel_list(tf)
      pixel_values= file_list[0]
      pixel_grouped= groups_of_3(pixel_values)
      header_list= file_list[1]
      my_file.write(str(header_list[0][0])+ "\n")
      my_file.write(str(header_list[1][0] + " " + header_list[1][1]) + "\n")
      my_file.write(str(header_list[2][0]) + "\n")
      for i in pixel_grouped:
         red_value=str(min((int(i[0][0]) * 10), 255))
         my_pixel= red_value +" "+ red_value +" "+ red_value +"\n"
         my_file.write(my_pixel)

   else:
      print "No file was indicated"
      sys.exit()
   my_file.close()
# my_file = open("filename", "w"), close when done, filename is hidden.ppm

def can_open(name, mode):
   try:
      f= open(name, 'r')
      return f
   except IOError as e:
      print >> sys.stderr, '{0} : {1}'.format(name, e.strerror)
      exit(1)

if __name__ == "__main__":
   main()
