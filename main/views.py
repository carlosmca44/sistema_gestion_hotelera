from django.shortcuts import render, redirect
from .forms import LoginAuth


def auth_login(request):
    if request.method == 'POST':
        form = LoginAuth(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = LoginAuth()

    context = {'form': form}
    return render(request, 'login/login.html', context)


def home(request):
    return render(request, 'home/home.html')
