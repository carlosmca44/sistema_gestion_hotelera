from django import forms


class LoginAuth (forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class SignInAuth(forms.Form):
    name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
    rol = forms.CharField()
