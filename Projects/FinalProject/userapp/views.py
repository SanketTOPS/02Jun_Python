from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.

def index(request):
    user=request.session.get("user")
    return render(request,'index.html',{'user':user})

def notes(request):
    return render(request,'notes.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def signin(request):
    if request.method=='POST':
        em=request.POST["email"]
        pa=request.POST["password"]
        
        user=UserSignup.objects.filter(email=em,password=pa)
        if user:
            print("Login Successfully!")
            request.session["user"]=em
            return redirect("/")
        else:
            print("Error!Login Faild...")
    return render(request,'signin.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("Signup Successfully!")
            return redirect("signin")
        else:
            print(form.errors)
    return render(request,'signup.html')

def userlogout(request):
    logout(request)
    return redirect('signin')
    