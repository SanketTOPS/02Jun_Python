import pandas

data={
    'id':[101,102,103],
    'name':['sanket','hitesh','nirav'],
    'sub':['python','php','java']
}

dt=pandas.DataFrame(data)
print(dt)