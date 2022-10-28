from django import forms


class LoginAuth (forms.Form):
    username = forms.CharField()
    password = forms.CharField()
