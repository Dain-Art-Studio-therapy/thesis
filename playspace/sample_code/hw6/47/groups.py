def groups_of_3(list):
   counter = 0
   mini_list = []
   mega_list = []
   
   for i in range(0,len(list)):
      if i != len(list)-1:
         if counter != 2: 
            counter = counter + 1
            mini_list.append(list[i])
         else:
            counter = 0
            mini_list.append(list[i])
            mega_list.append(mini_list)
            mini_list = []
      else:
         mini_list.append(list[i])
         mega_list.append(mini_list)
   return mega_list
