class studinfo:
    stid=101
    stnm="Sanket"

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

#Calling via Object
"""st=studinfo()
st.getdata()
st.stid=102
st.stnm="Ashok"
st.getdata()"""

#Calling via Instance 
studinfo().getdata()
studinfo().stid=102
studinfo().stnm="Hitesh"
studinfo().getdata()