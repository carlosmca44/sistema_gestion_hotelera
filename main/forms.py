from django import forms
from administracion.models import *
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
        model = UserProfile
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
        fields = ['customer', 'entry_date', 'out_date', 'habitaciones']
        


class CSuggestionsForm(forms.ModelForm):
    class Meta:
        model = Reclamacion
        fields = '__all__'


class AskCSuggestions(forms.ModelForm):
    class Meta:
        model = Reclamacion
        fields = ['response']
        labels = {
            'response': 'Respuesta'
        }
        widgets = {'response': forms.Textarea(attrs={'class': 'form-control'})}
