from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from administracion.models import *
from administracion.forms import *

@login_required
def indexR(request):
    totalUsers = UserProfile.objects.count()
    reclamaciones = Reclamacion.objects.all()

    context = {
        'reclamaciones': reclamaciones, 
        'totalUsers': totalUsers,
        'totalHospedajes': Hospedaje.objects.all().count(),
        'totalReclamaciones': Reclamacion.objects.all().count(),
        'totalReservaciones': Reservacion.objects.all().count()
    }
    return render(request, 'recepcion_dashboard/index.html', context)


@login_required
def reservationsR(request):
    reservation = Reservacion.objects.all()
    context = {'reservaciones': reservation}
    return render(request, 'reservacionesR/index.html', context)


@login_required
def complaintSuggestionR(request):
    cs = Reclamacion.objects.all()
    context = {'reclamaciones': cs}
    return render(request, 'reclamacionesR/index.html', context)


@login_required
def createCSuggestion(request):
    if request.method == 'POST':
        form = CSuggestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reclamaciones')
    else:
        form = CSuggestionsForm()

    context = {'form': form}
    return render(request, 'reclamacionesR/csuggestions_form.html', context)