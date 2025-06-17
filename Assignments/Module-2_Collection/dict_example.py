data={}

keys=['id','name','city']

for i in range(len(keys)):
    v=input(f"Enter value of {keys[i]}:")
    data[keys[i]]=v

print(data)
