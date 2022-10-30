from django.shortcuts import render, redirect
from .forms import LoginAuth, SignInAuth, ReservationForm
from .models import *


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
    names = Reservacion.objects.all()
    totalR = Reservacion.objects.count()
    disp = 100 - totalR
    context = {'names': names, 'total': totalR, 'disp': disp}
    return render(request, 'home/home.html', context)


def createReservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReservationForm()

    context = {'form': form}
    return render(request, 'reservations/reservation_form.html', context)


def deleteReservation(request, reservationId):
    reservation = Reservacion.objects.get(id=reservationId)
    reservation.delete()
    return redirect('home')


def editReservation(request, reservationId):
    reservation = Reservacion.objects.get(id=reservationId)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReservationForm(instance=reservation)

    context = {'form': form}
    return render(request, 'reservations/edit_reservation.html', context)
