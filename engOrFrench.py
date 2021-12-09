totalIterations = int(input())

wordsStr=""

for x in range(totalIterations):
  inputStr = str(input())
  wordsStr+=inputStr

wordsStr=wordsStr.lower()

sCount =0
tCount = 0

for char in wordsStr:
  if char == "s":
    sCount+=1
  elif char == "t":
    tCount+=1

if sCount>tCount:
  print("French")
elif tCount>sCount:
  print("English")
elif sCount==tCount:
  print("French")