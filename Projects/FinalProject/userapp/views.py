from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.

def index(request):
    user=request.session.get("user")
    return render(request,'index.html',{'user':user})

def notes(request):
    try:
        user=request.session.get("user")
        username=UserSignup.objects.get(email=user)
        if request.method=='POST':
            form=NotesForm(request.POST,request.FILES)
            if form.is_valid():
                x=form.save(commit=False)
                x.status="Pending"
                x.email=username
                x.save()
                print("Notes Subitted!")
                return redirect("/")

            else:
                print(form.errors)
    except:
        print("Error")
    return render(request,'notes.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def profile(request):
    uid=request.session.get("uid")
    cid=UserSignup.objects.get(id=uid)
    
    if request.method=='POST':
        form=SignupForm(request.POST,instance=cid)
        if form.is_valid():
            form.save()
            print("Profile Updated!")
            return redirect("/")
        else:
            print(form.errors)
    return render(request,'profile.html',{'cid':cid})

def signin(request):
    if request.method=='POST':
        em=request.POST["email"]
        pa=request.POST["password"]
        
        user=UserSignup.objects.filter(email=em,password=pa)
        uid=UserSignup.objects.get(email=em)
        print(uid.id)
        if user:
            print("Login Successfully!")
            request.session["user"]=em
            request.session["uid"]=uid.id
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
    