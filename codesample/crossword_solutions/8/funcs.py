def getPuzzle():
   fileIn = input()
   puzzle=[]
   i=0
   for i in range(0,10):
      row = (fileIn[i*10:(i+1)*10])
      puzzle.append(row)
   return puzzle

def getWords():
    fileIn = input()
    wordList = fileIn.split()
    return wordList

def search(puzzle,wordList):
     allLetters = ""
     for i in puzzle:
         allLetters+=i
         output=[]   
     for word in wordList:   
          lengthofWord=len(word)  
          wordPrinted=False
          if word[0] in allLetters:  
               cntofLetter=allLetters.count(word[0])   
               position=0
               for j in range(cntofLetter):   
                    num=allLetters.index(word[0],position)   
                    position=num+1
                    if num<=99 and num>=0:
                         if num+1<=99 and allLetters[num+1]==word[1]:    
                              letterFound=True
                              for k in range(2,lengthofWord):   
                                   if num+k<(num/10+1)*10 and allLetters[num+k]==word[k]:
                                        continue
                                   else:
                                        letterFound=False
                                        break
                              if letterFound:
                                   row=num//10
                                   col=num%10
                                   forward=[word,'FORWARD',row,col]  
                                   output.append(forward)
                                   wordPrinted=True
                    
                         if num-1>=0 and allLetters[num-1]==word[1]:   
                              letterFound=True
                              for k in range(2,lengthofWord):   
                                   if num-k>=num//10*10 and allLetters[num-k]==word[k]:
                                        continue
                                   else:
                                        letterFound=False
                                        break
                              if letterFound:
                                   row=num//10
                                   col=num%10
                                   backward=[word,'BACKWARD',row,col]  
                                   output.append(backward)
                                   wordPrinted=True

                         if num+10<=99 and allLetters[num+10]==word[1]:  
                              letterFound=True
                              for k in range(2,lengthofWord):   
                                   if num+k*10<=num+(9-num/10)*10 and allLetters[num+k*10]==word[k]:
                                        continue
                                   else:
                                        letterFound=False
                                        break
                              if  letterFound:
                                   row=num//10
                                   col=num%10
                                   down=[word,'DOWN',row,col]  
                                   output.append(down)
                                   wordPrinted=True
                    
                         if num-10>=0 and allLetters[num-10]==word[1]:  
                              letterFound=True
                              for k in range(2,lengthofWord):  
                                   if num-k*10>=num%10 and allLetters[num-k*10]==word[k]:
                                        continue
                                   else:
                                        letterFound=False
                                        break
                              if letterFound:
                                   row=num//10
                                   col=num%10
                                   up=[word,'UP',row,col]  
                                   output.append(up)
                                   wordPrinted=True
          if not wordPrinted:  
               otptN=[word,'word not found']
               output.append(otptN)
               

     return output
