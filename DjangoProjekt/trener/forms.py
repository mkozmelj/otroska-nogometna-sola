from django import forms

class dodajanje(forms.Form):
    besedilo = forms.CharField(widget=forms.Textarea)