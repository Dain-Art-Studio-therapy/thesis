def groups_of_3(list):
   group = []
   for i in range(0, len(list), 3):
      group.append(list[i:i+3])
   return group
