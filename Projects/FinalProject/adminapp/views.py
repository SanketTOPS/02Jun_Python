from django.shortcuts import render,redirect
from userapp.models import *

# Create your views here.
def admin_home(request):
    if request.method=='POST':
        un=request.POST["username"]
        pa=request.POST["password"]
        
        if un=="admin" and pa=="tops@123":
            print("Login Success!")
            return redirect("admin_dashboard")
        else:
            print("Error!Login Faild...")
    return render(request,'admin_home.html')

def admin_dashboard(request):
    data=UserSignup.objects.all()
    n_data=Mynotes.objects.all()
    n=data.count()
    nd=n_data.count()
    return render(request,'admin_dashboard.html',{'n':n,'nd':nd,'data':data})

def admin_userdata(request):
    data=UserSignup.objects.all()
    return render(request,'admin_userdata.html',{'data':data})

def admin_notesdata(request):
    data=Mynotes.objects.all()
    return render(request,'admin_notesdata.html',{'data':data})