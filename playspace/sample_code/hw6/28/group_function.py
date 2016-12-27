# Han Tran || CPE 101 -- 01,02
# group_function.py


def group_of_3(lst):
   newlist = []
   temp = []
   counter = 0
   for i in lst:
      temp.append(i)
      counter += 1
      if counter % 3 == 0:
         newlist.append(temp) 
         temp = []
   if temp:
      newlist.append(temp)
   return newlist


