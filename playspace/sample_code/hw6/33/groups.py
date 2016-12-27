def groups_of_3(nums):
   list = []
   new = []
   a = 3
   for e in range(0,len(nums),a):
      list = nums[e:e+a]
      new.append(list)
   return new
