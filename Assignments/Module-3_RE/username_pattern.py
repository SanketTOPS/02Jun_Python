import re

username="Sanket25"

usenm_pattern="[A-Z]+[a-z]+[0-9]"

x=re.findall(usenm_pattern,username)

if x:
    print("Username is valid!")
else:
    print("Error!Invalid Username")