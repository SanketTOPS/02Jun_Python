from django.contrib import admin
from django.urls import path,include
from userapp import views

urlpatterns = [
    path('',views.index),
    path('notes/',views.notes,name='notes'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('userlogout/',views.userlogout,name='userlogout'),
    
]