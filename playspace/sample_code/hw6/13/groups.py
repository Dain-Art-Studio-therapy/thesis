def groups_of_3(input):
   result = []
   place = 0
   while place < len(input):
      if place%3 == 0:
         result.append([])
      result[-1].append(input[place])
      place += 1
   return result
