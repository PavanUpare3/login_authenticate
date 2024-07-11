from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import signup
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout



def showform(request):
    if request.method == 'POST':
        ty = signup(request.POST)
        if ty.is_valid():
            ty.save()
            messages.success(request, 'account created')
            ty=signup()
    else:
        ty=signup()
    return render(request, 'signup.html', {'form':ty})


def loginShow(request):    
    if request.method == 'POST':
        hg = AuthenticationForm(request=request, data=request.POST)
        if hg.is_valid():
            uname= hg.cleaned_data['username']
            upass= hg.cleaned_data['password']
            
            
            user = authenticate(request, username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request,'login successfully')
                return HttpResponseRedirect('/profile/')
            
    else:
        hg = AuthenticationForm()
    return render(request, 'login.html', {'logen': hg})


def profiless(request):
    return render(request, 'profile.html')
