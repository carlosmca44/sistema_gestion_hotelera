from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required


def auth_signin(request):
    if request.method == 'POST':
        form = SignInAuth(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignInAuth()

    context = {'form': form}
    return render(request, 'login/signin.html', context)


@login_required
def home(request):
    # reception
    names = Reservacion.objects.all()
    totalReservations = Reservacion.objects.count()
    disp = 100 - totalReservations

    # administration
    totalUsers = UserProfile.objects.count()
    cs = QSugerencias.objects.all()

    context = {'names': names, 'total': totalReservations,
               'disp': disp, 'cs': cs}
    return render(request, 'home/home.html', context)


@login_required
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


@login_required
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


@login_required
def complaintSuggestion(request):
    cs = QSugerencias.objects.all()
    context = {'cs': cs}
    return render(request, 'complaint_suggestions/csuggestions.html', context)


@login_required
def createCSuggestion(request):
    if request.method == 'POST':
        form = CSuggestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('csuggestions')
    else:
        form = CSuggestionsForm()

    context = {'form': form}
    return render(request, 'complaint_suggestions/csuggestions_form.html', context)


@login_required
def editCSuggestion(request, csuggestionId):
    csuggestion = QSugerencias.objects.get(id=csuggestionId)
    if request.method == 'POST':
        form = CSuggestionsForm(request.POST, instance=csuggestion)
        if form.is_valid():
            form.save()
            return redirect('csuggestions')
    else:
        form = CSuggestionsForm(instance=csuggestion)

    context = {'form': form}
    return render(request, 'complaint_suggestions/csuggestion_edit.html', context)


@login_required
def askCSuggestion(request, csuggestionId):
    csuggestion = QSugerencias.objects.get(id=csuggestionId)
    info = csuggestion.info
    if request.method == 'POST':
        form = AskCSuggestions(request.POST, instance=csuggestion)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AskCSuggestions()

    context = {'form': form, 'info': info}
    return render(request, 'complaint_suggestions/csuggestion_response.html', context)


@login_required
def deleteCSuggestion(request, csuggestionId):
    csuggestion = QSugerencias.objects.get(id=csuggestionId)
    csuggestion.delete()
    return redirect('csuggestions')


@login_required
def editReponseCSuggestion(request, csuggestionId):
    csuggestion = QSugerencias.objects.get(id=csuggestionId)
    info = csuggestion.info
    if request.method == 'POST':
        form = AskCSuggestions(request.POST, instance=csuggestion)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AskCSuggestions(instance=csuggestion)

    context = {'form': form, 'info': info}
    return render(request, 'complaint_suggestions/edit_response_csuggestion.html', context)
