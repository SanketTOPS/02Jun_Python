a=10

print("A:",a) #10

def getvalue():
    global a
    a+=10
    print("Next A:",a) #15

getvalue()