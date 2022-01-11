
from django.forms import fields
from django.shortcuts import render
from User_app.forms import UserForm,LoginForm
from . import forms
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect


# Create your views here.


# homepage for application
def home(request):
    return render(request, "home.html")



# New user registration
def Register(request):
    form = forms.UserForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()                     # user object is saved 
            form = UserForm()

    return render(request, 'register.html', {"form": form})      



# Existing user registration
def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    
    return render(request, 'loggedin.html', context={'form': form, 'mesage': message})












