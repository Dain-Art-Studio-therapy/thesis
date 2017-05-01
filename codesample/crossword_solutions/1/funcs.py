def split_puzzle(letters):
    puzzle = []
    for i in range(0,100,10):
       puzzle.append(letters[i:i+10])
    return puzzle

def look_in_rows(puzzle, word):
    backword = turn_word_back(word)
    i = 0
    found = 'unknown'
    for row in puzzle:
        if word in row:
           found = 'yes'
           print(word+': (FORWARD) row: %d  column: %d' %(i,row.find(word)))
        elif backword in row:
           found = 'yes'
           print(word+ ': (BACKWARD) row: %d column: %d' %(i,row.find(backword)+len(word)-1))
        else:
         if found != 'yes':
          found = 'no'
        i += 1      
    return found
 
def turn_word_back(word):
    backwards = []
    i = len(word)-1
    while i >= 0:
        backwards.append(word[i])
        i -= 1
    return ''.join(backwards)
 
def look_in_cols(puzzle,word):
    backword = turn_word_back(word)
    cols = get_cols(puzzle) 
    i = 0
    found = 'unknown'
    for col in cols:
        if word in col:
           found = 'yes'
           print(word+ ': (DOWN) row: %d column: %d' %(col.find(word),i))
        elif backword in col:
           found = 'yes'
           print(word+ ': (UP) row: %d column: %d' %(col.find(backword)+len(word)-1,i))
        else:
          if found != 'yes':
           found = 'no'
        i += 1
    return found    
    
    
def get_cols(puzzle):
    columns = []
    for i in range(len(puzzle)):
        col = []
        for j in range(10):
            col.append(puzzle[j][i])
        columns.append(''.join(col))
    return columns
