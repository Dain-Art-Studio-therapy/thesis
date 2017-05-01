def get_puzzle():
    puzzle = input()
    words = input()
    return (puzzle, words)

def split_puzzle(puzzle):
    puzzle = [puzzle[i:i+10] for i in range(0, len(puzzle), 10)]
    return puzzle
   

def split_words(words):
    words = words.split(' ')
    return words


def check_row_col_forward(word, puzzle):
    for row in range(len(puzzle)):
        if word in puzzle[row]:
            col = puzzle[row].find(word)
            return (row, col)
    return None


def check_1row_col_forward(word, row):
    col = row.find(word)
    if col != -1:
       return col
    else:
       return None


      
def check_row_col_backward(word, row):
    word = word[::-1]
    result = check_1row_col_forward(word, row)
    if result != None:
        return result + len(word) - 1
    else:
        return None

#def check_all_row_col_backward(word, puzzle):
#    for i in range(len(puzzle)):
#        pos = check_row_col_backward(word, puzzle[i])
#        if pos != None:
#            return (i, pos)
#    return None

def check_all_row_col_backward(word, puzzle):
    word = word[::-1]
    for row in range(len(puzzle)):
        if word in puzzle[row]:
            col = puzzle[row].find(word) + len(word)-1
            return (row, col)
    return None







def check_row_col_up(word, puzzle, i):
    col = []
    for row in puzzle:
        col.append(row[i])
    col = ''.join(col)
    result = check_row_col_backward(word, col)
    if result != None:
        return (result, i)
    return None


def check_row_col_down(word, puzzle, i):
    col = []
    for row in puzzle:
        col.append(row[i])
    col = ''.join(col)
    result = check_1row_col_forward(word, col)
    if result != None:
        return (result, i)
    else:
        return None



def check_all_row_col_down(word, puzzle):
    for i in range(len(puzzle[0])):
        pos = check_row_col_down(word, puzzle, i)
        if pos != None:
            return pos
    return None



        
def check_all_row_col_up(word, puzzle):
    for i in range(len(puzzle[0])):
        pos = check_row_col_up(word, puzzle, i)
        if pos != None:
            return pos
    return None
