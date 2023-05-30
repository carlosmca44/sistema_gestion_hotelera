from django import forms
from administracion.models import *
from django.contrib.auth.forms import UserCreationForm


class userCreationForm(UserCreationForm):

    CATEGORIES = [('Administrador', 'Administrador'), ('Recepcionista', 'Recepcionista'), ('Cliente', 'Cliente')]

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


class CSuggestionsForm(forms.ModelForm):
    class Meta:
        model = Reclamacion
        fields = ['habitacion', 'info']
        labels = {
            'habitacion': 'Habitacion', 'info': 'Informacion'
        }
        widgets = {
            'habitacion': forms.Select(attrs={'class': 'form-select'}),
            'info': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AskCSuggestions(forms.ModelForm):
    class Meta:
        model = Reclamacion
        fields = ['response']
        labels = {
            'response': 'Respuesta'
        }
        widgets = {'response': forms.Textarea(attrs={'class': 'form-control'})}