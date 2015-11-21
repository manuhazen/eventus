from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, UserLoginForm
from .models import User

# Create your views here.

def UserLogin(request):
    if request.method == "POST":
        if 'register_form' in request.POST:

            user_register = UserRegisterForm(request.POST)
            if user_register.is_valid():
                User.objects.create_user(username=user_register.cleaned_data['username'],
                                         email=user_register.cleaned_data['email'],
                                         password=user_register.cleaned_data['password'])
                return (request, '/')
        if 'login_form' in request.POST:
            login_form = UserLoginForm(request.POST)
            if login_form.is_valid():
                user = authenticate(username= login_form.cleaned_data['username'],
                                    password= login_form.cleaned_data['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('/')
    else:
        user_register = UserRegisterForm()
        login_form = UserLoginForm()
    return render(request, 'users/login.html', {'user_register': user_register,
                                            'login_form': login_form})

def UserLogOut(request):
    logout(request)
    return redirect("/")
