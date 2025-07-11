import requests

class home:
    def __init__(self):
        try:
            url="https://www.google.co.in/"
            response=requests.get(url)
            print("Internet connection is ON!")
        except:
            print("Oops!There is no internet connection...Plz try to check!")
        

hm=home()
