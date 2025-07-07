class student:
    stid=12
    stnm="Sanket"

    def getdata(self):
        print("This is student class.")
    
    def getsum(self,a,b):
        print("Sum:",a+b)


st=student() #object of class

print("ID:",st.stid)
print("Name:",st.stnm)
st.getdata()
st.getsum(23,45)
