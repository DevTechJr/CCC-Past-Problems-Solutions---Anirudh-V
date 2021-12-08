order = str(input())
order=order.lower()

position = 1

for move in order:
  if move=="a" and position ==1:
    position=2
  elif move=="a" and position ==2:
    position = 1
  elif move=="b" and position ==2:
    position=3
  elif move=="b" and position==3:
    position=2
  elif move=="c" and position ==1:
    position=3
  elif move=="c" and position==3:
    position=1

print(position)