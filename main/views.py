from django.shortcuts import render, redirect
from .forms import LoginAuth, SignInAuth


def auth_login(request):
    if request.method == 'POST':
        form = LoginAuth(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = LoginAuth()

    context = {'form': form}
    return render(request, 'login/login.html', context)


def auth_signin(request):
    if request.method == 'POST':
        form = SignInAuth(request.POST)
        if form.is_valid():
            return redirect('login')
    else:
        form = SignInAuth()

    context = {'form': form}
    return render(request, 'login/signin.html', context)


def home(request):
    return render(request, 'home/home.html')
