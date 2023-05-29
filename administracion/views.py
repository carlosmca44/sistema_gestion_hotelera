from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def indexA(request):
    totalUsers = UserProfile.objects.count()
    reclamaciones = Reclamacion.objects.all()

    context = {
        'reclamaciones': reclamaciones, 
        'totalUsers': totalUsers,
        'totalHospedajes': Hospedaje.objects.all().count(),
        'totalReclamaciones': Reclamacion.objects.all().count(),
        'totalReservaciones': Reservacion.objects.all().count()
    }
    return render(request, 'admin_dashboard/index.html', context)


@login_required
def reservations(request):
    reservation = Reservacion.objects.all()
    context = {'reservaciones': reservation}
    return render(request, 'reservaciones/index.html', context)


@login_required
def complaintSuggestion(request):
    cs = Reclamacion.objects.all()
    context = {'reclamaciones': cs}
    return render(request, 'reclamaciones/index.html', context)

@login_required
def usersManagement(request):
    users = UserProfile.objects.all()
    users_count = UserProfile.objects.count()
    context = {'users': users, 'users_count': users_count}
    return render(request, 'usuarios/index.html', context)


def createUser(request):
    if request.method == 'POST':
        form = userCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = userCreationForm()

    context = {'form': form}
    return render(request, 'usuarios/createUser.html', context)


def deleteUser(request, userId):
    user = UserProfile.objects.get(id=userId)
    if request.user.id != userId:
        user.delete()

    return redirect('usuarios')


def editUser(request, userId):
    user = UserProfile.objects.get(id=userId)
    password = user.password
    if request.method == 'POST':
        form = userCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = userCreationForm(instance=user)

    context = {'form': form, 'password': password}
    return render(request, 'usuarios/edit_user.html', context)