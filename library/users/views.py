from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.models import CustomUser


def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        p1=request.POST['p1']
        e=request.POST['e']
        f=request.POST['f']
        ln=request.POST['ln']
        ph=request.POST['ph']
        ad=request.POST['ad']

        if(p==p1):
            u=CustomUser.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=ln,phone=ph,address=ad)
            u.save()
            return redirect("books:home")
        else:
            messages.error(request,"Passwords are not the same")

    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('books:home')
        else:
            messages.error(request,"Invalid Login Credentials")
    return render(request,'login.html')


@login_required()
def user_logout(request):
    logout(request)
    return redirect('users:login')