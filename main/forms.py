from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class userCreationForm(UserCreationForm):

    CATEGORIES = [('1', 'Administrador'), ('2', 'Recepcionista')]

    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(
        label='Rol', widget=forms.Select(attrs={'class': 'form-select'}), choices=CATEGORIES)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'password1', 'password2', 'category']
        help_texts = {k: '' for k in fields}
        labels = {'first_name': 'Nombre/s',
                  'last_name': 'Apellido/s', 'username': 'Nombre de usuario'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
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


class AskCSuggestions(forms.ModelForm):
    class Meta:
        model = QSugerencias
        fields = ['response']
        labels = {
            'response': 'Respuesta'
        }
        widgets = {'response': forms.Textarea(attrs={'class': 'form-control'})}
