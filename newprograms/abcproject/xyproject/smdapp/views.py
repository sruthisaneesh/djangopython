import email

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method=='POST':
        p=request.POST['username']
        q=request.POST['password']
        user=auth.authenticate(username=p,password=q)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid item")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        a=request.POST['username']
        b=request.POST['first_name']
        c=request.POST['last_name']
        d=request.POST['email']
        e=request.POST['password']
        f=request.POST['cpassword']
        if e==f:
           if User.objects.filter(username=a).exists():
               messages.info(request,"username is already taken")
               return redirect('register')
           elif User.objects.filter(email=d).exists():
                messages.info(request,"email is already taken")
                return redirect('register')
           else:
               user=User.objects.create_user(username=a,password=e,first_name=b,last_name=c,email=d)
               user.save();
               print("user created")
               return redirect('login')
        else:
            messages.info(request,"password is not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')