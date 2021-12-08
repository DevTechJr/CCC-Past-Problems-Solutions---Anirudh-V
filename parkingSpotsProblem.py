run = "python parkingSpotsProblem.py"

number = int(input())
yesterday = str(input())
today = str(input())

occupiedSpaces=0
for x in range(number):
  if yesterday[x]=="C"and today[x]=="C":
    occupiedSpaces=occupiedSpaces+1
  
print(occupiedSpaces)