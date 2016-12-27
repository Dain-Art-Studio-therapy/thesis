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

def process_file(f):
   file_object = open('hidden.ppm','w')

   long_list = []
   for line in f:
      a = line.split()
      for v in a:
         long_list.append(v)

   print>>file_object,long_list[0]
   print>>file_object,long_list[1],long_list[2]
   print>>file_object,long_list[3]

   just_values = []
   for i in range(4,len(long_list)):
      just_values.append(long_list[i])

   grouped_values = groups_of_3(just_values)
   for group in grouped_values:
      r = int(group[0])*10
      g = r
      b = r
      print>>file_object, r,g,b 
