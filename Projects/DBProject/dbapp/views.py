from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST': #TRUE
        form=userForm(request.POST)
        if form.is_valid(): #tRUE
            form.save()
            print("Record inserted!")
        else:
            print(form.errors)
    return render(request,'index.html')

def showdata(request):
    data=userinfo.objects.all()
    print(data)
    return render(request,'showdata.html',{'data':data})