def make_puzzle(Puzzle):
   puzzle = []
   for i in range(0,10):
      puzzle.append(Puzzle[i*10:i*10+10])
   return puzzle

def make_words(Words):
   return Words.split()
  

def check_rows(puzzle, word):
   newword = []
   j = len(word)
   while j > 0:
      newword.append(word[j-1])
      j -= 1
   backWord = ''.join(newword)
   for row in range(len(puzzle)):
      if word in puzzle[row]:
         length = 0
         col = 0
         for char in puzzle[row]:
            letter = word[length]
            if char != letter:
               length = 0
               letter = word[length]
            if char == letter:
                  length += 1
                  if len(word) == length:
                     col -= (length-1)
                     place = ['(FORWARD)', row, col]
                     return place
            col += 1
      if backWord in puzzle[row]:
         length = 0
         col = 0
    	 for char in puzzle[row]:
    	    letter = backWord[length]
            if char != letter:
               length = 0
               letter = backWord[length]
            if char == letter:
               length += 1
               if len(backWord) == length:
                  place = ['(BACKWARD)', row, col]
                  return place 
       	    col	+= 1
     
def check_cols(puzzle, word):
   newword = []
   j = len(word)
   while j > 0:
      newword.append(word[j-1])
      j -= 1
   backWord = ''.join(newword)
   newpuzzle = []
   for col in range(len(puzzle)):
      new = []
      for row in range(len(puzzle)):
         new.append(puzzle[row][col])
      newpuzz = ''.join(new)
      newpuzzle.append(newpuzz)
   for col in range(len(newpuzzle)):
      if word in newpuzzle[col]:
         length = 0
         row = 0
         for char in newpuzzle[col]:
            letter = word[length]
            if char != letter:
               length = 0
               letter = word[length]
            if char == letter:
               length += 1
               if len(word) == length:
                  row -= (length-1)
                  place = ['(DOWN)', row, col]
                  return place
            row += 1
      if backWord in newpuzzle[col]:
         length = 0
         row = 0
         for char in newpuzzle[col]:
            letter = backWord[length]
            if char != letter:
               length = 0
               letter = backWord[length]   
            if char == letter:
               length += 1
               if len(backWord) == length:
                  place = ['(UP)', row, col]
                  return place
            row += 1
