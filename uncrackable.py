import string

notValidChars = string.punctuation

password = str(input())
result=""

if len(password) >= 8 and len(password)<=12:
  # Tab from the hashtag
  for x in password:
    if x in notValidChars:
      result="Invalid"
      print(result)
      exit()
    
  lower=0
  upper=0
  digit=0
  for char in password:
    if char.isdigit():
      digit+=1
    elif char.islower():
      lower+=1
    elif char.isupper():
      upper+=1
  
  if lower>=3 and upper>=2 and digit>=1:
    print("Valid")
  else:
    print("Invalid")
    

else:
  print("Invalid")
  