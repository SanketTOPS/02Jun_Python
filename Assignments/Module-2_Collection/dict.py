stdata={'id':101,'name':'sanket','city':'rajkot'}
"""print(stdata)
print(stdata["name"])
print(stdata.get("city"))
print(len(stdata))
print(stdata.keys())
print(stdata.values())"""

# ---------------------------- #
"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo")"""

#print(stdata)
"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""


# --------------------------- #
print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

for i in stdata.items():
    print(i)