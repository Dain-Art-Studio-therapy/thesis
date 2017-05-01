def get_words():
   words = input()
   words = words.split(" ")
   return words

def cross_word(string):
   list = []
   for i in range(0,10):
      row = string[(10*i):(10+(10*i))]
      list.append(row)
   return list

def col_word(string):
   list = []
   some = []
   for i in range(10):
      for j in range(10):
         num = i + (j * 10)
         some.append(string[num])
      list.append("".join(some))
      some = []
   return list

def show_table(list):
   for x in list:
      print("".join(x))

def find_forward(string, words):
   found = []
   all = []
   i = 0
   while i < len(string):
      for j in range(len(words)):
         if words[j] in string[i]:
            found.append(i)
            found.append(string[i].find(words[j]))
            found.append("FORWARD")
            found.append(words[j])
         j += 1
      if len(found) > 0:
         if len(found) > 4:
            all.append(found[0:4])
            all.append(found[4:8])
         else:
            all.append(found)
      found = []
      i += 1
   return all

def reverse_word(words):
   rev = []
   new = []
   for word in words:
      for i in range(len(word)-1, -1,-1):
         rev.append(word[i])
      new.append("".join(rev))
      rev =[]
   return new

def find_backwards(string, words):
   found = []
   all = []
   i = 0
   new = reverse_word(words)
   while i < len(string):
      for j in range(len(new)):
         if new[j] in string[i]:
            found.append(i)
            found.append(string[i].find(new[j])+len(new[j])-1)
            found.append("BACKWARD")
            found.append(words[j])
         j += 1
      if len(found) > 0:
         if len(found) > 4:
            all.append(found[0:4])
            all.append(found[4:8])
         else:
            all.append(found)
      found = []
      i += 1
   return all

def find_down(string, words):
   new = col_word(string)
   found = []
   all = []
   i = 0
   for i in range(len(new)):
      for j in range(len(words)):
         if words[j] in new[i]:
            found.append(new[i].find(words[j]))
            found.append(i)
            found.append("DOWN")
            found.append(words[j])
      if len(found) > 0:
         if len(found) > 4:
            all.append(found[0:4])
            all.append(found[4:8])
         else:
            all.append(found)
      found = []
   return all

def find_up(string, words):
   new = col_word(string)
   word = reverse_word(words)
   found = []
   all = []
   i = 0               
   for i in range(len(new)):
      for j in range(len(word)):
         if word[j] in new[i]:       
            found.append(new[i].find(word[j])+len(word[j])-1)
            found.append(i)
            found.append("UP")   
            found.append(words[j])
      if len(found) > 0:
         if len(found) > 4:
            all.append(found[0:4])
            all.append(found[4:8])
         else:
            all.append(found)
      found = []
   return all
