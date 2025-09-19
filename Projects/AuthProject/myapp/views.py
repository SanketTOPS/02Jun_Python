from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        unm=request.POST['email']
        pas=request.POST['password']
        
        user=Usersignup.objects.filter(email=unm,password=pas)
        if user:
            print("Login Successfully!")
            return redirect('home')
        else:
            print("Error!Login Faild...")
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("Signup Successfull!")
            return redirect('/')
        else:
            print(form.errors)
    return render(request,'signup.html')

def home(request):
    return render(request,'home.html')