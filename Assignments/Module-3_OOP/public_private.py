class studinfo:
    #Private
    __stid=12
    __stnm="Sanket"

    #Private
    def __getdata(self):
        print("This is getdata!")
        print("ID:",self.__stid)
        print("Name:",self.__stnm)

    #Public
    def printdata(self):
        self.__getdata()


st=studinfo()
st.printdata()