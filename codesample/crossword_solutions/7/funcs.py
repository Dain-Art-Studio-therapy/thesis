def get_puzzle():
    puzzle = input()
    return puzzle

def get_words():
    words = input().split()
    return words

def search_row(row, word):
    row = ''.join(row)
    if row.find(word) != -1:
       return row.find(word)
    if row.find(word) == -1:
       return None

def check_forward(puzzle, word):
    r = 0
    for row in puzzle:
        position = search_row(row, word)
        if position != None:
           return (r, position)
        r += 1
    return None 
 
def check_backward(puzzle, word):
    r = 0
    for row in puzzle:
        reversedrow = row[::-1]
        position = search_row(reversedrow, word)
        if position != None:
           revpos = (len(row) - position - 1)
           return (r, revpos)
        r += 1
    return None

def check_up(puzzle, word):
    c = 0
    for i in range(len(puzzle[0])):
        col = ''.join(str(j[i]) for j in puzzle)
        reversedcol = col[::-1]
        position = search_row(reversedcol, word)
        if position != None:
           revpos = (len(col) - position - 1)
           return (c, revpos)
        c += 1
    return None

def check_down(puzzle, word):
    c = 0
    for i in range(len(puzzle[0])):
        col = ''.join(str(j[i]) for j in puzzle)
        position = search_row(col, word)
        if position != None:
           return (c, position)
        c += 1
    return None
