def getPuzzle():
   puz = raw_input()
   puzzle = [puz[0:10], puz[10:20], puz[20:30], puz[30:40], \
            puz[40:50], puz[50:60], puz[60:70], puz[70:80], \
            puz[80:90], puz[90:100]]
   return puzzle

def getWords():
   words = raw_input().split()
   return words

def searchRows(puzzle, words):
   foundRows = []
   for word in words:
      notFound = True
      while notFound:
         for i in range(10):
            if word in puzzle[i]:
               col = puzzle[i].find(word)
               foundRows.append((word, i, col, 'FORWARD'))
               notFound = False
            elif not word in puzzle[i]:
               rev = list(puzzle[i])
               j = 0
               k = 9
               while j <= k:
                  temp = rev[j]
                  rev[j] = rev[k]
                  rev[k] = temp
                  j += 1
                  k -= 1
               revRow = ''.join(rev)
               if word in revRow:
                  col = revRow.find(word)
                  foundRows.append((word, i, 9 - col, 'BACKWARD'))
                  notFound = False
         if notFound:
            foundRows.append((word, -1))
            notFound = False
   return foundRows

def searchCols(puzzle, words):
   cols = []
   for i in range(10):
      col = []
      for j in range(10):
         col.append(puzzle[j][i])
      cols.append(''.join(col)) 
   foundCols = []
   for word in words:
      notFound = True
      while notFound:
         for i in range(10):
            if word in cols[i]:
               row = cols[i].find(word)
               foundCols.append((word, row, i,'DOWN'))
               notFound = False
            elif not word in cols[i]:
               rev = list(cols[i])
               j = 0
               k = 9
               while j <= k:
                  temp = rev[j]
                  rev[j] = rev[k]
                  rev[k] = temp
                  j += 1
                  k -= 1
               revCol = ''.join(rev)
               if word in revCol:
                  row = revCol.find(word)
                  foundCols.append((word, 9 - row, i, 'UP'))
                  notFound = False
         if notFound:
            foundCols.append((word, -1))
            notFound = False
   return foundCols
