data={'id':1,'name':'sanket','sub':'python'}
#print(data)
#print(data["name"])
#print(data.get("sub"))
#print(data.keys())
#print(data.values())

#data["id"]=102
#data["city"]='Rajkot'
#print(data)


# ---------------------------- #
#print(data)

"""for i in data:
    print(i)"""

"""for i in data.values():
    print(i)"""

"""for i in data.items():
    print(i)"""

"""for i,j in data.items():
    print(f"Key={i} and Value={j}")"""


"""if 'name' in data:
    print("Yes...")
else:
    print("Noo")"""

"""if 'sanket' in data.values():
    print("Yes...")
else:
    print("Noo")"""


# ----------------------------------- #

print(data)
data["city"]="Rajkot" #add a new pair
data["name"]="ashok" #update a specific pair
#data.pop("sub")
#data.clear()
#del data
#print(data)
#print(data)
#print(len(data))

newdict=data.copy()
print(newdict)