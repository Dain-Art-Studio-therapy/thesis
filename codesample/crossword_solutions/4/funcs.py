h = ''
g = ''

def rows_and_columns(list):
	rows = []
	cols = []
	f_rows = []
	col_x = []


	for x in range(len(list)):
		f_rows.append(list[x])
		if len(f_rows) == 10:
			rows.append(f_rows)
			f_rows = []

	for x in range(len(rows)):
		for y in range(10):
			col_x.append(rows[y][x])
			if len(col_x) == 10:
				cols.append(col_x)
				col_x = []
	h = rows[0][0]
	g = cols[0][0]
	brows = rows
	bcols = cols


	return rows, cols, brows, bcols

def reversal(list1):
	list2 = []
	j = 0
	for i in list1:
		j = []
		for z in reversed(i):
			j.append(z)
		list2.append(j)
	return list2

def wordaroni(words, rows, cols, brows, bcols):
	result = []
	for i in words:
		result.append(word_finder(i, rows, cols, brows, bcols))
	return result


def word_finder(word, rows, cols, brows, bcols):

	for x in range(len(rows)):
		for y in range(len(rows[x])):
			if word[0] == rows[x][y] and len(rows[x]) - y >= len(word):
				for i in range(len(word)):
					if word[i] != rows[x][y+i]:
						break
					elif i == len(word) - 1:
						return addWord(word, x, y, 'f')

	for x in range(len(cols)):
		for y in range(len(cols[x])):
			if word[0] == cols[x][y] and len(cols[x]) - y >= len(word):
				for i in range(len(word)):
					if word[i] != cols[x][y+i]:
						break
					elif i == len(word) - 1:
						return addWord(word, y, x, 'd')


	brows = reversal(brows)

	for x in range(len(brows)):
		for y in range(len(brows[x])):
			if word[0] == brows[x][y] and len(brows[x]) - y >= len(word):
				for i in range(len(word)):
					if word[i] != brows[x][y+i]:
						break
					elif i == len(word) - 1:
						return addWord(word, x, 9-y, 'b')

	bcols = reversal(bcols)
	for x in range(len(bcols)):
		for y in range(len(bcols[x])):
			if word[0] == bcols[x][y] and len(bcols[x]) - y >= len(word):
				for i in range(len(word)):
					if word[i] != bcols[x][y+i]:
						break
					elif i == len(word) - 1:
						return addWord(word, 9 - y, x, 'u')

	return word + ': word not found'



def addWord(word, row, col, way):
	if way == 'f':
		return word + ': (FORWARD) row: ' + str(row) + ' column: ' + str(col) 
	if way == 'b':
		return word + ': (BACKWARD) row: ' + str(row) + ' column: ' + str(col)
	if way == 'u':
		return word + ': (UP) row: ' + str(row) + ' column: ' + str(col)
	if way == 'd':
		return word + ': (DOWN) row: ' + str(row) + ' column: ' + str(col)
