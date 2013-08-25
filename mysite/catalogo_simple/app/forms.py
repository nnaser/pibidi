# -*- encoding: utf-8 -*-

from django import forms

class LoginForm(forms.Form):
    #username = forms.CharField()
    #password = forms.CharField(widget=forms.PasswordInput())
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Password'})
    )

class ComentarioForm(forms.Form):
    texto = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'Escribe un comentario...'})
    )