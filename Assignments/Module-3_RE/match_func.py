import re

mystr="This is Python!"

x=re.match('Python',mystr)
print(x)

if x:
    print("Match Found...")
else:
    print("Error!")
