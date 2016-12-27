def groups_of_3(numlist):

   if numlist == []:
      return None
   grouplist = []
   
   
   x = 0
   y = 0
   trilist = []
   while x < len(numlist):
      trilist.append(numlist[x])
      if len(trilist) == 3:
         temp = [i for i in trilist]
         grouplist.append(temp)
         del trilist[:]
      x += 1

   if len(trilist) > 0:
      grouplist.append(trilist)

   return grouplist
