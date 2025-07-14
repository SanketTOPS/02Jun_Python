import re

mystr="Is This Python!"

#x=re.findall("^This",mystr)
#x=re.findall('^[A-Z]',mystr)
x=re.findall('on$',mystr)
print(x)