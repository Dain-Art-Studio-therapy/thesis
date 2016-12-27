def groups_of_three(list):
   list_of_groups = []

   for index in range(len(list)/3 +1):
      group = list[(index * 3):((index + 1) * 3)]
      if group != []:
         list_of_groups.append(group)
   return list_of_groups

def groups_of_certain(list, length):
   list_of_groups = []

   for index in range(len(list)/length +1):
      group = list[(index * length):((index + 1) * length)]
      if group != []:
         list_of_groups.append(group)
   return list_of_groups