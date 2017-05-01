def get_rows(puzzle):
   new_puzzle_rows = []
   begin = 0
   end = 10
   for row in range(10):
      puzzle_pieces = puzzle[begin:end]
      begin += 10
      end += 10
      new_puzzle_rows.append(puzzle_pieces)
   return new_puzzle_rows

def get_columns(puzzle):
	new_puzzle_cols = []
	columns = []
	for col in range(10):
		for letter in range(col,len(puzzle),10):
			columns.append(puzzle[letter])
		new_puzzle_cols.append("".join(columns))
		columns = []
	return new_puzzle_cols

#Apply the row/column format functions in main file, exclude from checks. Let the check functions do their own thing.

def check_rows_forward(new_puzzle_rows,word):
   for rows in range(len(new_puzzle_rows)):
   	if new_puzzle_rows[rows].find(word) != -1:
   		rf = [rows, new_puzzle_rows[rows].find(word)]
   		return rf

def check_rows_backward(new_puzzle_rows,word):
	for rows in range(len(new_puzzle_rows)):
		if new_puzzle_rows[rows][::-1].find(word) != -1:
			rb = [rows,(len(new_puzzle_rows[rows])-1) - new_puzzle_rows[rows][::-1].find(word)]
			return rb

# This is forward in get_columns format
def check_columns_down(new_puzzle_cols,word):
   for cols in range(len(new_puzzle_cols)):
   	if new_puzzle_cols[cols].find(word) != -1:
   		cd = [cols,new_puzzle_cols[cols].find(word)]
   		return cd

#This is backward in get_columns format
def check_columns_up(new_puzzle_cols,word):
	for cols in range(len(new_puzzle_cols)):
		if new_puzzle_cols[cols][::-1].find(word) != -1:
			cu = [cols,(len(new_puzzle_cols[cols])-1) - new_puzzle_cols[cols][::-1].find(word)]
			return cu
