import requests
import pandas

url="https://fakestoreapi.com/products"

req=requests.get(url)
data=req.json()

p=pandas.DataFrame(data)[["id","title","price"]]
print(p)

