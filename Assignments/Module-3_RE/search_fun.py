import re

mystr="That is Python!"

x=re.search('This',mystr)
print(x)

if x:
    print("Match Found...")
else:
    print("Error!")
