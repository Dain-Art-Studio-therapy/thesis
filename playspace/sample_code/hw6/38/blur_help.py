import math

def open_file(name,mode):
   try:
      return open(name,mode)
   except:
      print 'Error--file could not be opened'
      exit()

def groups_of_3(list):
   newlist = []
   for i in range(0,len(list),3):
      if i+2 >= len(list):
         if i+1 >= len(list):
            newlist.append([list[i]])
         else:
            newlist.append([list[i],list[i+1]])
      else:
         newlist.append([list[i],list[i+1],list[i+2]])

   return newlist

def process_file(f,reach):
   file_object = open('blurred.ppm','w')

   long_list = []
   for line in f:
      a = line.split()
      for v in a:
         long_list.append(v)
   width = long_list[1]
   height = long_list[2]
   print>>file_object,long_list[0]
   print>>file_object,width,height
   print>>file_object,long_list[3]

   just_values = []
   for i in range(4,len(long_list)):
      just_values.append(int(long_list[i]))

   grouped_pixels = groups_of_3(just_values)
   grid = []
   row = []
   starting_pix = 0
   ending_pix = starting_pix + int(width)
   if ending_pix <= len(grouped_pixels):
      for c in range(starting_pix,ending_pix):
         row.append(grouped_pixels[c])
         grid.append(row)
         starting_pix = ending_pix + 1

   red_total = 0
   green_total = 0
   blue_total = 0
   for i in range(len(grid)):
      for j in range(len(grid[i])):
         if i < reach:
            if j < reach:
               for row in range(i):
                  for pixel in range(j):
                     red_total += grid[row][pixel][0]
                     green_total += grid[row][pixel][1]
                     blue_total += grid[row][pixel][2]
                     r = int(red_total/(((reach*2)+1)**2))
                     g = int(green_total/(((reach*2)+1)**2))
       	             b = int(blue_total/(((reach*2)+1)**2))
                     print>>file_object, r,g,b
            elif j >= len(grid[i])-reach:
               for row in range(i):
                  for pixel in range(j,len(grid[i])):
                     red_total += grid[row][pixel][0]
                     green_total += grid[row][pixel][1]
                     blue_total += grid[row][pixel][2]
                     r = int(red_total/(((reach*2)+1)**2))
                     g = int(green_total/(((reach*2)+1)**2))
                     b = int(blue_total/(((reach*2)+1)**2))
               	     print>>file_object, r,g,b
            else:
               for row in range(i):
                  for pixel in range(j-reach,j+reach):
                     red_total += grid[row][pixel][0]
       	             green_total += grid[row][pixel][1]
       	             blue_total += grid[row][pixel][2]
       	             r = int(red_total/(((reach*2)+1)**2))
       	             g = int(green_total/(((reach*2)+1)**2))
       	             b = int(blue_total/(((reach*2)+1)**2))
                     print>>file_object, r,g,b

         elif i >= len(grid)-reach:
            if j < reach:
               for row in range(i,len(grid)):
                  for pixel in range(j):
                     red_total += grid[row][pixel][0]
                     green_total += grid[row][pixel][1]
                     blue_total += grid[row][pixel][2]
                     r = int(red_total/(((reach*2)+1)**2))
                     g = int(green_total/(((reach*2)+1)**2))
                     b = int(blue_total/(((reach*2)+1)**2))
                     print>>file_object, r,g,b
            elif j>= len(grid[i])-reach:
               for row in range(i,len(grid)):
                  for pixel in range(j,len(grid[i])):
                     red_total += grid[row][pixel][0]
                     green_total += grid[row][pixel][1]
                     blue_total += grid[row][pixel][2]
                     r = int(red_total/(((reach*2)+1)**2))
                     g = int(green_total/(((reach*2)+1)**2))
                     b = int(blue_total/(((reach*2)+1)**2))
                     print>>file_object, r,g,b
            else:
               for row in range(i,len(grid)):
                  for pixel in range(j-reach,j+reach):
                     red_total += grid[row][pixel][0]
                     green_total += grid[row][pixel][1]
                     blue_total += grid[row][pixel][2]
                     r = int(red_total/(((reach*2)+1)**2))
                     g = int(green_total/(((reach*2)+1)**2))
                     b = int(blue_total/(((reach*2)+1)**2))
                     print>>file_object, r,g,b
         else:
            if j < reach:
               for row in range(i-reach,i+reach):
                  for pixel in range(j):
                     red_total += grid[row][pixel][0]
                     green_total += grid[row][pixel][1]
                     blue_total += grid[row][pixel][2]
                     r = int(red_total/(((reach*2)+1)**2))
                     g = int(green_total/(((reach*2)+1)**2))
                     b = int(blue_total/(((reach*2)+1)**2))
                     print>>file_object, r,g,b
            elif j>= len(grid[i])-reach:
               for row in range(i-reach,i+reach):
                  for pixel in range(j,len(grid[i])):
                     red_total += grid[row][pixel][0]
                     green_total += grid[row][pixel][1]
                     blue_total += grid[row][pixel][2]
                     r = int(red_total/(((reach*2)+1)**2))
                     g = int(green_total/(((reach*2)+1)**2))
                     b = int(blue_total/(((reach*2)+1)**2))
                     print>>file_object, r,g,b
            else:
               for row in range(i-reach,i+reach):
                  for pixel in range(j-reach,j+reach):
                     red_total += grid[row][pixel][0]
                     green_total += grid[row][pixel][1]           
                     blue_total += grid[row][pixel][2]
                     r = int(red_total/(((reach*2)+1)**2))
                     g = int(green_total/(((reach*2)+1)**2))
                     b = int(blue_total/(((reach*2)+1)**2))
                     print>>file_object, r,g,b
