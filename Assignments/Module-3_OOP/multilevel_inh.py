class sanket:
    sid:int
    ssub:str

    def s_getdata(self):
        self.sid=input("Enter Sanket's ID:")
        self.ssub=input("Enter Sanket's Subject:")

class ashok(sanket):
    aid:int
    asub:str

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")

class darshan(ashok):
    did:int
    dsub:str

    def d_getdata(self):
        self.did=input("Enter Darshan's ID:")
        self.dsub=input("Enter Darshan's Subject:")


class tops(darshan):
    def printdata(self):
        print("------Sanket's Info------")
        print("Sanket's ID:",self.sid)
        print("Sanket's Subject:",self.ssub)
        print("------Ashok's Info------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)
        print("------Darshan's Info------")
        print("Darshan's ID:",self.did)
        print("Darshan's Subject:",self.dsub)


tops.s_getdata()
tops.a_getdata()
tops.d_getdata()
tops.printdata()