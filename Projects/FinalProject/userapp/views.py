from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def notes(request):
    return render(request,'notes.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')