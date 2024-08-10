from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class UserCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'}))
    email = forms.EmailField(label="Adresse mail",widget=forms.EmailInput(attrs={'placeholder': 'Adresse mail'}))

    password1 = forms.CharField(label="Mot de passe",
                              widget=forms.PasswordInput(attrs={'placeholder': 'Entrer le mot de passe'}))
    password2 = forms.CharField(label="Confirmer le mot de passe",
                              widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer le mot de passe'}))