import requests

url="https://fakestoreapi.com/products"

req=requests.get(url)
data=req.json()
print(data)


for i in data:
    #print(i)
    print("Product ID:",i["id"])
    print("Product Name:",i["title"])
    print("Price:",i["price"])


