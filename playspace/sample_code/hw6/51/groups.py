def groups_of_3(nums):
   newlist=[]
   num_threes=len(nums)/3
   if len(nums)%3>0:
      num_threes+=1
   for i in range(0,num_threes):
      if i*3+2 <=len(nums)-1:
         n1=nums[i*3]
         n2=nums[i*3+1]
         n3=nums[i*3+2]
         newlist.append([n1,n2,n3])
      elif i*3+1<=len(nums):
         n1=nums[i*3]
         n2=nums[i*3+1]
         newlist.append([n1,n2])
      else:
         n1=nums[i*3]
         newlist.append([n1])
   return newlist
