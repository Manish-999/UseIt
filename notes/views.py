from django.shortcuts import render
from notes.form import Userform
from django.core import validators
from django import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(req):
   return render(req,"index.html")


def register(req):
   if req.method=='POST':
      form=Userform(data=req.POST)
      
      if form.is_valid():
         user=form.save()
         user.set_password(user.password)
         user.save()
         login(req,user)
         print("data saved")
   else:
         form=Userform()
      
   return render(req,'register.html',{'form':form,'error':form.errors})


def loginn(req):

   if req.method=="POST":
         
         uname=req.POST.get('username')
         passs=req.POST.get('password')
         
         user=authenticate(username=uname,password=passs)

         if user:
            print(user)
            login(req, user)
         
         else:
            print('some error')
            return render(req,'login.html',{'error':'User Name or Password is incorrect'})
      
   return render(req,'login.html',{'error':''})


@login_required
def logoutt(req):
   logout(req)
   return render(req,"index.html")

@login_required
def game(req):
      return render(req,"game.html")