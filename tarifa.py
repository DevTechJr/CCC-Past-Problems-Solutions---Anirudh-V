monthly_mb = int(input())
monthsNum = int(input())

totalMbAmount = (monthly_mb*(monthsNum+1))
totalUsed = 0
for i in range(monthsNum):
  used = int(input())
  totalUsed=totalUsed+used

print(totalMbAmount-totalUsed)