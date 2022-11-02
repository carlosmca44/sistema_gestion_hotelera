from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.contrib.auth.views import LoginView


# class LoginAuth(forms.ModelForm):
#     username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(
#         attrs={'class': 'form-control'}))
#     password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
#         attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         help_texts = {k: '' for k in fields}


class SignInAuth(UserCreationForm):
    name = forms.CharField(
        label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    category = forms.CharField(
        label='Rol', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['name', 'username', 'password1', 'password2', 'category']
        help_texts = {k: '' for k in fields}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


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
