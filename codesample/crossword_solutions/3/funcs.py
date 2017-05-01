def columnize(puzzle):
    p = list(zip(*puzzle))
    newPuzzle =[]
    for x in range(0,len(p)):
        newPuzzle.append(''.join(p[x]))
    return newPuzzle
    

def searchPuzzle(puzzle, word, direction):
    if direction == 'FORWARD':
        #search every line, return position
        for x in range(0,len(puzzle)):
            y = puzzle[x].find(word)
            if y>0:
                return x, y
    elif direction == 'BACKWARD':
        for x in range(0,len(puzzle)):
            # find reverse of word in the string
            y = puzzle[x].find(word[::-1])
            if y>0:
                # calculate actual position considering the reversal
                y += len(word) -1
                return x, y
    elif direction == 'UP':
        # create strings for each column and search these
        tPuzzle = columnize(puzzle)
        for x in range(0,len(tPuzzle)):
            y = str(tPuzzle[x]).find(word[::-1])
            if y>=0:
                y += len(word) -1
                return y, x
    elif direction == 'DOWN':
        # create strings for each column and search these for the REVERSE of the word
        tPuzzle = columnize(puzzle)
        for x in range(0,len(tPuzzle)):
            y = str(tPuzzle[x]).find(word)
            if y>=0:
                return y, x
    return 0, 0
