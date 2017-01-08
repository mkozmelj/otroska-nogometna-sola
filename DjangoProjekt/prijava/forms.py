from django import forms
from django.forms import EmailField

class vpis(forms.Form):
    username = forms.CharField(label='Uporabnisko ime', max_length=100)
    password = forms.CharField(label='Geslo', widget=forms.PasswordInput)


class email(forms.Form):
    mail = forms.CharField(label='Elektronski naslov', widget=forms.EmailInput)
