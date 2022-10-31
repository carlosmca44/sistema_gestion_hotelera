from django import forms
from .models import *


class LoginAuth (forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class SignInAuth(forms.Form):
    name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
    rol = forms.CharField()


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ['name', 'lastName', 'entry_date', 'out_date', 'roomNumber']
        labels = {'name': 'Nombre', 'lastName': 'Apellidos', 'entry_date': 'Fecha de entrada',
                  'out_date': 'Fecha de salida', 'roomNumber': 'Numero de habitacion'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'entry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%d/%m/%Y'),
            'out_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%d/%m/%Y'),
            'roomNumber': forms.Select(attrs={'class': 'form-select'}),
        }


class CSuggestionsForm(forms.ModelForm):
    class Meta:
        model = QSugerencias
        fields = ['name', 'roomNumber', 'info']
        labels = {
            'name': 'A nombre de:', 'roomNumber': 'Habitacion', 'info': 'Informacion'
        }
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'roomNumber': forms.Select(attrs={'class': 'form-select'}),
            'info': forms.Textarea(attrs={'class': 'form-control'}),
        }
