import puzzle_def



def open_file(f): 
   try: 
      f = open(argv[1], 'w')
      return f
      f.close()
   except: 
      print "cannot open file" 
      exit(1)


def read_pixels(list):
   pixel_color_list = [] 
   for i in range(0,len(list),3): 
      pixel_color_list.append((list[i:i+3]))
   return pixel_color_list


        

