from django.shortcuts import render, redirect
from account.models import *
from account.forms import UserCreationForm, UserLoginForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def home(request):
    return render(request, 'home.html')

def singup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.changed_data)
            user = form.save()
            login(request, user)
            return redirect('user')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def user_view(request):
    return render(request, 'user.html')

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate( email = email, password = password)
            if user is not None:
                login(request, user)
                return redirect('user')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')