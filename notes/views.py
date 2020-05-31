from django.shortcuts import render
from notes.form import Userform
from django.core import validators
from django import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from notes.models import WriteNotes
from django.http import HttpResponseRedirect


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
def note(req):
   x=WriteNotes.objects.filter(user=req.user)
   for y in x:
      y.data=y.data.split('$')   
   return render(req,"notes/index.html",{'data':x})

@login_required
def edit(req):
   if req.method =='POST':
      data=WriteNotes.objects.filter(user=req.user,topic=req.POST.get('topic'))
      
      a = data[0].data.split('$')
      for y in data:
         y.data=y.data.split('$')
      return render(req,'notes/edit.html',{ 'data': data[0] })
   return render(req,"index.html")




@login_required
def delete(req):
   if req.method=="POST":
      data=WriteNotes.objects.get(user=req.user,topic=req.POST.get('topic'))
      print(data.data)
      y=data.data.split('$')
      print(type(y))
      i=0
      for x in y:
         if x==req.POST.get('value'):
            break
         else:
            i=i+1
      print(y)
      y.pop(i)
      print(y)
      s=''
      for x in y:
         s=s+x
         s=s+'$'
      s=s[:-1]
      print(s)
      data.data=s
      print(data.data,"=============")
      data.save()
      return HttpResponseRedirect("/notes")
   return render(req,"index.html")





@login_required
def update(req):
   if req.method=="POST":
      data=WriteNotes.objects.get(user=req.user,topic=req.POST.get('topic'))
      print(data.data)
      y=data.data.split('$')
      print(type(y))
      i=0
      for x in y:
         if x==req.POST.get('value'):
            break
         else:
            i=i+1
      y[i]=req.POST.get('Cvalue')
      s=''
      for x in y:
         s=s+x
         s=s+'$'
      s=s[:-1]
      print(data.data,"////////")
      data.data=s
      data.save()
      return HttpResponseRedirect("/notes")
   return render(req,"index.html")




@login_required
def add(req):
   if req.method=="POST":
      data=WriteNotes.objects.get(user=req.user,topic=req.POST.get('topic'))
      data.data=data.data+"$"+req.POST.get('value')
      data.save()
      return HttpResponseRedirect("/notes")
   return render(req,"index.html")




@login_required
def delTopic(req):
   if req.method=="POST":
      WriteNotes.objects.get(user=req.user,topic=req.POST.get('topic')).delete()
      print("done")
      return HttpResponseRedirect("/notes")
   return render(req,"index.html")




@login_required
def create(req):
   if req.method=="POST":
      a=WriteNotes(user=req.user,topic=req.POST.get('data'),data=" ")
      a.save()
      return HttpResponseRedirect("/notes")
   
   return render(req,"index.html")