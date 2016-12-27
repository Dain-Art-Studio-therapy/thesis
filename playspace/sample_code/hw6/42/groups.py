def groups_of_3(nums):
   new_list = []
   for x in range(0, len(nums), 3):
      if (len(nums)-x) / 3  > 0:
         new_list.append(nums[x:(x+3)])
      else:
         new_list.append(nums[x:len(nums)])
   return new_list
