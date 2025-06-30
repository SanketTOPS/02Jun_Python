x=open("stdata.txt","w")


n=int(input("Enter number of students:"))

for i in range(n):
    id=input("Enter an ID:")
    name=input("Enter a Name:")
    city=input("Enter a City:")

    x.write(f"ID:{id}\nName:{name}\nCity:{city}")
