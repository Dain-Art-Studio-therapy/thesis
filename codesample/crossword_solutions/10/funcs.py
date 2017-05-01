import math
def askForCharacters():
   puzzle = fillPuzzleWithNothing()
   i = 0 
   j = 0 
   count = 0 
   characters = raw_input().split()
   while(10 > i):
      j = 0 
      while(10 > j):
         puzzle[i][j] = characters[0][count]
         j += 1
         count += 1
      i += 1 
   return turnPuzzletoStrings(puzzle)

def askForWords():
   words = raw_input().split()
   return words 

def wordInfo(puzzle,wordList):
   foundList = []
   count = 0 
   while(len(wordList) > count):
      if(len( checkColumns(puzzle,wordList[count]) ) > 0):
         foundList.append(checkColumns(puzzle,wordList[count]) )
      elif(len(checkRows(puzzle,wordList[count])) > 0):
         foundList.append(checkRows(puzzle,wordList[count]) )
      else:
         foundList.append("word not found")
      count +=1  
   return foundList 

def checkRows(puzzle,word):
   rowNum = 0 
   column = 0 
   regString = 0 
   reverseString = 0
   infoList = []
   while( len((puzzle))> rowNum):
      rowString = puzzle[rowNum][:]
      reverse = rowString[::-1]
      column = 0 
      if(rowString.find(word) != -1):
         while(rowString.find(word,column) != -1):
            column += 1
         infoList.append("FORWARD")
         infoList.append(rowNum)
         infoList.append(column-1)
      elif(reverse.find(word) != -1):
         while(reverse.find(word,column) != -1):
            column += 1 
         infoList.append("BACKWARD")
         infoList.append(rowNum)
         infoList.append(opposite(column))
      rowNum += 1 
   return infoList 

def opposite(value):
   return abs(value - 10)

def checkColumns(puzzle,word):
   row = 0 
   col = 0 
   infoList = []
   columnString = 0 
   while(10 > col):
      row = 0 
      columnList = []
      reverse = 0 
      while(10 > row):
         columnList.append(puzzle[row][col])
         row += 1 
      columnString = ''.join(columnList)
      reverse = columnString[::-1]
      row = 0 
      if(columnString.find(word) != -1):
         while(columnString.find(word,row) != -1):
            row +=1 
         infoList.append("DOWN")
         infoList.append(row-1)
         infoList.append(col)
      elif(reverse.find(word) != -1):
        while(reverse.find(word,row) != -1):
           row += 1
        infoList.append("UP")
        infoList.append(opposite(row))
        infoList.append(col)

      col += 1
 
   return infoList

def turnPuzzletoStrings(puzzle):
   i = 0
   puzzleRow = [] 
   completedPuzzle = [0,0,0,0,0,0,0,0,0,0]
   while(10 > i):
      puzzleRow = puzzle[i][:]
      completedPuzzle[i] = ''.join(puzzleRow)
      i += 1
   return completedPuzzle
def displayWordInfo(wordList,infoList):
   for x in range(len(wordList)): 
      print wordList[x] + ":",
      if(len(infoList[x]) == 3):
         print "("+infoList[x][0]+")", "row" +":", infoList[x][1], "column" + ":", infoList[x][2]
      else:
         print infoList[x][:]

def fillPuzzleWithNothing(): 
   mainPuzzle = []
   while(len(mainPuzzle) < 10):
      puzzleRow = []
      count = 0
      while(count < 10): 
         puzzleRow.append(0)           
         count += 1 
      mainPuzzle.append(puzzleRow)
   return mainPuzzle
