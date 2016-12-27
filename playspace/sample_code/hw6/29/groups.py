def groups_of_3(list1):
   new_list = []
   
   remainder = len(list1) % 3

   if remainder == 0:
      for i in range(0, len(list1), 3):
         new_list.append([list1[i], list1[i+1], list1[i+2]])      

   elif remainder != 0: 
      for i in range(0, len(list1) - remainder, 3):
         new_list.append([list1[i], list1[i+1], list1[i+2]])

      if remainder == 1:
         new_list.append([list1[len(list1) - 1]])

      elif remainder == 2:
         new_list.append([list1[len(list1) - 2], list1[len(list1) - 1]])       

   return new_list
